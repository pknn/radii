import logging
import os
import tqdm
import codecs
import h5py

from scipy.sparse import coo_matrix, csr_matrix
from implicit.als import AlternatingLeastSquares

import numpy as np

log = logging.getLogger("implicit")


def calculate_similar_event(path, output_filename):
    model = AlternatingLeastSquares()

    a, b = read_event_data(path)
    event, users = hfd5_from_dataframe(a, b, output_filename)

    users.eliminate_zeros()
    users.data = np.ones(len(users.data))

    log.info("Start fitting")
    model.fit(users)

    user_count = np.ediff1d(users.indptr)
    to_generate = sorted(np.arange(len(event)), key=lambda x: -user_count[x])

    with tqdm.tqdm(total=len(to_generate)) as progress:
        with codecs.open(output_filename, "w", "utf-8") as o:
            for eventid in to_generate:
                if users.indptr[eventid] != users.indptr[eventid + 1]:
                    name = event[eventid]
                    for other, score in model.similar_items(
                        eventid, int(len(event) * 2 / 3)
                    ):
                        o.write(f"{name},{event[other]},{score}\n")
                progress.update(1)


def read_event_data(path):
    import pandas

    users = pandas.read_csv(os.path.join(path, "likes.csv"))
    event = pandas.read_csv(os.path.join(path, "events.csv"))

    print(users.columns.tolist())

    return users, event


def hfd5_from_dataframe(users, event, output_filename):
    print(users.columns.tolist())
    m = coo_matrix(
        ((users["like"].astype(np.int32)), (users["eventID"], users["userID"]))
    ).tocsr()

    with h5py.File(output_filename, "w") as f:
        g = f.create_group("users")
        g.create_dataset("data", data=m.data)
        g.create_dataset("indptr", data=m.indptr)
        g.create_dataset("indices", data=m.indices)

        name = np.empty(shape=(event.eventID.max() + 1,), dtype=np.object)
        name[event.eventID] = event.name
        dt = h5py.special_dtype(vlen=str)
        dset = f.create_dataset("event", (len(name),), dtype=dt)
        dset[:] = name

        plays = csr_matrix((g.get("data"), g.get("indices"), g.get("indptr")))
        return np.array(f["event"]), plays
        # return f


calculate_similar_event("./data", "similar-event.csv")
