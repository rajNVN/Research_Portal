from django.contrib.auth.admin import User
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


# from scholars.models import Profile

# Create your models here.
class UNIVERSITY(models.Model):
    id = models.PositiveSmallIntegerField(primary_key=True)
    Name = models.CharField(max_length=100)

    def __str__(self):
        return str(self.id) + "-" + self.Name


class BRANCH(models.Model):
    id = models.PositiveSmallIntegerField(primary_key=True)
    Name = models.CharField(max_length=30)

    def __str__(self):
        return str(self.id) + " - " + self.Name


class GROUP(models.Model):
    id = models.PositiveSmallIntegerField(primary_key=True)
    Name = models.CharField(max_length=30)
    Branch = models.ForeignKey(BRANCH, models.PROTECT, null=True)

    def __str__(self):
        return str(self.id) + " - " + self.Name


class TOPIC(models.Model):
    id = models.PositiveSmallIntegerField(primary_key=True)
    Name = models.CharField(max_length=30)
    Group = models.ForeignKey(GROUP, models.PROTECT)


class DATES(models.Model):
    start = models.DateField()
    end = models.DateField()


class GUIDE(models.Model):
    USN = models.CharField(max_length=10, primary_key=True)
    Name = models.CharField(max_length=30)
    DOB = models.DateField()
    Address = models.CharField(max_length=300)
    Mobile = models.IntegerField(max_length=10)
    graduated_year = models.PositiveSmallIntegerField()
    Branch = models.ForeignKey(BRANCH, on_delete=models.PROTECT)
    University = models.ForeignKey(UNIVERSITY, on_delete=models.PROTECT)
    Photo = models.ImageField()
    Designation = models.CharField(max_length=30, default='proffessor')
    PassCode = models.CharField(max_length=8, null=True)
    MailId = models.EmailField(null=True)
    # Password = models.CharField(max_length=15, default="123456sS")

    def __str__(self):
        return self.USN + "-" + self.Name


class USERS(models.Model):
    UserId = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    USN = models.CharField(max_length=10)
    is_Guide = models.BooleanField()

    def __str__(self):
        return self.UserId.username


"""
@receiver(post_save, sender=GUIDE)
def save_guide_user(sender, instance, created, **kwargs):
    if created:
        user = User.objects.create_user(username=instance.MailId, email=instance.MailId, password=instance.Password)
        # moves to the create_scholar_profile function
        user.profile.type = 'g'
        user.save()


@receiver(post_save, sender=User)
def create_guide_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_guide_profile(sender, instance, **kwargs):
    instance.profile.save()"""
