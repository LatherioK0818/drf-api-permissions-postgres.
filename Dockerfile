FROM python:3.11.5-slim-bullseye

# Set environment variables
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH=/usr/src/app

# Set work directory
WORKDIR /app

# Install dependencies
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# Install gunicorn
RUN pip install gunicorn

# Copy project
COPY . .

# Command to start the application
CMD ["gunicorn", "consumables_project.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "4"]
