from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _


class Role(models.Model):
	name = models.CharField(max_length=100)

	def __str__(self):
		return self.name


class Employee(AbstractUser):
    role = models.ForeignKey(Role, null=True, blank=True)
    skype_id = models.CharField(max_length=200, null=True, blank=True)
    last_month_score = models.PositiveIntegerField(default=0)
    current_month_score = models.PositiveIntegerField(default=0)
    level = models.PositiveIntegerField(default=0)
    total_score = models.PositiveIntegerField(default=0)
    avatar = models.ImageField(upload_to='avatar', null=True, blank=True)
		