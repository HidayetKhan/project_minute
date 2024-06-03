from django.db import models

# Create your models here.

class State_Master(models.Model):
    # id = models.AutoField(primary_key=True)
    state_name = models.CharField(max_length=200)
    state_code = models.CharField(max_length=100) 
    created_date = models.DateTimeField(auto_now_add=True)  
    updated_date = models.DateTimeField(auto_now=True) 
    is_active = models.BooleanField(default=True)

class User_Master(models.Model):
    Name=models.CharField(200)
    email=models.EmailField()
    password=models.CharField(20)
    phone=models.BigIntegerField()
    city=models.CharField(200)
    gender=models.CharField(10)
    joining_date=models.DateTimeField()
    state=models.ForeignKey(State_Master, on_delete=models.CASCADE)
    created_date=models.DateTimeField(auto_now_add=True)
    updated_date=models.DateTimeField(auto_now_add=True)
    is_active=models.BooleanField(default=True)

class Task_Master(models.Model):
    task_id=models.CharField()
    title=models.CharField()
    description=models.TextField()
    assing_date=models.DateTimeField()
    state=models.ForeignKey(State_Master, on_delete=models.CASCADE)
    created_date=models.DateTimeField(auto_now_add=True)
    updated_date=models.DateTimeField(auto_now_add=True)
    user_id=models.ForeignKey(User_Master, on_delete=models.CASCADE)
    is_active=models.BooleanField(default=True)






