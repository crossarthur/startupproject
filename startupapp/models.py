from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=25)
    email = models.EmailField()
    phone = models.CharField(max_length=11)
    description = models.TextField(max_length=250)

    def __str__(self):
        return self.name


class Courses(models.Model):
    course_name = models.CharField(max_length=150, primary_key=True)
    image = models.ImageField(upload_to='course', blank=True, null=True)
    course_fee = models.IntegerField()
    course_duration = models.IntegerField(default=0)
    syllabus = RichTextField(default='syllabus')
    about_course = RichTextField(default='about_course')
    stars = models.IntegerField(default=3)

    def __str__(self):
        return self.course_name


class Trainer(models.Model):
    trainer_name = models.CharField(max_length=50)
    trainer_designation = models.CharField(max_length=100)
    trainer_experience = models.DecimalField(max_digits=5, decimal_places=2)
    course = models.ForeignKey(Courses, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.trainer_name


class Register(models.Model):
    candidate_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    Phone_number = models.CharField(max_length=20)
    alternate_number = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    college_name = models.CharField(max_length=120)
    address = models.TextField(max_length=200)
    street = models.CharField(max_length=120)
    city = models.CharField(max_length=120)
    pincode = models.IntegerField()
    computer_knowledge = models.CharField(max_length=50)
    course = models.CharField(max_length=20, default=1)
    timestamp = models.DateField(auto_now_add=True)
    trainer = models.ForeignKey(Trainer, on_delete=models.DO_NOTHING, null=True)

    def __str__(self):
        return self.email


class Payments(models.Model):
    name = models.ForeignKey(Register, on_delete=models.CASCADE)
    amount_paid = models.IntegerField()
    balance = models.IntegerField()
    status = models.BooleanField(default=False)


class Attendance(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    date = models.CharField(max_length=50)
    logintime = models.CharField(max_length=50)
    logouttime = models.CharField(max_length=50)
    approve = models.BooleanField(default=False)

    def __str__(self):
        return self.email
