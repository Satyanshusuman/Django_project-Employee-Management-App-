from django.db import models

# Create your models here.

class Testimonial(models.Model):
    Type=models.CharField(max_length=100)
    testimonial=models.TextField()
    picture=models.ImageField(upload_to="testimonials")
    rating=models.IntegerField()
    
class Feedback(models.Model):
    email=models.EmailField(max_length=50)
    name=models.CharField(max_length=50)
    feedback=models.TextField(max_length=200)
    