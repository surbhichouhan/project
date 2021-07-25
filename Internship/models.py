from django.db import models
from django.utils import timezone
from django import forms
import uuid
import datetime
class Internship(models.Model):
    position = models.CharField(max_length=100)
    company_name = models.CharField(max_length=50)
    time_duration = models.IntegerField(default=0)
    description = models.TextField(max_length=1000)
    no_of_openings = models.IntegerField()
    skills  = models.CharField(max_length=500, default='')
    required = models.CharField(max_length=500, default='')
    start_date = models.DateField()
    stipend = models.IntegerField()
    location = models.CharField(max_length=50)
    postedDate = models.DateField(default=timezone.now)

    def __str__(self):
        return self.position


class UserProfile(models.Model):
    userId = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    full_name = models.CharField(max_length=100, default="")
    image = models.ImageField(upload_to="user_image", default ='user_image/profile_pic.png')
    skills = models.CharField(max_length=500)
    email = models.EmailField(default="")
    phone_no = models.PositiveIntegerField(unique=True)
    address = models.CharField(max_length=200)
    # education = models.ForeignKey(Education, on_delete= models.CASCADE, default=0)
    # experience = models.ForeignKey(Experience,related_name='experience', on_delete= models.CASCADE, default=0)
    
    # React project
    password = models.CharField(max_length=10,default="" ) 


    def __str__(self):
        return self.full_name


class Education(models.Model):
    institute_name = models.CharField(max_length=100)
    degree = models.CharField(max_length=50)
    start_year = models.DateField()
    end_year = models.DateField()
    percentage = models.IntegerField()
    stream = models.CharField(max_length=50)
    userProfile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, default=None)

class Experience(models.Model):
    type = models.CharField(max_length=50, choices=(('Internship','Internship'),('Job','Job')))
    profile = models.CharField(max_length=100)
    organization = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    location = models.CharField(max_length=50)
    description = models.TextField()
    currently_working = models.BooleanField(default=False)
    userProfile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.type+"("+self.profile+")"

class Application(models.Model):
    userProfile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    internship = models.ForeignKey(Internship, on_delete=models.CASCADE)
    applyDate = models.DateField(default=timezone.now)



class UploadImage(models.Model):
    userId = models.ForeignKey(to = 'UserProfile', on_delete = models.CASCADE)
    image = models.CharField(max_length=100)


class Demouser(models.Model):
    uId = models.UUIDField(primary_key=True,  default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=50)


class Demo(models.Model):
    date = models.DateField(default = datetime.datetime.now)
#     date = forms.DateField(
#     localize=True,
#     widget=forms.DateInput(format = '%d-%m-%y',attrs={'type': 'date'}),
# )
    text = models.TextField(max_length=500, default="")
    app = models.ForeignKey(Application, default=6, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="user_image", default ='user_image/profile_pic.png')



    






