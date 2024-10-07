# Dockerfile
FROM python:3.10-slim

# Instale as dependências do sistema necessárias
RUN apt-get update && apt-get install -y \
    libgdk-pixbuf2.0-0 \
    libpango-1.0-0 \
    libpangocairo-1.0-0 \
    libcairo2 \
    gobject-introspection \
    libcairo2-dev \
    gir1.2-pango-1.0 \
    gir1.2-glib-2.0 \
    gir1.2-freedesktop \
    python3-cffi

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt file
COPY requirements.txt /app/

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the project files into the container
COPY . /app/

# Expose the port that the app will run on
EXPOSE 8000

# Start the Django server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
