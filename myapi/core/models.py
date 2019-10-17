from django.db import models

# Create your models here.


class Role(models.Model):
    role_id = models.AutoField(db_column="role_id", primary_key=True)
    role_name = models.CharField(db_column="role_name",max_length=100)
    class Meta:
        # set table name here
        db_table = "roles"



class Privilege(models.Model):
    priv_id = models.AutoField(db_column="priv_id", primary_key= True)
    priv_name = models.CharField(db_column="priv_name",max_length=100)
    role = models.ManyToOneRel(to=Role, field_name="role_id", field="role_id", on_delete=NotImplementedError)
    class Meta:
        # set table name here
        db_table = "privileges"