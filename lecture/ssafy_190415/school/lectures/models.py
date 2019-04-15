from django.db import models
from faker import Faker

fake = Faker()

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Lecture(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    lecture = models.ForeignKey(Lecture, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.student}이(가) {self.lecture}을(를) 수강 중입니다."


# 리조트 예약
class Client(models.Model):
    name = models.CharField(max_length=746)

    @classmethod
    def dummy(cls, n):
        for i in range(n):
            cls.objects.create(name=fake.name())

    def __str__(self):
        return self.name


class Resort(models.Model):
    name = models.CharField(max_length=746)
    clients = models.ManyToManyField(Client, related_name="resorts")

    def __str__(self):
        return self.name
