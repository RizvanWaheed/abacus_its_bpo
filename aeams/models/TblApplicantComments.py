from django.conf import settings
from django.db import models
from .TblApplicant import TblApplicant


class TblApplicantComments(models.Model):
    # applicant_id = models.BigIntegerField(blank=True, null=True)
    applicant = models.ForeignKey(TblApplicant, on_delete=models.CASCADE, related_name="applicant_id_comments")
    remarks = models.TextField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    modified_by_id = models.BigIntegerField(blank=True, null=True)
    state_id = models.IntegerField(blank=True, null=True)
    call = models.IntegerField(blank=True, null=True)
    called_by = models.BigIntegerField(blank=True, null=True)
    called = models.DateTimeField(blank=True, null=True)
    # created_by_id = models.BigIntegerField()
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                                   related_name="created_id_applicants_comments")
    sub_state_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_applicant_comments'