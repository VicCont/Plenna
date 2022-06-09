
# Create your models here.
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from pyparsing import NoMatch


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

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
    id = models.BigAutoField(primary_key=True)
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


class Doctor(models.Model):
    id_doctor = models.AutoField(primary_key=True)
    nom_doc = models.CharField(max_length=70, blank=True, null=True)
    usuario = models.CharField(max_length=30, blank=True, null=True)
    hash_pass = models.CharField(max_length=120, blank=True, null=True)
    admin = models.BooleanField(blank=True, null=True)
    id_especialidad = models.ForeignKey('Especialidad', models.DO_NOTHING, db_column='id_especialidad')
    activo = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'doctor'

    def __str__(self):
        return self.nom_doc


class Especialidad(models.Model):
    id_especialidad = models.AutoField(primary_key=True)
    nombre_esp = models.CharField(max_length=60)
    activa = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'especialidad'
    def __str__(self):
            return self.nombre_esp


class IdDoc(models.Model):
    login = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'id_doc'


class Insight(models.Model):
    id_insight = models.AutoField(primary_key=True)
    id_doctor = models.ForeignKey(Doctor, models.DO_NOTHING, db_column='id_doctor')
    id_pac = models.ForeignKey('Paciente', models.DO_NOTHING, db_column='id_pac')
    comentario = models.CharField(max_length=750, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'insight'


class OpcPreg(models.Model):
    id_opc_preg = models.AutoField(primary_key=True)
    id_preg = models.ForeignKey('Pregunta', models.DO_NOTHING, db_column='id_preg')
    resp_opc_preg = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'opc_preg'
    def __str__(self):
        return self.resp_opc_preg


class Paciente(models.Model):
    id_pac = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=70, blank=True, null=True)
    clave_pac = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'paciente'
    def __str__(self):
        return f"{self.clave_pac} : {self.nombre}"


class Permisos(models.Model):
    id_permiso = models.AutoField(primary_key=True)
    id_doctor = models.ForeignKey(Doctor, models.DO_NOTHING, db_column='id_doctor')
    id_pac = models.ForeignKey(Paciente, models.DO_NOTHING, db_column='id_pac')
    id_especialidad = models.ForeignKey(Especialidad, models.DO_NOTHING, db_column='id_especialidad')
    activo = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'permisos'


class PregPac(models.Model):
    id_preg_pac = models.AutoField(primary_key=True)
    id_preg = models.ForeignKey('Pregunta', models.DO_NOTHING, db_column='id_preg')
    id_pac = models.ForeignKey(Paciente, models.DO_NOTHING, db_column='id_pac')

    class Meta:
        managed = False
        db_table = 'preg_pac'


class Pregunta(models.Model):
    id_preg = models.AutoField(primary_key=True)
    id_especialidad = models.ForeignKey(Especialidad, models.DO_NOTHING, db_column='id_especialidad')
    pregunta = models.CharField(max_length=80)
    tipo = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'pregunta'

    def __str__(self):
            return self.pregunta


class ResPregOpc(models.Model):
    id_resp_preg_opc = models.AutoField(primary_key=True)
    id_preg_pac = models.ForeignKey(PregPac, models.DO_NOTHING, db_column='id_preg_pac')
    id_opc_preg = models.ForeignKey(OpcPreg, models.DO_NOTHING, db_column='id_opc_preg')

    class Meta:
        managed = False
        db_table = 'res_preg_opc'


class RespAbierta(models.Model):
    id_resp_preg_pac = models.AutoField(primary_key=True)
    id_preg_pac = models.ForeignKey(PregPac, models.DO_NOTHING, db_column='id_preg_pac')
    resp_preg = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'resp_abierta'
