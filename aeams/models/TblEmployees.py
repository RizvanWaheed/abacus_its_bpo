from django.conf import settings
from django.db import models
from .TblSetups import TblSetups

class TblEmployees(models.Model):

    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    cnic = models.CharField(max_length=50)
    sap_code = models.CharField(max_length=50)
    joining_date = models.DateField(blank=True, null=True)
    induction_date = models.DateField(blank=True, null=True)
    batch_no = models.CharField(max_length=4, blank=True, null=True)

    designation = models.ForeignKey(TblSetups, on_delete=models.CASCADE,
                                   related_name="designation_id_employees")
    grade = models.ForeignKey(TblSetups, on_delete=models.CASCADE,
                                   related_name="grade_id_employees")
    department = models.ForeignKey(TblSetups, on_delete=models.CASCADE,
                                   related_name="departments_id_employees")
    employment_type = models.ForeignKey(TblSetups, on_delete=models.CASCADE,
                                   related_name="employment_type_id_employees")

    project = models.ForeignKey(TblSetups, on_delete=models.CASCADE,
                                   related_name="project_id_employees")

    center = models.ForeignKey(TblSetups, on_delete=models.CASCADE,
                                   related_name="center_id_employees")

    campaign = models.ForeignKey(TblSetups, on_delete=models.CASCADE,
                                   related_name="campaign_id_employees")

    sub_campaign = models.ForeignKey(TblSetups, on_delete=models.CASCADE,
                                   related_name="sub_campaign_id_employees")

    state = models.ForeignKey(TblSetups, on_delete=models.CASCADE,
                                   related_name="state_id_employees")

    last_working_date = models.DateField(blank=True, null=True)

    status = models.IntegerField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    # created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
    #                                related_name="created_id_applicants")

    updated = models.DateTimeField(auto_now=True)
    # updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
    #                                related_name="modified_id_applicants")


    # sub_state = models.ForeignKey(TblSetups, on_delete=models.CASCADE,
    #                                related_name="substate_id_applicants")

    full_name = models.CharField(max_length=255,blank=True, null=True)


    class Meta:
        managed = False
        db_table = 'tbl_employees'