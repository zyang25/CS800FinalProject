from django.utils import timezone
from django.conf import settings
import datetime
from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from django.contrib.auth.signals import user_logged_in, user_logged_out, user_login_failed
import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY


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



class userStripe(models.Model):
    user = models.OneToOneField(MyUser)
    stripe_id = models.CharField(max_length=200, null=True, blank=True)

    def __unicode__(self):
        if self.stripe_id:
            return str(self.stripe_id)
        else:
            return self.user.email

def stripeCallback(sender, request, user, **kwargs):
    user_stripe_account, created = userStripe.objects.get_or_create(user=user)
    if created:
        print 'created for %s'%(user.email)

    if user_stripe_account.stripe_id is None or user_stripe_account.stripe_id == '':
        new_stripe_id = stripe.Customer.create(email = user.email)
        user_stripe_account.stripe_id = new_stripe_id['id']
        user_stripe_account.save()

user_logged_in.connect(stripeCallback)



