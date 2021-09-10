from django.conf import settings
from django.db import models
from .TblApplicant import TblApplicant
from .TblSetups import TblSetups



class TblApplicantOrientations(models.Model):
    id = models.BigAutoField(primary_key=True)
    # applicant_id = models.BigIntegerField(blank=True, null=True)
    applicant = models.ForeignKey(TblApplicant, on_delete=models.CASCADE, related_name="applicant_id_orientations")
    orientation = models.ForeignKey(TblSetups, on_delete=models.CASCADE, related_name="orientation_id_orientations")
    orientation_level = models.CharField(max_length=5, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                                   related_name="created_id_applicants_orientations")
    status = models.IntegerField()
    active = models.IntegerField()
    checked = models.IntegerField()
    modified = models.DateTimeField(auto_now=True)
    modified_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                                   related_name="modified_id_applicants_orientations")
    role = models.TextField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'tbl_applicant_orientations'