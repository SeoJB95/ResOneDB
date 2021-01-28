# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class CfdMethod(models.Model):
    method = models.CharField(db_column='METHOD', primary_key=True, max_length=10)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cfd_method'


class CfdStarccmPowResults(models.Model):
    project_no = models.OneToOneField('PropellerMainParticular',models.DO_NOTHING, db_column='PROJECT_NO', primary_key=True)  # Field name made lowercase.
    version = models.ForeignKey('PropellerMainParticular',related_name='CCM_version',on_delete=  models.DO_NOTHING, db_column='VERSION')  # Field name made lowercase.
    prop_status = models.ForeignKey('PropellerMainParticular',related_name='CCM_prop_state',on_delete=  models.DO_NOTHING, db_column='PROP_STATUS')  # Field name made lowercase.
    geometry_file = models.TextField(db_column='GEOMETRY_FILE', blank=True, null=True)  # Field name made lowercase.
    java_file = models.TextField(db_column='JAVA_FILE', blank=True, null=True)  # Field name made lowercase.
    pow_stl_info_file = models.TextField(db_column='POW_STL_INFO_FILE', blank=True, null=True)  # Field name made lowercase.
    csv_pow_results = models.TextField(db_column='CSV_POW_RESULTS', blank=True, null=True)  # Field name made lowercase.
    png_suction_side = models.TextField(db_column='PNG_SUCTION_SIDE', blank=True, null=True)  # Field name made lowercase.
    png_pressure_side = models.TextField(db_column='PNG_PRESSURE_SIDE', blank=True, null=True)  # Field name made lowercase.
    comments = models.CharField(db_column='COMMENTS', max_length=250, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cfd_starccm_pow_results'
        unique_together = (('project_no', 'version', 'prop_status'),)


class CfdStarccmResistanceResults(models.Model):
    project_no = models.OneToOneField('ShipDraftData', models.DO_NOTHING, db_column='PROJECT_NO', primary_key=True)  # Field name made lowercase.
    version = models.ForeignKey('ShipDraftData',related_name='CCM_version', on_delete= models.DO_NOTHING, db_column='VERSION')  # Field name made lowercase.
    draft_name = models.ForeignKey('ShipDraftData',related_name='CCM_draft_name',on_delete=  models.DO_NOTHING, db_column='DRAFT_NAME')  # Field name made lowercase.
    ship_speed = models.DecimalField(db_column='SHIP_SPEED', max_digits=4, decimal_places=2)  # Field name made lowercase.
    designer = models.CharField(db_column='DESIGNER', max_length=10, blank=True, null=True)  # Field name made lowercase.
    cr = models.DecimalField(db_column='CR', max_digits=6, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    csv_wave_profile = models.TextField(db_column='CSV_WAVE_PROFILE', blank=True, null=True)  # Field name made lowercase.
    png_wave_pattern = models.TextField(db_column='PNG_WAVE_PATTERN', blank=True, null=True)  # Field name made lowercase.
    png_body_fore_pressure = models.TextField(db_column='PNG_BODY_FORE_PRESSURE', blank=True, null=True)  # Field name made lowercase.
    png_body_aft_pressure = models.TextField(db_column='PNG_BODY_AFT_PRESSURE', blank=True, null=True)  # Field name made lowercase.
    png_side_fore_pressure = models.TextField(db_column='PNG_SIDE_FORE_PRESSURE', blank=True, null=True)  # Field name made lowercase.
    png_side_aft_pressure = models.TextField(db_column='PNG_SIDE_AFT_PRESSURE', blank=True, null=True)  # Field name made lowercase.
    png_fore_stream = models.TextField(db_column='PNG_FORE_STREAM', blank=True, null=True)  # Field name made lowercase.
    png_aft_stream = models.TextField(db_column='PNG_AFT_STREAM', blank=True, null=True)  # Field name made lowercase.
    png_wake = models.TextField(db_column='PNG_WAKE', blank=True, null=True)  # Field name made lowercase.
    txt_vtt_ccm_info = models.TextField(db_column='TXT_VTT_CCM_INFO', blank=True, null=True)  # Field name made lowercase.
    java_vtt_cfd_update = models.TextField(db_column='JAVA_VTT_CFD_UPDATE', blank=True, null=True)  # Field name made lowercase.
    csv_fx_mean = models.TextField(db_column='CSV_FX_MEAN', blank=True, null=True)  # Field name made lowercase.
    csv_trimsinkage_mean = models.TextField(db_column='CSV_TRIMSINKAGE_MEAN', blank=True, null=True)  # Field name made lowercase.
    comments = models.CharField(db_column='COMMENTS', max_length=250, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cfd_starccm_resistance_results'
        unique_together = (('project_no', 'version', 'draft_name', 'ship_speed'),)


class CfdWavis22ResistanceResults(models.Model):
    project_no = models.OneToOneField('ShipDraftData', models.DO_NOTHING, db_column='PROJECT_NO', primary_key=True)  # Field name made lowercase.
    version = models.ForeignKey('ShipDraftData',related_name='WAVIS_version', on_delete= models.DO_NOTHING, db_column='VERSION')  # Field name made lowercase.
    draft_name = models.ForeignKey('ShipDraftData',related_name='WAVIS_draft_name',on_delete=  models.DO_NOTHING, db_column='DRAFT_NAME')  # Field name made lowercase.
    ship_speed = models.DecimalField(db_column='SHIP_SPEED', max_digits=4, decimal_places=2)  # Field name made lowercase.
    designer = models.CharField(db_column='DESIGNER', max_length=10, blank=True, null=True)  # Field name made lowercase.
    cr = models.DecimalField(db_column='CR', max_digits=6, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    wave_profile = models.TextField(db_column='WAVE_PROFILE', blank=True, null=True)  # Field name made lowercase.
    png_wave_pattern = models.TextField(db_column='PNG_WAVE_PATTERN', blank=True, null=True)  # Field name made lowercase.
    png_body_fore_pressure = models.TextField(db_column='PNG_BODY_FORE_PRESSURE', blank=True, null=True)  # Field name made lowercase.
    png_body_aft_pressure = models.TextField(db_column='PNG_BODY_AFT_PRESSURE', blank=True, null=True)  # Field name made lowercase.
    png_side_fore_pressure = models.TextField(db_column='PNG_SIDE_FORE_PRESSURE', blank=True, null=True)  # Field name made lowercase.
    png_side_aft_pressure = models.TextField(db_column='PNG_SIDE_AFT_PRESSURE', blank=True, null=True)  # Field name made lowercase.
    png_fore_stream = models.TextField(db_column='PNG_FORE_STREAM', blank=True, null=True)  # Field name made lowercase.
    png_aft_stream = models.TextField(db_column='PNG_AFT_STREAM', blank=True, null=True)  # Field name made lowercase.
    png_wake = models.TextField(db_column='PNG_WAKE', blank=True, null=True)  # Field name made lowercase.
    surmesh_cpm = models.TextField(db_column='SurMesh_cpm', blank=True, null=True)  # Field name made lowercase.
    wavis_prx = models.TextField(db_column='Wavis_prx', blank=True, null=True)  # Field name made lowercase.
    wavis_fix = models.TextField(db_column='Wavis_fix', blank=True, null=True)  # Field name made lowercase.
    fieldgenh_cph = models.TextField(db_column='fieldgenH_cph', blank=True, null=True)  # Field name made lowercase.
    wavis_prm = models.TextField(db_column='Wavis_prm', blank=True, null=True)  # Field name made lowercase.
    wavis_pro = models.TextField(db_column='Wavis_pro', blank=True, null=True)  # Field name made lowercase.
    wavis_cpv = models.TextField(db_column='Wavis_cpv', blank=True, null=True)  # Field name made lowercase.
    comments = models.CharField(db_column='COMMENTS', max_length=250, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cfd_wavis22_resistance_results'
        unique_together = (('project_no', 'version', 'draft_name', 'ship_speed'),)


class DraftName(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=10)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'draft_name'


class ManeuveringImoCriteria(models.Model):
    project_no = models.OneToOneField('ShipMainParticular', models.DO_NOTHING, db_column='PROJECT_NO', primary_key=True)  # Field name made lowercase.
    version = models.ForeignKey('ShipMainParticular',related_name='ManeuveringImo_version',on_delete=  models.DO_NOTHING, db_column='VERSION')  # Field name made lowercase.
    draft_name = models.ForeignKey(DraftName, models.DO_NOTHING, db_column='DRAFT_NAME')  # Field name made lowercase.
    init_turn = models.DecimalField(db_column='INIT_TURN', max_digits=6, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    advance = models.DecimalField(db_column='ADVANCE', max_digits=6, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    tactical_dia = models.DecimalField(db_column='TACTICAL_DIA', max_digits=6, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    overshoot_10_1st = models.DecimalField(db_column='OVERSHOOT_10_1ST', max_digits=6, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    overshoot_10_2nd = models.DecimalField(db_column='OVERSHOOT_10_2ND', max_digits=6, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    overshoot_20_1st = models.DecimalField(db_column='OVERSHOOT_20_1ST', max_digits=6, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    track_reach_crash = models.DecimalField(db_column='TRACK_REACH_CRASH', max_digits=8, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    comments = models.CharField(db_column='COMMENTS', max_length=250, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'maneuvering_imo_criteria'
        unique_together = (('project_no', 'version', 'draft_name'),)


class ModelTestCavitationPressure(models.Model):
    project_no = models.OneToOneField('ShipDraftData', models.DO_NOTHING, db_column='PROJECT_NO', primary_key=True)  # Field name made lowercase.
    version = models.ForeignKey('ShipDraftData',related_name='ModelTestCavitation_version', on_delete= models.DO_NOTHING, db_column='VERSION')  # Field name made lowercase.
    prop_status = models.ForeignKey('PropellerMainParticular', models.DO_NOTHING, db_column='PROP_STATUS')  # Field name made lowercase.
    draft_name = models.ForeignKey('ShipDraftData',related_name='ModelTestCavitation_draft_name',on_delete=  models.DO_NOTHING, db_column='DRAFT_NAME')  # Field name made lowercase.
    ship_model_id = models.CharField(db_column='SHIP_MODEL_ID', max_length=15, blank=True, null=True)  # Field name made lowercase.
    prop_id = models.CharField(db_column='PROP_ID', max_length=15, blank=True, null=True)  # Field name made lowercase.
    rudder_no = models.IntegerField(db_column='RUDDER_NO', blank=True, null=True)  # Field name made lowercase.
    stern_wave = models.DecimalField(db_column='STERN_WAVE', max_digits=3, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    tunnel_speed = models.DecimalField(db_column='TUNNEL_SPEED', max_digits=3, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    rotation_rps = models.DecimalField(db_column='ROTATION_RPS', max_digits=3, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    advance_coef = models.DecimalField(db_column='ADVANCE_COEF', max_digits=5, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    thrust_coef = models.DecimalField(db_column='THRUST_COEF', max_digits=5, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    cavitation_no = models.DecimalField(db_column='CAVITATION_NO', max_digits=6, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    rn_06 = models.DecimalField(db_column='RN_06', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    air_content = models.DecimalField(db_column='AIR_CONTENT', max_digits=3, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    sheet_start = models.IntegerField(db_column='SHEET_START', blank=True, null=True)  # Field name made lowercase.
    sheet_end = models.IntegerField(db_column='SHEET_END', blank=True, null=True)  # Field name made lowercase.
    tip_start = models.IntegerField(db_column='TIP_START', blank=True, null=True)  # Field name made lowercase.
    tip_end = models.IntegerField(db_column='TIP_END', blank=True, null=True)  # Field name made lowercase.
    face_margin = models.IntegerField(db_column='FACE_MARGIN', blank=True, null=True)  # Field name made lowercase.
    png_model_view_all = models.TextField(db_column='PNG_MODEL_VIEW_ALL', blank=True, null=True)  # Field name made lowercase.
    png_model_view_fore = models.TextField(db_column='PNG_MODEL_VIEW_FORE', blank=True, null=True)  # Field name made lowercase.
    png_model_view_aft = models.TextField(db_column='PNG_MODEL_VIEW_AFT', blank=True, null=True)  # Field name made lowercase.
    png_model_view_prop = models.TextField(db_column='PNG_MODEL_VIEW_PROP', blank=True, null=True)  # Field name made lowercase.
    png_model_stbd_port = models.TextField(db_column='PNG_MODEL_STBD_PORT', blank=True, null=True)  # Field name made lowercase.
    png_angle_definition = models.TextField(db_column='PNG_ANGLE_DEFINITION', blank=True, null=True)  # Field name made lowercase.
    png_sensor_position = models.TextField(db_column='PNG_SENSOR_POSITION', blank=True, null=True)  # Field name made lowercase.
    png_cavi_shetch_1 = models.TextField(db_column='PNG_CAVI_SHETCH_1', blank=True, null=True)  # Field name made lowercase.
    png_cavi_sketch_2 = models.TextField(db_column='PNG_CAVI_SKETCH_2', blank=True, null=True)  # Field name made lowercase.
    png_cavi_sketch_3 = models.TextField(db_column='PNG_CAVI_SKETCH_3', blank=True, null=True)  # Field name made lowercase.
    png_cavi_sketch_4 = models.TextField(db_column='PNG_CAVI_SKETCH_4', blank=True, null=True)  # Field name made lowercase.
    png_cavi_sketch_5 = models.TextField(db_column='PNG_CAVI_SKETCH_5', blank=True, null=True)  # Field name made lowercase.
    png_cavi_sketch_6 = models.TextField(db_column='PNG_CAVI_SKETCH_6', blank=True, null=True)  # Field name made lowercase.
    png_cavi_sketch_7 = models.TextField(db_column='PNG_CAVI_SKETCH_7', blank=True, null=True)  # Field name made lowercase.
    png_cavi_sketch_8 = models.TextField(db_column='PNG_CAVI_SKETCH_8', blank=True, null=True)  # Field name made lowercase.
    png_cavi_photo_1a = models.TextField(db_column='PNG_CAVI_PHOTO_1A', blank=True, null=True)  # Field name made lowercase.
    png_cavi_photo_1b = models.TextField(db_column='PNG_CAVI_PHOTO_1B', blank=True, null=True)  # Field name made lowercase.
    png_cavi_photo_2a = models.TextField(db_column='PNG_CAVI_PHOTO_2A', blank=True, null=True)  # Field name made lowercase.
    png_cavi_photo_2b = models.TextField(db_column='PNG_CAVI_PHOTO_2B', blank=True, null=True)  # Field name made lowercase.
    png_cavi_photo_3a = models.TextField(db_column='PNG_CAVI_PHOTO_3A', blank=True, null=True)  # Field name made lowercase.
    png_cavi_photo_3b = models.TextField(db_column='PNG_CAVI_PHOTO_3B', blank=True, null=True)  # Field name made lowercase.
    png_cavi_photo_4a = models.TextField(db_column='PNG_CAVI_PHOTO_4A', blank=True, null=True)  # Field name made lowercase.
    png_cavi_photo_4b = models.TextField(db_column='PNG_CAVI_PHOTO_4B', blank=True, null=True)  # Field name made lowercase.
    png_cavi_photo_5a = models.TextField(db_column='PNG_CAVI_PHOTO_5A', blank=True, null=True)  # Field name made lowercase.
    png_cavi_photo_5b = models.TextField(db_column='PNG_CAVI_PHOTO_5B', blank=True, null=True)  # Field name made lowercase.
    png_cavi_photo_6a = models.TextField(db_column='PNG_CAVI_PHOTO_6A', blank=True, null=True)  # Field name made lowercase.
    png_cavi_photo_6b = models.TextField(db_column='PNG_CAVI_PHOTO_6B', blank=True, null=True)  # Field name made lowercase.
    png_cavi_photo_7a = models.TextField(db_column='PNG_CAVI_PHOTO_7A', blank=True, null=True)  # Field name made lowercase.
    png_cavi_photo_7b = models.TextField(db_column='PNG_CAVI_PHOTO_7B', blank=True, null=True)  # Field name made lowercase.
    png_cavi_photo_8a = models.TextField(db_column='PNG_CAVI_PHOTO_8A', blank=True, null=True)  # Field name made lowercase.
    png_cavi_photo_8b = models.TextField(db_column='PNG_CAVI_PHOTO_8B', blank=True, null=True)  # Field name made lowercase.
    png_pressure_result = models.TextField(db_column='PNG_PRESSURE_RESULT', blank=True, null=True)  # Field name made lowercase.
    max_pressure_position = models.CharField(db_column='MAX_PRESSURE_POSITION', max_length=5, blank=True, null=True)  # Field name made lowercase.
    number_1st_pressure = models.DecimalField(db_column='1ST_PRESSURE', max_digits=5, decimal_places=3, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2nd_pressure = models.DecimalField(db_column='2ND_PRESSURE', max_digits=5, decimal_places=3, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3rd_pressure = models.DecimalField(db_column='3RD_PRESSURE', max_digits=5, decimal_places=3, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_4th_pressure = models.DecimalField(db_column='4TH_PRESSURE', max_digits=5, decimal_places=3, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_5th_pressure = models.DecimalField(db_column='5TH_PRESSURE', max_digits=5, decimal_places=3, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    mp4_port_cavitation = models.TextField(db_column='MP4_PORT_CAVITATION', blank=True, null=True)  # Field name made lowercase.
    mp4_stbd_cavitation = models.TextField(db_column='MP4_STBD_CAVITATION', blank=True, null=True)  # Field name made lowercase.
    pdf_test_report = models.TextField(db_column='PDF_TEST_REPORT', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'model_test_cavitation_pressure'
        unique_together = (('project_no', 'version', 'prop_status', 'draft_name'),)


class ModelTestCrashStopAstern(models.Model):
    project_no = models.OneToOneField('ShipMainParticular', models.DO_NOTHING, db_column='PROJECT_NO', primary_key=True)  # Field name made lowercase.
    version = models.ForeignKey('ShipMainParticular',related_name='ModelTestCrashStopAstern_version', on_delete=models.DO_NOTHING, db_column='VERSION')  # Field name made lowercase.
    prop_status = models.ForeignKey('PropStatus', models.DO_NOTHING, db_column='PROP_STATUS')  # Field name made lowercase.
    draft_name = models.ForeignKey(DraftName, models.DO_NOTHING, db_column='DRAFT_NAME')  # Field name made lowercase.
    testdate = models.DateField(db_column='TESTDATE', blank=True, null=True)  # Field name made lowercase.
    rpm_1 = models.DecimalField(db_column='RPM_1', max_digits=6, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    time_1 = models.DecimalField(db_column='TIME_1', max_digits=6, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    rpm_2 = models.DecimalField(db_column='RPM_2', max_digits=6, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    time_2 = models.DecimalField(db_column='TIME_2', max_digits=6, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    rpm_3 = models.DecimalField(db_column='RPM_3', max_digits=6, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    time_3 = models.DecimalField(db_column='TIME_3', max_digits=6, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    rpm_4 = models.DecimalField(db_column='RPM_4', max_digits=6, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    time_4 = models.DecimalField(db_column='TIME_4', max_digits=6, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    initial_rpm = models.DecimalField(db_column='INITIAL_RPM', max_digits=5, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    initial_speed = models.DecimalField(db_column='INITIAL_SPEED', max_digits=5, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    track_reach = models.DecimalField(db_column='TRACK_REACH', max_digits=7, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    track_ratio = models.DecimalField(db_column='TRACK_RATIO', max_digits=6, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    rpm_zero_time = models.DecimalField(db_column='RPM_ZERO_TIME', max_digits=6, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    elap_time = models.DateField(db_column='ELAP_TIME', blank=True, null=True)  # Field name made lowercase.
    p_manager = models.CharField(db_column='P_MANAGER', max_length=15, blank=True, null=True)  # Field name made lowercase.
    update_date = models.DateField(db_column='UPDATE_DATE', blank=True, null=True)  # Field name made lowercase.
    comments = models.CharField(db_column='COMMENTS', max_length=250, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'model_test_crash_stop_astern'
        unique_together = (('project_no', 'version', 'prop_status', 'draft_name'),)


class ModelTestPropellerOpenWater(models.Model):
    project_no = models.OneToOneField('PropellerMainParticular', models.DO_NOTHING, db_column='PROJECT_NO', primary_key=True)  # Field name made lowercase.
    version = models.ForeignKey('PropellerMainParticular',related_name='ModelTestPropellerOpenWater_version', on_delete=models.DO_NOTHING, db_column='VERSION')  # Field name made lowercase.
    prop_status = models.ForeignKey('PropellerMainParticular',related_name='ModelTestPropellerOpenWater_prop_status',on_delete= models.DO_NOTHING, db_column='PROP_STATUS')  # Field name made lowercase.
    prop_id = models.CharField(db_column='PROP_ID', max_length=15, blank=True, null=True)  # Field name made lowercase.
    water_temp = models.DecimalField(db_column='WATER_TEMP', max_digits=4, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    test_rps = models.DecimalField(db_column='TEST_RPS', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    local_rn = models.DecimalField(db_column='LOCAL_RN', max_digits=6, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    shaft_immersion = models.DecimalField(db_column='SHAFT_IMMERSION', max_digits=6, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    pow_full = models.TextField(db_column='POW_FULL', blank=True, null=True)  # Field name made lowercase.
    pow_model = models.TextField(db_column='POW_MODEL', blank=True, null=True)  # Field name made lowercase.
    test_manager = models.CharField(db_column='TEST_MANAGER', max_length=15, blank=True, null=True)  # Field name made lowercase.
    test_date = models.DateField(db_column='TEST_DATE', blank=True, null=True)  # Field name made lowercase.
    update_date = models.DateField(db_column='UPDATE_DATE', blank=True, null=True)  # Field name made lowercase.
    comments = models.CharField(db_column='COMMENTS', max_length=250, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'model_test_propeller_open_water'
        unique_together = (('project_no', 'version', 'prop_status'),)


class ModelTestSelfPropulsion(models.Model):
    project_no = models.OneToOneField('ShipDraftData', models.DO_NOTHING, db_column='PROJECT_NO', primary_key=True)  # Field name made lowercase.
    version = models.ForeignKey('ShipDraftData',related_name='ModelTestSelfPropulsion_version', on_delete=models.DO_NOTHING, db_column='VERSION')  # Field name made lowercase.
    draft_name = models.ForeignKey('ShipDraftData',related_name='ModelTestSelfPropulsion_draft_name', on_delete=models.DO_NOTHING, db_column='DRAFT_NAME')  # Field name made lowercase.
    prop_status = models.ForeignKey('PropellerMainParticular', models.DO_NOTHING, db_column='PROP_STATUS')  # Field name made lowercase.
    test_option = models.CharField(db_column='TEST_OPTION', max_length=25)  # Field name made lowercase.
    model_no = models.CharField(db_column='MODEL_NO', max_length=12, blank=True, null=True)  # Field name made lowercase.
    rudder_no = models.CharField(db_column='RUDDER_NO', max_length=12, blank=True, null=True)  # Field name made lowercase.
    wave_height = models.TextField(db_column='WAVE_HEIGHT', blank=True, null=True)  # Field name made lowercase.
    comments = models.CharField(db_column='COMMENTS', max_length=250, blank=True, null=True)  # Field name made lowercase.
    resistance_date = models.DateField(db_column='RESISTANCE_DATE', blank=True, null=True)  # Field name made lowercase.
    scale_ratio = models.DecimalField(db_column='SCALE_RATIO', max_digits=6, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    resistance_temp = models.DecimalField(db_column='RESISTANCE_TEMP', max_digits=4, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    hull_roughness = models.IntegerField(db_column='HULL_ROUGHNESS', blank=True, null=True)  # Field name made lowercase.
    ca = models.DecimalField(db_column='CA', max_digits=7, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    cas = models.DecimalField(db_column='CAS', max_digits=7, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    cair = models.DecimalField(db_column='CAIR', max_digits=7, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    prop_no = models.CharField(db_column='PROP_NO', max_length=12, blank=True, null=True)  # Field name made lowercase.
    self_date = models.DateField(db_column='SELF_DATE', blank=True, null=True)  # Field name made lowercase.
    self_temp = models.DecimalField(db_column='SELF_TEMP', max_digits=4, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    prop_roughness = models.IntegerField(db_column='PROP_ROUGHNESS', blank=True, null=True)  # Field name made lowercase.
    etat = models.DecimalField(db_column='ETAT', max_digits=4, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    model_basin = models.CharField(db_column='MODEL_BASIN', max_length=15, blank=True, null=True)  # Field name made lowercase.
    cp = models.DecimalField(db_column='CP', max_digits=4, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    cn = models.DecimalField(db_column='CN', max_digits=4, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    trial_speeed = models.DecimalField(db_column='TRIAL_SPEEED', max_digits=4, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    trial_rpm = models.DecimalField(db_column='TRIAL_RPM', max_digits=5, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    trial_power = models.IntegerField(db_column='TRIAL_POWER', blank=True, null=True)  # Field name made lowercase.
    service_speed = models.DecimalField(db_column='SERVICE_SPEED', max_digits=4, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    service_rpm = models.DecimalField(db_column='SERVICE_RPM', max_digits=5, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    sea_margin = models.DecimalField(db_column='SEA_MARGIN', max_digits=3, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    resistance_result = models.TextField(db_column='RESISTANCE_RESULT', blank=True, null=True)  # Field name made lowercase.
    propulsion_result = models.TextField(db_column='PROPULSION_RESULT', blank=True, null=True)  # Field name made lowercase.
    resistance_manager = models.CharField(db_column='RESISTANCE_MANAGER', max_length=15, blank=True, null=True)  # Field name made lowercase.
    propulsion_manager = models.CharField(db_column='PROPULSION_MANAGER', max_length=15, blank=True, null=True)  # Field name made lowercase.
    jpg_bow_photo_1 = models.TextField(db_column='JPG_BOW_PHOTO_1', blank=True, null=True)  # Field name made lowercase.
    jpg_bow_photo_2 = models.TextField(db_column='JPG_BOW_PHOTO_2', blank=True, null=True)  # Field name made lowercase.
    jpg_bow_photo_3 = models.TextField(db_column='JPG_BOW_PHOTO_3', blank=True, null=True)  # Field name made lowercase.
    jpg_bow_photo_4 = models.TextField(db_column='JPG_BOW_PHOTO_4', blank=True, null=True)  # Field name made lowercase.
    jpg_bow_photo_5 = models.TextField(db_column='JPG_BOW_PHOTO_5', blank=True, null=True)  # Field name made lowercase.
    jpg_bow_photo_6 = models.TextField(db_column='JPG_BOW_PHOTO_6', blank=True, null=True)  # Field name made lowercase.
    jpg_bow_photo_7 = models.TextField(db_column='JPG_BOW_PHOTO_7', blank=True, null=True)  # Field name made lowercase.
    jpg_ap_photo_1 = models.TextField(db_column='JPG_AP_PHOTO_1', blank=True, null=True)  # Field name made lowercase.
    jpg_ap_photo_2 = models.TextField(db_column='JPG_AP_PHOTO_2', blank=True, null=True)  # Field name made lowercase.
    jpg_ap_photo_3 = models.TextField(db_column='JPG_AP_PHOTO_3', blank=True, null=True)  # Field name made lowercase.
    jpg_ap_photo_4 = models.TextField(db_column='JPG_AP_PHOTO_4', blank=True, null=True)  # Field name made lowercase.
    jpg_ap_photo_5 = models.TextField(db_column='JPG_AP_PHOTO_5', blank=True, null=True)  # Field name made lowercase.
    jpg_ap_photo_6 = models.TextField(db_column='JPG_AP_PHOTO_6', blank=True, null=True)  # Field name made lowercase.
    jpg_ap_photo_7 = models.TextField(db_column='JPG_AP_PHOTO_7', blank=True, null=True)  # Field name made lowercase.
    jpg_fp_photo_1 = models.TextField(db_column='JPG_FP_PHOTO_1', blank=True, null=True)  # Field name made lowercase.
    jpg_fp_photo_2 = models.TextField(db_column='JPG_FP_PHOTO_2', blank=True, null=True)  # Field name made lowercase.
    jpg_fp_photo_3 = models.TextField(db_column='JPG_FP_PHOTO_3', blank=True, null=True)  # Field name made lowercase.
    jpg_fp_photo_4 = models.TextField(db_column='JPG_FP_PHOTO_4', blank=True, null=True)  # Field name made lowercase.
    jpg_fp_photo_5 = models.TextField(db_column='JPG_FP_PHOTO_5', blank=True, null=True)  # Field name made lowercase.
    jpg_fp_photo_6 = models.TextField(db_column='JPG_FP_PHOTO_6', blank=True, null=True)  # Field name made lowercase.
    jpg_fp_photo_7 = models.TextField(db_column='JPG_FP_PHOTO_7', blank=True, null=True)  # Field name made lowercase.
    mpg_fore_wave = models.TextField(db_column='MPG_FORE_WAVE', blank=True, null=True)  # Field name made lowercase.
    mpg_aft_wave = models.TextField(db_column='MPG_AFT_WAVE', blank=True, null=True)  # Field name made lowercase.
    pdf_test_report = models.TextField(db_column='PDF_TEST_REPORT', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'model_test_self_propulsion'
        unique_together = (('project_no', 'version', 'draft_name', 'prop_status', 'test_option'),)


class ModelTestStopping(models.Model):
    project_no = models.OneToOneField('ShipMainParticular', models.DO_NOTHING, db_column='PROJECT_NO', primary_key=True)  # Field name made lowercase.
    version = models.ForeignKey('ShipMainParticular',related_name='ModelTestStopping_version', on_delete=models.DO_NOTHING, db_column='VERSION')  # Field name made lowercase.
    prop_status = models.ForeignKey('PropStatus', models.DO_NOTHING, db_column='PROP_STATUS')  # Field name made lowercase.
    draft_name = models.ForeignKey(DraftName, models.DO_NOTHING, db_column='DRAFT_NAME')  # Field name made lowercase.
    eng_power = models.IntegerField(db_column='ENG_POWER')  # Field name made lowercase.
    analy_method = models.IntegerField(db_column='ANALY_METHOD')  # Field name made lowercase.
    prop_id = models.CharField(db_column='PROP_ID', max_length=15, blank=True, null=True)  # Field name made lowercase.
    model_id = models.CharField(db_column='MODEL_ID', max_length=15, blank=True, null=True)  # Field name made lowercase.
    initial_speed = models.DecimalField(db_column='INITIAL_SPEED', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    initial_rpm = models.DecimalField(db_column='INITIAL_RPM', max_digits=5, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    test_date = models.DateField(db_column='TEST_DATE', blank=True, null=True)  # Field name made lowercase.
    model_basin = models.IntegerField(db_column='MODEL_BASIN', blank=True, null=True)  # Field name made lowercase.
    trav_leng = models.DecimalField(db_column='TRAV_LENG', max_digits=6, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    elapsed_time = models.IntegerField(db_column='ELAPSED_TIME', blank=True, null=True)  # Field name made lowercase.
    rpm_zero_time = models.IntegerField(db_column='RPM_ZERO_TIME', blank=True, null=True)  # Field name made lowercase.
    p_manager = models.CharField(db_column='P_MANAGER', max_length=15, blank=True, null=True)  # Field name made lowercase.
    update_date = models.DateField(db_column='UPDATE_DATE', blank=True, null=True)  # Field name made lowercase.
    comments = models.CharField(db_column='COMMENTS', max_length=250, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'model_test_stopping'
        unique_together = (('project_no', 'version', 'prop_status', 'draft_name', 'eng_power', 'analy_method'),)


class ModelTestTurning(models.Model):
    project_no = models.OneToOneField('ShipMainParticular', models.DO_NOTHING, db_column='PROJECT_NO', primary_key=True)  # Field name made lowercase.
    version = models.ForeignKey('ShipMainParticular',related_name='ModelTestTurning_version', on_delete=models.DO_NOTHING, db_column='VERSION')  # Field name made lowercase.
    prop_status = models.ForeignKey('PropStatus', models.DO_NOTHING, db_column='PROP_STATUS')  # Field name made lowercase.
    draft_name = models.ForeignKey(DraftName, models.DO_NOTHING, db_column='DRAFT_NAME')  # Field name made lowercase.
    eng_power = models.IntegerField(db_column='ENG_POWER')  # Field name made lowercase.
    turn_dir = models.IntegerField(db_column='TURN_DIR')  # Field name made lowercase.
    prop_id = models.CharField(db_column='PROP_ID', max_length=15, blank=True, null=True)  # Field name made lowercase.
    model_id = models.CharField(db_column='MODEL_ID', max_length=15, blank=True, null=True)  # Field name made lowercase.
    testdate = models.DateField(db_column='TESTDATE', blank=True, null=True)  # Field name made lowercase.
    initial_rpm = models.DecimalField(db_column='INITIAL_RPM', max_digits=5, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    initial_speed = models.DecimalField(db_column='INITIAL_SPEED', max_digits=5, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    max_tactical_dia = models.DecimalField(db_column='MAX_TACTICAL_DIA', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    max_trans_leng = models.DecimalField(db_column='MAX_TRANS_LENG', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    advance = models.DecimalField(db_column='ADVANCE', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    elap_time_advance = models.DecimalField(db_column='ELAP_TIME_ADVANCE', max_digits=6, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    tactical_dia = models.DecimalField(db_column='TACTICAL_DIA', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    trans_leng = models.DecimalField(db_column='TRANS_LENG', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    speed_at_90 = models.DecimalField(db_column='SPEED_AT_90', max_digits=5, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    time_at_90 = models.DecimalField(db_column='TIME_AT_90', max_digits=6, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    speed_at_180 = models.DecimalField(db_column='SPEED_AT_180', max_digits=5, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    time_at_180 = models.DecimalField(db_column='TIME_AT_180', max_digits=6, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    speed_at_360 = models.DecimalField(db_column='SPEED_AT_360', max_digits=5, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    time_at_360 = models.DecimalField(db_column='TIME_AT_360', max_digits=6, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    elap_time = models.DecimalField(db_column='ELAP_TIME', max_digits=6, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    abylbp = models.DecimalField(db_column='ABYLBP', max_digits=6, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    tbylbp = models.DecimalField(db_column='TBYLBP', max_digits=6, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    p_manager = models.CharField(db_column='P_MANAGER', max_length=15, blank=True, null=True)  # Field name made lowercase.
    update_date = models.DateField(db_column='UPDATE_DATE', blank=True, null=True)  # Field name made lowercase.
    comments = models.CharField(db_column='COMMENTS', max_length=250, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'model_test_turning'
        unique_together = (('project_no', 'version', 'prop_status', 'draft_name', 'eng_power', 'turn_dir'),)


class ModelTestWakeHarmonic(models.Model):
    project_no = models.OneToOneField('ShipDraftData', models.DO_NOTHING, db_column='PROJECT_NO', primary_key=True)  # Field name made lowercase.
    version = models.ForeignKey('ShipDraftData',related_name='ModelTestWakeHarmonic_version', on_delete=models.DO_NOTHING, db_column='VERSION')  # Field name made lowercase.
    draft_name = models.ForeignKey('ShipDraftData',related_name='ModelTestWakeHarmonic_draft_name', on_delete=models.DO_NOTHING, db_column='DRAFT_NAME')  # Field name made lowercase.
    test_option = models.CharField(db_column='TEST_OPTION', max_length=25)  # Field name made lowercase.
    test_no = models.CharField(db_column='TEST_NO', max_length=15, blank=True, null=True)  # Field name made lowercase.
    test_date = models.DateField(db_column='TEST_DATE', blank=True, null=True)  # Field name made lowercase.
    ship_speed = models.DecimalField(db_column='SHIP_SPEED', max_digits=6, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    model_speed = models.DecimalField(db_column='MODEL_SPEED', max_digits=6, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    water_temp = models.DecimalField(db_column='WATER_TEMP', max_digits=4, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    nominal_wake = models.DecimalField(db_column='NOMINAL_WAKE', max_digits=4, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    velocity_mean = models.TextField(db_column='VELOCITY_MEAN', blank=True, null=True)  # Field name made lowercase.
    axi_harmonics = models.TextField(db_column='AXI_HARMONICS', blank=True, null=True)  # Field name made lowercase.
    rad_harmonics = models.TextField(db_column='RAD_HARMONICS', blank=True, null=True)  # Field name made lowercase.
    tan_harmonics = models.TextField(db_column='TAN_HARMONICS', blank=True, null=True)  # Field name made lowercase.
    png_axi_vel_deg = models.TextField(db_column='PNG_AXI_VEL_DEG', blank=True, null=True)  # Field name made lowercase.
    png_rad_tan_vel_deg = models.TextField(db_column='PNG_RAD_TAN_VEL_DEG', blank=True, null=True)  # Field name made lowercase.
    png_axi_contour = models.TextField(db_column='PNG_AXI_CONTOUR', blank=True, null=True)  # Field name made lowercase.
    png_radtan_contour = models.TextField(db_column='PNG_RADTAN_CONTOUR', blank=True, null=True)  # Field name made lowercase.
    comments = models.CharField(db_column='COMMENTS', max_length=250, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'model_test_wake_harmonic'
        unique_together = (('project_no', 'version', 'draft_name', 'test_option'),)


class ModelTestZigzag(models.Model):
    project_no = models.OneToOneField('ShipMainParticular', models.DO_NOTHING, db_column='PROJECT_NO', primary_key=True)  # Field name made lowercase.
    version = models.ForeignKey('ShipMainParticular',related_name='ModelTestZigzag_version', on_delete=models.DO_NOTHING, db_column='VERSION')  # Field name made lowercase.
    prop_status = models.ForeignKey('PropStatus', models.DO_NOTHING, db_column='PROP_STATUS')  # Field name made lowercase.
    draft_name = models.ForeignKey(DraftName, models.DO_NOTHING, db_column='DRAFT_NAME')  # Field name made lowercase.
    eng_power = models.IntegerField(db_column='ENG_POWER')  # Field name made lowercase.
    turn_dir = models.IntegerField(db_column='TURN_DIR')  # Field name made lowercase.
    analy_method = models.IntegerField(db_column='ANALY_METHOD')  # Field name made lowercase.
    prop_id = models.CharField(db_column='PROP_ID', max_length=15, blank=True, null=True)  # Field name made lowercase.
    model_id = models.CharField(db_column='MODEL_ID', max_length=15, blank=True, null=True)  # Field name made lowercase.
    test_kind = models.IntegerField(db_column='TEST_KIND', blank=True, null=True)  # Field name made lowercase.
    testdate = models.DateField(db_column='TESTDATE', blank=True, null=True)  # Field name made lowercase.
    initial_rpm = models.DecimalField(db_column='INITIAL_RPM', max_digits=5, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    initial_speed = models.DecimalField(db_column='INITIAL_SPEED', max_digits=7, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    overshoot1 = models.DecimalField(db_column='OVERSHOOT1', max_digits=5, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    overshoot2 = models.DecimalField(db_column='OVERSHOOT2', max_digits=5, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    elap_time_1 = models.DecimalField(db_column='ELAP_TIME_1', max_digits=6, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    elap_time_2 = models.DecimalField(db_column='ELAP_TIME_2', max_digits=6, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    init_track_reach = models.DecimalField(db_column='INIT_TRACK_REACH', max_digits=6, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    init_elap_time = models.DecimalField(db_column='INIT_ELAP_TIME', max_digits=6, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    p_manager = models.CharField(db_column='P_MANAGER', max_length=15, blank=True, null=True)  # Field name made lowercase.
    update_date = models.DateField(db_column='UPDATE_DATE', blank=True, null=True)  # Field name made lowercase.
    comments = models.CharField(db_column='COMMENTS', max_length=250, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'model_test_zigzag'
        unique_together = (('project_no', 'version', 'prop_status', 'draft_name', 'eng_power', 'turn_dir', 'analy_method'),)


class PressureFluctuationTest(models.Model):
    project_no = models.OneToOneField('ShipMainParticular', models.DO_NOTHING, db_column='PROJECT_NO', primary_key=True)  # Field name made lowercase.
    version = models.ForeignKey('ShipMainParticular',related_name='PressureFluctuationTest_version', on_delete=models.DO_NOTHING, db_column='VERSION')  # Field name made lowercase.
    prop_status = models.ForeignKey('PropStatus', models.DO_NOTHING, db_column='PROP_STATUS')  # Field name made lowercase.
    draft_name = models.ForeignKey(DraftName, models.DO_NOTHING, db_column='DRAFT_NAME')  # Field name made lowercase.
    serial_no = models.IntegerField(db_column='SERIAL_NO')  # Field name made lowercase.
    x_position = models.DecimalField(db_column='X_POSITION', max_digits=6, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    y_position = models.DecimalField(db_column='Y_POSITION', max_digits=6, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    cavi_no = models.DecimalField(db_column='CAVI_NO', max_digits=6, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    test_kt = models.DecimalField(db_column='TEST_KT', max_digits=6, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    test_power = models.DecimalField(db_column='TEST_POWER', max_digits=9, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    test_rpm = models.DecimalField(db_column='TEST_RPM', max_digits=6, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    amp1wo = models.DecimalField(db_column='AMP1WO', max_digits=6, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    pha1wo = models.DecimalField(db_column='PHA1WO', max_digits=6, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    amp2wo = models.DecimalField(db_column='AMP2WO', max_digits=6, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    pha2wo = models.DecimalField(db_column='PHA2WO', max_digits=6, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    amp3wo = models.DecimalField(db_column='AMP3WO', max_digits=6, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    pha3wo = models.DecimalField(db_column='PHA3WO', max_digits=6, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    amp4wo = models.DecimalField(db_column='AMP4WO', max_digits=6, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    pha4wo = models.DecimalField(db_column='PHA4WO', max_digits=6, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    amp1with = models.DecimalField(db_column='AMP1WITH', max_digits=6, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    pha1with = models.DecimalField(db_column='PHA1WITH', max_digits=6, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    amp2with = models.DecimalField(db_column='AMP2WITH', max_digits=6, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    pha2with = models.DecimalField(db_column='PHA2WITH', max_digits=6, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    amp3with = models.DecimalField(db_column='AMP3WITH', max_digits=6, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    pha3with = models.DecimalField(db_column='PHA3WITH', max_digits=6, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    amp4with = models.DecimalField(db_column='AMP4WITH', max_digits=6, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    pha4with = models.DecimalField(db_column='PHA4WITH', max_digits=6, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    comments = models.CharField(db_column='COMMENTS', max_length=250, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'pressure_fluctuation_test'
        unique_together = (('project_no', 'version', 'prop_status', 'draft_name', 'serial_no'),)


class PropStatus(models.Model):
    status = models.CharField(db_column='STATUS', primary_key=True, max_length=15)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'prop_status'


class PropellerGeometry(models.Model):
    project_no = models.OneToOneField('PropellerMainParticular', models.DO_NOTHING, db_column='PROJECT_NO', primary_key=True)  # Field name made lowercase.
    version = models.ForeignKey('PropellerMainParticular',related_name='PropellerGeometry_version', on_delete=models.DO_NOTHING, db_column='VERSION')  # Field name made lowercase.
    prop_status = models.ForeignKey('PropellerMainParticular',related_name='PropellerGeometry_prop_status', on_delete=models.DO_NOTHING, db_column='PROP_STATUS')  # Field name made lowercase.
    geometry = models.TextField(db_column='GEOMETRY', blank=True, null=True)  # Field name made lowercase.
    comments = models.CharField(db_column='COMMENTS', max_length=250, blank=True, null=True)  # Field name made lowercase.
    offset = models.TextField(db_column='OFFSET', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'propeller_geometry'
        unique_together = (('project_no', 'version', 'prop_status'),)


class PropellerMainParticular(models.Model):
    project_no = models.OneToOneField('ShipMainParticular', models.DO_NOTHING, db_column='PROJECT_NO', primary_key=True)  # Field name made lowercase.
    version = models.ForeignKey('ShipMainParticular',related_name='PropellerMainParticular_version', on_delete=models.DO_NOTHING, db_column='VERSION')  # Field name made lowercase.
    prop_status = models.ForeignKey(PropStatus, models.DO_NOTHING, db_column='PROP_STATUS')  # Field name made lowercase.
    manufacturer = models.CharField(db_column='MANUFACTURER', max_length=15, blank=True, null=True)  # Field name made lowercase.
    design_dept = models.CharField(db_column='DESIGN_DEPT', max_length=15, blank=True, null=True)  # Field name made lowercase.
    designer = models.CharField(db_column='DESIGNER', max_length=15, blank=True, null=True)  # Field name made lowercase.
    model_scale = models.DecimalField(db_column='MODEL_SCALE', max_digits=7, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    design_draft_f = models.DecimalField(db_column='DESIGN_DRAFT_F', max_digits=6, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    design_draft_a = models.DecimalField(db_column='DESIGN_DRAFT_A', max_digits=6, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    design_power = models.DecimalField(db_column='DESIGN_POWER', max_digits=9, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    design_rpm = models.DecimalField(db_column='DESIGN_RPM', max_digits=8, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    sec_type = models.CharField(db_column='SEC_TYPE', max_length=15, blank=True, null=True)  # Field name made lowercase.
    prop_type = models.CharField(db_column='PROP_TYPE', max_length=15, blank=True, null=True)  # Field name made lowercase.
    turn_type = models.CharField(db_column='TURN_TYPE', max_length=15, blank=True, null=True)  # Field name made lowercase.
    material_type = models.CharField(db_column='MATERIAL_TYPE', max_length=15, blank=True, null=True)  # Field name made lowercase.
    no_of_radius = models.IntegerField(db_column='NO_OF_RADIUS', blank=True, null=True)  # Field name made lowercase.
    no_of_offset = models.IntegerField(db_column='NO_OF_OFFSET', blank=True, null=True)  # Field name made lowercase.
    no_of_blade = models.IntegerField(db_column='NO_OF_BLADE', blank=True, null=True)  # Field name made lowercase.
    diameter = models.DecimalField(db_column='DIAMETER', max_digits=7, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    hub_ratio = models.DecimalField(db_column='HUB_RATIO', max_digits=6, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    ear = models.DecimalField(db_column='EAR', max_digits=6, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    pitch_mean = models.DecimalField(db_column='PITCH_MEAN', max_digits=6, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    pitch_07r = models.DecimalField(db_column='PITCH_07R', max_digits=6, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    chord_07r = models.DecimalField(db_column='CHORD_07R', max_digits=6, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    thick_07r = models.DecimalField(db_column='THICK_07R', max_digits=6, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    rake_angle = models.DecimalField(db_column='RAKE_ANGLE', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    rake_maxpos = models.DecimalField(db_column='RAKE_MAXPOS', max_digits=6, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    skew_total = models.DecimalField(db_column='SKEW_TOTAL', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    skew_rate = models.DecimalField(db_column='SKEW_RATE', max_digits=6, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    skew_min = models.DecimalField(db_column='SKEW_MIN', max_digits=6, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    max_chord = models.DecimalField(db_column='MAX_CHORD', max_digits=6, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    gl_to_left = models.DecimalField(db_column='GL_TO_LEFT', max_digits=6, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    gl_to_right = models.DecimalField(db_column='GL_TO_RIGHT', max_digits=6, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    hub_dia_left = models.DecimalField(db_column='HUB_DIA_LEFT', max_digits=6, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    hub_dia_right = models.DecimalField(db_column='HUB_DIA_RIGHT', max_digits=6, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    shaft_dia = models.DecimalField(db_column='SHAFT_DIA', max_digits=6, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    blade_weight = models.DecimalField(db_column='BLADE_WEIGHT', max_digits=8, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    total_weight = models.DecimalField(db_column='TOTAL_WEIGHT', max_digits=8, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    moi_air = models.DecimalField(db_column='MOI_AIR', max_digits=9, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    gdsqrt_air = models.DecimalField(db_column='GDSQRT_AIR', max_digits=10, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    moi_water = models.DecimalField(db_column='MOI_WATER', max_digits=9, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    gdsqrt_water = models.DecimalField(db_column='GDSQRT_WATER', max_digits=10, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    class_field = models.CharField(db_column='CLASS', max_length=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it was a Python reserved word.
    ice_class = models.CharField(db_column='ICE_CLASS', max_length=15, blank=True, null=True)  # Field name made lowercase.
    design_j = models.DecimalField(db_column='DESIGN_J', max_digits=6, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    pow_kt = models.DecimalField(db_column='POW_KT', max_digits=6, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    pow_kq = models.DecimalField(db_column='POW_KQ', max_digits=7, decimal_places=5, blank=True, null=True)  # Field name made lowercase.
    pow_etao = models.DecimalField(db_column='POW_ETAO', max_digits=6, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    update_date = models.DateField(db_column='UPDATE_DATE', blank=True, null=True)  # Field name made lowercase.
    comments = models.CharField(db_column='COMMENTS', max_length=250, blank=True, null=True)  # Field name made lowercase.
    pdf_drawing = models.TextField(db_column='PDF_DRAWING', blank=True, null=True)  # Field name made lowercase.
    txt_offset = models.TextField(db_column='TXT_OFFSET', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'propeller_main_particular'
        unique_together = (('project_no', 'version', 'prop_status'),)


class ShipDraftData(models.Model):
    project_no = models.OneToOneField('ShipMainParticular', models.DO_NOTHING, db_column='PROJECT_NO', primary_key=True)  # Field name made lowercase.
    version = models.ForeignKey('ShipMainParticular',related_name='ShipDraftData_version', on_delete=models.DO_NOTHING, db_column='VERSION')  # Field name made lowercase.
    draft_name = models.ForeignKey(DraftName, models.DO_NOTHING, db_column='DRAFT_NAME')  # Field name made lowercase.
    lwl = models.DecimalField(db_column='LWL', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    draft_fore = models.DecimalField(db_column='DRAFT_FORE', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    draft_aft = models.DecimalField(db_column='DRAFT_AFT', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    lob = models.DecimalField(db_column='LOB', max_digits=6, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    bod = models.DecimalField(db_column='BOD', max_digits=6, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    fn = models.DecimalField(db_column='FN', max_digits=6, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    fnb = models.DecimalField(db_column='FNB', max_digits=6, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    fnle = models.DecimalField(db_column='FNLE', max_digits=6, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    cb = models.DecimalField(db_column='CB', max_digits=6, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    cm = models.DecimalField(db_column='CM', max_digits=6, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    cw = models.DecimalField(db_column='CW', max_digits=6, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    lcb = models.DecimalField(db_column='LCB', max_digits=6, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    cb_fore = models.DecimalField(db_column='CB_FORE', max_digits=6, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    cb_aft = models.DecimalField(db_column='CB_AFT', max_digits=6, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    cp_fore = models.DecimalField(db_column='CP_FORE', max_digits=6, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    cp_aft = models.DecimalField(db_column='CP_AFT', max_digits=6, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    cw_fore = models.DecimalField(db_column='CW_FORE', max_digits=7, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    cw_aft = models.DecimalField(db_column='CW_AFT', max_digits=7, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    kb = models.DecimalField(db_column='KB', max_digits=4, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    bm = models.DecimalField(db_column='BM', max_digits=4, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    kmt = models.DecimalField(db_column='KMT', max_digits=4, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    displacement = models.DecimalField(db_column='DISPLACEMENT', max_digits=9, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    cp_curve_p_leng = models.DecimalField(db_column='CP_CURVE_P_LENG', max_digits=7, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    cp_curve_fp_leng = models.DecimalField(db_column='CP_CURVE_FP_LENG', max_digits=7, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    cp_curve_ap_leng = models.DecimalField(db_column='CP_CURVE_AP_LENG', max_digits=7, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    cp_deriv_at_fp = models.DecimalField(db_column='CP_DERIV_AT_FP', max_digits=7, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    cp_deriv_max_pos = models.DecimalField(db_column='CP_DERIV_MAX_POS', max_digits=7, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    cp_deriv_min_pos = models.DecimalField(db_column='CP_DERIV_MIN_POS', max_digits=7, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    cp_deriv_max_value = models.DecimalField(db_column='CP_DERIV_MAX_VALUE', max_digits=7, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    cp_deriv_min_value = models.DecimalField(db_column='CP_DERIV_MIN_VALUE', max_digits=7, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    bluntness = models.DecimalField(db_column='BLUNTNESS', max_digits=6, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    wet_surface = models.DecimalField(db_column='WET_SURFACE', max_digits=9, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    wet_bilge_keel = models.DecimalField(db_column='WET_BILGE_KEEL', max_digits=5, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    bulb_immer = models.DecimalField(db_column='BULB_IMMER', max_digits=6, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    trans_proj_area = models.DecimalField(db_column='TRANS_PROJ_AREA', max_digits=7, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    cp_value = models.TextField(db_column='CP_VALUE', blank=True, null=True)  # Field name made lowercase.
    hb_value = models.TextField(db_column='HB_VALUE', blank=True, null=True)  # Field name made lowercase.
    comments = models.CharField(db_column='COMMENTS', max_length=250, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ship_draft_data'
        unique_together = (('project_no', 'version', 'draft_name'),)


class ShipHullParticular(models.Model):
    project_no = models.OneToOneField('ShipMainParticular', models.DO_NOTHING, db_column='PROJECT_NO', primary_key=True)  # Field name made lowercase.
    version = models.ForeignKey('ShipMainParticular',related_name='ShipHullParticular_version', on_delete=models.DO_NOTHING, db_column='VERSION')  # Field name made lowercase.
    mother_fore = models.DecimalField(db_column='MOTHER_FORE', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    mother_aft = models.DecimalField(db_column='MOTHER_AFT', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    model_no = models.CharField(db_column='MODEL_NO', max_length=12, blank=True, null=True)  # Field name made lowercase.
    model_scale = models.DecimalField(db_column='MODEL_SCALE', max_digits=6, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    ap_boss_end = models.DecimalField(db_column='AP_BOSS_END', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    br20dw = models.DecimalField(db_column='BR20DW', max_digits=6, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    br2065sh = models.DecimalField(db_column='BR2065SH', max_digits=6, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    br30dw = models.DecimalField(db_column='BR30DW', max_digits=6, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    br3065sh = models.DecimalField(db_column='BR3065SH', max_digits=6, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    tau_2st_upper = models.DecimalField(db_column='TAU_2ST_UPPER', max_digits=6, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    tau_2st_center = models.DecimalField(db_column='TAU_2ST_CENTER', max_digits=6, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    tau_2st_lower = models.DecimalField(db_column='TAU_2ST_LOWER', max_digits=6, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    ap_vert_height = models.DecimalField(db_column='AP_VERT_HEIGHT', max_digits=6, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    ap_slope_angle = models.DecimalField(db_column='AP_SLOPE_ANGLE', max_digits=6, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    ap_hori_length = models.DecimalField(db_column='AP_HORI_LENGTH', max_digits=6, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    ent_ang_1925 = models.DecimalField(db_column='ENT_ANG_1925', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ent_ang_1950 = models.DecimalField(db_column='ENT_ANG_1950', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ent_ang_1975 = models.DecimalField(db_column='ENT_ANG_1975', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ent_tang_1925 = models.DecimalField(db_column='ENT_TANG_1925', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ent_tang_1950 = models.DecimalField(db_column='ENT_TANG_1950', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ent_tang_1975 = models.DecimalField(db_column='ENT_TANG_1975', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    run_angle_45 = models.DecimalField(db_column='RUN_ANGLE_45', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    run_angle_65 = models.DecimalField(db_column='RUN_ANGLE_65', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    run_angle_85 = models.DecimalField(db_column='RUN_ANGLE_85', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    bulb_type = models.CharField(db_column='BULB_TYPE', max_length=12, blank=True, null=True)  # Field name made lowercase.
    bulb_area_f = models.DecimalField(db_column='BULB_AREA_F', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    bulb_area_s = models.DecimalField(db_column='BULB_AREA_S', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    bulb_length = models.DecimalField(db_column='BULB_LENGTH', max_digits=6, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    bulb_breadth = models.DecimalField(db_column='BULB_BREADTH', max_digits=6, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    bulb_nose_heig = models.DecimalField(db_column='BULB_NOSE_HEIG', max_digits=6, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    bulb_nose_leng = models.DecimalField(db_column='BULB_NOSE_LENG', max_digits=6, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    bulb_upper_shape = models.DecimalField(db_column='BULB_UPPER_SHAPE', max_digits=6, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    bulb_lower_shape = models.DecimalField(db_column='BULB_LOWER_SHAPE', max_digits=6, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    fore_side_image = models.TextField(db_column='FORE_SIDE_IMAGE', blank=True, null=True)  # Field name made lowercase.
    aft_side_image = models.TextField(db_column='AFT_SIDE_IMAGE', blank=True, null=True)  # Field name made lowercase.
    fore_front_image = models.TextField(db_column='FORE_FRONT_IMAGE', blank=True, null=True)  # Field name made lowercase.
    aft_front_image = models.TextField(db_column='AFT_FRONT_IMAGE', blank=True, null=True)  # Field name made lowercase.
    bird_eye_image = models.TextField(db_column='BIRD_EYE_IMAGE', blank=True, null=True)  # Field name made lowercase.
    stem_profile = models.TextField(db_column='STEM_PROFILE', blank=True, null=True)  # Field name made lowercase.
    stern_profile = models.TextField(db_column='STERN_PROFILE', blank=True, null=True)  # Field name made lowercase.
    side_tangent = models.TextField(db_column='SIDE_TANGENT', blank=True, null=True)  # Field name made lowercase.
    bottom_tangent = models.TextField(db_column='BOTTOM_TANGENT', blank=True, null=True)  # Field name made lowercase.
    lines_caeses_fdb = models.TextField(db_column='LINES_CAESES_FDB', blank=True, null=True)  # Field name made lowercase.
    lines_wavis_grd_fore = models.TextField(db_column='LINES_WAVIS_GRD_FORE', blank=True, null=True)  # Field name made lowercase.
    lines_wavis_grd_aft = models.TextField(db_column='LINES_WAVIS_GRD_AFT', blank=True, null=True)  # Field name made lowercase.
    lines_iges2d = models.TextField(db_column='LINES_IGES2D', blank=True, null=True)  # Field name made lowercase.
    lines_iges2d_fore = models.TextField(db_column='LINES_IGES2D_FORE', blank=True, null=True)  # Field name made lowercase.
    lines_iges2d_aft = models.TextField(db_column='LINES_IGES2D_AFT', blank=True, null=True)  # Field name made lowercase.
    lines_iges3d = models.TextField(db_column='LINES_IGES3D', blank=True, null=True)  # Field name made lowercase.
    lines_iges3d_fore = models.TextField(db_column='LINES_IGES3D_FORE', blank=True, null=True)  # Field name made lowercase.
    lines_iges3d_aft = models.TextField(db_column='LINES_IGES3D_AFT', blank=True, null=True)  # Field name made lowercase.
    lines_stl = models.TextField(db_column='LINES_STL', blank=True, null=True)  # Field name made lowercase.
    lines_opthull = models.TextField(db_column='LINES_OPTHULL', blank=True, null=True)  # Field name made lowercase.
    lines_dmp = models.TextField(db_column='LINES_DMP', blank=True, null=True)  # Field name made lowercase.
    lines_offset = models.TextField(db_column='LINES_OFFSET', blank=True, null=True)  # Field name made lowercase.
    insert_date = models.DateField(db_column='INSERT_DATE', blank=True, null=True)  # Field name made lowercase.
    update_date = models.DateField(db_column='UPDATE_DATE', blank=True, null=True)  # Field name made lowercase.
    comments = models.CharField(db_column='COMMENTS', max_length=250, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ship_hull_particular'
        unique_together = (('project_no', 'version'),)


class ShipInitialDesignResult(models.Model):
    project_no = models.OneToOneField('ShipMainParticular', models.DO_NOTHING, db_column='PROJECT_NO', primary_key=True)  # Field name made lowercase.
    version = models.ForeignKey('ShipMainParticular',related_name='ShipInitialDesignResult_version', on_delete=models.DO_NOTHING, db_column='VERSION')  # Field name made lowercase.
    png_main_dim_review = models.TextField(db_column='PNG_MAIN_DIM_REVIEW', blank=True, null=True)  # Field name made lowercase.
    png_main_eng_review = models.TextField(db_column='PNG_MAIN_ENG_REVIEW', blank=True, null=True)  # Field name made lowercase.
    png_navigation_review = models.TextField(db_column='PNG_NAVIGATION_REVIEW', blank=True, null=True)  # Field name made lowercase.
    png_initial_ga = models.TextField(db_column='PNG_INITIAL_GA', blank=True, null=True)  # Field name made lowercase.
    png_fuel_tank_review = models.TextField(db_column='PNG_FUEL_TANK_REVIEW', blank=True, null=True)  # Field name made lowercase.
    pdf_final_ga = models.TextField(db_column='PDF_FINAL_GA', blank=True, null=True)  # Field name made lowercase.
    png_lng_tank_fgss = models.TextField(db_column='PNG_LNG_TANK_FGSS', blank=True, null=True)  # Field name made lowercase.
    pdf_visibility_report = models.TextField(db_column='PDF_VISIBILITY_REPORT', blank=True, null=True)  # Field name made lowercase.
    png_compart_deck = models.TextField(db_column='PNG_COMPART_DECK', blank=True, null=True)  # Field name made lowercase.
    png_lightweight = models.TextField(db_column='PNG_LIGHTWEIGHT', blank=True, null=True)  # Field name made lowercase.
    pdf_trim_stability = models.TextField(db_column='PDF_TRIM_STABILITY', blank=True, null=True)  # Field name made lowercase.
    pdf_damage_stability = models.TextField(db_column='PDF_DAMAGE_STABILITY', blank=True, null=True)  # Field name made lowercase.
    pdf_eedi_report = models.TextField(db_column='PDF_EEDI_REPORT', blank=True, null=True)  # Field name made lowercase.
    png_eedi_result = models.TextField(db_column='PNG_EEDI_RESULT', blank=True, null=True)  # Field name made lowercase.
    pdf_initial_report = models.TextField(db_column='PDF_INITIAL_REPORT', blank=True, null=True)  # Field name made lowercase.
    png_engine_room = models.TextField(db_column='PNG_ENGINE_ROOM', blank=True, null=True)  # Field name made lowercase.
    png_is_code = models.TextField(db_column='PNG_IS_CODE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ship_initial_design_result'
        unique_together = (('project_no', 'version'),)


class ShipMainParticular(models.Model):
    project_no = models.DecimalField(db_column='PROJECT_NO', primary_key=True, max_digits=10, decimal_places=2)  # Field name made lowercase.
    version = models.IntegerField(db_column='VERSION')  # Field name made lowercase.
    builder = models.CharField(db_column='BUILDER', max_length=15, blank=True, null=True)  # Field name made lowercase.
    purpose_of_proj = models.CharField(db_column='PURPOSE_OF_PROJ', max_length=15, blank=True, null=True)  # Field name made lowercase.
    ship_size = models.DecimalField(db_column='SHIP_SIZE', max_digits=9, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ship_title = models.CharField(db_column='SHIP_TITLE', max_length=70, blank=True, null=True)  # Field name made lowercase.
    ship_kind = models.IntegerField(db_column='SHIP_KIND', blank=True, null=True)  # Field name made lowercase.
    owner_name = models.CharField(db_column='OWNER_NAME', max_length=30, blank=True, null=True)  # Field name made lowercase.
    project_requested = models.CharField(db_column='PROJECT_REQUESTED', max_length=30, blank=True, null=True)  # Field name made lowercase.
    flag = models.CharField(db_column='FLAG', max_length=15, blank=True, null=True)  # Field name made lowercase.
    imo_no = models.IntegerField(db_column='IMO_NO', blank=True, null=True)  # Field name made lowercase.
    loa = models.DecimalField(db_column='LOA', max_digits=6, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    lbp = models.DecimalField(db_column='LBP', max_digits=6, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    breadth = models.DecimalField(db_column='BREADTH', max_digits=6, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    depth = models.DecimalField(db_column='DEPTH', max_digits=6, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    contract_draft_f = models.DecimalField(db_column='CONTRACT_DRAFT_F', max_digits=6, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    contract_draft_a = models.DecimalField(db_column='CONTRACT_DRAFT_A', max_digits=6, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    contract_speed = models.DecimalField(db_column='CONTRACT_SPEED', max_digits=6, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    eedi_level = models.IntegerField(db_column='EEDI_LEVEL', blank=True, null=True)  # Field name made lowercase.
    eedi_speed = models.DecimalField(db_column='EEDI_SPEED', max_digits=6, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    special_device_1 = models.CharField(db_column='SPECIAL_DEVICE_1', max_length=12, blank=True, null=True)  # Field name made lowercase.
    special_device_2 = models.CharField(db_column='SPECIAL_DEVICE_2', max_length=12, blank=True, null=True)  # Field name made lowercase.
    esd_fore1 = models.CharField(db_column='ESD_FORE1', max_length=12, blank=True, null=True)  # Field name made lowercase.
    esd_fore2 = models.CharField(db_column='ESD_FORE2', max_length=12, blank=True, null=True)  # Field name made lowercase.
    esd_aft1 = models.CharField(db_column='ESD_AFT1', max_length=12, blank=True, null=True)  # Field name made lowercase.
    esd_aft2 = models.CharField(db_column='ESD_AFT2', max_length=12, blank=True, null=True)  # Field name made lowercase.
    model_basin_sp = models.CharField(db_column='MODEL_BASIN_SP', max_length=12, blank=True, null=True)  # Field name made lowercase.
    model_basin_cavi = models.CharField(db_column='MODEL_BASIN_CAVI', max_length=12, blank=True, null=True)  # Field name made lowercase.
    engine_type = models.CharField(db_column='ENGINE_TYPE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    nmcr_power = models.DecimalField(db_column='NMCR_POWER', max_digits=8, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    nmcr_rpm = models.DecimalField(db_column='NMCR_RPM', max_digits=8, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    smcr_power = models.DecimalField(db_column='SMCR_POWER', max_digits=8, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    smcr_rpm = models.DecimalField(db_column='SMCR_RPM', max_digits=8, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    ncr_power = models.DecimalField(db_column='NCR_POWER', max_digits=8, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    ncr_rpm = models.DecimalField(db_column='NCR_RPM', max_digits=8, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    sea_margin = models.DecimalField(db_column='SEA_MARGIN', max_digits=5, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    rpm_margin = models.DecimalField(db_column='RPM_MARGIN', max_digits=3, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    shaft_gen_power = models.DecimalField(db_column='SHAFT_GEN_POWER', max_digits=7, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    no_prop = models.IntegerField(db_column='NO_PROP', blank=True, null=True)  # Field name made lowercase.
    class_1 = models.CharField(db_column='CLASS_1', max_length=12, blank=True, null=True)  # Field name made lowercase.
    class_2 = models.CharField(db_column='CLASS_2', max_length=12, blank=True, null=True)  # Field name made lowercase.
    class_3 = models.CharField(db_column='CLASS_3', max_length=12, blank=True, null=True)  # Field name made lowercase.
    ice_class = models.CharField(db_column='ICE_CLASS', max_length=12, blank=True, null=True)  # Field name made lowercase.
    prop_type = models.CharField(db_column='PROP_TYPE', max_length=12, blank=True, null=True)  # Field name made lowercase.
    prop_dia = models.DecimalField(db_column='PROP_DIA', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    mean_pitch = models.DecimalField(db_column='MEAN_PITCH', max_digits=6, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    ear = models.DecimalField(db_column='EAR', max_digits=6, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    no_blade = models.IntegerField(db_column='NO_BLADE', blank=True, null=True)  # Field name made lowercase.
    tip_clearance = models.DecimalField(db_column='TIP_CLEARANCE', max_digits=3, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    lines_date = models.DateField(db_column='LINES_DATE', blank=True, null=True)  # Field name made lowercase.
    project_manager = models.CharField(db_column='PROJECT_MANAGER', max_length=12, blank=True, null=True)  # Field name made lowercase.
    lines_designer = models.CharField(db_column='LINES_DESIGNER', max_length=12, blank=True, null=True)  # Field name made lowercase.
    propeller_designer = models.CharField(db_column='PROPELLER_DESIGNER', max_length=12, blank=True, null=True)  # Field name made lowercase.
    esd_designer = models.CharField(db_column='ESD_DESIGNER', max_length=12, blank=True, null=True)  # Field name made lowercase.
    delivery_date = models.DateField(db_column='DELIVERY_DATE', blank=True, null=True)  # Field name made lowercase.
    rudder_type = models.CharField(db_column='RUDDER_TYPE', max_length=12, blank=True, null=True)  # Field name made lowercase.
    rudder_area = models.DecimalField(db_column='RUDDER_AREA', max_digits=6, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    rudder_span = models.DecimalField(db_column='RUDDER_SPAN', max_digits=6, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    rudder_aspect_ratio = models.DecimalField(db_column='RUDDER_ASPECT_RATIO', max_digits=6, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    sfoc_ncr = models.DecimalField(db_column='SFOC_NCR', max_digits=6, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    bilge_radius = models.DecimalField(db_column='BILGE_RADIUS', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    shaft_heig = models.DecimalField(db_column='SHAFT_HEIG', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    shaft_dia = models.DecimalField(db_column='SHAFT_DIA', max_digits=5, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    depthcen = models.DecimalField(db_column='DEPTHCEN', max_digits=6, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    flatkeel = models.DecimalField(db_column='FLATKEEL', max_digits=6, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    risefloor = models.DecimalField(db_column='RISEFLOOR', max_digits=6, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    rakekeel = models.DecimalField(db_column='RAKEKEEL', max_digits=7, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    sternover = models.DecimalField(db_column='STERNOVER', max_digits=7, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    stemover = models.DecimalField(db_column='STEMOVER', max_digits=7, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    maximumz = models.DecimalField(db_column='MAXIMUMZ', max_digits=7, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    minimumz = models.DecimalField(db_column='MINIMUMZ', max_digits=7, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    comments = models.CharField(db_column='COMMENTS', max_length=250, blank=True, null=True)  # Field name made lowercase.
    ship_main_particularcol = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ship_main_particular'
        unique_together = (('project_no', 'version'),)


class ShipPropulsionResults(models.Model):
    project_no = models.OneToOneField(ShipDraftData, models.DO_NOTHING, db_column='PROJECT_NO', primary_key=True)  # Field name made lowercase.
    version = models.ForeignKey(ShipDraftData,related_name='ShipPropulsionResults_version', on_delete=models.DO_NOTHING, db_column='VERSION')  # Field name made lowercase.
    prop_status = models.ForeignKey(PropellerMainParticular, models.DO_NOTHING, db_column='PROP_STATUS')  # Field name made lowercase.
    draft_name = models.ForeignKey(ShipDraftData,related_name='ShipPropulsionResults_draft_name', on_delete=models.DO_NOTHING, db_column='DRAFT_NAME')  # Field name made lowercase.
    speed = models.DecimalField(db_column='SPEED', max_digits=5, decimal_places=2)  # Field name made lowercase.
    fn = models.DecimalField(db_column='FN', max_digits=6, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    ctm = models.DecimalField(db_column='CTM', max_digits=6, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    cfm = models.DecimalField(db_column='CFM', max_digits=6, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    cr = models.DecimalField(db_column='CR', max_digits=6, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    trim = models.DecimalField(db_column='TRIM', max_digits=6, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    pe = models.DecimalField(db_column='PE', max_digits=8, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    sink_fp_s = models.DecimalField(db_column='SINK_FP_S', max_digits=6, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    sink_ap_s = models.DecimalField(db_column='SINK_AP_S', max_digits=6, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    advance_m = models.DecimalField(db_column='ADVANCE_M', max_digits=6, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    thrust_m = models.DecimalField(db_column='THRUST_M', max_digits=5, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    torque_m = models.DecimalField(db_column='TORQUE_M', max_digits=6, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    rps_m = models.DecimalField(db_column='RPS_M', max_digits=6, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    pd = models.DecimalField(db_column='PD', max_digits=8, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    advance_s = models.DecimalField(db_column='ADVANCE_S', max_digits=6, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    rpm_s = models.DecimalField(db_column='RPM_S', max_digits=6, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    thrust_s = models.DecimalField(db_column='THRUST_S', max_digits=6, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    torque_s = models.DecimalField(db_column='TORQUE_S', max_digits=6, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    wm = models.DecimalField(db_column='WM', max_digits=6, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    ws = models.DecimalField(db_column='WS', max_digits=6, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    td = models.DecimalField(db_column='TD', max_digits=6, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    etah = models.DecimalField(db_column='ETAH', max_digits=6, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    etar = models.DecimalField(db_column='ETAR', max_digits=6, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    etao = models.DecimalField(db_column='ETAO', max_digits=6, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    etab = models.DecimalField(db_column='ETAB', max_digits=6, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    etad = models.DecimalField(db_column='ETAD', max_digits=6, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    trial_bhp = models.IntegerField(db_column='TRIAL_BHP', blank=True, null=True)  # Field name made lowercase.
    trial_rpm = models.DecimalField(db_column='TRIAL_RPM', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ship_propulsion_results'
        unique_together = (('project_no', 'version', 'prop_status', 'draft_name', 'speed'),)


class ShipRudderGeometry(models.Model):
    project_no = models.OneToOneField(ShipMainParticular, models.DO_NOTHING, db_column='PROJECT_NO', primary_key=True)  # Field name made lowercase.
    version = models.ForeignKey(ShipMainParticular,related_name='ShipRudderGeometry_version', on_delete=models.DO_NOTHING, db_column='VERSION')  # Field name made lowercase.
    rudder_type = models.CharField(db_column='RUDDER_TYPE', max_length=25, blank=True, null=True)  # Field name made lowercase.
    area = models.DecimalField(db_column='AREA', max_digits=7, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    area_ratio = models.DecimalField(db_column='AREA_RATIO', max_digits=7, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    balance_ratio = models.DecimalField(db_column='BALANCE_RATIO', max_digits=7, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    aspect_ratio = models.DecimalField(db_column='ASPECT_RATIO', max_digits=6, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    rudder_vol = models.DecimalField(db_column='RUDDER_VOL', max_digits=6, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    section_type = models.CharField(db_column='SECTION_TYPE', max_length=25, blank=True, null=True)  # Field name made lowercase.
    req_area = models.DecimalField(db_column='REQ_AREA', max_digits=7, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    cargo_heig = models.DecimalField(db_column='CARGO_HEIG', max_digits=7, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    profile_area = models.DecimalField(db_column='PROFILE_AREA', max_digits=7, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    td = models.DecimalField(db_column='TD', max_digits=5, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    ws = models.DecimalField(db_column='WS', max_digits=5, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    thrust = models.DecimalField(db_column='THRUST', max_digits=7, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    cavi_coef = models.DecimalField(db_column='CAVI_COEF', max_digits=6, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    base_clear = models.DecimalField(db_column='BASE_CLEAR', max_digits=5, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    thk_top = models.DecimalField(db_column='THK_TOP', max_digits=7, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    thk_pintle = models.DecimalField(db_column='THK_PINTLE', max_digits=7, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    thk_bottom = models.DecimalField(db_column='THK_BOTTOM', max_digits=7, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    pint_to_lead = models.DecimalField(db_column='PINT_TO_LEAD', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    dist1 = models.DecimalField(db_column='DIST1', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    dist2 = models.DecimalField(db_column='DIST2', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    dist3 = models.DecimalField(db_column='DIST3', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    dist4 = models.DecimalField(db_column='DIST4', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    dist5 = models.DecimalField(db_column='DIST5', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    dist6 = models.DecimalField(db_column='DIST6', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    dist7 = models.DecimalField(db_column='DIST7', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    dist8 = models.DecimalField(db_column='DIST8', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    dist9 = models.DecimalField(db_column='DIST9', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    dist10 = models.DecimalField(db_column='DIST10', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    dist11 = models.DecimalField(db_column='DIST11', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    dist12 = models.DecimalField(db_column='DIST12', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    dist13 = models.DecimalField(db_column='DIST13', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    dist14 = models.DecimalField(db_column='DIST14', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    dist15 = models.DecimalField(db_column='DIST15', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    dist16 = models.DecimalField(db_column='DIST16', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    comments = models.CharField(db_column='COMMENTS', max_length=250, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ship_rudder_geometry'
        unique_together = (('project_no', 'version'),)


class ShipType(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    type = models.CharField(db_column='TYPE', max_length=30)  # Field name made lowercase.
    detail_type = models.CharField(db_column='DETAIL_TYPE', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ship_type'
