FROM python:3.9

COPY app/ .

RUN python -m venv venv

RUN sh venv/bin/activate

RUN pip install -r requirements.txt

CMD ["python", "main.py"]