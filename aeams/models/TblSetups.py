from django.db import models


class TblSetups(models.Model):
    group = models.CharField(max_length=50, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    slug = models.CharField(max_length=100, blank=True, null=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name='children')
    base_id = models.IntegerField(blank=True, null=True)
    created = models.DateTimeField()
    created_by = models.IntegerField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)
    modified_by = models.IntegerField(blank=True, null=True)
    status = models.IntegerField()
    type = models.CharField(max_length=6)
    levels = models.IntegerField()
    lft = models.IntegerField(blank=True, null=True)
    rght = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_setups'