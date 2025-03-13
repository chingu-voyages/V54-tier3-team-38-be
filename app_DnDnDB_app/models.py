from django.db import models

# Create your models here.
class SessionData(models.Model):
    session_id = models.CharField(max_length=100, unique=True)  # Unique ID for each session
    data = models.JSONField()  # Store incoming JSON data
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp when created

    def __str__(self):
        return f"Session {self.session_id}"
    

class Asset(models.Model):
    name = models.CharField(max_length=100, unique=True)  
    description = models.TextField(blank=True, null=True)  
    image = models.ImageField(upload_to='assets/', blank=True, null=True)  # ✅ Image is optional
    created_at = models.DateTimeField(auto_now_add=True)  # ✅ Auto timestamp when created
    updated_at = models.DateTimeField(auto_now=True)  # ✅ Auto timestamp when updated

    def __str__(self):
        return self.name