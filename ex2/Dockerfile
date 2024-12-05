FROM python:3.9-slim

# Install dependencies
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app code
COPY app.py .

# Create config directory
RUN mkdir /config

EXPOSE 5000

CMD ["python", "app.py"]
