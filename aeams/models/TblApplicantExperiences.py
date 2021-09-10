from django.conf import settings
from django.db import models
from .TblApplicant import TblApplicant



class TblApplicantExperiences(models.Model):
    # applicant_id = models.BigIntegerField(blank=True, null=True)
    applicant = models.ForeignKey(TblApplicant, on_delete=models.CASCADE, related_name="applicant_id_experiences")
    company_name = models.CharField(max_length=100, blank=True, null=True)
    designation = models.CharField(max_length=50, blank=True, null=True)
    job_description = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                                   related_name="created_id_applicants_experiences")
    status = models.IntegerField(blank=True, null=True)
    modified = models.DateTimeField(auto_now=True)
    modified_by_id = models.BigIntegerField(blank=True, null=True)
    ended = models.DateField(blank=True, null=True)
    started = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_applicant_experiences'