
FROM python:3-onbuild


EXPOSE 5000

RUN pip install  --no-cache-dir -Ur requirements.txt 

CMD ["python3", "./app.py"]
