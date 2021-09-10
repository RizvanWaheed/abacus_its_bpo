# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class DailyAttendance(models.Model):
    date = models.DateField()
    sap_id = models.CharField(max_length=20)
    other_id = models.CharField(max_length=35, blank=True, null=True)
    name = models.CharField(max_length=50)
    shift = models.TimeField(blank=True, null=True)
    status = models.CharField(max_length=10)
    campaign = models.CharField(max_length=100, blank=True, null=True)
    working_hours = models.IntegerField(blank=True, null=True)
    date_time = models.DateTimeField()
    server = models.CharField(max_length=35, blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(blank=True, null=True)
    created_by = models.IntegerField()
    asm_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'daily_attendance'


class FailedJobs(models.Model):
    id = models.BigAutoField(primary_key=True)
    connection = models.TextField()
    queue = models.TextField()
    payload = models.TextField()
    exception = models.TextField()
    failed_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'failed_jobs'


class Migrations(models.Model):
    migration = models.CharField(max_length=255)
    batch = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'migrations'


class TblAcClientProjects(models.Model):
    client_id = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    created_by = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    seats = models.IntegerField(blank=True, null=True)
    gst = models.IntegerField(blank=True, null=True)
    amount = models.IntegerField(blank=True, null=True)
    updated = models.DateTimeField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    amount_per = models.CharField(max_length=7, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_ac_client_projects'


class TblAcClientRevenues(models.Model):
    client_id = models.IntegerField(blank=True, null=True)
    project_id = models.IntegerField(blank=True, null=True)
    bill_amount = models.IntegerField(blank=True, null=True)
    gst = models.IntegerField(blank=True, null=True)
    totals = models.IntegerField(blank=True, null=True)
    bill_period = models.CharField(max_length=250, blank=True, null=True)
    invoice = models.CharField(max_length=255, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    po_date = models.DateField(blank=True, null=True)
    account_record = models.CharField(max_length=255, blank=True, null=True)
    bill_date = models.DateField(blank=True, null=True)
    collection = models.CharField(max_length=255, blank=True, null=True)
    turnaround_time = models.CharField(max_length=255, blank=True, null=True)
    sub_pro = models.CharField(max_length=255, blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    created_by = models.IntegerField(blank=True, null=True)
    updated = models.DateTimeField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_ac_client_revenues'


class TblAcClients(models.Model):
    short_name = models.CharField(max_length=100, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    added_date = models.DateTimeField(blank=True, null=True)
    added_by = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_ac_clients'


class TblAcProjects(models.Model):
    client_id = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    created_by = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    updated = models.DateTimeField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_ac_projects'


class TblAnnualForward(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.BigIntegerField()
    quota_year = models.BigIntegerField()
    new_quota_year = models.BigIntegerField()
    days = models.BigIntegerField()
    remaining_days = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'tbl_annual_forward'


class TblAnnualsForward(models.Model):
    asm_id = models.CharField(max_length=50)
    annuals = models.IntegerField()
    year = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tbl_annuals_forward'


















class TblAssetTypes(models.Model):
    code = models.CharField(max_length=100, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    created_by = models.IntegerField(blank=True, null=True)
    updated = models.DateTimeField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    deleted = models.DateTimeField(blank=True, null=True)
    deleted_by = models.IntegerField(blank=True, null=True)
    parent_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_asset_types'


class TblAttendance(models.Model):
    attendance_id = models.BigAutoField(primary_key=True)
    user_id = models.BigIntegerField()
    physical_shift = models.ForeignKey('TblPhysicalShift', models.DO_NOTHING)
    roster_status = models.ForeignKey('TblRosterStatus', models.DO_NOTHING)
    time_in = models.CharField(max_length=8, blank=True, null=True)
    time_out = models.CharField(max_length=8, blank=True, null=True)
    last_update = models.DateTimeField()
    tc_approval = models.SmallIntegerField()
    marked_by = models.BigIntegerField()
    approved_by = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'tbl_attendance'


class TblAttendanceEvents(models.Model):
    attendance_event_id = models.BigAutoField(primary_key=True)
    attendance_event_desc = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'tbl_attendance_events'


class TblAttendanceRoutes(models.Model):
    name = models.CharField(max_length=50)
    method = models.CharField(max_length=15, blank=True, null=True)
    created_at = models.DateTimeField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tbl_attendance_routes'


class TblAttendanceUserRoutes(models.Model):
    route_id = models.IntegerField()
    user_id = models.IntegerField()
    can_access = models.CharField(max_length=1)
    created_at = models.DateTimeField()
    created_by = models.IntegerField()
    status = models.IntegerField()
    updated_at = models.DateTimeField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_attendance_user_routes'


class TblBehaviourTitle(models.Model):
    behaviour_title_id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    category_group = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'tbl_behaviour_title'


class TblBehaviouralAssessment(models.Model):
    behaviour_assessment_id = models.BigAutoField(primary_key=True)
    quarter_id = models.BigIntegerField()
    behaviour_title_id = models.BigIntegerField()
    rating = models.BigIntegerField()
    user_id = models.BigIntegerField()
    average = models.FloatField()
    added_by = models.BigIntegerField()
    last_modified_by = models.BigIntegerField()
    deleted = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'tbl_behavioural_assessment'


class TblBehaviouralAssessmentAssign(models.Model):
    behavioural_assessment_assign_id = models.BigAutoField(primary_key=True)
    user_id = models.BigIntegerField()
    quarter_id = models.BigIntegerField()
    behaviour_title_id = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'tbl_behavioural_assessment_assign'


class TblCampaignsQuota(models.Model):
    campaigns = models.CharField(max_length=50)
    annual = models.IntegerField()
    cl = models.IntegerField()
    sl = models.IntegerField()
    absent = models.IntegerField()
    center_id = models.IntegerField()
    status = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    created_by = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_campaigns_quota'


class TblConfiguration(models.Model):
    config_id = models.AutoField(primary_key=True)
    config_name = models.CharField(max_length=60)
    config_value = models.BigIntegerField()
    config_description = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'tbl_configuration'


class TblCountry(models.Model):
    ccode = models.CharField(max_length=2)
    country = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'tbl_country'





class TblEducation(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    active = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'tbl_education'


class TblEmployeeAuthorities(models.Model):
    user_id = models.BigIntegerField()
    for_field = models.CharField(db_column='for', max_length=9)  # Field renamed because it was a Python reserved word.
    active = models.IntegerField()
    created = models.DateTimeField()
    created_by = models.BigIntegerField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)
    modified_by = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_employee_authorities'


class TblEmployeeEducations(models.Model):
    employee_id = models.BigIntegerField(primary_key=True)
    education_id = models.IntegerField(blank=True, null=True)
    institute_id = models.IntegerField(blank=True, null=True)
    major_id = models.IntegerField(blank=True, null=True)
    start_year = models.CharField(max_length=4, blank=True, null=True)
    end_year = models.CharField(max_length=4, blank=True, null=True)
    percentage = models.CharField(max_length=3, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    created_by = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_employee_educations'


class TblEmployeeLogs(models.Model):
    employee = models.ForeignKey('TblEmployees', models.DO_NOTHING)
    cnic = models.CharField(max_length=15, blank=True, null=True)
    designation = models.ForeignKey('TblSetups', models.DO_NOTHING, blank=True, null=True, related_name="designation_setup_employee_log")
    grade = models.ForeignKey('TblSetups', models.DO_NOTHING, blank=True, null=True, related_name="grade_setup_employee_log")
    department_id = models.CharField(max_length=150, blank=True, null=True)
    project_id = models.CharField(max_length=100, blank=True, null=True)
    reporting_to = models.IntegerField(blank=True, null=True)
    employment_type = models.ForeignKey('TblSetups', models.DO_NOTHING, blank=True, null=True, related_name="type_setup_employee_log")
    created = models.DateTimeField()
    created_by = models.BigIntegerField(blank=True, null=True)
    updated = models.DateTimeField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    remarks = models.TextField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    center = models.ForeignKey('TblSetups', models.DO_NOTHING, blank=True, null=True, related_name="center_setup_employee_log")
    updated_by = models.BigIntegerField(blank=True, null=True)
    approved = models.DateTimeField(blank=True, null=True)
    approved_by = models.BigIntegerField(blank=True, null=True)
    state = models.IntegerField()
    form = models.CharField(max_length=9, blank=True, null=True)
    campaign_id = models.CharField(max_length=200, blank=True, null=True)
    sub_campaign_id = models.CharField(max_length=255, blank=True, null=True)
    reporting_to_too = models.BigIntegerField(blank=True, null=True)
    weekly_off = models.CharField(max_length=50)
    role_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tbl_employee_logs'


class TblEmployeeOffices(models.Model):
    cnic = models.CharField(max_length=50, blank=True, null=True)
    user_id = models.BigIntegerField(blank=True, null=True)
    employee_id = models.BigIntegerField(blank=True, null=True)
    office_id = models.IntegerField(blank=True, null=True)
    status = models.IntegerField()
    created = models.DateTimeField()
    created_by = models.BigIntegerField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)
    modified_by = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_employee_offices'


class TblEmployeeProfiles(models.Model):
    employee_id = models.BigIntegerField(unique=True)
    father_husband_name = models.CharField(max_length=150, blank=True, null=True)
    marital_status = models.CharField(max_length=11, blank=True, null=True)
    religion_id = models.IntegerField(blank=True, null=True)
    gender = models.CharField(max_length=6, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    blood_group = models.CharField(max_length=10, blank=True, null=True)
    cnic = models.CharField(max_length=50, blank=True, null=True)
    passport = models.CharField(max_length=30, blank=True, null=True)
    eobi = models.CharField(max_length=30, blank=True, null=True)
    social_security_no = models.CharField(max_length=30, blank=True, null=True)
    email = models.CharField(max_length=80, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    current_address = models.TextField(blank=True, null=True)
    current_city_id = models.IntegerField(blank=True, null=True)
    home_phone = models.CharField(max_length=17, blank=True, null=True)
    mobile_phone = models.CharField(max_length=17, blank=True, null=True)
    sect_id = models.IntegerField(blank=True, null=True)
    city_id = models.IntegerField(blank=True, null=True)
    country_id = models.IntegerField(blank=True, null=True)
    language_id = models.IntegerField(blank=True, null=True)
    cnic_issuance_date = models.DateField(blank=True, null=True)
    laptop_id = models.CharField(max_length=30, blank=True, null=True)
    telenor_sim_issuance_date = models.DateField(blank=True, null=True)
    telenor_no = models.CharField(max_length=17, blank=True, null=True)
    work_phone = models.CharField(max_length=17, blank=True, null=True)
    work_phone_ext = models.CharField(max_length=10, blank=True, null=True)
    sect = models.CharField(max_length=50, blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    updated = models.DateTimeField(blank=True, null=True)
    updated_by = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_employee_profiles'


class TblEmployeeReportings(models.Model):
    reportee = models.CharField(max_length=20)
    reporting_to = models.CharField(max_length=20)
    column = models.CharField(max_length=11)
    created = models.DateTimeField()
    created_by = models.BigIntegerField()
    status = models.IntegerField()
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_employee_reportings'


class TblEmployeeResignations(models.Model):
    id = models.BigAutoField(primary_key=True)
    employee_id = models.BigIntegerField()
    last_working_day = models.DateField()
    reason = models.CharField(max_length=255)
    description = models.TextField()
    applied_on = models.DateTimeField()
    state = models.IntegerField()
    verified = models.DateTimeField(blank=True, null=True)
    verified_by = models.BigIntegerField(blank=True, null=True)
    verified_state = models.CharField(max_length=255, blank=True, null=True)
    verified_desc = models.TextField(blank=True, null=True)
    approved_by = models.BigIntegerField(blank=True, null=True)
    approved = models.DateTimeField(blank=True, null=True)
    approved_state = models.CharField(max_length=255, blank=True, null=True)
    approved_desc = models.TextField(blank=True, null=True)
    finalized_by = models.BigIntegerField(blank=True, null=True)
    finalized = models.DateTimeField(blank=True, null=True)
    finalized_state = models.CharField(max_length=255, blank=True, null=True)
    finalized_desc = models.TextField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    updated_by = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_employee_resignations'


class TblEmployeeSetups(models.Model):
    cnic = models.CharField(max_length=50, blank=True, null=True)
    user_id = models.BigIntegerField(blank=True, null=True)
    employee = models.ForeignKey('TblEmployees', models.DO_NOTHING, blank=True, null=True)
    setup = models.ForeignKey('TblSetups', models.DO_NOTHING, blank=True, null=True, related_name="setup_id_employee_setup")
    status = models.IntegerField()
    created = models.DateTimeField()
    created_by = models.BigIntegerField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)
    modified_by = models.BigIntegerField(blank=True, null=True)
    base = models.ForeignKey('TblSetups', models.DO_NOTHING, blank=True, null=True, related_name="base_id_employee_setup")
    transfered = models.DateField(blank=True, null=True)
    reason = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_employee_setups'


class TblEmployeeWorkforces(models.Model):
    employee_id = models.BigIntegerField()
    cluster_seat_id = models.IntegerField()
    shift_time_id = models.IntegerField()
    short_break_one_id = models.IntegerField(blank=True, null=True)
    short_break_two_id = models.IntegerField(blank=True, null=True)
    long_break_id = models.IntegerField(blank=True, null=True)
    created = models.DateTimeField()
    created_by = models.BigIntegerField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)
    modified_by = models.BigIntegerField(blank=True, null=True)
    active = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tbl_employee_workforces'


# class TblEmployees(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     name = models.CharField(max_length=100)
#     sap_code = models.BigIntegerField(blank=True, null=True)
#     designation = models.ForeignKey('TblSetups', models.DO_NOTHING, related_name="employee_setup_designation")
#     grade = models.ForeignKey('TblSetups', models.DO_NOTHING, blank=True, null=True, related_name="employee_setup_grade")
#     department_id = models.CharField(max_length=150)
#     reporting_to = models.BigIntegerField()
#     joining_date = models.DateField()
#     user_type = models.CharField(max_length=1)
#     employment_type = models.ForeignKey('TblSetups', models.DO_NOTHING, related_name="employee_setup_type")
#     status = models.IntegerField()
#     created = models.DateTimeField(blank=True, null=True)
#     image = models.CharField(max_length=150, blank=True, null=True)
#     thumbnail = models.CharField(max_length=150, blank=True, null=True)
#     is_hod = models.CharField(max_length=1)
#     created_by = models.IntegerField(blank=True, null=True)
#     updated = models.DateTimeField(blank=True, null=True)
#     updated_by = models.IntegerField(blank=True, null=True)
#     cnic = models.CharField(max_length=50, blank=True, null=True)
#     project_id = models.CharField(max_length=100, blank=True, null=True)
#     center = models.ForeignKey('TblSetups', models.DO_NOTHING, blank=True, null=True, related_name="employee_setup_center")
#     last_name = models.CharField(max_length=30, blank=True, null=True)
#     batch_no = models.CharField(max_length=4, blank=True, null=True)
#     campaign_id = models.CharField(max_length=200, blank=True, null=True)
#     sub_campaign_id = models.CharField(max_length=255, blank=True, null=True)
#     state_id = models.IntegerField(blank=True, null=True)
#     induction_date = models.DateField(blank=True, null=True)
#     last_working_date = models.DateField(blank=True, null=True)
#     reporting_to_too = models.BigIntegerField(blank=True, null=True)
#     weekly_off = models.CharField(max_length=50)
#     last_relocation_date = models.DateField(blank=True, null=True)
#     full_name = models.CharField(max_length=255, blank=True, null=True)
#     leaves_start = models.DateField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tbl_employees'


class TblEvaluationRating(models.Model):
    rating_id = models.AutoField(primary_key=True)
    rating_description = models.TextField()
    rating = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tbl_evaluation_rating'


class TblForms(models.Model):
    name = models.CharField(max_length=100)
    status = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    created_by = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tbl_forms'


class TblFormsInput(models.Model):
    forms_id = models.IntegerField()
    field_name = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    searchable = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_forms_input'


class TblFormsInputSelect(models.Model):
    forms_input_id = models.IntegerField()
    options = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_forms_input_select'


class TblHold(models.Model):
    asm_id = models.CharField(max_length=25)
    date = models.DateField()
    reason = models.TextField()
    status = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(blank=True, null=True)
    created_by = models.IntegerField()
    updated_by = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_hold'


class TblInsuranceClaimTypes(models.Model):
    claim_type_id = models.AutoField(primary_key=True)
    claim_type = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'tbl_insurance_claim_types'


class TblInsuranceEntitlement(models.Model):
    entitlement_id = models.AutoField(primary_key=True)
    grade_id = models.IntegerField()
    plan = models.CharField(max_length=3)
    claim_type = models.ForeignKey(TblInsuranceClaimTypes, models.DO_NOTHING)
    claim_limit = models.DecimalField(max_digits=15, decimal_places=0)

    class Meta:
        managed = False
        db_table = 'tbl_insurance_entitlement'


class TblInterestCategories(models.Model):
    interest_category_id = models.BigAutoField(primary_key=True)
    category = models.CharField(max_length=55)
    field_name = models.CharField(max_length=20)
    deleted = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'tbl_interest_categories'


class TblInterestSubCategories(models.Model):
    sub_category_id = models.BigAutoField(primary_key=True)
    interest_category_id = models.BigIntegerField()
    sub_category = models.CharField(max_length=55)
    deleted = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'tbl_interest_sub_categories'


class TblJobs(models.Model):
    job_id = models.BigAutoField(primary_key=True)
    job_title = models.CharField(max_length=200)
    job_description = models.TextField()
    added_date = models.DateTimeField()
    deleted = models.IntegerField()
    deleted_by = models.BigIntegerField()
    deleted_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tbl_jobs'


class TblKpiAttendance(models.Model):
    date = models.DateField()
    status = models.CharField(max_length=10, blank=True, null=True)
    user = models.CharField(max_length=50)
    sip = models.CharField(max_length=20)
    asm_id = models.BigIntegerField()
    calls = models.IntegerField(blank=True, null=True)
    agent_time = models.TimeField()
    wait = models.TimeField(blank=True, null=True)
    talk = models.TimeField(blank=True, null=True)
    dispo = models.TimeField(blank=True, null=True)
    pause = models.TimeField()
    dead = models.TimeField(blank=True, null=True)
    customer = models.TimeField(blank=True, null=True)
    sb1 = models.TimeField(blank=True, null=True)
    md = models.TimeField(blank=True, null=True)
    login = models.TimeField(blank=True, null=True)
    lb = models.TimeField(blank=True, null=True)
    sb2 = models.TimeField(blank=True, null=True)
    lagged = models.TimeField(blank=True, null=True)
    server = models.CharField(max_length=35, blank=True, null=True)
    aht = models.TimeField(blank=True, null=True)
    tickets = models.IntegerField(blank=True, null=True)
    campaign = models.CharField(max_length=100)
    created_at = models.DateTimeField()
    created_by = models.IntegerField()
    updated_at = models.DateTimeField()
    updated_by = models.IntegerField(blank=True, null=True)
    lid = models.BigIntegerField(blank=True, null=True)
    validation_applied = models.IntegerField(blank=True, null=True)
    logout = models.DateTimeField(blank=True, null=True)
    management = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_kpi_attendance'


class TblKpiAttendanceValidation(models.Model):
    kpi_attendance_id = models.BigIntegerField(primary_key=True)
    type = models.CharField(max_length=100, blank=True, null=True)
    reason = models.CharField(max_length=255, blank=True, null=True)
    file = models.CharField(max_length=255, blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    created_by = models.BigIntegerField(blank=True, null=True)
    updated = models.DateTimeField()
    updated_by = models.BigIntegerField(blank=True, null=True)
    state = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tbl_kpi_attendance_validation'


class TblLeaveApplications(models.Model):
    asm_id = models.BigIntegerField()
    start = models.DateField()
    end = models.DateField()
    total = models.IntegerField(blank=True, null=True)
    type = models.CharField(max_length=25)
    title = models.CharField(max_length=100)
    status = models.IntegerField(blank=True, null=True)
    reason = models.TextField(blank=True, null=True)
    treason = models.TextField(db_column='Treason', blank=True, null=True)  # Field name made lowercase.
    am_approve = models.IntegerField()
    am_reason = models.TextField(blank=True, null=True)
    e_type = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(blank=True, null=True)
    updated_by = models.BigIntegerField(blank=True, null=True)
    role_id = models.IntegerField(blank=True, null=True)
    created_by = models.BigIntegerField(blank=True, null=True)
    volunteer = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_leave_applications'


class TblLeaveQuota(models.Model):
    fall_year = models.IntegerField()
    fall_month = models.IntegerField()
    sl_allowed = models.IntegerField()
    cl_allowed = models.IntegerField()
    al_allowed = models.IntegerField()
    quota_for = models.IntegerField()
    added_date = models.DateTimeField(blank=True, null=True)
    added_by = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_leave_quota'


class TblLeavesSwapLog(models.Model):
    agent1 = models.CharField(max_length=40)
    date1 = models.DateField()
    agent2 = models.CharField(max_length=40)
    date2 = models.DateField()
    reason = models.TextField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    created_by = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tbl_leaves_swap_log'


class TblMiscellaneouses(models.Model):
    code = models.BigIntegerField()
    name = models.CharField(max_length=100)
    active = models.SmallIntegerField()
    parent_id = models.BigIntegerField(blank=True, null=True)
    misc_type = models.CharField(max_length=50, blank=True, null=True)
    domain = models.CharField(max_length=30, blank=True, null=True)
    id = models.IntegerField(primary_key=True, blank=False, null=False)

    class Meta:
        managed = False
        db_table = 'tbl_miscellaneouses'


class TblMonthlyAttendance(models.Model):
    asm_id = models.BigIntegerField()
    mon = models.IntegerField()
    year = models.IntegerField()
    month = models.DateField()
    annual = models.IntegerField()
    cl = models.IntegerField()
    sl = models.IntegerField()
    ncns = models.IntegerField()
    off = models.IntegerField()
    offcall = models.IntegerField()
    p = models.IntegerField()
    a = models.IntegerField()
    hold = models.IntegerField()
    an = models.IntegerField()
    c = models.IntegerField()
    s = models.IntegerField()
    ml = models.IntegerField()
    pl = models.IntegerField()
    ft = models.IntegerField()
    pt = models.IntegerField()
    vl = models.IntegerField()
    oc = models.IntegerField()
    r = models.IntegerField()
    t = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tbl_monthly_attendance'


class TblMprCriterion(models.Model):
    sub_campaign_id = models.IntegerField()
    mpr_criteria_id = models.IntegerField()
    designation_id = models.IntegerField()
    grade = models.CharField(max_length=2)
    points = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    percentage = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    target = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    level = models.DecimalField(max_digits=6, decimal_places=0, blank=True, null=True)
    score = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    count = models.IntegerField(blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    created_by = models.BigIntegerField(blank=True, null=True)
    active = models.IntegerField(blank=True, null=True)
    modified_by = models.BigIntegerField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_mpr_criterion'


class TblNews(models.Model):
    news_id = models.BigAutoField(primary_key=True)
    news_title = models.CharField(max_length=255)
    news_detail = models.TextField()
    news_date = models.DateField()
    news_file = models.CharField(max_length=255, blank=True, null=True)
    added_by = models.BigIntegerField()
    added_date = models.DateTimeField()
    deleted = models.SmallIntegerField()
    deleted_by = models.BigIntegerField()
    deleted_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tbl_news'


class TblObServers(models.Model):
    serverip = models.CharField(max_length=255)
    username = models.CharField(max_length=255, blank=True, null=True)
    password = models.CharField(max_length=255, blank=True, null=True)
    dbname = models.CharField(max_length=255, blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    created_by = models.IntegerField(blank=True, null=True)
    mysql_port = models.IntegerField(blank=True, null=True)
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tbl_ob_servers'


class TblObUsersStats(models.Model):
    server_ip = models.CharField(max_length=100, blank=True, null=True)
    agent_id = models.IntegerField(blank=True, null=True)
    agent_name = models.CharField(max_length=255, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    agentpause = models.TimeField(db_column='agentPause', blank=True, null=True)  # Field name made lowercase.
    pause = models.TimeField(blank=True, null=True)
    resume = models.TimeField(blank=True, null=True)
    dispo = models.TimeField(blank=True, null=True)
    manualcall = models.TimeField(db_column='manualCall', blank=True, null=True)  # Field name made lowercase.
    manual = models.TimeField(blank=True, null=True)
    autocall = models.TimeField(db_column='autoCall', blank=True, null=True)  # Field name made lowercase.
    totalcall = models.TimeField(db_column='totalCall', blank=True, null=True)  # Field name made lowercase.
    logout = models.TimeField(blank=True, null=True)
    login = models.TimeField(blank=True, null=True)
    agentpausecount = models.IntegerField(db_column='agentPauseCount', blank=True, null=True)  # Field name made lowercase.
    resumecount = models.IntegerField(db_column='resumeCount', blank=True, null=True)  # Field name made lowercase.
    dispocount = models.IntegerField(db_column='dispoCount', blank=True, null=True)  # Field name made lowercase.
    manualcallcount = models.IntegerField(db_column='manualCallCount', blank=True, null=True)  # Field name made lowercase.
    manualcount = models.IntegerField(db_column='manualCount', blank=True, null=True)  # Field name made lowercase.
    autocallcount = models.IntegerField(db_column='autoCallCount', blank=True, null=True)  # Field name made lowercase.
    logoutcount = models.IntegerField(db_column='logoutCount', blank=True, null=True)  # Field name made lowercase.
    logincount = models.IntegerField(db_column='loginCount', blank=True, null=True)  # Field name made lowercase.
    added_date = models.DateTimeField(blank=True, null=True)
    added_by = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_ob_users_stats'


class TblObUsersStatsLogs(models.Model):
    server_ip = models.CharField(max_length=100, blank=True, null=True)
    server_id = models.IntegerField(blank=True, null=True)
    from_time = models.DateTimeField(blank=True, null=True)
    from_state = models.CharField(max_length=100, blank=True, null=True)
    to_time = models.DateTimeField(blank=True, null=True)
    to_state = models.CharField(max_length=100, blank=True, null=True)
    agent_id = models.IntegerField(blank=True, null=True)
    added_by = models.CharField(max_length=255, blank=True, null=True)
    added_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_ob_users_stats_logs'


class TblObUsersStatsStates(models.Model):
    id = models.IntegerField(primary_key=True)
    server_ip = models.CharField(max_length=100, blank=True, null=True)
    server_id = models.IntegerField(blank=True, null=True)
    loaded_time = models.DateTimeField(blank=True, null=True)
    loaded_by = models.IntegerField(blank=True, null=True)
    loaded = models.IntegerField(blank=True, null=True)
    arranged_time = models.DateTimeField(blank=True, null=True)
    arranged_by = models.IntegerField(blank=True, null=True)
    arranged = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_ob_users_stats_states'


class TblObjectiveRating(models.Model):
    objective_rated_id = models.BigAutoField(primary_key=True)
    objective_id = models.BigIntegerField()
    quarter_id = models.BigIntegerField()
    added_by = models.BigIntegerField()
    result = models.CharField(max_length=255)
    rating = models.IntegerField()
    average = models.FloatField()

    class Meta:
        managed = False
        db_table = 'tbl_objective_rating'


class TblObjectivesForwarding(models.Model):
    quarter_finalize_id = models.BigAutoField(primary_key=True)
    quarter_id = models.BigIntegerField()
    user_id = models.BigIntegerField()
    forwarded_to = models.BigIntegerField()
    finalized_by = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'tbl_objectives_forwarding'


class TblOffices(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    slug = models.CharField(max_length=100, blank=True, null=True)
    parent_id = models.IntegerField()
    setup_id = models.IntegerField()
    status = models.IntegerField()
    created = models.DateTimeField()
    created_by = models.BigIntegerField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)
    modified_by = models.BigIntegerField(blank=True, null=True)
    title = models.CharField(max_length=50, blank=True, null=True)
    start = models.CharField(max_length=20, blank=True, null=True)
    end = models.CharField(max_length=20, blank=True, null=True)
    type = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_offices'


class TblOvertime(models.Model):
    asm_id = models.CharField(max_length=25)
    description = models.TextField(blank=True, null=True)
    misdescription = models.TextField(blank=True, null=True)
    date = models.DateField()
    hours = models.IntegerField(blank=True, null=True)
    type = models.CharField(max_length=25)
    status = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    created_by = models.IntegerField()
    updated_by = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_overtime'


class TblPages(models.Model):
    page_id = models.BigAutoField(primary_key=True)
    page_name = models.CharField(max_length=100)
    module_id = models.IntegerField()
    page_link = models.CharField(max_length=255)
    parent = models.IntegerField()
    active = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tbl_pages'


class TblPdpEvents(models.Model):
    event_id = models.BigAutoField(primary_key=True)
    year = models.IntegerField()
    date_added = models.DateField()
    deleted = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'tbl_pdp_events'


class TblPhysicalShift(models.Model):
    physical_shift_id = models.BigAutoField(primary_key=True)
    working_day_id = models.DateField()
    shift = models.ForeignKey('TblShifts', models.DO_NOTHING)
    attendance_event_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_physical_shift'


class TblPolicy(models.Model):
    id = models.BigAutoField(primary_key=True)
    topic = models.CharField(max_length=255)
    file_path = models.CharField(max_length=255)
    published_to = models.CharField(max_length=50)
    uploaded_by = models.BigIntegerField()
    uploaded_on = models.DateField()
    deleted = models.SmallIntegerField()
    deleted_by = models.BigIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_policy'


class TblPortalAccesses(models.Model):
    user_id = models.BigIntegerField(blank=True, null=True)
    portal_id = models.CharField(max_length=255)
    active = models.IntegerField()
    created = models.DateTimeField()
    created_by = models.BigIntegerField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)
    modified_by = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_portal_accesses'


class TblPortals(models.Model):
    name = models.CharField(max_length=100)
    active = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tbl_portals'


class TblQna(models.Model):
    question_answers = models.CharField(max_length=255)
    parent_id = models.IntegerField()
    campaign_id = models.IntegerField(blank=True, null=True)
    is_correct = models.IntegerField()
    time = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    created_by = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    deleted_by = models.IntegerField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_qna'


class TblQuarter(models.Model):
    quarter_id = models.BigAutoField(primary_key=True)
    quarter = models.IntegerField()
    year = models.IntegerField()
    batch_id = models.IntegerField()
    active = models.SmallIntegerField()
    date_added = models.DateField()
    deleted = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'tbl_quarter'


class TblQuizRoutes(models.Model):
    name = models.CharField(max_length=50)
    method = models.CharField(max_length=15, blank=True, null=True)
    created_at = models.DateTimeField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tbl_quiz_routes'


class TblQuizScore(models.Model):
    asm_id = models.CharField(max_length=50)
    agent_id = models.CharField(max_length=50)
    call_count = models.IntegerField()
    good_call_scores = models.FloatField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    created_by = models.IntegerField()
    updated_by = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_quiz_score'


class TblQuizUserRoutes(models.Model):
    route_id = models.IntegerField()
    user_id = models.IntegerField()
    can_access = models.CharField(max_length=1)
    created_at = models.DateTimeField()
    created_by = models.IntegerField()
    status = models.IntegerField()
    updated_at = models.DateTimeField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_quiz_user_routes'


class TblQuizes(models.Model):
    name = models.CharField(max_length=255)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    campaign_id = models.IntegerField()
    type = models.IntegerField()
    status = models.IntegerField()
    created_at = models.DateTimeField()
    created_by = models.IntegerField()
    updated_at = models.DateTimeField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    deleted_by = models.IntegerField(blank=True, null=True)
    question_count = models.IntegerField(blank=True, null=True)
    role_id = models.IntegerField(blank=True, null=True)
    group = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_quizes'


class TblQuizesQuestions(models.Model):
    quiz_id = models.IntegerField()
    question_id = models.IntegerField()
    created_by = models.BigIntegerField(blank=True, null=True)
    created = models.DateTimeField()
    group = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_quizes_questions'


class TblReferrals(models.Model):
    id = models.BigAutoField(primary_key=True)
    staff_id = models.CharField(max_length=15, blank=True, null=True)
    login_id = models.CharField(max_length=15, blank=True, null=True)
    sap_id = models.CharField(max_length=15, blank=True, null=True)
    staff_name = models.CharField(max_length=25, blank=True, null=True)
    candidate_name = models.CharField(max_length=25, blank=True, null=True)
    candidate_msisdn = models.CharField(max_length=12, blank=True, null=True)
    referral_desg = models.CharField(max_length=25, blank=True, null=True)
    reporting_to = models.CharField(max_length=25, blank=True, null=True)
    project = models.CharField(max_length=25, blank=True, null=True)
    added_date = models.DateTimeField(blank=True, null=True)
    added_by = models.CharField(max_length=25, blank=True, null=True)
    is_deleted = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_referrals'


class TblReversion(models.Model):
    reversion_id = models.BigAutoField(primary_key=True)
    user_id = models.BigIntegerField()
    physical_shift = models.ForeignKey(TblPhysicalShift, models.DO_NOTHING)
    roster_status = models.ForeignKey('TblRosterStatus', models.DO_NOTHING)
    time_in = models.TimeField()
    time_out = models.TimeField()
    teamlead_approval = models.SmallIntegerField(db_column='teamLead_Approval', blank=True, null=True)  # Field name made lowercase.
    action_pending = models.SmallIntegerField()
    user_applied_time = models.DateTimeField()
    teamlead_approval_time = models.DateTimeField(db_column='teamLead_Approval_time')  # Field name made lowercase.
    tc_approval_time = models.DateTimeField(db_column='TC_Approval_time')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_reversion'


class TblRosterStatus(models.Model):
    roster_status_id = models.BigAutoField(primary_key=True)
    roster_status = models.CharField(max_length=50)
    deleted = models.SmallIntegerField()
    deleted_by = models.BigIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_roster_status'


class TblSalaryDetails(models.Model):
    id = models.BigAutoField(primary_key=True)
    employee = models.ForeignKey(TblEmployees, models.DO_NOTHING)
    total_salary = models.FloatField()
    gross_salary = models.FloatField()
    basic_salary = models.FloatField()
    utility = models.FloatField()
    house_rent = models.FloatField()
    stipend_pay = models.FloatField()
    arrears = models.FloatField()
    bonus = models.FloatField()
    additional_allowance = models.FloatField()
    mobile_allowance = models.FloatField()
    upselling_commission = models.FloatField()
    incentive = models.FloatField()
    ot_amount = models.FloatField(db_column='ot_Amount')  # Field name made lowercase.
    total_gross = models.FloatField()
    advance_deduction = models.FloatField()
    mobile_deduction = models.FloatField()
    misc_deduction = models.FloatField()
    p_fund = models.FloatField()
    sal_adv_installment = models.FloatField()
    car_deduction = models.FloatField()
    income_tax = models.FloatField()
    other_tax_deduction = models.FloatField()
    deduction = models.FloatField()
    eobi_employee = models.FloatField()
    net_payable = models.FloatField()
    paid_days = models.BigIntegerField()
    sal_month = models.CharField(max_length=10)
    sal_year = models.BigIntegerField()
    sal_monyear = models.DateField(db_column='sal_monYear')  # Field name made lowercase.
    action_date = models.DateTimeField(blank=True, null=True)
    deleted = models.SmallIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)
    deleted_by = models.BigIntegerField(blank=True, null=True)
    uploaded = models.DateTimeField(blank=True, null=True)
    uploaded_by = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_salary_details'


class TblSeatIps(models.Model):
    extension = models.CharField(max_length=30, blank=True, null=True)
    seat_number = models.CharField(max_length=30, blank=True, null=True)
    ip_address = models.CharField(max_length=30)
    created = models.DateTimeField(blank=True, null=True)
    created_by = models.IntegerField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    updated = models.DateTimeField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    subnet_mask = models.CharField(max_length=30, blank=True, null=True)
    gate_way = models.CharField(max_length=30, blank=True, null=True)
    primary_dns = models.CharField(max_length=30, blank=True, null=True)
    secondary_dns = models.CharField(max_length=30, blank=True, null=True)
    center_id = models.IntegerField()
    seat_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_seat_ips'








class TblSetups04112019(models.Model):
    old_id = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    slug = models.CharField(max_length=100, blank=True, null=True)
    parent_id = models.IntegerField(blank=True, null=True)
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
        db_table = 'tbl_setups_04112019'


class TblSetups13112019(models.Model):
    old_id = models.CharField(max_length=50, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    slug = models.CharField(max_length=100, blank=True, null=True)
    parent_id = models.IntegerField(blank=True, null=True)
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
        db_table = 'tbl_setups_13112019'


class TblSetupsAccesses(models.Model):
    user_id = models.BigIntegerField()
    setup_id = models.IntegerField()
    base_id = models.IntegerField()
    level = models.IntegerField()
    active = models.IntegerField()
    created = models.DateTimeField(blank=True, null=True)
    created_by = models.BigIntegerField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)
    modified_by = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_setups_accesses'


class TblSetupsRights(models.Model):
    employee_id = models.BigIntegerField()
    setup_id = models.IntegerField()
    base_id = models.IntegerField()
    level = models.IntegerField()
    created_by = models.BigIntegerField(blank=True, null=True)
    created = models.DateTimeField()
    active = models.IntegerField()
    modified = models.DateTimeField(blank=True, null=True)
    modified_by = models.BigIntegerField(blank=True, null=True)
    can_edit = models.IntegerField()
    can_access = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tbl_setups_rights'


class TblShiftSwaps(models.Model):
    shift_swap_id = models.BigAutoField(primary_key=True)
    roster = models.BigIntegerField()
    user_id = models.BigIntegerField()
    actual_duty_person = models.BigIntegerField()
    shift_swap_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tbl_shift_swaps'


class TblShifts(models.Model):
    shift_id = models.BigAutoField(primary_key=True)
    shift_title = models.CharField(max_length=100)
    shift_code = models.CharField(max_length=20)
    start_time = models.TimeField()
    end_time = models.TimeField()
    deleted = models.SmallIntegerField()
    deleted_by = models.BigIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_shifts'


class TblSwap(models.Model):
    f_asm_id = models.CharField(max_length=35)
    t_asm_id = models.CharField(max_length=35)
    f_date = models.DateField()
    t_date = models.DateField()
    status = models.IntegerField()
    f_reason = models.TextField()
    t_reason = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tbl_swap'


class TblTasks(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    desc = models.TextField(blank=True, null=True)
    start_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)
    add_date = models.DateTimeField(blank=True, null=True)
    update_date = models.DateTimeField(blank=True, null=True)
    assigned_to = models.IntegerField(blank=True, null=True)
    assigned_by = models.IntegerField(blank=True, null=True)
    task_id = models.IntegerField(blank=True, null=True)
    task_status = models.CharField(max_length=11, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    hours = models.IntegerField(blank=True, null=True)
    quailty_rating = models.IntegerField(blank=True, null=True)
    grading = models.IntegerField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    remarks = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_tasks'


class TblTerminationReason(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_termination_reason'


class TblTickets(models.Model):
    project_id = models.IntegerField(blank=True, null=True)
    cli_effected = models.DecimalField(max_digits=17, decimal_places=0, blank=True, null=True)
    type_id = models.IntegerField(blank=True, null=True)
    time_start = models.DateTimeField(blank=True, null=True)
    time_end = models.DateTimeField(blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    created_by = models.ForeignKey('TblUsers', models.DO_NOTHING, db_column='created_by', blank=True, null=True, related_name="user_ticket_created")
    updated_by = models.ForeignKey('TblUsers', models.DO_NOTHING, db_column='updated_by', blank=True, null=True, related_name="user_ticket_updated")
    updated = models.DateTimeField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    image = models.CharField(max_length=255, blank=True, null=True)
    remarks = models.CharField(max_length=255, blank=True, null=True)
    temp_issue = models.IntegerField(blank=True, null=True)
    comment = models.CharField(max_length=255, blank=True, null=True)
    ip_address = models.CharField(max_length=100, blank=True, null=True)
    time_taken = models.DecimalField(max_digits=11, decimal_places=0, blank=True, null=True)
    type_id2 = models.IntegerField(blank=True, null=True)
    resolved_types = models.IntegerField(blank=True, null=True)
    decribe = models.CharField(max_length=255, blank=True, null=True)
    fraud_types = models.IntegerField(blank=True, null=True)
    fraud_status = models.IntegerField(blank=True, null=True)
    modified_by = models.BigIntegerField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)
    center_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_tickets'


class TblUploadMpr(models.Model):
    sap_id = models.BigIntegerField()
    staff_id = models.CharField(max_length=12)
    sip_id = models.IntegerField()
    name = models.CharField(max_length=30)
    mpr_month = models.IntegerField()
    mpr_year = models.IntegerField()
    mpr_points = models.DecimalField(max_digits=10, decimal_places=2)
    grade = models.CharField(max_length=1)
    amount = models.IntegerField()
    upload_date = models.DateTimeField()
    upload_by = models.IntegerField()
    is_deleted = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_upload_mpr'


class TblUserAnswers(models.Model):
    user_id = models.IntegerField()
    quiz_id = models.IntegerField()
    question_id = models.IntegerField()
    answer_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_user_answers'


class TblUserAttendances(models.Model):
    id = models.BigAutoField(primary_key=True)
    asm_id = models.BigIntegerField()
    user_id = models.BigIntegerField(blank=True, null=True)
    shift_id = models.IntegerField(blank=True, null=True)
    time_in = models.DateTimeField()
    time_out = models.DateTimeField(blank=True, null=True)
    created = models.DateTimeField()
    created_by = models.BigIntegerField(blank=True, null=True)
    updated = models.DateTimeField(blank=True, null=True)
    updated_by = models.BigIntegerField(blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    hours = models.IntegerField(blank=True, null=True)
    minutes = models.IntegerField(blank=True, null=True)
    today_diff = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_user_attendances'


class TblUserDelegation(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.BigIntegerField()
    delegate_to = models.BigIntegerField()
    page = models.ForeignKey(TblPages, models.DO_NOTHING)
    added_by = models.BigIntegerField()
    added_date = models.DateTimeField()
    deleted = models.SmallIntegerField()
    deleted_by = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'tbl_user_delegation'


class TblUserDepartmentHistory(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.BigIntegerField(blank=True, null=True)
    department_id = models.BigIntegerField(blank=True, null=True)
    prev_department_id = models.BigIntegerField(blank=True, null=True)
    transfer_date = models.DateTimeField(blank=True, null=True)
    leaving_date = models.DateTimeField(blank=True, null=True)
    reporting_to = models.BigIntegerField(blank=True, null=True)
    prev_reporting_to = models.BigIntegerField(blank=True, null=True)
    added_date = models.DateTimeField(blank=True, null=True)
    r_transfer_date = models.DateTimeField(blank=True, null=True)
    r_leaving_date = models.DateTimeField(blank=True, null=True)
    designation_id = models.BigIntegerField(blank=True, null=True)
    prev_designation_id = models.BigIntegerField(blank=True, null=True)
    transfer_date_desg = models.DateTimeField(blank=True, null=True)
    leaving_date_desg = models.DateTimeField(blank=True, null=True)
    user_type = models.SmallIntegerField(blank=True, null=True)
    prev_user_type = models.SmallIntegerField(blank=True, null=True)
    transfer_date_user_type = models.DateTimeField(blank=True, null=True)
    leaving_date_user_type = models.DateTimeField(blank=True, null=True)
    employment_type = models.CharField(max_length=12, blank=True, null=True)
    prev_emp_type = models.CharField(max_length=12, blank=True, null=True)
    transfer_date_emp_type = models.DateTimeField(blank=True, null=True)
    leaving_date_emp_type = models.DateTimeField(blank=True, null=True)
    release_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_user_department_history'


class TblUserDependent(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.BigIntegerField()
    dependent_name = models.CharField(max_length=255)
    relationship = models.CharField(max_length=30)
    birth_year = models.TextField()  # This field type is a guess.
    added_by = models.BigIntegerField()
    added_date = models.DateTimeField()
    deleted = models.SmallIntegerField()
    deleted_by = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'tbl_user_dependent'


class TblUserEducation(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.BigIntegerField()
    education = models.ForeignKey(TblEducation, models.DO_NOTHING)
    institute_name = models.CharField(max_length=150, blank=True, null=True)
    major = models.CharField(max_length=100, blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    score = models.CharField(max_length=25, blank=True, null=True)
    start_year = models.TextField(blank=True, null=True)  # This field type is a guess.
    end_year = models.TextField(blank=True, null=True)  # This field type is a guess.
    added_date = models.DateTimeField()
    deleted = models.SmallIntegerField()
    deleted_by = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'tbl_user_education'


class TblUserEvaluationObjectives(models.Model):
    objective_id = models.BigAutoField(primary_key=True)
    user_id = models.BigIntegerField()
    quarter_id = models.IntegerField()
    objective = models.TextField()
    added_by = models.BigIntegerField()
    date_added = models.DateTimeField()
    date_updated = models.DateTimeField(blank=True, null=True)
    deleted = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'tbl_user_evaluation_objectives'


class TblUserExperience(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.BigIntegerField()
    company = models.CharField(max_length=150)
    position = models.CharField(max_length=150)
    description = models.TextField(blank=True, null=True)
    date_from = models.DateField()
    date_to = models.DateField(blank=True, null=True)
    current_company = models.CharField(max_length=1)
    added_date = models.DateTimeField(blank=True, null=True)
    deleted = models.SmallIntegerField()
    deleted_by = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'tbl_user_experience'


class TblUserIds(models.Model):
    user_id = models.BigIntegerField()
    sap_id = models.CharField(max_length=25)
    staff_id = models.CharField(max_length=12)
    sip_id = models.CharField(max_length=10)
    cnic = models.CharField(max_length=14)
    added_date = models.DateTimeField()
    added_by = models.IntegerField()
    updated_date = models.DateTimeField(blank=True, null=True)
    updated_by = models.IntegerField()
    ids_lock = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tbl_user_ids'


class TblUserInsuranceClaims(models.Model):
    claim_id = models.BigAutoField(primary_key=True)
    user_id = models.BigIntegerField()
    entitlement = models.ForeignKey(TblInsuranceEntitlement, models.DO_NOTHING)
    claim_year = models.DateField()
    claim_amount = models.DecimalField(max_digits=15, decimal_places=0)
    approved = models.SmallIntegerField()
    approved_date = models.DateTimeField()
    added_by = models.BigIntegerField()
    added_date = models.DateTimeField()
    deleted = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'tbl_user_insurance_claims'


class TblUserInterest(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.BigIntegerField()
    interest_category_id = models.BigIntegerField()
    sub_category_id = models.TextField()
    other = models.CharField(max_length=100)
    instrument = models.CharField(max_length=50)
    added_date = models.DateTimeField()
    deleted = models.CharField(max_length=1)
    deleted_by = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'tbl_user_interest'


class TblUserMedicalInsurance(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.BigIntegerField()
    insurance_id = models.CharField(max_length=20)
    insurance_policy_no = models.CharField(max_length=20)
    plan = models.CharField(max_length=3)
    added_date = models.DateTimeField()
    deleted = models.SmallIntegerField()
    deleted_by = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'tbl_user_medical_insurance'


class TblUserProfile(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.BigIntegerField()
    father_name = models.CharField(max_length=150)
    marital_status = models.CharField(max_length=8, blank=True, null=True)
    religion = models.BigIntegerField()
    gender = models.CharField(max_length=6, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    blood_group = models.CharField(max_length=10, blank=True, null=True)
    cnic_no = models.CharField(max_length=15)
    passport_no = models.CharField(max_length=30, blank=True, null=True)
    eobi_no = models.CharField(max_length=30, blank=True, null=True)
    laptop_id = models.CharField(max_length=30, blank=True, null=True)
    social_security_no = models.CharField(max_length=30, blank=True, null=True)
    rfid_card_issued = models.CharField(max_length=1, blank=True, null=True)
    employee_card_issuance_date = models.DateField(blank=True, null=True)
    telenor_sim_issuance_date = models.DateField(blank=True, null=True)
    telenor_no = models.CharField(max_length=17, blank=True, null=True)
    permanent_address = models.TextField(blank=True, null=True)
    current_address = models.TextField(blank=True, null=True)
    home_phone = models.CharField(max_length=17, blank=True, null=True)
    mobile_phone = models.CharField(max_length=17, blank=True, null=True)
    work_phone = models.CharField(max_length=17, blank=True, null=True)
    work_phone_ext = models.CharField(max_length=10, blank=True, null=True)
    sect = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'tbl_user_profile'


class TblUserQuarterStatus(models.Model):
    quarter_user_id = models.BigAutoField(primary_key=True)
    quarter_id = models.IntegerField()
    user_id = models.IntegerField()
    active = models.SmallIntegerField()
    date_active = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tbl_user_quarter_status'


class TblUserRecommendation(models.Model):
    recommendation_id = models.BigAutoField(primary_key=True)
    event_id = models.BigIntegerField()
    appraiser_id = models.BigIntegerField()
    appraisee_id = models.BigIntegerField()
    training_recevied = models.TextField()
    training_remarks = models.TextField(blank=True, null=True)
    special_contribution = models.TextField(blank=True, null=True)
    obstacles_encountered = models.TextField(blank=True, null=True)
    recommend_for_promotion = models.TextField(blank=True, null=True)
    specific_areas = models.TextField(blank=True, null=True)
    agree_with_appraisal = models.TextField(blank=True, null=True)
    disagree_with_appraisal = models.TextField(blank=True, null=True)
    date_added = models.DateTimeField()
    ref_recommendation_id = models.BigIntegerField()
    locked = models.CharField(max_length=1)
    forward_to = models.BigIntegerField()
    forward_by = models.BigIntegerField()
    forward_on = models.DateTimeField(blank=True, null=True)
    processed_by = models.CharField(max_length=1)
    tl_viewed = models.CharField(max_length=1)
    added_by = models.BigIntegerField()
    actual_recomm_id = models.BigIntegerField()
    finalized = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'tbl_user_recommendation'


class TblUserRecommendationDevelopmentAreas(models.Model):
    id = models.BigAutoField(primary_key=True)
    recommendation = models.ForeignKey(TblUserRecommendation, models.DO_NOTHING)
    development_area = models.TextField()
    date_added = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_user_recommendation_development_areas'


class TblUserSessions(models.Model):
    user_id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    ip = models.CharField(max_length=100)
    user_agent = models.TextField()
    token = models.CharField(max_length=255)
    active = models.IntegerField()
    created = models.DateTimeField()
    modified = models.DateTimeField()
    accesses = models.TextField(blank=True, null=True)
    center_id = models.IntegerField(blank=True, null=True)
    department_id = models.IntegerField(blank=True, null=True)
    designation_id = models.IntegerField(blank=True, null=True)
    project_id = models.CharField(max_length=100, blank=True, null=True)
    campaign_id = models.CharField(max_length=150, blank=True, null=True)
    sub_campaign_id = models.CharField(max_length=200, blank=True, null=True)
    employee_id = models.BigIntegerField(blank=True, null=True)
    cnic = models.CharField(max_length=20, blank=True, null=True)
    role_id = models.IntegerField(blank=True, null=True)
    reporting_to = models.BigIntegerField(blank=True, null=True)
    reporting_too = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_user_sessions'
        unique_together = (('user_id', 'token'),)


class TblUserSkills(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.BigIntegerField()
    skill_id = models.CharField(max_length=100)
    years_of_exp = models.DateField()
    comments = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'tbl_user_skills'


class TblUserStatus(models.Model):
    status_id = models.AutoField(primary_key=True)
    status = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'tbl_user_status'


class TblUserStatusLog(models.Model):
    log_id = models.BigAutoField(primary_key=True)
    user_id = models.BigIntegerField()
    status = models.BigIntegerField()
    change_date = models.DateTimeField()
    action_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tbl_user_status_log'





class TblVendorCompanies(models.Model):
    phone = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    created_by = models.IntegerField(blank=True, null=True)
    updated = models.DateTimeField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    deleted = models.DateTimeField(blank=True, null=True)
    deleted_by = models.IntegerField(blank=True, null=True)
    person_name = models.CharField(max_length=100, blank=True, null=True)
    person_phone = models.IntegerField(blank=True, null=True)
    remarks = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_vendor_companies'


class TblWorkingDays(models.Model):
    working_day_id = models.DateField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'tbl_working_days'


class Test(models.Model):
    sap_id = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'test'
