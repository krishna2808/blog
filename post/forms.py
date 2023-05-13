
# from urllib.robotparser import RequestRate
# from .models import Post
# from django import forms 


# class AddPost(forms.ModelForm):
#     # pic = forms.ImageField(label='Add Image ', label_suffix='' , error_messages=  {'required': 'Add images ', } )
    
#     def __init__(self, *args, **kwargs):
#         super(AddPost, self).__init__(*args, **kwargs)
#         self.label_suffix = ' '


#     class Meta:
#         model = Post
#         fields = ['post_title', 'pic',  'post_discription']
#         labels = {'post_title': 'Title ', 'pic':  'Add Image', 'post_discription': 'Discription '}
#         error_messages  = {'post_title' : {'required': 'Add title ', },
#                             'pic' : {'required': 'Add images ', },
                        
#                             'post_discription' : {'required': 'Add Post Discription ', },
#                           }
                
# class EditPost(forms.ModelForm):
#     def __init__(self, *args, **kwargs):
#         super(EditPost, self).__init__(*args, **kwargs)
#         self.label_suffix = ' '


#     class Meta:
#         model = Post
#         fields = ['post_title',   'post_discription']
#         labels = {'post_title': 'Title ', 'post_discription': 'Discription '}
#         error_messages  = {'post_title' : {'required': 'Add title ', },
#                             'post_discription' : {'required': 'Add Post Discription ', },
#                           }
