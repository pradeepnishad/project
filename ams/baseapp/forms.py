from .models import *
from django.forms.models import ModelForm
from django.forms.widgets import FileInput
from django import forms



class ImageUploadForm(forms.Form):
    title = forms.CharField(max_length=255)
    image = forms.ImageField()



class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        field =  '__all__'
        exclude = ['user']
    
    COURSES_CHOICES= [
    ('Bachelor of Science in Computer Science', 'Bachelor of Science in Computer Science'),
    ('Bachelor of Science in Information technology', 'Bachelor of Science in Information technology'),
    ('Bachelor of Management Studies', 'Bachelor of Management Studies'),
    ('Bachelor of Accounts and Finance', 'Bachelor of Accounts and Finance'),
    ]  

    name = forms.CharField(
        widget=forms.TextInput(attrs={'class':'form-control','type':'text'}),
    )
    phone = forms.CharField(
        widget=forms.TextInput(attrs={'class':'form-control','type':'text'}),
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class':'form-control','type':'email'}),
    )
    course = forms.ChoiceField(
        choices= COURSES_CHOICES,
        widget=forms.Select(attrs={'class':'form-select'    }),
    )

    profile_img = forms.ImageField(
        widget=forms.FileInput(attrs={'class': 'form-control'}),
        
    )

class PersonalDetailsForm(forms.ModelForm):
    class Meta:
        model = PersonalDetails
        field =  '__all__'
        exclude = ['user','created_at']


    GENDER_CHOICES = [
    ('SELECT YOUR GENDER', 'SELECT YOUR GENDER'),   
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Other', 'Other'),
    ]

    MARTIAL_STATUS = [
        ('Married', 'Married'),
        ('Unmarried', 'Unmarried'),
        ('Divorced','Divorced'),
        ('Widowed','Widowed'),
        
    ]    
    name = forms.CharField(
        widget=forms.TextInput(attrs={'class':'form-control','type':'text'}),
    )

    date_of_birth = forms.DateField(
        widget=forms.DateInput(attrs={'class': 'form-control', 'type':'date' }),
        
    )

    alternative_phone = forms.CharField(
        widget=forms.TextInput(attrs={'class':'form-control','type':'text'}),
    )

    parent_phone = forms.CharField(
        widget=forms.TextInput(attrs={'class':'form-control','type':'text'}),
    )

    gender = forms.ChoiceField(
        choices= GENDER_CHOICES,
        widget=forms.Select(attrs={'class':'form-select'}),
    )

    address = forms.CharField(
        widget=forms.Textarea(attrs={'rows':4,'cols':50 ,'class':'form-control'}),
    )

    district = forms.CharField(
        widget=forms.TextInput(attrs={'class':'form-control','type':'text'}),
    )

    tehsil = forms.CharField(
        widget=forms.TextInput(attrs={'class':'form-control','type':'text'}),
    )

    mother_tongue = forms.CharField(
        widget=forms.TextInput(attrs={'class':'form-control','type':'text'}),
    )

    martial_status = forms.ChoiceField(
        choices= MARTIAL_STATUS,
        widget=forms.Select(attrs={'class':'form-select'}),
    )

    nationality = forms.CharField(
        widget=forms.TextInput(attrs={'class':'form-control','type':'text'}),
    )

    state_of_domicile = forms.CharField(
        widget=forms.TextInput(attrs={'class':'form-control','type':'text'}),
    )

    adhaar_number= forms.CharField(
        widget= forms.TextInput(attrs={'class':'form-control','type':'text'})
    )


class AcademicDetailsForm(forms.ModelForm):
    class Meta:
        model = AcademicDetails
        field =  '__all__'
        exclude = ['user']
    
    SSC_BOARD_CHOICES = [
     ('SELECT YOUR BOARD', 'SELECT YOUR BOARD'),   
    ('Maharashtra state board (SSC)', 'Maharashtra state board (SSC)'),
    ('Other state board', 'Other state board'),
    ('Central Board of Secondary Education (CBSE)', 'Central Board of Secondary Education (CBSE)'),
    ('Indian Certificate of Secondary Education (ICSE)', 'Indian Certificate of Secondary Education (ICSE)'),
    ('Council for the Indian School Certificate Examination (CISCE)', 'Council for the Indian School Certificate Examination (CISCE)'),
    ('National Institute of Open Schooling (NIOS)', 'National Institute of Open Schooling (NIOS)'),
    ('International Baccalaureate (IB)', 'International Baccalaureate (IB)'),
    ('Cambridge International Examinations (CIE)', 'Cambridge International Examinations (CIE)'),
    ]

    CLASS_GRADE = [
        ('SELECT YOUR CLASS GRADESG', 'SELECT YOUR CLASS GRADE'),
        ('Distinctive class', 'Distinctive class'),
        ('First class', 'First class'),
        ('Second class', 'Second class'),
    ]

    HSC_BOARD_CHOICES = [
        ('SELECT YOUR BOARD', 'SELECT YOUR BOARD'),
        ('Maharashtra state board (HSC)', 'Maharashtra state board (HSC)'),
        ('Other state board', 'Other state board'),
        ('All India Senior School Certificate Examination (AISSCE)' ,'All India Senior School Certificate Examination (AISSCE)'),
        ('Indian Certificate of Secondary Education (ICSE)', 'Indian Certificate of Secondary Education (ICSE)'),
        ('National Institute of Open Schooling (NIOS)', 'National Institute of Open Schooling (NIOS)'),
        ('International Baccalaureate (IB)', 'International Baccalaureate (IB)'),     
    ]
    ssc_school_name = forms.CharField(
        widget=forms.TextInput(attrs={'class':'form-control','type':'text'}),
    )

    ssc_school_board = forms.ChoiceField(
        choices= SSC_BOARD_CHOICES,
        widget=forms.Select(attrs={'class':'form-select'}),
    )

    ssc_passing_year = forms.DateField(
        widget=forms.DateInput(attrs={'class': 'form-control', 'type':'date' }),
        
    )

    ssc_rollno = forms.CharField(
        widget=forms.TextInput(attrs={'class':'form-control','type':'text'}),
    )

    ssc_marks = forms.CharField(
        widget=forms.TextInput(attrs={'class':'form-control','type':'text'}),
    )

    ssc_class_grade = forms.ChoiceField(
        choices= CLASS_GRADE,
        widget=forms.Select(attrs={'class':'form-select'}),
    )

    ssc_class_percent = forms.IntegerField(
        widget= forms.TextInput(attrs={'class':'form-control'})
    )

    # hsc

    hsc_school_name = forms.CharField(
        widget=forms.TextInput(attrs={'class':'form-control','type':'text'}),
    )

    hsc_school_board = forms.ChoiceField(
        choices= HSC_BOARD_CHOICES,
        widget=forms.Select(attrs={'class':'form-select'}),
    )

    hsc_passing_year = forms.DateField(
        widget=forms.DateInput(attrs={'class': 'form-control', 'type':'date' }),
        
    )

    hsc_rollno = forms.CharField(
        widget=forms.TextInput(attrs={'class':'form-control','type':'text'}),
    )

    hsc_marks = forms.CharField(
        widget=forms.TextInput(attrs={'class':'form-control','type':'text'}),
    )

    hsc_class_grade = forms.ChoiceField(
        choices= CLASS_GRADE,
        widget=forms.Select(attrs={'class':'form-select'}),
    )

    hsc_class_percent = forms.IntegerField(
        widget= forms.TextInput(attrs={'class':'form-control'})
    )

    hsc_maths_mark = forms.IntegerField(
        widget= forms.TextInput(attrs={'class':'form-control'})
    )
# CategoryDetails
class CategoryDetailsForm(forms.ModelForm):
    class Meta:
        model = CategoryDetails
        field =  '__all__'
        exclude = ['user']

    CATEGORY_CHOICES = [
        ('General class', 'General class'),
        ('OBC class', 'OBC class'),
        ('ST class', 'ST class'),
        ('SC class', 'SC class'),
    ]

    category =  forms.ChoiceField(
        choices= CATEGORY_CHOICES,
        widget=forms.Select(attrs={'class':'form-select'}),
    )           

    science = forms.BooleanField(
        widget=forms.CheckboxInput(attrs={'class': 'stream form-check-input'}),
        required=False  
    ) 

    commerce = forms.BooleanField(
        widget=forms.CheckboxInput(attrs={'class': 'stream form-check-input'}),
        required=False  
    ) 

    art = forms.BooleanField(
        widget=forms.CheckboxInput(attrs={'class': 'stream form-check-input'}),
        required=False 
    ) 

    minority = forms.BooleanField(
        widget=forms.CheckboxInput(attrs={'class': 'custom-checkbox form-check-input'}),
        required=False 
    ) 

    physically = forms.BooleanField(
        widget=forms.CheckboxInput(attrs={'class': 'custom-checkbox form-check-input    '}),
        required=False  
    ) 


class DocumentDetailsForm(forms.ModelForm):
    class Meta:
        model = DocumentDetails
        field =  '__all__'
        exclude = ['user']
     
    
