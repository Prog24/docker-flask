FROM python:3.7.3-alpine

ARG project_dir=/projects/

ADD src/requirements.txt $project_dir

WORKDIR $project_dir

RUN pip install flask
# RUN pip install -r requirements.txt