from django.db import models

# Create your models here.
from guides.models import BRANCH, GROUP, GUIDE
from scholars.models import PAPER


class STUDENT(models.Model):
    USN = models.CharField(max_length=10, primary_key=True)
    Name = models.CharField(max_length=100)
    DOB = models.DateField()
    Address = models.CharField(max_length=200)
    Course = models.CharField(max_length=2)
    Year = models.PositiveIntegerField()
    Branch = models.ForeignKey(BRANCH, on_delete=models.PROTECT)
    Email = models.EmailField()
    Mobile = models.CharField(max_length=10)
    Gender = models.CharField(max_length=1)
    Photo = models.ImageField()
    PassCode = models.CharField(max_length=8,null=True)

    def __str__(self):
        return self.pk + "-" + self.Name


class LANGUAGE(models.Model):
    id = models.PositiveSmallIntegerField(primary_key=True)
    name = models.CharField(max_length=10)


    def __str__(self):
        return self.name


class R_STUDENT(models.Model):
    Usn = models.CharField(max_length=100, primary_key=True)
    CodedIn = models.ForeignKey(LANGUAGE, on_delete=models.PROTECT)
    Code = models.CharField(max_length=1000)
    Github = models.CharField(max_length=40)
    When = models.DateTimeField()

    def __str__(self):
        return self.pk


class K_LANGUAGES(models.Model):
    class Meta:
        unique_together = ('Student', "Language")

    Student = models.ForeignKey(STUDENT, on_delete=models.PROTECT)
    Language = models.ForeignKey(LANGUAGE, on_delete=models.CASCADE)

    def __str__(self):
        return self.Student.Name + " - " + self.Language.name


class INTEREST(models.Model):
    class Meta:
        unique_together = ('Student', 'Group')

    Student = models.ForeignKey(STUDENT, on_delete=models.CASCADE)
    Group = models.ForeignKey(GROUP, on_delete=models.PROTECT)

    def __str__(self):
        return self.Student.Name + " - " + self.Group.Name


class P_STUDENT(models.Model):
    class Meta:
        unique_together = ('Paper', 'Number')

    Paper = models.ForeignKey(PAPER, on_delete=models.CASCADE)
    Number = models.PositiveSmallIntegerField()
    Student = models.ForeignKey(STUDENT, on_delete=models.CASCADE)


class SCORE(models.Model):
    class Meta:
        unique_together = ('Student', 'Guide')
    Student = models.ForeignKey(STUDENT, on_delete=models.PROTECT)
    Guide = models.ForeignKey(GUIDE, on_delete=models.PROTECT)
    Rank = models.PositiveSmallIntegerField()