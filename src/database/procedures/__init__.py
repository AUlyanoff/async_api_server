# -*- coding: utf-8 -*-
from database.procedures.procedure_list import *

# Данный файл сгенерирован автоматически, любые изменения будут утеряны при запуске parser.py
# Подробности: src/database/README.md


class ProcedureList:
    def __init__(self):
        self.sp_ab_imdm_list_for_kit: SP_AB_IMDM_LIST_FOR_KIT = SP_AB_IMDM_LIST_FOR_KIT()
        self.sp_app_cfg_imdm_get_checked: SP_APP_CFG_IMDM_GET_CHECKED = SP_APP_CFG_IMDM_GET_CHECKED()
        self.sp_app_cfg_imdm_get_v2: SP_APP_CFG_IMDM_GET_V2 = SP_APP_CFG_IMDM_GET_V2()
        self.sp_app_cfg_imdm_register_install: SP_APP_CFG_IMDM_REGISTER_INSTALL = SP_APP_CFG_IMDM_REGISTER_INSTALL()
        self.sp_app_cfg_imdm_register_remove: SP_APP_CFG_IMDM_REGISTER_REMOVE = SP_APP_CFG_IMDM_REGISTER_REMOVE()
        self.sp_app_distrib_imdm_get_icon: SP_APP_DISTRIB_IMDM_GET_ICON = SP_APP_DISTRIB_IMDM_GET_ICON()
        self.sp_app_kit_imdm_event_change: SP_APP_KIT_IMDM_EVENT_CHANGE = SP_APP_KIT_IMDM_EVENT_CHANGE()
        self.sp_app_kit_imdm_event_change_ios: SP_APP_KIT_IMDM_EVENT_CHANGE_IOS = SP_APP_KIT_IMDM_EVENT_CHANGE_IOS()
        self.sp_app_kit_imdm_event_change_v2: SP_APP_KIT_IMDM_EVENT_CHANGE_V2 = SP_APP_KIT_IMDM_EVENT_CHANGE_V2()
        self.sp_app_kit_imdm_event_inst: SP_APP_KIT_IMDM_EVENT_INST = SP_APP_KIT_IMDM_EVENT_INST()
        self.sp_app_kit_imdm_event_inst_ios: SP_APP_KIT_IMDM_EVENT_INST_IOS = SP_APP_KIT_IMDM_EVENT_INST_IOS()
        self.sp_app_kit_imdm_event_inst_v2: SP_APP_KIT_IMDM_EVENT_INST_V2 = SP_APP_KIT_IMDM_EVENT_INST_V2()
        self.sp_app_kit_imdm_event_uninst: SP_APP_KIT_IMDM_EVENT_UNINST = SP_APP_KIT_IMDM_EVENT_UNINST()
        self.sp_app_kit_imdm_get_app_monitor: SP_APP_KIT_IMDM_GET_APP_MONITOR = SP_APP_KIT_IMDM_GET_APP_MONITOR()
        self.sp_app_kit_imdm_list: SP_APP_KIT_IMDM_LIST = SP_APP_KIT_IMDM_LIST()
        self.sp_app_kit_srv_event_app_list_json: SP_APP_KIT_SRV_EVENT_APP_LIST_JSON = SP_APP_KIT_SRV_EVENT_APP_LIST_JSON()
        self.sp_app_kit_srv_event_change: SP_APP_KIT_SRV_EVENT_CHANGE = SP_APP_KIT_SRV_EVENT_CHANGE()
        self.sp_app_kit_srv_event_inst: SP_APP_KIT_SRV_EVENT_INST = SP_APP_KIT_SRV_EVENT_INST()
        self.sp_app_kit_srv_event_uninst: SP_APP_KIT_SRV_EVENT_UNINST = SP_APP_KIT_SRV_EVENT_UNINST()
        self.sp_app_rule_imdm_exists_for_accode: SP_APP_RULE_IMDM_EXISTS_FOR_ACCODE = SP_APP_RULE_IMDM_EXISTS_FOR_ACCODE()
        self.sp_app_rule_imdm_exists_for_guid: SP_APP_RULE_IMDM_EXISTS_FOR_GUID = SP_APP_RULE_IMDM_EXISTS_FOR_GUID()
        self.sp_app_rule_imdm_exists_for_upn: SP_APP_RULE_IMDM_EXISTS_FOR_UPN = SP_APP_RULE_IMDM_EXISTS_FOR_UPN()
        self.sp_app_rule_imdm_get_checked: SP_APP_RULE_IMDM_GET_CHECKED = SP_APP_RULE_IMDM_GET_CHECKED()
        self.sp_app_rule_imdm_get_checked_legacy: SP_APP_RULE_IMDM_GET_CHECKED_LEGACY = SP_APP_RULE_IMDM_GET_CHECKED_LEGACY()
        self.sp_app_rule_imdm_get_current_monitors: SP_APP_RULE_IMDM_GET_CURRENT_MONITORS = SP_APP_RULE_IMDM_GET_CURRENT_MONITORS()
        self.sp_app_rule_imdm_get_managed_applications: SP_APP_RULE_IMDM_GET_MANAGED_APPLICATIONS = SP_APP_RULE_IMDM_GET_MANAGED_APPLICATIONS()
        self.sp_app_rule_imdm_get_v2: SP_APP_RULE_IMDM_GET_V2 = SP_APP_RULE_IMDM_GET_V2()
        self.sp_app_rule_imdm_register_install: SP_APP_RULE_IMDM_REGISTER_INSTALL = SP_APP_RULE_IMDM_REGISTER_INSTALL()
        self.sp_app_rule_imdm_register_remove: SP_APP_RULE_IMDM_REGISTER_REMOVE = SP_APP_RULE_IMDM_REGISTER_REMOVE()
        self.sp_app_rule_imdm_register_status: SP_APP_RULE_IMDM_REGISTER_STATUS = SP_APP_RULE_IMDM_REGISTER_STATUS()
        self.sp_app_store_imdm_get_icon: SP_APP_STORE_IMDM_GET_ICON = SP_APP_STORE_IMDM_GET_ICON()
        self.sp_app_store_imdm_list: SP_APP_STORE_IMDM_LIST = SP_APP_STORE_IMDM_LIST()
        self.sp_app_store_imdm_request: SP_APP_STORE_IMDM_REQUEST = SP_APP_STORE_IMDM_REQUEST()
        self.sp_app_trust_imdm_exists_for_os: SP_APP_TRUST_IMDM_EXISTS_FOR_OS = SP_APP_TRUST_IMDM_EXISTS_FOR_OS()
        self.sp_app_trust_imdm_get: SP_APP_TRUST_IMDM_GET = SP_APP_TRUST_IMDM_GET()
        self.sp_app_trust_imdm_get_data_with_blob: SP_APP_TRUST_IMDM_GET_DATA_WITH_BLOB = SP_APP_TRUST_IMDM_GET_DATA_WITH_BLOB()
        self.sp_app_trust_imdm_get_file_fulldata: SP_APP_TRUST_IMDM_GET_FILE_FULLDATA = SP_APP_TRUST_IMDM_GET_FILE_FULLDATA()
        self.sp_app_trust_imdm_get_file_info: SP_APP_TRUST_IMDM_GET_FILE_INFO = SP_APP_TRUST_IMDM_GET_FILE_INFO()
        self.sp_app_trust_imdm_get_icon: SP_APP_TRUST_IMDM_GET_ICON = SP_APP_TRUST_IMDM_GET_ICON()
        self.sp_assignment_imdm_list_for_kit: SP_ASSIGNMENT_IMDM_LIST_FOR_KIT = SP_ASSIGNMENT_IMDM_LIST_FOR_KIT()
        self.sp_certificate_imdm_authentication: SP_CERTIFICATE_IMDM_AUTHENTICATION = SP_CERTIFICATE_IMDM_AUTHENTICATION()
        self.sp_certificate_imdm_get: SP_CERTIFICATE_IMDM_GET = SP_CERTIFICATE_IMDM_GET()
        self.sp_certificate_imdm_get_active_list: SP_CERTIFICATE_IMDM_GET_ACTIVE_LIST = SP_CERTIFICATE_IMDM_GET_ACTIVE_LIST()
        self.sp_certificate_imdm_get_client: SP_CERTIFICATE_IMDM_GET_CLIENT = SP_CERTIFICATE_IMDM_GET_CLIENT()
        self.sp_certificate_imdm_get_jwt: SP_CERTIFICATE_IMDM_GET_JWT = SP_CERTIFICATE_IMDM_GET_JWT()
        self.sp_certificate_imdm_get_server: SP_CERTIFICATE_IMDM_GET_SERVER = SP_CERTIFICATE_IMDM_GET_SERVER()
        self.sp_certificate_imdm_try_set_jwt: SP_CERTIFICATE_IMDM_TRY_SET_JWT = SP_CERTIFICATE_IMDM_TRY_SET_JWT()
        self.sp_components_imdm_version_check: SP_COMPONENTS_IMDM_VERSION_CHECK = SP_COMPONENTS_IMDM_VERSION_CHECK()
        self.sp_emp_imdm_get_by_id: SP_EMP_IMDM_GET_BY_ID = SP_EMP_IMDM_GET_BY_ID()
        self.sp_emp_imdm_get_emp_id: SP_EMP_IMDM_GET_EMP_ID = SP_EMP_IMDM_GET_EMP_ID()
        self.sp_emp_imdm_get_substitutions_by_accesscode: SP_EMP_IMDM_GET_SUBSTITUTIONS_BY_ACCESSCODE = SP_EMP_IMDM_GET_SUBSTITUTIONS_BY_ACCESSCODE()
        self.sp_emp_imdm_ldap_url: SP_EMP_IMDM_LDAP_URL = SP_EMP_IMDM_LDAP_URL()
        self.sp_event_imdm_add: SP_EVENT_IMDM_ADD = SP_EVENT_IMDM_ADD()
        self.sp_event_imdm_add_connect: SP_EVENT_IMDM_ADD_CONNECT = SP_EVENT_IMDM_ADD_CONNECT()
        self.sp_event_imdm_add_connect_by_udid: SP_EVENT_IMDM_ADD_CONNECT_BY_UDID = SP_EVENT_IMDM_ADD_CONNECT_BY_UDID()
        self.sp_event_imdm_add_control_off: SP_EVENT_IMDM_ADD_CONTROL_OFF = SP_EVENT_IMDM_ADD_CONTROL_OFF()
        self.sp_event_imdm_add_hacking_device: SP_EVENT_IMDM_ADD_HACKING_DEVICE = SP_EVENT_IMDM_ADD_HACKING_DEVICE()
        self.sp_event_imdm_add_json: SP_EVENT_IMDM_ADD_JSON = SP_EVENT_IMDM_ADD_JSON()
        self.sp_event_imdm_add_last_ack: SP_EVENT_IMDM_ADD_LAST_ACK = SP_EVENT_IMDM_ADD_LAST_ACK()
        self.sp_ext_dir_user_sync_imdm_rule_exists: SP_EXT_DIR_USER_SYNC_IMDM_RULE_EXISTS = SP_EXT_DIR_USER_SYNC_IMDM_RULE_EXISTS()
        self.sp_file_to_send_imdm_get: SP_FILE_TO_SEND_IMDM_GET = SP_FILE_TO_SEND_IMDM_GET()
        self.sp_gps_imdm_add_for_kit: SP_GPS_IMDM_ADD_FOR_KIT = SP_GPS_IMDM_ADD_FOR_KIT()
        self.sp_inst_schema_all_get_last_ver: SP_INST_SCHEMA_ALL_GET_LAST_VER = SP_INST_SCHEMA_ALL_GET_LAST_VER()
        self.sp_kit_imdm_add_by_emp: SP_KIT_IMDM_ADD_BY_EMP = SP_KIT_IMDM_ADD_BY_EMP()
        self.sp_kit_imdm_add_with_os: SP_KIT_IMDM_ADD_WITH_OS = SP_KIT_IMDM_ADD_WITH_OS()
        self.sp_kit_imdm_checkin_url_delete: SP_KIT_IMDM_CHECKIN_URL_DELETE = SP_KIT_IMDM_CHECKIN_URL_DELETE()
        self.sp_kit_imdm_checkin_url_get: SP_KIT_IMDM_CHECKIN_URL_GET = SP_KIT_IMDM_CHECKIN_URL_GET()
        self.sp_kit_imdm_checkin_url_set: SP_KIT_IMDM_CHECKIN_URL_SET = SP_KIT_IMDM_CHECKIN_URL_SET()
        self.sp_kit_imdm_find_by_imei: SP_KIT_IMDM_FIND_BY_IMEI = SP_KIT_IMDM_FIND_BY_IMEI()
        self.sp_kit_imdm_find_by_json: SP_KIT_IMDM_FIND_BY_JSON = SP_KIT_IMDM_FIND_BY_JSON()
        self.sp_kit_imdm_find_by_udid_for_ios: SP_KIT_IMDM_FIND_BY_UDID_FOR_IOS = SP_KIT_IMDM_FIND_BY_UDID_FOR_IOS()
        self.sp_kit_imdm_find_metadata: SP_KIT_IMDM_FIND_METADATA = SP_KIT_IMDM_FIND_METADATA()
        self.sp_kit_imdm_get: SP_KIT_IMDM_GET = SP_KIT_IMDM_GET()
        self.sp_kit_imdm_get_next_command_for_ios: SP_KIT_IMDM_GET_NEXT_COMMAND_FOR_IOS = SP_KIT_IMDM_GET_NEXT_COMMAND_FOR_IOS()
        self.sp_kit_imdm_get_settings: SP_KIT_IMDM_GET_SETTINGS = SP_KIT_IMDM_GET_SETTINGS()
        self.sp_kit_imdm_is_supervised: SP_KIT_IMDM_IS_SUPERVISED = SP_KIT_IMDM_IS_SUPERVISED()
        self.sp_kit_imdm_not_now: SP_KIT_IMDM_NOT_NOW = SP_KIT_IMDM_NOT_NOW()
        self.sp_kit_imdm_set_ownership: SP_KIT_IMDM_SET_OWNERSHIP = SP_KIT_IMDM_SET_OWNERSHIP()
        self.sp_kit_imdm_status_control_off: SP_KIT_IMDM_STATUS_CONTROL_OFF = SP_KIT_IMDM_STATUS_CONTROL_OFF()
        self.sp_kit_srv_event_add_container: SP_KIT_SRV_EVENT_ADD_CONTAINER = SP_KIT_SRV_EVENT_ADD_CONTAINER()
        self.sp_kit_srv_event_del_container: SP_KIT_SRV_EVENT_DEL_CONTAINER = SP_KIT_SRV_EVENT_DEL_CONTAINER()
        self.sp_license_imdm_get: SP_LICENSE_IMDM_GET = SP_LICENSE_IMDM_GET()
        self.sp_license_imdm_get_active_kit_count: SP_LICENSE_IMDM_GET_ACTIVE_KIT_COUNT = SP_LICENSE_IMDM_GET_ACTIVE_KIT_COUNT()
        self.sp_loader_imdm_access: SP_LOADER_IMDM_ACCESS = SP_LOADER_IMDM_ACCESS()
        self.sp_loader_imdm_add_by_code: SP_LOADER_IMDM_ADD_BY_CODE = SP_LOADER_IMDM_ADD_BY_CODE()
        self.sp_loader_imdm_add_code_4emp_ios_ldap: SP_LOADER_IMDM_ADD_CODE_4EMP_IOS_LDAP = SP_LOADER_IMDM_ADD_CODE_4EMP_IOS_LDAP()
        self.sp_loader_imdm_add_kit_with_os: SP_LOADER_IMDM_ADD_KIT_WITH_OS = SP_LOADER_IMDM_ADD_KIT_WITH_OS()
        self.sp_loader_imdm_deactivate_code: SP_LOADER_IMDM_DEACTIVATE_CODE = SP_LOADER_IMDM_DEACTIVATE_CODE()
        self.sp_loader_imdm_find_kit_by_token: SP_LOADER_IMDM_FIND_KIT_BY_TOKEN = SP_LOADER_IMDM_FIND_KIT_BY_TOKEN()
        self.sp_loader_ldr_access: SP_LOADER_LDR_ACCESS = SP_LOADER_LDR_ACCESS()
        self.sp_loader_ldr_auth: SP_LOADER_LDR_AUTH = SP_LOADER_LDR_AUTH()
        self.sp_login_result_imdm_fail: SP_LOGIN_RESULT_IMDM_FAIL = SP_LOGIN_RESULT_IMDM_FAIL()
        self.sp_login_result_imdm_get: SP_LOGIN_RESULT_IMDM_GET = SP_LOGIN_RESULT_IMDM_GET()
        self.sp_login_result_imdm_success: SP_LOGIN_RESULT_IMDM_SUCCESS = SP_LOGIN_RESULT_IMDM_SUCCESS()
        self.sp_mob_schedule_imdm_schedule_device_info: SP_MOB_SCHEDULE_IMDM_SCHEDULE_DEVICE_INFO = SP_MOB_SCHEDULE_IMDM_SCHEDULE_DEVICE_INFO()
        self.sp_mob_schedule_imdm_schedule_managed_app_list: SP_MOB_SCHEDULE_IMDM_SCHEDULE_MANAGED_APP_LIST = SP_MOB_SCHEDULE_IMDM_SCHEDULE_MANAGED_APP_LIST()
        self.sp_mob_schedule_imdm_schedule_push: SP_MOB_SCHEDULE_IMDM_SCHEDULE_PUSH = SP_MOB_SCHEDULE_IMDM_SCHEDULE_PUSH()
        self.sp_monitor_db_upd_activity: SP_MONITOR_DB_UPD_ACTIVITY = SP_MONITOR_DB_UPD_ACTIVITY()
        self.sp_monitor_imdm_event_start: SP_MONITOR_IMDM_EVENT_START = SP_MONITOR_IMDM_EVENT_START()
        self.sp_monitor_imdm_get_container_token: SP_MONITOR_IMDM_GET_CONTAINER_TOKEN = SP_MONITOR_IMDM_GET_CONTAINER_TOKEN()
        self.sp_monitor_imdm_get_device_token: SP_MONITOR_IMDM_GET_DEVICE_TOKEN = SP_MONITOR_IMDM_GET_DEVICE_TOKEN()
        self.sp_monitor_imdm_get_for_os: SP_MONITOR_IMDM_GET_FOR_OS = SP_MONITOR_IMDM_GET_FOR_OS()
        self.sp_monitor_imdm_set_mob_param: SP_MONITOR_IMDM_SET_MOB_PARAM = SP_MONITOR_IMDM_SET_MOB_PARAM()
        self.sp_monitor_srv_event_strt: SP_MONITOR_SRV_EVENT_STRT = SP_MONITOR_SRV_EVENT_STRT()
        self.sp_policy_imdm_get_subst_val_list: SP_POLICY_IMDM_GET_SUBST_VAL_LIST = SP_POLICY_IMDM_GET_SUBST_VAL_LIST()
        self.sp_policy_srv_event_apply_error: SP_POLICY_SRV_EVENT_APPLY_ERROR = SP_POLICY_SRV_EVENT_APPLY_ERROR()
        self.sp_profile_imdm_get: SP_PROFILE_IMDM_GET = SP_PROFILE_IMDM_GET()
        self.sp_profile_imdm_get_checked: SP_PROFILE_IMDM_GET_CHECKED = SP_PROFILE_IMDM_GET_CHECKED()
        self.sp_profile_imdm_get_ios_monitor_profile: SP_PROFILE_IMDM_GET_IOS_MONITOR_PROFILE = SP_PROFILE_IMDM_GET_IOS_MONITOR_PROFILE()
        self.sp_profile_imdm_get_safelife_profile: SP_PROFILE_IMDM_GET_SAFELIFE_PROFILE = SP_PROFILE_IMDM_GET_SAFELIFE_PROFILE()
        self.sp_profile_imdm_register_install: SP_PROFILE_IMDM_REGISTER_INSTALL = SP_PROFILE_IMDM_REGISTER_INSTALL()
        self.sp_profile_imdm_register_remove: SP_PROFILE_IMDM_REGISTER_REMOVE = SP_PROFILE_IMDM_REGISTER_REMOVE()
        self.sp_profile_srv_event_inst_err_client: SP_PROFILE_SRV_EVENT_INST_ERR_CLIENT = SP_PROFILE_SRV_EVENT_INST_ERR_CLIENT()
        self.sp_profile_srv_event_inst_err_subst: SP_PROFILE_SRV_EVENT_INST_ERR_SUBST = SP_PROFILE_SRV_EVENT_INST_ERR_SUBST()
        self.sp_profile_srv_event_inst_err_subst_restr: SP_PROFILE_SRV_EVENT_INST_ERR_SUBST_RESTR = SP_PROFILE_SRV_EVENT_INST_ERR_SUBST_RESTR()
        self.sp_profile_srv_event_inst_ok: SP_PROFILE_SRV_EVENT_INST_OK = SP_PROFILE_SRV_EVENT_INST_OK()
        self.sp_profile_srv_event_uninst_err_client: SP_PROFILE_SRV_EVENT_UNINST_ERR_CLIENT = SP_PROFILE_SRV_EVENT_UNINST_ERR_CLIENT()
        self.sp_profile_srv_event_uninst_ok: SP_PROFILE_SRV_EVENT_UNINST_OK = SP_PROFILE_SRV_EVENT_UNINST_OK()
        self.sp_push_clients_imdm_get: SP_PUSH_CLIENTS_IMDM_GET = SP_PUSH_CLIENTS_IMDM_GET()
        self.sp_push_clients_imdm_invalid_token: SP_PUSH_CLIENTS_IMDM_INVALID_TOKEN = SP_PUSH_CLIENTS_IMDM_INVALID_TOKEN()
        self.sp_push_clients_imdm_poll: SP_PUSH_CLIENTS_IMDM_POLL = SP_PUSH_CLIENTS_IMDM_POLL()
        self.sp_push_clients_imdm_set: SP_PUSH_CLIENTS_IMDM_SET = SP_PUSH_CLIENTS_IMDM_SET()
        self.sp_scep_settings_imdm_authentication: SP_SCEP_SETTINGS_IMDM_AUTHENTICATION = SP_SCEP_SETTINGS_IMDM_AUTHENTICATION()
        self.sp_scep_settings_imdm_authentication_by_token: SP_SCEP_SETTINGS_IMDM_AUTHENTICATION_BY_TOKEN = SP_SCEP_SETTINGS_IMDM_AUTHENTICATION_BY_TOKEN()
        self.sp_scep_settings_imdm_prepare: SP_SCEP_SETTINGS_IMDM_PREPARE = SP_SCEP_SETTINGS_IMDM_PREPARE()
        self.sp_server_connection_imdm_get_certificate: SP_SERVER_CONNECTION_IMDM_GET_CERTIFICATE = SP_SERVER_CONNECTION_IMDM_GET_CERTIFICATE()
        self.sp_server_connection_imdm_get_server_cert_list: SP_SERVER_CONNECTION_IMDM_GET_SERVER_CERT_LIST = SP_SERVER_CONNECTION_IMDM_GET_SERVER_CERT_LIST()
        self.sp_server_connection_imdm_get_server_connection: SP_SERVER_CONNECTION_IMDM_GET_SERVER_CONNECTION = SP_SERVER_CONNECTION_IMDM_GET_SERVER_CONNECTION()
        self.sp_server_log_imdm_add: SP_SERVER_LOG_IMDM_ADD = SP_SERVER_LOG_IMDM_ADD()
        self.sp_sim_imdm_event_change: SP_SIM_IMDM_EVENT_CHANGE = SP_SIM_IMDM_EVENT_CHANGE()
        self.sp_sim_imdm_get_sim_kit: SP_SIM_IMDM_GET_SIM_KIT = SP_SIM_IMDM_GET_SIM_KIT()
        self.sp_sim_imdm_list_corp_kit: SP_SIM_IMDM_LIST_CORP_KIT = SP_SIM_IMDM_LIST_CORP_KIT()
        self.sp_sim_srv_event_change: SP_SIM_SRV_EVENT_CHANGE = SP_SIM_SRV_EVENT_CHANGE()
        self.sp_task_imdm_get_task: SP_TASK_IMDM_GET_TASK = SP_TASK_IMDM_GET_TASK()
        self.sp_task_imdm_get_task_by_kit_id: SP_TASK_IMDM_GET_TASK_BY_KIT_ID = SP_TASK_IMDM_GET_TASK_BY_KIT_ID()
        self.sp_task_imdm_get_task_list_by_kit_id: SP_TASK_IMDM_GET_TASK_LIST_BY_KIT_ID = SP_TASK_IMDM_GET_TASK_LIST_BY_KIT_ID()
        self.sp_task_imdm_upd_error_with_details: SP_TASK_IMDM_UPD_ERROR_WITH_DETAILS = SP_TASK_IMDM_UPD_ERROR_WITH_DETAILS()
        self.sp_task_imdm_upd_res: SP_TASK_IMDM_UPD_RES = SP_TASK_IMDM_UPD_RES()
        self.sp_user_agreement_imdm_event_confirm: SP_USER_AGREEMENT_IMDM_EVENT_CONFIRM = SP_USER_AGREEMENT_IMDM_EVENT_CONFIRM()
        self.sp_user_agreement_imdm_get: SP_USER_AGREEMENT_IMDM_GET = SP_USER_AGREEMENT_IMDM_GET()
        self.sp_user_agreement_imdm_get_last: SP_USER_AGREEMENT_IMDM_GET_LAST = SP_USER_AGREEMENT_IMDM_GET_LAST()
        self.sp_user_agreement_srv_event_confirm: SP_USER_AGREEMENT_SRV_EVENT_CONFIRM = SP_USER_AGREEMENT_SRV_EVENT_CONFIRM()
        self.sp_ws_imdm_list_for_kit: SP_WS_IMDM_LIST_FOR_KIT = SP_WS_IMDM_LIST_FOR_KIT()
        