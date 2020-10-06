FROM python:3

WORKDIR /opt/reconmap-job-processing-svc

RUN mkdir ./logs

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY src/* ./src/

EXPOSE 8765

CMD ["python3", "/opt/reconmap-job-processing-svc/src/main.py"]

