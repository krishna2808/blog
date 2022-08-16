from django.contrib import admin
from .models import User, Friend
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Register your models here.

@admin.register(User)
class AuthenticationAdmin(BaseUserAdmin):

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('id', 'email', 'name', 'user_name',  'user_about',   'image', 'is_admin', 'password')
    list_filter = ('is_admin',)
    fieldsets = (
        ('User Credentials', {'fields': ('email','password')}),
        ('Personal info', {'fields': ('user_name', 'name', 'image', 'user_about')}),
        ('Permissions', {'fields': ('is_admin',)}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'name','user_about',  'password1', 'password2'),
        }),
    )
    search_fields = ('email',)
    ordering = ('email', 'name')
    filter_horizontal = ()
    
    
@admin.register(Friend)
class FriendAdmin(admin.ModelAdmin):
    
    list_display = ('current_user', 'friend', 'friend_request', 'request_date')