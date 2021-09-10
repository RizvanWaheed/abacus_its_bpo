from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser, PermissionsMixin, BaseUserManager
from .TblSetups import TblSetups
from .TblEmployees import TblEmployees

class UserManager(BaseUserManager):
    def create_user(self, login, password=None):
        """
        Creates and saves a User with the given username and password.
        """
        if not login:
            raise ValueError('Error: The User you want to create must have an username, try again')

        my_user = self.model(
            user=self.model.normalize_username(login),
        )

        my_user.set_password(password)
        my_user.save(using=self._db)
        return my_user

    def create_staffuser(self, login, password):
        """
        Creates and saves a staff user with the given username and password.
        """
        my_user = self.create_user(
            login=login,
            password=password,
        )
        # my_user.staff = True
        my_user.save(using=self._db)
        return my_user

    def create_superuser(self, user, password):
        """
        Creates and saves a superuser with the given username and password.
        """
        my_user = self.create_user(
            user,
            password=password,
        )
        # my_user.staff = True
        # my_user.admin = True
        my_user.save(using=self._db)
        return my_user



#1. class TblUsers(models.Model):
class TblUsers(AbstractBaseUser):

    USERNAME_FIELD = 'login'
    REQUIRED_FIELDS = 'name'

    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    login = models.BigIntegerField(unique=True)
    password = models.CharField(max_length=250)
    email = models.CharField(max_length=100, blank=True, null=True)
    # role_id = models.BigIntegerField()
    role = models.ForeignKey(TblSetups, on_delete=models.CASCADE, related_name="role_id_setups")
    status = models.IntegerField(blank=True, null=True)
    login_user_ip = models.CharField(max_length=16, blank=True, null=True)
    last_login = models.DateTimeField(blank=True, null=True, db_column="last_login_time")
    deleted = models.SmallIntegerField(blank=True, null=True)
    is_terminated = models.SmallIntegerField(blank=True, null=True)
    termination_date = models.DateField(blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField(blank=True, null=True)
    auth_forwarding = models.BigIntegerField(blank=True, null=True)
    created_by = models.IntegerField(blank=True, null=True)
    updated = models.DateTimeField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    left_reason = models.CharField(max_length=255, blank=True, null=True)
    tele_code = models.CharField(max_length=255, blank=True, null=True)

    employee = models.ForeignKey(TblEmployees, blank=True, null=True, on_delete=models.CASCADE,
                                   related_name="employee_id_users")

    cnic = models.CharField(max_length=100, blank=True, null=True)
    remember_token = models.CharField(max_length=255, blank=True, null=True)
    lid = models.BigIntegerField(blank=True, null=True)
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)

    REQUIRED_FIELDS = ['name', 'role_id']

    class Meta:
        managed = False
        db_table = 'tbl_users'

    objects = UserManager()

    def get_name(self):
        return self.name