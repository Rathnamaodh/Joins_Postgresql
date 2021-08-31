from django.db import models

# Create your models here.
class Shop_A(models.Model):
    fruit = models.CharField(max_length=60) 
    
   
    def __str__(self):
        return self.fruit

class Shop_B(models.Model):
    fruit = models.CharField(max_length=60)
    
    def __str__(self):
        return self.fruit
class Employee(models.Model):
    emp_name = models.CharField(max_length=60)
    emp_no = models.IntegerField()
    dept = models.CharField(max_length=60)
    age = models.IntegerField()
    address = models.CharField(max_length=60)

    def __str__(self):
        return self.name

class Salary(models.Model):
    salary = models.IntegerField()
    emp_no = models.IntegerField()
    

    def __str__(self):
        return self.salary


