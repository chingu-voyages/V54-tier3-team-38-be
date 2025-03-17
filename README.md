# 📜 README for DnDnDB Backend

Welcome to the backend for **DnDnDB**! This project is built using **Django REST Framework (DRF)** with a **MySQL** database to support a **React + TypeScript** frontend.

This repository contains the API for managing session data, assets, authentication, and other backend operations.

---

## 📌 Frontend Repository

The frontend for this project can be found here:  
[DnDnDB Frontend](https://github.com/chingu-voyages/V54-tier3-team-38-fe)

---

## 🚀 Tech Stack

- **Backend**: Django REST Framework (DRF)
- **Database**: MySQL
- **Authentication**: JWT (using `djangorestframework_simplejwt`)
- **CORS Handling**: `django-cors-headers`
- **Environment Management**: `django-environ`

---

## 🛠️ Installation & Setup

### 🔹 Prerequisites

Before you begin, ensure you have the following installed on your system:

- **Python** (≥ 3.10)
- **pip** (Python package manager)
- **MySQL** (Ensure MySQL is running)
- **Virtual Environment** (`venv`) (Optional but recommended)

---

### 🔹 Step 1: Clone the Repository

git clone https://github.com/chingu-voyages/V54-tier3-team-38-be.git
cd V54-tier3-team-38-be



```bash
git clone https://github.com/chingu-voyages/V54-tier3-team-38-be.git
cd V54-tier3-team-38-be

```

### 🔹 Step 2: Set up a Virtual environment

```bash
python -m venv env_dndndb


```


# Activate it
# On macOS/Linux:
source env_dndndb\bin\activate
# On Windows:
env_dndndb/Scripts/activate


```bash

pip install -r requirements.txt


CREATE DATABASE dndndb;

python manage.py makemigrations
python manage.py migrate

python manage.py createsuperuser

python manage.py runserver

```

server should be at 
http://127.0.0.1:8000/

- Erica Holden: [GitHub](https://github.com/ericadev) / [LinkedIn](https://linkedin.com/in/ericadev)
- Eoin McDonnell [GitHub](https://github.com/oldmcdonnell) / [LinkedIn](https://linkedin.com/in/mcdonnell.eoin)

## 🌎 Deployment
The backend will be deployed using Fly.io or another cloud provider. Stay tuned for updates.

