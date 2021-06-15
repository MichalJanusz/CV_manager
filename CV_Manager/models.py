from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.utils.translation import ugettext_lazy as _
from datetime import date


# Create your models here.

class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    """User model."""

    username = None
    email = models.EmailField(
        _('email address'),
        unique=True,
        error_messages={
            'unique': _("A user with that email already exists."),
        },
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email


class Application(models.Model):
    """Application model."""

    position = models.CharField(max_length=64)
    company = models.CharField(max_length=128)
    location = models.CharField(max_length=64)
    description = models.TextField(max_length=500)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='applications')

    SENT = 1
    VIEWED = 2
    EXAMINATION = 3
    ONGOING = 4
    HIRED = 5
    REJECTED = 6
    DECLINED = 7
    NO_RESPONSE = 8

    STATUS_CHOICES = [
        (SENT, 'Application Sent'),
        (VIEWED, 'Application Viewed'),
        (EXAMINATION, 'Application is examined'),
        (ONGOING, 'Recruitment in progress'),
        (HIRED, 'Hired'),
        (REJECTED, 'Rejected'),
        (DECLINED, 'Offer declined'),
        (NO_RESPONSE, 'No response from the company'),
    ]
    status = models.IntegerField(choices=STATUS_CHOICES, default=1)
    date = models.DateField(default=date.today)

    DIRECT_MAIL = 'Direct Mail'
    LINKEDIN = 'LinkedIn'
    JUSTJOINIT = 'JustJoinIT'
    NOFLUFFLJOBS = 'No Fluff Jobs'
    OTHER = 'Other'

    METHOD_CHOICES = [
        (DIRECT_MAIL, 'Direct Mail'),
        (LINKEDIN, 'LinkedIn'),
        (JUSTJOINIT, 'JustJoinIT'),
        (NOFLUFFLJOBS, 'No Fluff Jobs'),
        (OTHER, 'Other'),
    ]

    method = models.CharField(max_length=64, choices=METHOD_CHOICES, blank=True)
    remote = models.BooleanField()
    comment = models.TextField(max_length=200)

    def __str__(self):
        return f"Application for {self.position} in {self.company}"
