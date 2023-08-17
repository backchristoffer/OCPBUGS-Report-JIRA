FROM python:slim-bullseye
WORKDIR /app
COPY . .
RUN pip3 install pipenv
RUN pipenv install
ENTRYPOINT [ "pipenv","run","python3","ocpbugpull.py" ]