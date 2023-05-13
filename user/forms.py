# from cProfile import label
# from django import forms
# from .models import User 

# class RegistraionForm(forms.Form):
#     user_name = forms.CharField(label='Username ', min_length=5, max_length=15, label_suffix=' ', error_messages={'required': 'Enter Usernane '})
#     name = forms.CharField(label='Name  ', min_length=5, max_length=15, label_suffix=' ', error_messages={'required': 'Enter Name '})
#     email = forms.EmailField(label='Email ', min_length=12, max_length=30 , label_suffix=' ', error_messages={'required': 'Enter Email '})
#     password = forms.CharField(label='Password ', widget=forms.PasswordInput, label_suffix= ' ' , error_messages={'required': 'Enter Password '})
#     re_password = forms.CharField(label='Password(Again) ', widget=forms.PasswordInput, label_suffix=' ',  error_messages={'required': 'Enter Password '})

#     def clean(self):
#         cleaned_data = super().clean()
#         password1 = self.cleaned_data.get('password')
#         password2 = self.cleaned_data.get('re_password')
#         if password1 and password2: 
#             if password1 != password2:
#                 # raise forms.ValidationError('Password Not Matched')
#                 self.add_error('re_password', "passwords do not match !")

#         user_name = self.cleaned_data.get('user_name')
#         if user_name:
#             user_query_set = User.objects.filter(user_name=user_name)
#             if user_query_set:
#                 self.add_error('user_name', 'Username  is already exist try different one ')

#         user_email = self.cleaned_data.get('email')
#         if user_email:
#             user_query_set = User.objects.filter(email=user_email)
#             if user_query_set:
#                 self.add_error('email', 'Email is already exist try different one ')        

                
                
                

# class LoginForm(forms.Form):
#     email  = forms.EmailField(label='Email ', label_suffix=' ',min_length=4, max_length=50,  error_messages={'required': 'Enter Usernane '} )
#     password = forms.CharField(label='Password', widget=forms.PasswordInput, label_suffix= ' ',  error_messages={'required': 'Enter Password '})


# class ProfileForm(forms.Form):
#     pic = forms.ImageField(label='Image', label_suffix=' ', required=False)
#     user_name = forms.CharField(label='Username', label_suffix='  ',min_length=5, max_length=15 , disabled = True)
#     email = forms.EmailField(label='Email', min_length=12, max_length=30 , label_suffix='  ', disabled = True)
#     user_about = forms.CharField(label='Author About ',label_suffix='  ', max_length=500, required=False)
    

#     # def clean(self):
#     #     user_name = self.cleaned_data.get('user_name')
#     #     if user_name:
#     #         user_query_set = User.Users.filter(user_name=user_name)
#     #         if user_query_set:
#     #             self.add_error('user_name', 'Username  is already exist try different one ')

#     #     user_email = self.cleaned_data.get('email')
#     #     if user_email:
#     #         user_query_set = User.Users.filter(email=user_email)
#     #         if user_query_set:
#     #             self.add_error('email', 'Email is already exist try different one ')        
