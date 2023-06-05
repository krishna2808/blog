


from django.db import models

from django.db import models
import datetime 

# Create your models here.
from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)



class CustomUserManager(BaseUserManager):
    def create_user(self, email, user_name, first_name = None, last_name = None, user_about=None,  password=None, password2=None):
        """
        Creates and saves a User with the given email, name, address,  and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            first_name = first_name,
            last_name = last_name,
            user_name  = user_name,
            user_about = user_about, 
            # image = image
            
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, user_name,first_name = None, last_name =None, user_about=None,  password=None, password2=None):
        """
        Creates and saves a superuser with the given email, name, address, image, and password.
        """
        user = self.create_user(
            email,
            first_name = first_name,
            last_name = last_name,
            user_name  = user_name,
            user_about = user_about, 
            # image = image
            
        )
        user.set_password(password)
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    user_name = models.CharField(max_length=50)
    user_about = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(null=True,blank=True, default='default.png'   ,upload_to='image/profile/'+ str(datetime.datetime.now()).replace(' ', '-') )
    
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'user_name']

    def __str__(self):
        return self.user_name

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return self.is_admin

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin


class Friend(models.Model):
    current_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="follower")
    friend = models.ForeignKey(User, on_delete=models.CASCADE, related_name="following")
    friend_request = models.IntegerField(default=-1)
    request_date = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return str(self.current_user.user_name) + '  '+  str(self.friend.user_name)
    
    
    class Meta: 
      ordering = ['-request_date']
    
    



# class User(models.Model):
#     user_name = models.CharField(max_length=25, unique=True)
#     email = models.EmailField(max_length=40, unique=True)
#     password = models.CharField(max_length=20)
#     # pic = models.ImageField(null=True, upload_to='images/profile/')
#     pic = models.ImageField(null=True, upload_to='images/profile/%Y/%m/%d/%T')

#     author_about = models.TextField(null=True)


#     def __str__(self):
#        return self.user_name
    
#     # Change model manager 
#     Users = models.Manager()
