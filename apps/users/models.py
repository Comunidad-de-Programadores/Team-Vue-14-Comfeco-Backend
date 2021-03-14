from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from .managers import UserManager
from django.utils.translation import ugettext_lazy as _
from apps.core.models import CoreTimeModel
from .constants import CHOICES_AREA

# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    first_name = models.CharField(_('first name'), max_length=120, blank=True)
    last_name = models.CharField(_('last name'), max_length=120, blank=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Designates whether the user can log into this admin site.'),
    )
    objects = UserManager()
    birth_day = models.DateField(null=True, blank=True)
    area = models.CharField(max_length=255, choices=CHOICES_AREA)
    country = models.CharField(max_length=255)
    gender = models.CharField("gender", max_length=250)
    facebook = models.CharField("facebook", max_length=250)
    github = models.CharField("github", max_length=250)
    linkedin = models.CharField("linkedin", max_length=250)
    twitter = models.CharField("twitter", max_length=250)
    biography = models.TextField(max_length=140)

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email


class UserEvent(CoreTimeModel):
    user = models.ForeignKey("User", on_delete=models.CASCADE, related_name="user_events")
    event = models.ForeignKey("events.Event", on_delete=models.CASCADE, related_name="events_user")

    class Meta:
        """Meta definition for UserEvent."""

        verbose_name = 'UserEvent'
        verbose_name_plural = 'UserEvents'
        unique_together = ('user', 'event')

    def __str__(self):
        """Unicode representation of UserEvent."""
        return '{0} - {1}'.format(self.user.email, self.event.name)


class UserGroup(CoreTimeModel):
    user = models.ForeignKey("User", on_delete=models.CASCADE, related_name="user_groups")
    group = models.ForeignKey("groups.Group", on_delete=models.CASCADE, related_name="group_users")

    class Meta:
        """Meta definition for UserEvent."""

        verbose_name = 'UserEvent'
        verbose_name_plural = 'UserEvents'
        unique_together = ('user', 'group')
        
    def __str__(self):
        """Unicode representation of UserEvent."""
        return '{0} - {1}'.format(self.user.email, self.group.name)
