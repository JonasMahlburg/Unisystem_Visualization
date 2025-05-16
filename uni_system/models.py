from django.db import models

# Create your models here.
class Semester(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class Prof(models.Model):
    name = models.CharField(max_length=30)
   
    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=20)
    course = models.ManyToManyField('Course', related_name='students')

    def __str__(self):
        return f"{self.name}, {self.course}"


class Course_Description(models.Model):
    description = models.CharField(max_length=300)
    
    def __str__(self):
        return f"This course is about: {self.description}"


class Student_ID(models.Model):
    card_number = models.FloatField(max_length=15, unique=True)
    student = models.OneToOneField(Student, on_delete=models.CASCADE, related_name='id_card')
        
    def __str__(self):
        return f"ID Number {self.card_number} for:{self.student}"



class Course(models.Model):
    title = models.CharField(max_length=50)
    description = models.OneToOneField(Course_Description, on_delete= models.SET_NULL, null=True, related_name='course')
    semester = models.ForeignKey(Semester, on_delete= models.CASCADE, related_name='course')
    professor = models.ForeignKey(Prof, on_delete= models.SET_NULL, null=True, related_name='course' )

    def __str__(self):
        return f"{self.title}, {self.semester}"