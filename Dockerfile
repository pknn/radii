FROM python:3.6
COPY . /radii
WORKDIR /radii
RUN . venv/bin/activate
RUN pip install -r requirements.txt
ENV DATABASE_URL=postgresql://localhost/radii_app