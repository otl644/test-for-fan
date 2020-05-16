FROM python:3.8

COPY . ./

RUN pip install fastapi uvicorn

EXPOSE 8000

CMD ["uvicorn", "src.app:app", "--host", "0.0.0.0", "--port", "8000"]
