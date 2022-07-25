FROM python:3.9
COPY ./requirements.txt .
RUN pip install --upgrade pip
RUN pip install  -r requirements.txt
COPY ./main.py .
COPY ./aws_class.py .
EXPOSE 3838
ARG WORKERS
ENV ENVWORKERS=$WORKERS
CMD ["sh", "-c","uvicorn main:app --host 0.0.0.0 --port 3838 --workers ${ENVWORKERS}"]
