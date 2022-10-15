from django.db import models



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


class Course(models.Model):
    title = models.CharField(max_length=255)
    info = models.TextField()
    duration_months = models.IntegerField()
    price = models.FloatField()
    teacher = models.ManyToManyField(Teacher)

    def __str__(self):
        return self.title


class Student(Person):
    course = models.ManyToManyField(Course, blank=True)
