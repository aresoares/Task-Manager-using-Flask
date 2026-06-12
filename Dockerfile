FROM python:3.10-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV SECRET_KEY=devsecops-local-secret

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY todo_project ./todo_project

EXPOSE 5000

WORKDIR /app/todo_project

CMD ["python", "-c", "from todo_project import app; app.run(host='0.0.0.0', port=5000, debug=False)"]
