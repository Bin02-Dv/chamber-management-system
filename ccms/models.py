from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model()

class SignUp(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_user = models.IntegerField()
    fullname = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)

    def __str__(self):
        return self.fullname

class Scheduling(models.Model):
    case_number = models.CharField(max_length=10000, blank=True)
    case_title = models.CharField(max_length=10000, blank=True)
    case_time = models.CharField(max_length=100, blank=True)
    case_date = models.CharField(max_length=100, blank=True)
    judged = models.CharField(max_length=100, blank=True)
    case_status = models.BooleanField(True)

    def __str__(self):
        return self.case_title
    
class DocumentManagement(models.Model):
    doc_number = models.ForeignKey(Scheduling, on_delete=models.CASCADE)
    doc_id = models.IntegerField()
    document = models.FileField(upload_to='documents')

    def __str__(self):
        return self.doc_number.case_title
