FROM python:3.8

# Install miscroservice from git
ARG GIT_USER=user
ARG GIT_PASSWORD=password

RUN mkdir /code

WORKDIR /code

ADD . /code/

RUN pip install -r requirements.txt

EXPOSE 9090
CMD ["python", "run.py"]