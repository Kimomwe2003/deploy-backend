from django.db import models

# Create your models here.
class School(models.Model):
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=20)
    email = models.EmailField(unique=True, null=True, blank=True)
    capacity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.name}"
    
class Grade(models.Model):
    name = models.CharField(max_length=20)
    school = models.ForeignKey(School, on_delete=models.PROTECT)


    def __str__(self):
        return f"{self.name}"


class Teacher(models.Model):
    GENDER_CHOICES = [
        ("Male", "Male"),
        ("Female", "Female"),
    ]

    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20, default="Johnson")
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    grade = models.OneToOneField(Grade, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    

class Subjects(models.Model):
    name = models.CharField(max_length=20)
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE)


    def __str__(self):
        return f"{self.name}"
    
class Student(models.Model):

    GENDER_CHOICES ={
        "M": "Male",
        "F":  "Female",
    }


    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE)


    def __str__(self):
        return f"{self.first_name} {self.last_name} "