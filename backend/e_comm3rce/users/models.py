from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError("User must have an email")
        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password):
        user = self.create_user(email, password)
        user.is_staff = True
        user.save()
        return user


class User(AbstractBaseUser):
    email = models.EmailField(
        unique=True, max_length=255, verbose_name='E-Mail')
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'

    def __str__(self) -> str:
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True


class Customer(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, verbose_name='User')
    first_name = models.CharField(max_length=255, verbose_name="First name")
    last_name = models.CharField(
        max_length=255, verbose_name="Last name")
    phone_number = PhoneNumberField(unique=True, null=True, blank=True, verbose_name='Phone number')

    def __str__(self):
        return self.user.email

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'
