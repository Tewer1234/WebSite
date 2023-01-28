# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    first_name = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Browsetable(models.Model):
    transcriptid = models.TextField(db_column='TranscriptID', blank=True, primary_key=True)  # Field name made lowercase.
    geneid = models.TextField(db_column='GeneID', blank=True, null=True)  # Field name made lowercase.
    status = models.TextField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
    sequence = models.TextField(db_column='Sequence', blank=True, null=True)  # Field name made lowercase.
    genename = models.TextField(db_column='GeneName', blank=True, null=True)  # Field name made lowercase.
    othername = models.TextField(db_column='OtherName', blank=True, null=True)  # Field name made lowercase.
    types = models.TextField(db_column='Types', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'browseTable'



class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    action_flag = models.PositiveSmallIntegerField()

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class MrnaTbl(models.Model):
    numid = models.IntegerField(db_column='Num_ID', blank=True, null=True)  # Field name made lowercase.
    geneid = models.TextField(db_column='Gene_ID', blank=True, primary_key=True)  # Field name made lowercase.
    transcriptid = models.TextField(db_column='mRNAIsoforms', blank=True, null=True)  # Field name made lowercase.
    numbers = models.IntegerField(db_column='Numbers', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'mRNA_TBL'
        
class W285Table(models.Model):
    geneid = models.TextField(db_column='WormBase_ID', blank=True, primary_key=True)  # Field name made lowercase.
    status = models.TextField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
    sequence = models.TextField(db_column='Sequence_Name', blank=True, null=True)  # Field name made lowercase.
    genename = models.TextField(db_column='Gene_Name', blank=True, null=True)  # Field name made lowercase.
    othername = models.TextField(db_column='Other_Name', blank=True, null=True)  # Field name made lowercase.
    transcript = models.TextField(blank=True, null=True)
    type = models.TextField(blank=True, null=True)
    transcript_count = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'W285Table'

class Datatable(models.Model):
    geneid = models.TextField(db_column='GeneID', blank=True, primary_key=True)  # Field name made lowercase.
    status = models.TextField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
    sequence = models.TextField(db_column='Sequence', blank=True, null=True)  # Field name made lowercase.
    genename = models.TextField(db_column='GeneName', blank=True, null=True)  # Field name made lowercase.
    othername = models.TextField(db_column='OtherName', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'dataTable'
