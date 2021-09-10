from django.conf import settings
from django.db import models
from .TblSetups import TblSetups
from .TblDomains import TblDomains

class TblApplicant(models.Model):
    id = models.BigAutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    father_name = models.CharField(max_length=100)
    dob = models.DateField()
    cnic_insurance_date = models.DateField()
    cnic = models.CharField(max_length=50)
    eaddress = models.CharField(max_length=50, blank=True, null=True)
    contact = models.CharField(max_length=20)
    joining_date = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=6)
    address = models.TextField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.CASCADE,
                                   related_name="created_id_applicants")
    employee_id = models.BigIntegerField(blank=True, null=True)

    modified = models.DateTimeField(auto_now=True)
    modified_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.CASCADE,
                                   related_name="modified_id_applicants")

    selected = models.DateField(blank=True, null=True)
    selected_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.CASCADE,
                                   related_name="selected_id_applicants")

    approved = models.DateField(blank=True, null=True)
    approved_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.CASCADE,
                                   related_name="approved_id_applicants")

    finalized_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.CASCADE,
                                     related_name="finalized_id_applicants")
    finalized = models.DateTimeField(blank=True, null=True)

    designation = models.ForeignKey(TblSetups, null=True, blank=True, on_delete=models.CASCADE,
                                   related_name="designation_id_applicants")
    department = models.ForeignKey(TblSetups, null=True, blank=True, on_delete=models.CASCADE,
                                   related_name="department_id_applicants")
    project = models.ForeignKey(TblSetups, null=True, blank=True, on_delete=models.CASCADE,
                                   related_name="project_id_applicants")

    state = models.ForeignKey(TblSetups, null=True, blank=True, on_delete=models.CASCADE,
                                   related_name="state_id_applicants")
    sub_state = models.ForeignKey(TblSetups, null=True, blank=True, on_delete=models.CASCADE,
                                   related_name="substate_id_applicants")

    center = models.ForeignKey(TblSetups, null=True, blank=True, on_delete=models.CASCADE,
                                  related_name="center_id_applicants")

    city = models.ForeignKey(TblDomains, null=True, blank=True, on_delete=models.CASCADE,
                                   related_name="city_id_applicants")
    # models.IntegerField(blank=True, null=True)

    language = models.ForeignKey(TblDomains, null=True, blank=True, on_delete=models.CASCADE,
                                   related_name="language_id_applicants")
    #models.IntegerField(blank=True, null=True)

    state_name = models.CharField(max_length=20)
    # full_name = models.CharField(max_length=255,blank=True, null=True)
    source = models.CharField(max_length=30, blank=True, null=True)
    in_interview = models.IntegerField(blank=True, null=True)

    marital_status = models.CharField(max_length=50, blank=True, null=True)
    ip_address = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_applicant'