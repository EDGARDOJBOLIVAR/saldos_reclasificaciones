FROM python

WORKDIR /app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

# Set the environment variable for Flask
ENV FLASK_APP=app.py

# Run the command to start the server
CMD ["python", "app.py"]