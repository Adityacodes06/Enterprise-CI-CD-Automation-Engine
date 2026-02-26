FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
RUN pip install -e .

ENV PYTHONUNBUFFERED=1
EXPOSE 8080

CMD ["python", "-c", "from app.main import create_app; app = create_app(); print(app.get_status())"]
