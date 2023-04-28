FROM python:3.9-slim-buster
WORKDIR /beta_branch
COPY requirements.txt requirements.txt
ADD /fgm /fgm
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5000
ENV FLASK_APP=project
CMD ["flask", "run", "--host", "0.0.0.0"]