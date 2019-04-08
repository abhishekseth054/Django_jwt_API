from django.db import models

class Employee(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    email = models.EmailField()
    permanenetAddress = models.TextField()
    presentAddress = models.TextField()


    def __str__(self):
        return self.firstName
