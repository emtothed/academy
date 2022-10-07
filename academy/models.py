from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    fullname = models.CharField(max_length=50)
    courses = models.ManyToManyField("academy.Course",related_name="students")
    passed =  models.ManyToManyField("academy.Course",related_name="passedstudents")

class Course(models.Model):
    title = models.CharField(max_length=50)
    examdate = models.DateField()
    day = models.CharField(max_length=10)
    time = models.CharField(max_length=10)
    professor = models.CharField(max_length=50)
    def serialize(self):
        return {
            "id": self.id,
            "title": self.title,
            "examdate": self.examdate,
            "day": self.day,
            "time": self.time,
            "professor":self.professor
            
        }
    def __str__(self):
        return f"{self.title}"

class Scores(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE , related_name="scores")
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    score = models.FloatField()
    def __str__(self):
        return f"{self.id} : {self.student}'s {self.course}" 

class quest(models.Model):
    course = models.ForeignKey(Course,on_delete=models.CASCADE,related_name="quests")
    question = models.CharField(max_length=300)
    answer = models.CharField(max_length=50)
    def serialize(self):
        return {
            "id": self.id,
            "question": self.question,
            "answer": self.answer,
        }
    def __str__(self):
        return f"{self.id}:{self.course}  Q:{self.question}"
