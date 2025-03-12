from django.db import models

# Create your models here.
class SessionData(models.Model):
    session_id = models.CharField(max_length=100, unique=True)  # Unique ID for each session
    data = models.JSONField()  # Store incoming JSON data
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp when created

    def __str__(self):
        return f"Session {self.session_id}"
    

class Asset (models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='assets/')
    # Add other fields as needed

    def __str__(self):
        return self.name