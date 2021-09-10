from django.conf import settings
from django.db import models
from .TblApplicant import TblApplicant
from .TblDomains import TblDomains


class ApplicantSchedulers(models.Model):
    # applicant_id = models.BigIntegerField(blank=True, null=True)
    applicant = models.ForeignKey(TblApplicant, on_delete=models.CASCADE, related_name="applicant_id_schedule")
    schedule_with = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                                   related_name="schedule_with_id_applicants_schedule")
    schedule_for = models.CharField(max_length=30, blank=True, null=True)
    schedule_on = models.DateField(auto_now=False)
    created = models.DateTimeField(auto_now_add=True)
    # created_by_id = models.BigIntegerField()
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                                   related_name="created_id_applicants_schedule")
    status = models.IntegerField(blank=True, null=True)
    modified = models.DateTimeField(auto_now=True)
    modified_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                                   related_name="modified_id_applicants_schedule")

    class Meta:
        managed = False
        db_table = 'tbl_applicant_schedules'