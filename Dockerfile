FROM python:3.6
COPY . /radii
WORKDIR /radii
RUN python3 -m venv venv
RUN . venv/bin/activate
RUN pip install -r requirements.txt
ENV DATABASE_URL=mysql+pymysql://root:root@db/radii