from django.db import models

# Create your models here.
from django.db.models.functions import datetime

from guides.models import GUIDE, GROUP, BRANCH

from django.core.validators import MinLengthValidator, RegexValidator

from django.contrib.auth.admin import User
from django.dispatch import receiver

from django.db.models.signals import post_save, post_delete


class MASTERS(models.Model):
    USN = models.CharField(max_length=10, primary_key=True)
    Name = models.CharField(max_length=25)
    Rank = models.PositiveSmallIntegerField()
    Branch = models.ForeignKey(BRANCH, on_delete=models.PROTECT, null=True)
    Mail = models.EmailField()
    PassKey = models.CharField(max_length=15, null=True)


class COUNSEL(models.Model):
    class Meta:
        unique_together = ('Scholar', 'Option')

    Option = models.PositiveSmallIntegerField()
    Scholar = models.ForeignKey(MASTERS, on_delete=models.PROTECT)
    Guide = models.ForeignKey(GUIDE, on_delete=models.PROTECT)
    Group = models.ForeignKey(GROUP, on_delete=models.PROTECT)


class RESULT(models.Model):
    Option = models.PositiveSmallIntegerField()
    Scholar = models.ForeignKey(MASTERS, on_delete=models.PROTECT, primary_key=True)


class REGISTER(models.Model):
    class Meta:
        unique_together = ('Year', 'Group')

    Year = models.PositiveSmallIntegerField()
    Group = models.ForeignKey(GROUP, on_delete=models.PROTECT)
    Count = models.PositiveSmallIntegerField()


class SCHOLAR(models.Model):
    USN = models.CharField(max_length=10, primary_key=True)
    Name = models.CharField(max_length=100)
    DOB = models.DateField()
    Address = models.CharField(max_length=300)
    Year_of_joining = models.PositiveSmallIntegerField()
    Group = models.ForeignKey(GROUP, on_delete=models.PROTECT)
    Course_type = models.CharField(max_length=10, default='full_time')
    Photo = models.ImageField()
    Phone = models.CharField(max_length=10, default=0000000000)
    Gender = models.CharField(max_length=8, default='not mentioned')
    Guide = models.ForeignKey(GUIDE, on_delete=models.PROTECT)
    Entrance = models.ForeignKey(MASTERS, on_delete=models.PROTECT, null=True)
    Mail = models.EmailField(default="scholar@uvce.org")
    PassCode = models.CharField(max_length=8, null=True)

    # Password = models.CharField(default="123456sS", max_length=15, validators=[MinLengthValidator(8)])

    def __str__(self):
        return str(self.USN) + " - " + str(self.Name)


"""
@receiver(post_save, sender=SCHOLAR)
def save_s_user(sender, instance, created, **kwargs):
    if created:
        user = User.objects.create_user(username=instance.MailId, email=instance.MailId, password=instance.Password)
        #moves to the create_scholar_profile function
        user.profile.type = 's'
        user.save()


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    type = models.CharField(default='s', max_length=1)

    def __str__(self):
        return self.user.username + " " + self.type

@receiver(post_save, sender=User)
def create_scholar_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_scholar_profile(sender, instance, **kwargs):
    instance.profile.save()
"""


class PAPER(models.Model):
    class Meta:
        unique_together = ('Number', 'TakenBy')

    Number = models.PositiveSmallIntegerField(null=True)
    Title = models.CharField(max_length=100)
    TakenBy = models.ForeignKey(SCHOLAR, on_delete=models.PROTECT)
    Status = models.CharField(max_length=30)
    Pdf = models.FileField(null=True)
    AddedOn = models.DateTimeField(null=True)
    StartedOn = models.DateTimeField(null=True)
    FinishedOn = models.DateTimeField(null=True)

    def __str__(self):
        return str(self.id) + " - " + self.Title
