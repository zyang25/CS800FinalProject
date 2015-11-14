from django.utils import timezone
import datetime
from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

class MyUserManager(BaseUserManager):
    
    def create_user(self, email, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        """
        Creates and saves a superuser with the given email, password.
        """
        user = self.create_user(email,
            password=password,
        )
        user.is_active = True
        user.is_admin = True
        user.is_vertified = True
        user.is_poster = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    is_active = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_vertified = models.BooleanField(default=False)
    is_poster = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'

    def get_full_name(self):
        # The user is identified by their email address
        return self.email

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    def __str__(self):              # __unicode__ on Python 2
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

class UserActivation(models.Model):
    user = models.OneToOneField(MyUser)
    activation_key = models.CharField(max_length=40, blank=True)
    key_expires = models.DateTimeField()
      
    def __str__(self):
        return self.user.email

    class Meta:
        verbose_name_plural=u'User activation'


class UserInfo(models.Model):
    owner = models.OneToOneField(MyUser, primary_key=True)
    first_name = models.CharField(max_length=35,blank=True)
    last_name = models.CharField(max_length=35,blank=True)
    address = models.CharField(max_length=254,blank=True)
    city = models.CharField(max_length=35,blank=True)
    zipcode = models.CharField(max_length=10,blank=True)
    title = models.CharField(max_length=15,blank=True)
    phone_number = models.CharField(max_length=15, blank=True)
    wechat_number = models.CharField(max_length=15,blank=True)
    introduction = models.TextField(blank=True)

    def __str__(self):
        return self.owner.email

    class Meta:
        verbose_name_plural=u'User information'
