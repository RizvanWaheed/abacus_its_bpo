from django.conf import settings
from django.db import models


class TblDomains(models.Model):
    name = models.CharField(max_length=200)
    domain_id = models.IntegerField(blank=True, null=True)
    domain_type = models.CharField(max_length=50, blank=True, null=True)
    code = models.CharField(max_length=30)
    status = models.IntegerField(blank=True, null=True)

    created = models.DateTimeField(auto_now_add=True)
    created_by = models.IntegerField(blank=True, null=True)
    # created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
    #                                related_name="created_id_domain")

    class Meta:
        managed = False
        db_table = 'tbl_domains'