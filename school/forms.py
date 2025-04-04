from django import forms
from django.core import validators
from .models import departments,students,teachers
# from .forms import Meta_1,Meta_2

# class loginform(forms.Form):
#     Name = forms.CharField(
#         widget=forms.TextInput(
#         attrs={
#             "type":"text",
#             "placeholder":"Enter Your Name",
#             "class":"form-control",
#             "autocomplete":"off",
#             "autofocus":"on"
            
#         }
#     ))
#     Lastname = forms.CharField(widget=forms.TextInput(
#         attrs={
#             "type":"text",
#             "placeholder":"Enter Your Lastname",
#             "class":'form-control',
#             "autocomplete":"off",
            

#         }
#     ))
#     Email = forms.EmailField(widget=forms.EmailInput(
#         attrs={
#             "placeholder":"Enter Your Email",
#             "class":"form-control",
#             "type":"text",
#             "autocomplete":"off",
          

#         }
    
#     ))




# class Meta_2:
#     model = students
#     fields = ['firstname','lastname','middelname','mobile']
#     widgets = {
#         'firstname':forms.TextInput(attrs={'class':'form-control','placeholder':"Enter Firstname"}),
#         'middelename':forms.TextInput(attrs={'class':'form-control','placeholder':"Enter Middlename"}),
#         'lastname':forms.TextInput(attrs={'class':'forms-control',"placeholder":"Enter Lastname"}),
#         'mobile':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Mobile Number'})
#     }
# class department_form(forms.ModelForm):
#     class Multimodelform(forms.ModelForm):
#         class Meta(Meta_1,Meta_2):
#             pass



class department_form(forms.ModelForm):
    class Meta:
        model = departments
        fields = ['depname','depcode']
        widgets = {
            'depname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Department Name'}),
            'depcode': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Enter Department Code'})
            
        }
        labels = {
            'depname': 'Department Name',
            'depcode': 'Department Code',
        }

class teacher_form(forms.ModelForm):
    class Meta:
        model = teachers
        fields = ['firstname','lastname','emailid','mobile','designation','dep','photo']
        widgets = {
            'firstname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Firstname'}),
            # 'middlename': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Enter Middlename '}),
            'lastname': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Enter Lastname'}),

            'mobile': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Enter Mobile Number'}),
            'emailid':forms.EmailInput(attrs={'class': 'form-control', 'placeholder':'Enter Email ID'}),
            'designation':forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Enter Designation'}),
            'dep': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Enter Department'}),

            
        }
        labels = {
            'firstname': 'First Name',
            'lastname': 'Last Name',
            # 'middlename': 'Middle Name',
            'mobile': 'Mobile',
            'emailid':'Email ID',
            'dep': 'Department',
            'photo':'Choose Photo',
            'designation':'Designation'

        }


class student_form(forms.ModelForm):
    class Meta:
        model = students
        fields = ['firstname','middlename','lastname','housename','fathername','mobile','depart']
        widgets = {
            'firstname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Firstname'}),
            'middlename': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Enter Middlename '}),
            'lastname': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Enter Lastname'}),

            'housename': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Enter Address '}),
            'fathername': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Enter Parent Name '}),


            'mobile': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Enter Mobile Number'}),
            'depart': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Enter Department'})

            
        }
        labels = {
            'firstname': 'First Name',
            'lastname': 'Last Name',
            'middlename': 'Middle Name',
            'housename': 'Address',
            'fathername': 'Parent Name',
            'mobile': 'Mobile',
            'depart': 'Department',
        }

