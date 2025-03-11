### DnDnDB

Create a virtual environment and activate your environment. Within your activated environment cd into the project directory and run:

```
pip install -r requirements.txt
```

Install MySQL on your system and ensure the server is running, and set up your environment variables on your system for DNDNDB_NAME (database name), DNDNDB_USER and DNDNDB_PASSWORD. Ensure you create the database and user with the password you've set in your environment variable. Still within your activated environment and in the correct project directory, run:

```
python manage.py migrate
```
