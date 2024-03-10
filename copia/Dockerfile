FROM python:3.11


WORKDIR /opt/app

COPY . .

RUN pip install --no-cache-dir -r requirements-prod.txt
EXPOSE 5000

# Command "python3 -m flask run --host=0.0.0.0"
CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]

