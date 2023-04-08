FROM python:3.10.0-alpine

# Create directory
RUN mkdir /app

#Copy stuff into /app
COPY ./src /app
COPY src/requirements.txt .
RUN pip3 install -r requirements.txt

# set workdir as "/app"
WORKDIR /app 

ENTRYPOINT ["python","main.py", "hello wrld"]
