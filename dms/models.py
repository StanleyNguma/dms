from __future__ import unicode_literals

from django.db import models


# Define the Alpha_dms modules here


class Users(models.Model):
    first_name = models.CharField(max_length=20)
    middle_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=255)
    email = models.CharField(max_length=45, unique=True)
    phone_no = models.CharField(max_length=20, default=None)
    group_id = models.IntegerField()
    company_id = models.IntegerField()
    maker = models.IntegerField()
    date_created = models.DateTimeField(auto_created=True)
    date_modified = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'alpha_users'  # this is the name of the database table


class UserGroups(models.Model):
    name = models.CharField(max_length=45)
    description = models.CharField(max_length=255)
    company_id = models.IntegerField()
    maker = models.IntegerField()
    date_created = models.DateTimeField(auto_created=True)
    date_modified = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'alpha_user_groups'


class Folder(models.Model):
    name = models.CharField(max_length=255)


class File(models.Model):
    name = models.CharField(max_length=255)
    dms_name = models.CharField(max_length=255)
    size = models.CharField(max_length=20)
    type = models.CharField(max_length=50)

