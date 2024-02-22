# Lab: Combining Permissions, Authentication & Production Server with PostgreSQL

**Author:** Latherio Kidd

## Overview

In this lab, I enhanced our site by adding permissions, JWT authentication, and switching to a PostgreSQL database, bringing it closer to production-grade.

## Features

### General

- Merged functionality from two demos:
  - Restrict access to portions of the API's data.
  - Switch to using PostgreSQL instead of SQLite.
- Customized the project to use different application features/models.

### Django REST Framework

- Added JWT Authentication to the API.
- Installed necessary libraries in project configuration and/or site settings.
- Preserved pre-existing authentication for DRF Browsable API usability.

### Docker

- Switched to using Gunicorn instead of Django’s built-in development server.
- Handled static files properly using Whitenoise on the Django side.
- Adjusted `docker-compose.yml` to persist data in a volume outside of the container.


## Implementation Notes

- No unit tests required.



