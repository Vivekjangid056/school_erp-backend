from django.db import models
from django.core.validators import RegexValidator
from colorfield.fields import ColorField

# Create your models here.


class LmCategoryMaster(models.Model):
    code = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
class LmDesignationMaster(models.Model):
    code = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
class LmDepartmentMaster(models.Model):
    code = models.CharField(max_length=100)
    name = models.CharField(max_length=100)    
    
    def __str__(self):
        return self.name
        
class LmAttendanceType(models.Model):
    
    PRESENT = 'Present'
    ABSENT = 'Absent'
    LEAVE = 'Leave'
    
    NATURE_CHOICES = [
        (PRESENT,'Present'),
        (ABSENT,'Absent'),
        (LEAVE,'Leave'),
    ]
    
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=100)
    nature = models.CharField(max_length=100,choices=NATURE_CHOICES,default=PRESENT)
    attendance = models.DecimalField(max_digits=5, decimal_places=2)
    
    def __str__(self):
        return self.name     
    
class LmHolidayList(models.Model):
    code = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    description = models.TextField()