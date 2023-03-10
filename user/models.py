from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    email = models.EmailField(unique=True)
    is_student = models.BooleanField(default=False)
    is_staff_user = models.BooleanField(default=False)
    is_hod = models.BooleanField(default=False)

    def __str__(self):
        return self.username

class Level(models.Model):
    level = models.CharField(max_length=2555)
    school_fees = models.FloatField(default=100000.00)

class HODUser(models.Model):
    title_list = (
        ("Dr.", "Dr."),
        ("Dr. Mrs.", "Dr. Mrs."),
        ("Professor", "Professor"),
        ("Mr.", "Mr."),
        ("Mrs.", "Mrs.")
    )
    title = models.CharField(max_length=255, choices=title_list, default="Mr.")
    hod_user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.TextField(default="ogbomosho")
    phone = models.PositiveBigIntegerField(default=8011223344)

    def get_phone_number(self):
        return "+234" + self.phone

    def __str__(self):
        return self.title + " " + self.hod_user.first_name + " " + self.hod_user.last_name

class Department(models.Model):
    dept_name = models.CharField(max_length=1000000, blank=True, null=True, verbose_name="Department Name")
    dept_code = models.CharField(max_length=2550, blank=True, null=True, verbose_name="Department Name")
    cordinator = models.ForeignKey(HODUser, null=True, blank=True, on_delete=models.SET_NULL)

class StudentUser(models.Model):
    #student_user_list = User.objects.filter(is_student=True)
    student_user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='students/profile_pics')
    gender_type =(
        ("Male", "Male"),
        ("Female", "Female"),
        ("Others", "Others"),
    )
    gender = models.CharField(max_length=255, choices=gender_type, default="Male")
    dob = models.DateField()
    address = models.TextField(default="ogbomosho")
    phone = models.PositiveBigIntegerField(default=8011223344)
    admission_year = models.DateField()
    department = models.ForeignKey(Department, on_delete=models.DO_NOTHING)
    current_level = models.ForeignKey(Level, on_delete=models.DO_NOTHING)

    def get_phone_number(self):
        return "+234" + self.phone

class StaffUser(models.Model):
    staff_user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='staff/profile_pics')
    title_list = (
        ("Dr.", "Dr."),
        ("Dr. Mrs.", "Dr. Mrs."),
        ("Professor", "Professor"),
        ("Mr.", "Mr."),
        ("Mrs.", "Mrs.")
    )
    title = models.CharField(max_length=255, choices=title_list, default="Mr.")
    address = models.TextField(default="ogbomosho")
    phone = models.PositiveBigIntegerField(default=8011223344)
    appointment_year = models.DateField(verbose_name="Year of Appointment")
    department = models.ForeignKey(Department, on_delete=models.DO_NOTHING)

    def get_phone_number(self):
        return "+234" + self.phone
    
    def __str__(self):
        return self.title + " " + self.staff_user.first_name + " " + self.staff_user.last_name