from django.db import models
from .TblSetups import TblSetups

class TblSetupSetups(models.Model):
    setup = models.ForeignKey(TblSetups, on_delete=models.CASCADE, related_name="setup_id_setup")
    sub_setup = models.ForeignKey(TblSetups, on_delete=models.CASCADE, related_name="setup_id_sub_setup")
    created = models.DateTimeField()
    created_by = models.BigIntegerField(blank=True, null=True)
    type = models.CharField(max_length=11)
    active = models.IntegerField()
    modified = models.DateTimeField(blank=True, null=True)
    modified_by = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_setup_setups'
        unique_together = (('setup_id', 'sub_setup_id', 'created'),)