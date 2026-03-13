FROM python:3.11

WORKDIR /app

# utworzenie użytkownika
RUN useradd -m appuser

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# zmiana właściciela plików
RUN chown -R appuser:appuser /app

USER appuser

EXPOSE 5000

CMD ["python", "app.py"]