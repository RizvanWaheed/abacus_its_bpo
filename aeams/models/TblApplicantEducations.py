from django.conf import settings
from django.db import models
from .TblApplicant import TblApplicant
from .TblDomains import TblDomains


class TblApplicantEducations(models.Model):
    # applicant_id = models.BigIntegerField(blank=True, null=True)
    applicant = models.ForeignKey(TblApplicant, on_delete=models.CASCADE, related_name="applicant_id_educations")
    # education_id = models.IntegerField(blank=True, null=True)
    education = models.ForeignKey(TblDomains, on_delete=models.CASCADE, related_name='education_id_applicants_educations')
    # major_id = models.IntegerField(blank=True, null=True)
    major = models.ForeignKey(TblDomains, on_delete=models.CASCADE)
    year = models.CharField(max_length=10, blank=True, null=True)
    institut = models.CharField(max_length=255, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                                   related_name="created_id_applicants_educations")
    status = models.IntegerField(blank=True, null=True)
    modified = models.DateTimeField(auto_now=True)
    modified_by_id = models.BigIntegerField(blank=True, null=True)
    # institute_id = models.IntegerField(blank=True, null=True)
    institute = models.ForeignKey(TblDomains, on_delete=models.CASCADE, related_name='institute_id_applicants_educations')

    class Meta:
        managed = False
        db_table = 'tbl_applicant_educations'