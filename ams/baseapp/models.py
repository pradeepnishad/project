from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
import uuid
# Create your models here.


User = get_user_model()

class UserProfile(models.Model):

    

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    course = models.CharField(max_length=50, blank=False)
    profile_img = models.ImageField(default='media/default.jpg', upload_to='media',null=True, blank=True)
    


    def __str__(self):
        return f'{self.user.username} profile'


# User main form

# personal detail

class PersonalDetails(models.Model):
    
    
    

    user = models.OneToOneField(User, on_delete= models.CASCADE)
    name =  models.CharField(max_length=40)
    gender = models.CharField(max_length=30)
    alternative_phone = models.CharField(max_length=10)
    parent_phone =  models.CharField(max_length=10)
    address = models.TextField(max_length= 500)
    district = models.CharField(max_length=20)
    tehsil = models.CharField(max_length=20)
    date_of_birth = models.DateField( 'Date of birth (yyyy-mm-dd):', null=True, blank=True)
    mother_tongue = models.CharField(max_length=15)
    martial_status = models.CharField(max_length=30)
    nationality = models.CharField(max_length=15)
    state_of_domicile = models.CharField(max_length=25)
    adhaar_number = models.CharField(max_length= 15)
    created_at = models.DateTimeField( auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} Personal details.'

class AcademicDetails(models.Model):


    user = models.OneToOneField(User, on_delete= models.CASCADE)
    ssc_school_name = models.CharField(max_length=30)
    ssc_school_board = models.CharField(max_length=50)
    ssc_passing_year = models.DateField(max_length=10,null=True)
    ssc_rollno = models.CharField(max_length=6)
    ssc_marks = models.CharField(max_length=3)
    ssc_class_grade = models.CharField(max_length=30 ,null=True, blank=True)
    ssc_class_percent = models.IntegerField(null=True , blank= True)

    hsc_school_name = models.CharField(max_length=30)
    hsc_school_board = models.CharField(max_length=50)
    hsc_passing_year = models.DateField(max_length=10,null=True)
    hsc_rollno = models.CharField(max_length=6)
    hsc_marks = models.CharField(max_length=3)
    hsc_class_grade = models.CharField(max_length=30, null=True, blank=True)
    hsc_class_percent = models.IntegerField(null=True , blank=True)
    hsc_maths_mark = models.IntegerField(null=True, blank= True)

    def __str__(self):
        return f'{self.user.username} Academic details.'
    


class CategoryDetails(models.Model):
    
   

    user = models.OneToOneField(User, on_delete= models.CASCADE )
    category = models.CharField(max_length= 30)
    science = models.BooleanField(null=True)
    commerce = models.BooleanField(null=True)
    art = models.BooleanField(null=True)
    minority = models.BooleanField(null=True)
    physically = models.BooleanField('Physically chanlleged',null=True)


    def __str__(self):
        return f'{self.user.username} Category details.'


# document upload
class DocumentDetails(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE)
    signature = models.FileField(upload_to='media',null=False, blank=False)
    uniform = models.FileField(upload_to='media',null=False, blank=False)
    hsc_result = models.FileField(upload_to='media',null=False, blank=False)
    reservation_certificate = models.FileField('Reservation Certificate',upload_to='media',null=True, blank=True)
    pc_certificate = models.FileField('Physically Challeged Certificate',upload_to='media',null=True, blank=True)

    def __str__(self):
        return f'{self.user.username} Documents details.'






 # enquiry database models   
class Contact(models.Model):
    name = models.CharField(max_length=20, null= True, blank= True)
    number = models.CharField(max_length= 10)
    message = models.TextField(max_length=500, blank= False)

    def __str__(self):
        return self.name 
    
#notice database models

class bsccsnotice(models.Model):
    notice = models.CharField(max_length=400, null=False)
    link = models.URLField(null=True, blank=True)
    

    def __str__(self):
        return self.notice

class bscitnotice(models.Model):
    notice = models.CharField(max_length=400, null=False)
    link = models.URLField(null=True, blank=True)
    

    def __str__(self):
        return self.notice
    
class bmsnotice(models.Model):
    notice = models.CharField(max_length=400, null=False)
    link = models.URLField(null=True, blank=True)
   

    def __str__(self):
        return self.notice
    
class bafnotice(models.Model):
    notice = models.CharField(max_length=400, null=False)
    link = models.URLField(null=True, blank=True)
    

    def __str__(self):
        return self.notice




# ui changer
class change_1(models.Model):
    college_name = models.CharField(max_length= 10, null= False)
    admission_desk_number = models.CharField(max_length=12, null= False)
    college_tel_number_1 = models.CharField(max_length = 10, null = False)
    college_tel_number_2 = models.CharField(max_length = 10, null = False)
    college_email = models.EmailField()
    college_map_link = models.URLField(null=True, blank=True)
    college_img_1 = models.ImageField(default='media/default.jpg', upload_to='media',null=True, blank=True)
    college_img_2 = models.ImageField(default='media/default.jpg', upload_to='media',null=True, blank=True)
    college_img_3 = models.ImageField(default='media/default.jpg', upload_to='media',null=True, blank=True)
    college_img_4 = models.ImageField(default='media/default.jpg', upload_to='media',null=True, blank=True)
    college_logo = models.ImageField(default='media/default.jpg', upload_to='media',null=True, blank=True)
    for_career_email = models.EmailField()

    def __str__(self):
        return self.college_name


#test models
class ImageModel(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='media')



