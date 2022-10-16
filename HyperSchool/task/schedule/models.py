from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Person(models.Model):
    class Meta:
        abstract = True
    name = models.CharField(max_length=61)
    surname = models.CharField(max_length=61)
    age = models.IntegerField(null=True)

    def __str__(self):
        return f'{self.surname}, {self.name}'


class Teacher(Person):
    about = models.TextField(null=True, blank=True)

    def get_detail_url(self):
        return reverse('teacher-detail', args=(self.pk,))


class Course(models.Model):
    title = models.CharField(max_length=255)
    info = models.TextField()
    duration_months = models.IntegerField()
    price = models.FloatField()
    teacher = models.ManyToManyField(Teacher)

    def __str__(self):
        return self.title

    def get_detail_url(self):
        return reverse('course-detail', args=(self.pk,))


class Student(Person):
    course = models.ManyToManyField(Course, blank=True)
