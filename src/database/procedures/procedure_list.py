# -*- coding: utf-8 -*-
from datetime import datetime
from typing import NamedTuple, Any

from asyncpg import Connection

from database.procedures.base_procedure import BaseProcedure

# Данный файл сгенерирован автоматически, любые изменения будут утеряны при запуске parser.py
# Подробности: src/database/README.md


# noinspection PyPep8Naming
class SP_AB_IMDM_LIST_FOR_KIT(BaseProcedure):

    class OutArgs(NamedTuple):
        o_rc: int
        o_err: str
        o_rs: str
        
    class AbRS(NamedTuple):
        ab: Any
        
    # noinspection PyMethodOverriding
    async def __call__(self, connection: Connection, i_mcc_id: int, check_rc: bool = False) -> tuple[OutArgs, list[AbRS]]:
        out_args, ab_rs = await super().__call__(connection, 'sp_ab_imdm_list_for_kit', i_mcc_id , check_rc=check_rc)
        return out_args, ab_rs


# noinspection PyPep8Naming
class SP_APP_CFG_IMDM_GET_CHECKED(BaseProcedure):

    class OutArgs(NamedTuple):
        o_rc: int
        o_err: str
        o_rs: str
        
    class ApplicationConfigRS(NamedTuple):
        app_uid: Any
        ae_aek_id: Any
        ae_checksum: Any
        cfg_location: Any
        cfg_value: Any
        
    # noinspection PyMethodOverriding
    async def __call__(self, connection: Connection, i_mob_id: int, i_cfg_id: int, i_cfg_version: int, check_rc: bool = False) -> tuple[OutArgs, list[ApplicationConfigRS]]:
        out_args, application_config_rs = await super().__call__(connection, 'sp_app_cfg_imdm_get_checked', i_mob_id, i_cfg_id, i_cfg_version , check_rc=check_rc)
        return out_args, application_config_rs


# noinspection PyPep8Naming
class SP_APP_CFG_IMDM_GET_V2(BaseProcedure):

    class OutArgs(NamedTuple):
        o_rc: int
        o_err: str
        o_rs: str
        
    class ApplicationConfigRS(NamedTuple):
        app_uid: Any
        ae_aek_id: Any
        ae_checksum: Any
        cfg_location: Any
        cfg_value: Any
        
    # noinspection PyMethodOverriding
    async def __call__(self, connection: Connection, i_cfg_id: int, check_rc: bool = False) -> tuple[OutArgs, list[ApplicationConfigRS]]:
        out_args, application_config_rs = await super().__call__(connection, 'sp_app_cfg_imdm_get_v2', i_cfg_id , check_rc=check_rc)
        return out_args, application_config_rs


# noinspection PyPep8Naming
class SP_APP_CFG_IMDM_REGISTER_INSTALL(BaseProcedure):

    class OutArgs(NamedTuple):
        o_rc: int
        o_err: str
        
    # noinspection PyMethodOverriding
    async def __call__(self, connection: Connection, i_mob_id: int, i_ae_aek_id: int, i_ae_checksum: str, i_subst_version: int, i_status: str, i_error_details: str, check_rc: bool = False) -> tuple[OutArgs, ]:
        out_args,  = await super().__call__(connection, 'sp_app_cfg_imdm_register_install', i_mob_id, i_ae_aek_id, i_ae_checksum, i_subst_version, i_status, i_error_details , check_rc=check_rc)
        return out_args, 


# noinspection PyPep8Naming
class SP_APP_CFG_IMDM_REGISTER_REMOVE(BaseProcedure):

    class OutArgs(NamedTuple):
        o_rc: int
        o_err: str
        
    # noinspection PyMethodOverriding
    async def __call__(self, connection: Connection, i_mob_id: int, i_ae_aek_id: int, check_rc: bool = False) -> tuple[OutArgs, ]:
        out_args,  = await super().__call__(connection, 'sp_app_cfg_imdm_register_remove', i_mob_id, i_ae_aek_id , check_rc=check_rc)
        return out_args, 


# noinspection PyPep8Naming
class SP_APP_DISTRIB_IMDM_GET_ICON(BaseProcedure):

    class OutArgs(NamedTuple):
        o_rc: int
        o_err: str
        o_rs: str
        
    class AppDistribIconRS(NamedTuple):
        app_distrib_icon: Any
        
    # noinspection PyMethodOverriding
    async def __call__(self, connection: Connection, i_appd_id: int, check_rc: bool = False) -> tuple[OutArgs, list[AppDistribIconRS]]:
        out_args, app_distrib_icon_rs = await super().__call__(connection, 'sp_app_distrib_imdm_get_icon', i_appd_id , check_rc=check_rc)
        return out_args, app_distrib_icon_rs


# noinspection PyPep8Naming
class SP_APP_KIT_IMDM_EVENT_CHANGE(BaseProcedure):

    class OutArgs(NamedTuple):
        o_rc: int
        o_err: str
        
    # noinspection PyMethodOverriding
    async def __call__(self, connection: Connection, i_srv_ts: datetime, i_mob_id: int, i_mob_ts: datetime, i_app_is_in_container: int, i_app_uid: str, i_app_title: str, i_app_version: str, i_app_version_code: str, i_app_can_uninstall: int, i_app_can_disable: int, i_app_is_enabled: int, i_app_is_managed: int, check_rc: bool = False) -> tuple[OutArgs, ]:
        out_args,  = await super().__call__(connection, 'sp_app_kit_imdm_event_change', i_srv_ts, i_mob_id, i_mob_ts, i_app_is_in_container, i_app_uid, i_app_title, i_app_version, i_app_version_code, i_app_can_uninstall, i_app_can_disable, i_app_is_enabled, i_app_is_managed , check_rc=check_rc)
        return out_args, 


# noinspection PyPep8Naming
class SP_APP_KIT_IMDM_EVENT_CHANGE_IOS(BaseProcedure):

    class OutArgs(NamedTuple):
        o_rc: int
        o_err: str
        
    # noinspection PyMethodOverriding
    async def __call__(self, connection: Connection, i_srv_ts: datetime, i_mob_id: int, i_mob_ts: datetime, i_app_uid: str, i_app_title: str, i_app_version: str, i_app_version_code: str, i_app_is_managed: int, check_rc: bool = False) -> tuple[OutArgs, ]:
        out_args,  = await super().__call__(connection, 'sp_app_kit_imdm_event_change_ios', i_srv_ts, i_mob_id, i_mob_ts, i_app_uid, i_app_title, i_app_version, i_app_version_code, i_app_is_managed , check_rc=check_rc)
        return out_args, 


# noinspection PyPep8Naming
class SP_APP_KIT_IMDM_EVENT_CHANGE_V2(BaseProcedure):

    class OutArgs(NamedTuple):
        o_rc: int
        o_err: str
        
    # noinspection PyMethodOverriding
    async def __call__(self, connection: Connection, i_srv_ts: datetime, i_mob_id: int, i_mob_ts: datetime, i_app_is_in_container: int, i_app_uid: str, i_app_title: str, i_app_version: str, i_app_version_code: str, i_app_can_uninstall: int, i_app_can_disable: int, i_app_is_enabled: int, i_app_is_managed: int, i_app_reputation: str, i_app_is_threat: int, check_rc: bool = False) -> tuple[OutArgs, ]:
        out_args,  = await super().__call__(connection, 'sp_app_kit_imdm_event_change_v2', i_srv_ts, i_mob_id, i_mob_ts, i_app_is_in_container, i_app_uid, i_app_title, i_app_version, i_app_version_code, i_app_can_uninstall, i_app_can_disable, i_app_is_enabled, i_app_is_managed, i_app_reputation, i_app_is_threat , check_rc=check_rc)
        return out_args, 


# noinspection PyPep8Naming
class SP_APP_KIT_IMDM_EVENT_INST(BaseProcedure):

    class OutArgs(NamedTuple):
        o_rc: int
        o_err: str
        
    # noinspection PyMethodOverriding
    async def __call__(self, connection: Connection, i_srv_ts: datetime, i_mob_id: int, i_mob_ts: datetime, i_app_is_in_container: int, i_app_uid: str, i_app_title: str, i_app_version: str, i_app_version_code: str, i_app_can_uninstall: int, i_app_can_disable: int, i_app_is_enabled: int, i_app_is_managed: int, check_rc: bool = False) -> tuple[OutArgs, ]:
        out_args,  = await super().__call__(connection, 'sp_app_kit_imdm_event_inst', i_srv_ts, i_mob_id, i_mob_ts, i_app_is_in_container, i_app_uid, i_app_title, i_app_version, i_app_version_code, i_app_can_uninstall, i_app_can_disable, i_app_is_enabled, i_app_is_managed , check_rc=check_rc)
        return out_args, 


# noinspection PyPep8Naming
class SP_APP_KIT_IMDM_EVENT_INST_IOS(BaseProcedure):

    class OutArgs(NamedTuple):
        o_rc: int
        o_err: str
        
    # noinspection PyMethodOverriding
    async def __call__(self, connection: Connection, i_srv_ts: datetime, i_mob_id: int, i_mob_ts: datetime, i_app_uid: str, i_app_title: str, i_app_version: str, i_app_version_code: str, i_app_is_managed: int, check_rc: bool = False) -> tuple[OutArgs, ]:
        out_args,  = await super().__call__(connection, 'sp_app_kit_imdm_event_inst_ios', i_srv_ts, i_mob_id, i_mob_ts, i_app_uid, i_app_title, i_app_version, i_app_version_code, i_app_is_managed , check_rc=check_rc)
        return out_args, 


# noinspection PyPep8Naming
class SP_APP_KIT_IMDM_EVENT_INST_V2(BaseProcedure):

    class OutArgs(NamedTuple):
        o_rc: int
        o_err: str
        
    # noinspection PyMethodOverriding
    async def __call__(self, connection: Connection, i_srv_ts: datetime, i_mob_id: int, i_mob_ts: datetime, i_app_is_in_container: int, i_app_uid: str, i_app_title: str, i_app_version: str, i_app_version_code: str, i_app_can_uninstall: int, i_app_can_disable: int, i_app_is_enabled: int, i_app_is_managed: int, i_app_reputation: str, i_app_is_threat: int, check_rc: bool = False) -> tuple[OutArgs, ]:
        out_args,  = await super().__call__(connection, 'sp_app_kit_imdm_event_inst_v2', i_srv_ts, i_mob_id, i_mob_ts, i_app_is_in_container, i_app_uid, i_app_title, i_app_version, i_app_version_code, i_app_can_uninstall, i_app_can_disable, i_app_is_enabled, i_app_is_managed, i_app_reputation, i_app_is_threat , check_rc=check_rc)
        return out_args, 


# noinspection PyPep8Naming
class SP_APP_KIT_IMDM_EVENT_UNINST(BaseProcedure):

    class OutArgs(NamedTuple):
        o_rc: int
        o_err: str
        
    # noinspection PyMethodOverriding
    async def __call__(self, connection: Connection, i_srv_ts: datetime, i_mob_id: int, i_mob_ts: datetime, i_app_is_in_container: int, i_app_uid: str, check_rc: bool = False) -> tuple[OutArgs, ]:
        out_args,  = await super().__call__(connection, 'sp_app_kit_imdm_event_uninst', i_srv_ts, i_mob_id, i_mob_ts, i_app_is_in_container, i_app_uid , check_rc=check_rc)
        return out_args, 


# noinspection PyPep8Naming
class SP_APP_KIT_IMDM_GET_APP_MONITOR(BaseProcedure):

    class OutArgs(NamedTuple):
        o_rc: int
        o_err: str
        o_app_id: int
        o_app_version: str
        o_app_version_code: str
        
    # noinspection PyMethodOverriding
    async def __call__(self, connection: Connection, i_mob_id: int, i_app_is_in_container: int, check_rc: bool = False) -> tuple[OutArgs, ]:
        out_args,  = await super().__call__(connection, 'sp_app_kit_imdm_get_app_monitor', i_mob_id, i_app_is_in_container , check_rc=check_rc)
        return out_args, 


# noinspection PyPep8Naming
class SP_APP_KIT_IMDM_LIST(BaseProcedure):

    class OutArgs(NamedTuple):
        o_rc: int
        o_err: str
        o_rs: str
        
    class AppKitRS(NamedTuple):
        app_kit: Any
        
    # noinspection PyMethodOverriding
    async def __call__(self, connection: Connection, i_mob_id: int, i_app_is_in_container: int, check_rc: bool = False) -> tuple[OutArgs, list[AppKitRS]]:
        out_args, app_kit_rs = await super().__call__(connection, 'sp_app_kit_imdm_list', i_mob_id, i_app_is_in_container , check_rc=check_rc)
        return out_args, app_kit_rs


# noinspection PyPep8Naming
class SP_APP_KIT_SRV_EVENT_APP_LIST_JSON(BaseProcedure):

    class OutArgs(NamedTuple):
        o_rc: int
        o_err: str
        
    # noinspection PyMethodOverriding
    async def __call__(self, connection: Connection, i_mob_id: int, i_event: bytes, check_rc: bool = False) -> tuple[OutArgs, ]:
        out_args,  = await super().__call__(connection, 'sp_app_kit_srv_event_app_list_json', i_mob_id, i_event , check_rc=check_rc)
        return out_args, 


# noinspection PyPep8Naming
class SP_APP_KIT_SRV_EVENT_CHANGE(BaseProcedure):

    class OutArgs(NamedTuple):
        o_rc: int
        o_err: str
        
    # noinspection PyMethodOverriding
    async def __call__(self, connection: Connection, i_srv_ts: datetime, i_mob_id: int, i_mob_ts: datetime, i_app_is_in_container: int, i_app_uid: str, i_app_title: str, i_app_version: str, i_app_version_code: str, i_app_can_uninstall: int, i_app_can_disable: int, i_app_is_enabled: int, i_app_is_inst_by_safephone: int, i_app_is_managed: int, check_rc: bool = False) -> tuple[OutArgs, ]:
        out_args,  = await super().__call__(connection, 'sp_app_kit_srv_event_change', i_srv_ts, i_mob_id, i_mob_ts, i_app_is_in_container, i_app_uid, i_app_title, i_app_version, i_app_version_code, i_app_can_uninstall, i_app_can_disable, i_app_is_enabled, i_app_is_inst_by_safephone, i_app_is_managed , check_rc=check_rc)
        return out_args, 


# noinspection PyPep8Naming
class SP_APP_KIT_SRV_EVENT_INST(BaseProcedure):

    class OutArgs(NamedTuple):
        o_rc: int
        o_err: str
        
    # noinspection PyMethodOverriding
    async def __call__(self, connection: Connection, i_srv_ts: datetime, i_mob_id: int, i_mob_ts: datetime, i_app_is_in_container: int, i_app_uid: str, i_app_title: str, i_app_version: str, i_app_version_code: str, i_app_can_uninstall: int, i_app_can_disable: int, i_app_is_enabled: int, i_app_is_inst_by_safephone: int, i_app_is_managed: int, check_rc: bool = False) -> tuple[OutArgs, ]:
        out_args,  = await super().__call__(connection, 'sp_app_kit_srv_event_inst', i_srv_ts, i_mob_id, i_mob_ts, i_app_is_in_container, i_app_uid, i_app_title, i_app_version, i_app_version_code, i_app_can_uninstall, i_app_can_disable, i_app_is_enabled, i_app_is_inst_by_safephone, i_app_is_managed , check_rc=check_rc)
        return out_args, 


# noinspection PyPep8Naming
class SP_APP_KIT_SRV_EVENT_UNINST(BaseProcedure):

    class OutArgs(NamedTuple):
        o_rc: int
        o_err: str
        
    # noinspection PyMethodOverriding
    async def __call__(self, connection: Connection, i_srv_ts: datetime, i_mob_id: int, i_mob_ts: datetime, i_app_is_in_container: int, i_app_uid: str, check_rc: bool = False) -> tuple[OutArgs, ]:
        out_args,  = await super().__call__(connection, 'sp_app_kit_srv_event_uninst', i_srv_ts, i_mob_id, i_mob_ts, i_app_is_in_container, i_app_uid , check_rc=check_rc)
        return out_args, 


# noinspection PyPep8Naming
class SP_APP_RULE_IMDM_EXISTS_FOR_ACCODE(BaseProcedure):

    class OutArgs(NamedTuple):
        o_rc: int
        o_err: str
        o_exists: int
        
    # noinspection PyMethodOverriding
    async def __call__(self, connection: Connection, i_code: str, i_ost_platform: str, i_os_version: str, check_rc: bool = False) -> tuple[OutArgs, ]:
        out_args,  = await super().__call__(connection, 'sp_app_rule_imdm_exists_for_accode', i_code, i_ost_platform, i_os_version , check_rc=check_rc)
        return out_args, 


# noinspection PyPep8Naming
class SP_APP_RULE_IMDM_EXISTS_FOR_GUID(BaseProcedure):

    class OutArgs(NamedTuple):
        o_rc: int
        o_err: str
        o_exists: int
        
    # noinspection PyMethodOverriding
    async def __call__(self, connection: Connection, i_guid: str, i_ost_platform: str, i_os_version: str, check_rc: bool = False) -> tuple[OutArgs, ]:
        out_args,  = await super().__call__(connection, 'sp_app_rule_imdm_exists_for_guid', i_guid, i_ost_platform, i_os_version , check_rc=check_rc)
        return out_args, 


# noinspection PyPep8Naming
class SP_APP_RULE_IMDM_EXISTS_FOR_UPN(BaseProcedure):

    class OutArgs(NamedTuple):
        o_rc: int
        o_err: str
        o_exists: int
        
    # noinspection PyMethodOverriding
    async def __call__(self, connection: Connection, i_upn: str, i_ost_platform: str, i_os_version: str, check_rc: bool = False) -> tuple[OutArgs, ]:
        out_args,  = await super().__call__(connection, 'sp_app_rule_imdm_exists_for_upn', i_upn, i_ost_platform, i_os_version , check_rc=check_rc)
        return out_args, 


# noinspection PyPep8Naming
class SP_APP_RULE_IMDM_GET_CHECKED(BaseProcedure):

    class OutArgs(NamedTuple):
        o_rc: int
        o_err: str
        o_rs: str
        
    class AppRuleRS(NamedTuple):
        app_rule_id: Any
        app_rule_version: Any
        ae_aek_id: Any
        ae_checksum: Any
        app_rule_source_id: Any
        app_rule_source_type: Any
        app_uid: Any
        app_version: Any
        app_version_code: Any
        apprv_is_installed: Any
        apprv_is_enabled: Any
        apprv_install_to_container: Any
        apprv_delete_on_cutoff: Any
        apprv_prevent_closing: Any
        app_name: Any
        icon_id: int
        
    # noinspection PyMethodOverriding
    async def __call__(self, connection: Connection, i_mob_id: int, i_app_rule_id: int, i_app_rule_version: int, check_rc: bool = False) -> tuple[OutArgs, list[AppRuleRS]]:
        out_args, app_rule_rs = await super().__call__(connection, 'sp_app_rule_imdm_get_checked', i_mob_id, i_app_rule_id, i_app_rule_version , check_rc=check_rc)
        return out_args, app_rule_rs


# noinspection PyPep8Naming
class SP_APP_RULE_IMDM_GET_CHECKED_LEGACY(BaseProcedure):

    class OutArgs(NamedTuple):
        o_rc: int
        o_err: str
        o_rs: str
        
    class AppRuleRS(NamedTuple):
        app_rule_id: Any
        app_rule_version: Any
        ae_aek_id: Any
        ae_checksum: Any
        app_rule_source_id: Any
        app_rule_source_type: Any
        app_uid: Any
        app_version: Any
        app_version_code: Any
        apprv_is_installed: Any
        apprv_is_enabled: Any
        apprv_install_to_container: Any
        apprv_delete_on_cutoff: Any
        
    # noinspection PyMethodOverriding
    async def __call__(self, connection: Connection, i_mob_id: int, i_app_rule_id: int, i_app_rule_version: int, check_rc: bool = False) -> tuple[OutArgs, list[AppRuleRS]]:
        out_args, app_rule_rs = await super().__call__(connection, 'sp_app_rule_imdm_get_checked_legacy', i_mob_id, i_app_rule_id, i_app_rule_version , check_rc=check_rc)
        return out_args, app_rule_rs


# noinspection PyPep8Naming
class SP_APP_RULE_IMDM_GET_CURRENT_MONITORS(BaseProcedure):

    class OutArgs(NamedTuple):
        o_rc: int
        o_err: str
        o_rs: str
        
    class MonitorsListRS(NamedTuple):
        app_uid: Any
        
    # noinspection PyMethodOverriding
    async def __call__(self, connection: Connection, i_mob_id: int, check_rc: bool = False) -> tuple[OutArgs, list[MonitorsListRS]]:
        out_args, monitors_list_rs = await super().__call__(connection, 'sp_app_rule_imdm_get_current_monitors', i_mob_id , check_rc=check_rc)
        return out_args, monitors_list_rs


# noinspection PyPep8Naming
class SP_APP_RULE_IMDM_GET_MANAGED_APPLICATIONS(BaseProcedure):

    class OutArgs(NamedTuple):
        o_rc: int
        o_err: str
        o_rs: str
        
    class ManagedAppListRS(NamedTuple):
        app_uid: Any
        status: str
        
    # noinspection PyMethodOverriding
    async def __call__(self, connection: Connection, i_mob_id: int, check_rc: bool = False) -> tuple[OutArgs, list[ManagedAppListRS]]:
        out_args, managed_app_list_rs = await super().__call__(connection, 'sp_app_rule_imdm_get_managed_applications', i_mob_id , check_rc=check_rc)
        return out_args, managed_app_list_rs


# noinspection PyPep8Naming
class SP_APP_RULE_IMDM_GET_V2(BaseProcedure):

    class OutArgs(NamedTuple):
        o_rc: int
        o_err: str
        o_rs: str
        
    class AppRuleRS(NamedTuple):
        app_uid: Any
        app_rule_source_type: Any
        app_rule_source_id: Any
        ae_aek_id: int
        ae_checksum: str
        appr_delete_on_cutoff: bool
        appr_backup_denied: bool
        app_is_monitor: Any
        
    # noinspection PyMethodOverriding
    async def __call__(self, connection: Connection, i_app_rule_id: int, check_rc: bool = False) -> tuple[OutArgs, list[AppRuleRS]]:
        out_args, app_rule_rs = await super().__call__(connection, 'sp_app_rule_imdm_get_v2', i_app_rule_id , check_rc=check_rc)
        return out_args, app_rule_rs


# noinspection PyPep8Naming
class SP_APP_RULE_IMDM_REGISTER_INSTALL(BaseProcedure):

    class OutArgs(NamedTuple):
        o_rc: int
        o_err: str
        
    # noinspection PyMethodOverriding
    async def __call__(self, connection: Connection, i_mob_id: int, i_ae_aek_id: int, i_ae_checksum: str, i_status: str, i_error_details: str, check_rc: bool = False) -> tuple[OutArgs, ]:
        out_args,  = await super().__call__(connection, 'sp_app_rule_imdm_register_install', i_mob_id, i_ae_aek_id, i_ae_checksum, i_status, i_error_details , check_rc=check_rc)
        return out_args, 


# noinspection PyPep8Naming
class SP_APP_RULE_IMDM_REGISTER_REMOVE(BaseProcedure):

    class OutArgs(NamedTuple):
        o_rc: int
        o_err: str
        
    # noinspection PyMethodOverriding
    async def __call__(self, connection: Connection, i_mob_id: int, i_ae_aek_id: int, check_rc: bool = False) -> tuple[OutArgs, ]:
        out_args,  = await super().__call__(connection, 'sp_app_rule_imdm_register_remove', i_mob_id, i_ae_aek_id , check_rc=check_rc)
        return out_args, 


# noinspection PyPep8Naming
class SP_APP_RULE_IMDM_REGISTER_STATUS(BaseProcedure):

    class OutArgs(NamedTuple):
        o_rc: int
        o_err: str
        
    # noinspection PyMethodOverriding
    async def __call__(self, connection: Connection, i_mob_id: int, i_app_uid: str, i_status: str, check_rc: bool = False) -> tuple[OutArgs, ]:
        out_args,  = await super().__call__(connection, 'sp_app_rule_imdm_register_status', i_mob_id, i_app_uid, i_status , check_rc=check_rc)
        return out_args, 


# noinspection PyPep8Naming
class SP_APP_STORE_IMDM_GET_ICON(BaseProcedure):

    class OutArgs(NamedTuple):
        o_rc: int
        o_err: str
        o_rs: str
        
    class AppStoreIconRS(NamedTuple):
        app_store_icon: Any
        
    # noinspection PyMethodOverriding
    async def __call__(self, connection: Connection, i_appd_id: int, check_rc: bool = False) -> tuple[OutArgs, list[AppStoreIconRS]]:
        out_args, app_store_icon_rs = await super().__call__(connection, 'sp_app_store_imdm_get_icon', i_appd_id , check_rc=check_rc)
        return out_args, app_store_icon_rs


# noinspection PyPep8Naming
class SP_APP_STORE_IMDM_LIST(BaseProcedure):

    class OutArgs(NamedTuple):
        o_rc: int
        o_err: str
        o_rs: str
        
    class AppStoreRS(NamedTuple):
        app_store: Any
        
    # noinspection PyMethodOverriding
    async def __call__(self, connection: Connection, i_mob_id: int, check_rc: bool = False) -> tuple[OutArgs, list[AppStoreRS]]:
        out_args, app_store_rs = await super().__call__(connection, 'sp_app_store_imdm_list', i_mob_id , check_rc=check_rc)
        return out_args, app_store_rs


# noinspection PyPep8Naming
class SP_APP_STORE_IMDM_REQUEST(BaseProcedure):

    class OutArgs(NamedTuple):
        o_rc: int
        o_err: str
        
    # noinspection PyMethodOverriding
    async def __call__(self, connection: Connection, i_mob_id: int, i_app_uid: str, i_is_needed: int, i_app_is_in_container: int, check_rc: bool = False) -> tuple[OutArgs, ]:
        out_args,  = await super().__call__(connection, 'sp_app_store_imdm_request', i_mob_id, i_app_uid, i_is_needed, i_app_is_in_container , check_rc=check_rc)
        return out_args, 


# noinspection PyPep8Naming
class SP_APP_TRUST_IMDM_EXISTS_FOR_OS(BaseProcedure):

    class OutArgs(NamedTuple):
        o_rc: int
        o_err: str
        o_res: int
        
    # noinspection PyMethodOverriding
    async def __call__(self, connection: Connection, i_app_id: int, i_os_id: int, check_rc: bool = False) -> tuple[OutArgs, ]:
        out_args,  = await super().__call__(connection, 'sp_app_trust_imdm_exists_for_os', i_app_id, i_os_id , check_rc=check_rc)
        return out_args, 


# noinspection PyPep8Naming
class SP_APP_TRUST_IMDM_GET(BaseProcedure):

    class OutArgs(NamedTuple):
        o_rc: int
        o_err: str
        o_rs: str
        
    class AppTrustRS(NamedTuple):
        app_trust: Any
        
    # noinspection PyMethodOverriding
    async def __call__(self, connection: Connection, i_app_id: int, check_rc: bool = False) -> tuple[OutArgs, list[AppTrustRS]]:
        out_args, app_trust_rs = await super().__call__(connection, 'sp_app_trust_imdm_get', i_app_id , check_rc=check_rc)
        return out_args, app_trust_rs


# noinspection PyPep8Naming
class SP_APP_TRUST_IMDM_GET_DATA_WITH_BLOB(BaseProcedure):

    class OutArgs(NamedTuple):
        o_rc: int
        o_err: str
        o_rs: str
        
    class AppTrustFileWithBlobRS(NamedTuple):
        app_trust_file_with_blob: Any
        
    # noinspection PyMethodOverriding
    async def __call__(self, connection: Connection, i_app_id: int, check_rc: bool = False) -> tuple[OutArgs, list[AppTrustFileWithBlobRS]]:
        out_args, app_trust_file_with_blob_rs = await super().__call__(connection, 'sp_app_trust_imdm_get_data_with_blob', i_app_id , check_rc=check_rc)
        return out_args, app_trust_file_with_blob_rs


# noinspection PyPep8Naming
class SP_APP_TRUST_IMDM_GET_FILE_FULLDATA(BaseProcedure):

    class OutArgs(NamedTuple):
        o_rc: int
        o_err: str
        o_rs: str
        
    class AppTrustRS(NamedTuple):
        app_trust: Any
        
    # noinspection PyMethodOverriding
    async def __call__(self, connection: Connection, i_app_id: int, i_file_type: str, check_rc: bool = False) -> tuple[OutArgs, list[AppTrustRS]]:
        out_args, app_trust_rs = await super().__call__(connection, 'sp_app_trust_imdm_get_file_fulldata', i_app_id, i_file_type , check_rc=check_rc)
        return out_args, app_trust_rs


# noinspection PyPep8Naming
class SP_APP_TRUST_IMDM_GET_FILE_INFO(BaseProcedure):

    class OutArgs(NamedTuple):
        o_rc: int
        o_err: str
        o_rs: str
        
    class AppTrustRS(NamedTuple):
        app_trust: Any
        
    # noinspection PyMethodOverriding
    async def __call__(self, connection: Connection, i_app_id: int, i_file_type: str, check_rc: bool = False) -> tuple[OutArgs, list[AppTrustRS]]:
        out_args, app_trust_rs = await super().__call__(connection, 'sp_app_trust_imdm_get_file_info', i_app_id, i_file_type , check_rc=check_rc)
        return out_args, app_trust_rs


# noinspection PyPep8Naming
class SP_APP_TRUST_IMDM_GET_ICON(BaseProcedure):

    class OutArgs(NamedTuple):
        o_rc: int
        o_err: str
        o_rs: str
        
    class AppTrustIconRS(NamedTuple):
        app_trust_icon: Any
        
    # noinspection PyMethodOverriding
    async def __call__(self, connection: Connection, i_appt_id: int, check_rc: bool = False) -> tuple[OutArgs, list[AppTrustIconRS]]:
        out_args, app_trust_icon_rs = await super().__call__(connection, 'sp_app_trust_imdm_get_icon', i_appt_id , check_rc=check_rc)
        return out_args, app_trust_icon_rs


# noinspection PyPep8Naming
class SP_ASSIGNMENT_IMDM_LIST_FOR_KIT(BaseProcedure):

    class OutArgs(NamedTuple):
        o_rc: int
        o_err: str
        o_rs: str
        
    class AssignmentEntityRS(NamedTuple):
        ae_objid: int
        ae_version: int
        ae_type_id: int
        ae_aek_id: int
        ae_checksum: str
        
    # noinspection PyMethodOverriding
    async def __call__(self, connection: Connection, i_mob_id: int, check_rc: bool = False) -> tuple[OutArgs, list[AssignmentEntityRS]]:
        out_args, assignment_entity_rs = await super().__call__(connection, 'sp_assignment_imdm_list_for_kit', i_mob_id , check_rc=check_rc)
        return out_args, assignment_entity_rs


# noinspection PyPep8Naming
class SP_CERTIFICATE_IMDM_AUTHENTICATION(BaseProcedure):

    class OutArgs(NamedTuple):
        o_rc: int
        o_err: str
        
    # noinspection PyMethodOverriding
    async def __call__(self, connection: Connection, i_mob_id: int, i_cert_fingerprint: str, check_rc: bool = False) -> tuple[OutArgs, ]:
        out_args,  = await super().__call__(connection, 'sp_certificate_imdm_authentication', i_mob_id, i_cert_fingerprint , check_rc=check_rc)
        return out_args, 


# noinspection PyPep8Naming
class SP_CERTIFICATE_IMDM_GET(BaseProcedure):

    class OutArgs(NamedTuple):
        o_rc: int
        o_err: str
        o_rs: str
        
    class CertRS(NamedTuple):
        cert: Any
        
    # noinspection PyMethodOverriding
    async def __call__(self, connection: Connection, i_mob_id: int, i_cert_id: int, check_rc: bool = False) -> tuple[OutArgs, list[CertRS]]:
        out_args, cert_rs = await super().__call__(connection, 'sp_certificate_imdm_get', i_mob_id, i_cert_id , check_rc=check_rc)
        return out_args, cert_rs


# noinspection PyPep8Naming
class SP_CERTIFICATE_IMDM_GET_ACTIVE_LIST(BaseProcedure):

    class OutArgs(NamedTuple):
        o_rc: int
        o_err: str
        o_rs: str
        
    class CertFingerprintRS(NamedTuple):
        cert_fingerprint: str
        
    # noinspection PyMethodOverriding
    async def __call__(self, connection: Connection, i_mob_id: int, check_rc: bool = False) -> tuple[OutArgs, list[CertFingerprintRS]]:
        out_args, cert_fingerprint_rs = await super().__call__(connection, 'sp_certificate_imdm_get_active_list', i_mob_id , check_rc=check_rc)
        return out_args, cert_fingerprint_rs


# noinspection PyPep8Naming
class SP_CERTIFICATE_IMDM_GET_CLIENT(BaseProcedure):

    class OutArgs(NamedTuple):
        o_rc: int
        o_err: str
        o_rs: str
        
    class CertRS(NamedTuple):
        cert: Any
        
    # noinspection PyMethodOverriding
    async def __call__(self, connection: Connection, i_mob_id: int, i_cert_id: int, check_rc: bool = False) -> tuple[OutArgs, list[CertRS]]:
        out_args, cert_rs = await super().__call__(connection, 'sp_certificate_imdm_get_client', i_mob_id, i_cert_id , check_rc=check_rc)
        return out_args, cert_rs


# noinspection PyPep8Naming
class SP_CERTIFICATE_IMDM_GET_JWT(BaseProcedure):

    class OutArgs(NamedTuple):
        o_rc: int
        o_err: str
        o_cert_file: bytes
        
    # noinspection PyMethodOverriding
    async def __call__(self, connection: Connection, check_rc: bool = False) -> tuple[OutArgs, ]:
        out_args,  = await super().__call__(connection, 'sp_certificate_imdm_get_jwt',  check_rc=check_rc)
        return out_args, 


# noinspection PyPep8Naming
class SP_CERTIFICATE_IMDM_GET_SERVER(BaseProcedure):

    class OutArgs(NamedTuple):
        o_rc: int
        o_err: str
        o_rs: str
        
    class CertRS(NamedTuple):
        cert: Any
        
    # noinspection PyMethodOverriding
    async def __call__(self, connection: Connection, i_cert_id: int, check_rc: bool = False) -> tuple[OutArgs, list[CertRS]]:
        out_args, cert_rs = await super().__call__(connection, 'sp_certificate_imdm_get_server', i_cert_id , check_rc=check_rc)
        return out_args, cert_rs


# noinspection PyPep8Naming
class SP_CERTIFICATE_IMDM_TRY_SET_JWT(BaseProcedure):

    class OutArgs(NamedTuple):
        o_rc: int
        o_err: str
        o_cert_file: bytes
        
    # noinspection PyMethodOverriding
    async def __call__(self, connection: Connection, i_cert_fingerprint: str, i_cert_title: str, i_cert_file: bytes, i_cert_version: str, i_cert_sn: str, i_cert_issuer_name: str, i_cert_validity_not_before: datetime, i_cert_validity_not_after: datetime, i_cert_subject_name: str, check_rc: bool = False) -> tuple[OutArgs, ]:
        out_args,  = await super().__call__(connection, 'sp_certificate_imdm_try_set_jwt', i_cert_fingerprint, i_cert_title, i_cert_file, i_cert_version, i_cert_sn, i_cert_issuer_name, i_cert_validity_not_before, i_cert_validity_not_after, i_cert_subject_name , check_rc=check_rc)
        return out_args, 


# noinspection PyPep8Naming
class SP_COMPONENTS_IMDM_VERSION_CHECK(BaseProcedure):

    class OutArgs(NamedTuple):
        o_rc: int
        o_err: str
        
    # noinspection PyMethodOverriding
    async def __call__(self, connection: Connection, check_rc: bool = False) -> tuple[OutArgs, ]:
        out_args,  = await super().__call__(connection, 'sp_components_imdm_version_check',  check_rc=check_rc)
        return out_args, 


# noinspection PyPep8Naming
class SP_EMP_IMDM_GET_BY_ID(BaseProcedure):

    class OutArgs(NamedTuple):
        o_rc: int
        o_err: str
        o_rs: str
        
    class EmpIdRS(NamedTuple):
        emp: Any
        
    # noinspection PyMethodOverriding
    async def __call__(self, connection: Connection, i_emp_id: int, check_rc: bool = False) -> tuple[OutArgs, list[EmpIdRS]]:
        out_args, emp_id_rs = await super().__call__(connection, 'sp_emp_imdm_get_by_id', i_emp_id , check_rc=check_rc)
        return out_args, emp_id_rs


# noinspection PyPep8Naming
class SP_EMP_IMDM_GET_EMP_ID(BaseProcedure):

    class OutArgs(NamedTuple):
        o_rc: int
        o_err: str
        o_emp_id: int
        
    # noinspection PyMethodOverriding
    async def __call__(self, connection: Connection, i_username: str, check_rc: bool = False) -> tuple[OutArgs, ]:
        out_args,  = await super().__call__(connection, 'sp_emp_imdm_get_emp_id', i_username , check_rc=check_rc)
        return out_args, 


# noinspection PyPep8Naming
class SP_EMP_IMDM_GET_SUBSTITUTIONS_BY_ACCESSCODE(BaseProcedure):

    class OutArgs(NamedTuple):
        o_rc: int
        o_err: str
        o_rs: str
        
    class PolValListRS(NamedTuple):
        policy_subst_value: Any
        
    # noinspection PyMethodOverriding
    async def __call__(self, connection: Connection, i_accesstoken: str, check_rc: bool = False) -> tuple[OutArgs, list[PolValListRS]]:
        out_args, pol_val_list_rs = await super().__call__(connection, 'sp_emp_imdm_get_substitutions_by_accesscode', i_accesstoken , check_rc=check_rc)
        return out_args, pol_val_list_rs


# noinspection PyPep8Naming
class SP_EMP_IMDM_LDAP_URL(BaseProcedure):

    class OutArgs(NamedTuple):
        o_rc: int
        o_err: str
        o_rs: str
        
    class EmpRS(NamedTuple):
        ldaps_url: str
        base_dn: str
        group_dn: str
        
    # noinspection PyMethodOverriding
    async def __call__(self, connection: Connection, i_username: str, check_rc: bool = False) -> tuple[OutArgs, list[EmpRS]]:
        out_args, emp_rs = await super().__call__(connection, 'sp_emp_imdm_ldap_url', i_username , check_rc=check_rc)
        return out_args, emp_rs


# noinspection PyPep8Naming
class SP_EVENT_IMDM_ADD(BaseProcedure):

    class OutArgs(NamedTuple):
        o_rc: int
        o_err: str
        
    # noinspection PyMethodOverriding
    async def __call__(self, connection: Connection, i_ts: datetime, i_mcc_id: int, i_tsmobile: datetime, i_eventcode: int, i_attrid1: int, i_attrvalue1: str, i_attrid2: int, i_attrvalue2: str, i_attrid3: int, i_attrvalue3: str, check_rc: bool = False) -> tuple[OutArgs, ]:
        out_args,  = await super().__call__(connection, 'sp_event_imdm_add', i_ts, i_mcc_id, i_tsmobile, i_eventcode, i_attrid1, i_attrvalue1, i_attrid2, i_attrvalue2, i_attrid3, i_attrvalue3 , check_rc=check_rc)
        return out_args, 


# noinspection PyPep8Naming
class SP_EVENT_IMDM_ADD_CONNECT(BaseProcedure):

    class OutArgs(NamedTuple):
        o_rc: int
        o_err: str
        
    # noinspection PyMethodOverriding
    async def __call__(self, connection: Connection, i_ts: datetime, i_mccid: int, i_tsmcc: datetime, i_ipaddress: str, i_conntype: str, check_rc: bool = False) -> tuple[OutArgs, ]:
        out_args,  = await super().__call__(connection, 'sp_event_imdm_add_connect', i_ts, i_mccid, i_tsmcc, i_ipaddress, i_conntype , check_rc=check_rc)
        return out_args, 


# noinspection PyPep8Naming
class SP_EVENT_IMDM_ADD_CONNECT_BY_UDID(BaseProcedure):

    class OutArgs(NamedTuple):
        o_rc: int
        o_err: str
        o_mob_id: int
        
    # noinspection PyMethodOverriding
    async def __call__(self, connection: Connection, i_mob_udid: str, i_ipaddress: str, check_rc: bool = False) -> tuple[OutArgs, ]:
        out_args,  = await super().__call__(connection, 'sp_event_imdm_add_connect_by_udid', i_mob_udid, i_ipaddress , check_rc=check_rc)
        return out_args, 


# noinspection PyPep8Naming
class SP_EVENT_IMDM_ADD_CONTROL_OFF(BaseProcedure):

    class OutArgs(NamedTuple):
        o_rc: int
        o_err: str
        
    # noinspection PyMethodOverriding
    async def __call__(self, connection: Connection, i_ts: datetime, i_kit_id: int, i_tsmcc: datetime, check_rc: bool = False) -> tuple[OutArgs, ]:
        out_args,  = await super().__call__(connection, 'sp_event_imdm_add_control_off', i_ts, i_kit_id, i_tsmcc , check_rc=check_rc)
        return out_args, 


# noinspection PyPep8Naming
class SP_EVENT_IMDM_ADD_HACKING_DEVICE(BaseProcedure):

    class OutArgs(NamedTuple):
        o_rc: int
        o_err: str
        
    # noinspection PyMethodOverriding
    async def __call__(self, connection: Connection, i_ts: datetime, i_kit_id: int, i_tsmcc: datetime, check_rc: bool = False) -> tuple[OutArgs, ]:
        out_args,  = await super().__call__(connection, 'sp_event_imdm_add_hacking_device', i_ts, i_kit_id, i_tsmcc , check_rc=check_rc)
        return out_args, 


# noinspection PyPep8Naming
class SP_EVENT_IMDM_ADD_JSON(BaseProcedure):

    class OutArgs(NamedTuple):
        o_rc: int
        o_err: str
        
    # noinspection PyMethodOverriding
    async def __call__(self, connection: Connection, i_ts: datetime, i_mob_id: int, i_tsmobile: datetime, i_event: bytes, check_rc: bool = False) -> tuple[OutArgs, ]:
        out_args,  = await super().__call__(connection, 'sp_event_imdm_add_json', i_ts, i_mob_id, i_tsmobile, i_event , check_rc=check_rc)
        return out_args, 


# noinspection PyPep8Naming
class SP_EVENT_IMDM_ADD_LAST_ACK(BaseProcedure):

    class OutArgs(NamedTuple):
        o_rc: int
        o_err: str
        
    # noinspection PyMethodOverriding
    async def __call__(self, connection: Connection, i_mccid: int, i_pduid: int, i_ack: bytes, check_rc: bool = False) -> tuple[OutArgs, ]:
        out_args,  = await super().__call__(connection, 'sp_event_imdm_add_last_ack', i_mccid, i_pduid, i_ack , check_rc=check_rc)
        return out_args, 


# noinspection PyPep8Naming
class SP_EXT_DIR_USER_SYNC_IMDM_RULE_EXISTS(BaseProcedure):

    class OutArgs(NamedTuple):
        o_rc: int
        o_err: str
        o_rule_exists: int
        
    # noinspection PyMethodOverriding
    async def __call__(self, connection: Connection, check_rc: bool = False) -> tuple[OutArgs, ]:
        out_args,  = await super().__call__(connection, 'sp_ext_dir_user_sync_imdm_rule_exists',  check_rc=check_rc)
        return out_args, 


# noinspection PyPep8Naming
class SP_FILE_TO_SEND_IMDM_GET(BaseProcedure):

    class OutArgs(NamedTuple):
        o_rc: int
        o_err: str
        o_file_oid: str
        o_file_name: str
        
    # noinspection PyMethodOverriding
    async def __call__(self, connection: Connection, i_mcc_id: int, i_task_id: int, i_md5: str, check_rc: bool = False) -> tuple[OutArgs, ]:
        out_args,  = await super().__call__(connection, 'sp_file_to_send_imdm_get', i_mcc_id, i_task_id, i_md5 , check_rc=check_rc)
        return out_args, 


# noinspection PyPep8Naming
class SP_GPS_IMDM_ADD_FOR_KIT(BaseProcedure):

    class OutArgs(NamedTuple):
        o_rc: int
        o_err: str
        
    # noinspection PyMethodOverriding
    async def __call__(self, connection: Connection, i_mccid: int, i_tsmcc: datetime, i_latitude: str, i_longitude: str, i_source: str, i_event: str, check_rc: bool = False) -> tuple[OutArgs, ]:
        out_args,  = await super().__call__(connection, 'sp_gps_imdm_add_for_kit', i_mccid, i_tsmcc, i_latitude, i_longitude, i_source, i_event , check_rc=check_rc)
        return out_args, 


# noinspection PyPep8Naming
class SP_INST_SCHEMA_ALL_GET_LAST_VER(BaseProcedure):

    class OutArgs(NamedTuple):
        o_rc: int
        o_err: str
        o_version: str
        o_ts: datetime
        
    # noinspection PyMethodOverriding
    async def __call__(self, connection: Connection, check_rc: bool = False) -> tuple[OutArgs, ]:
        out_args,  = await super().__call__(connection, 'sp_inst_schema_all_get_last_ver',  check_rc=check_rc)
        return out_args, 


# noinspection PyPep8Naming
class SP_KIT_IMDM_ADD_BY_EMP(BaseProcedure):

    class OutArgs(NamedTuple):
        o_rc: int
        o_err: str
        o_mcc_id: int
        
    # noinspection PyMethodOverriding
    async def __call__(self, connection: Connection, i_emp_id: int, i_model: str, i_mob_udid: str, i_ser_no: str, i_os: str, i_ownership: str, check_rc: bool = False) -> tuple[OutArgs, ]:
        out_args,  = await super().__call__(connection, 'sp_kit_imdm_add_by_emp', i_emp_id, i_model, i_mob_udid, i_ser_no, i_os, i_ownership , check_rc=check_rc)
        return out_args, 


# noinspection PyPep8Naming
class SP_KIT_IMDM_ADD_WITH_OS(BaseProcedure):

    class OutArgs(NamedTuple):
        o_rc: int
        o_err: str
        o_mcc_id: int
        
    # noinspection PyMethodOverriding
    async def __call__(self, connection: Connection, i_emp_id: int, i_ost_platform: str, i_os_version: str, check_rc: bool = False) -> tuple[OutArgs, ]:
        out_args,  = await super().__call__(connection, 'sp_kit_imdm_add_with_os', i_emp_id, i_ost_platform, i_os_version , check_rc=check_rc)
        return out_args, 


# noinspection PyPep8Naming
class SP_KIT_IMDM_CHECKIN_URL_DELETE(BaseProcedure):

    class OutArgs(NamedTuple):
        o_rc: int
        o_err: str
        
    # noinspection PyMethodOverriding
    async def __call__(self, connection: Connection, i_mob_id: int, check_rc: bool = False) -> tuple[OutArgs, ]:
        out_args,  = await super().__call__(connection, 'sp_kit_imdm_checkin_url_delete', i_mob_id , check_rc=check_rc)
        return out_args, 


# noinspection PyPep8Naming
class SP_KIT_IMDM_CHECKIN_URL_GET(BaseProcedure):

    class OutArgs(NamedTuple):
        o_rc: int
        o_err: str
        o_checkin_url: str
        
    # noinspection PyMethodOverriding
    async def __call__(self, connection: Connection, i_mob_id: int, check_rc: bool = False) -> tuple[OutArgs, ]:
        out_args,  = await super().__call__(connection, 'sp_kit_imdm_checkin_url_get', i_mob_id , check_rc=check_rc)
        return out_args, 


# noinspection PyPep8Naming
class SP_KIT_IMDM_CHECKIN_URL_SET(BaseProcedure):

    class OutArgs(NamedTuple):
        o_rc: int
        o_err: str
        
    # noinspection PyMethodOverriding
    async def __call__(self, connection: Connection, i_mob_id: int, i_checkin_url: str, check_rc: bool = False) -> tuple[OutArgs, ]:
        out_args,  = await super().__call__(connection, 'sp_kit_imdm_checkin_url_set', i_mob_id, i_checkin_url , check_rc=check_rc)
        return out_args, 


# noinspection PyPep8Naming
class SP_KIT_IMDM_FIND_BY_IMEI(BaseProcedure):

    class OutArgs(NamedTuple):
        o_rc: int
        o_err: str
        o_rs: str
        
    class MobileRS(NamedTuple):
        kit: Any
        kit_status_block: dict
        
    # noinspection PyMethodOverriding
    async def __call__(self, connection: Connection, i_mob_imei: str, check_rc: bool = False) -> tuple[OutArgs, list[MobileRS]]:
        out_args, mobile_rs = await super().__call__(connection, 'sp_kit_imdm_find_by_imei', i_mob_imei , check_rc=check_rc)
        return out_args, mobile_rs


# noinspection PyPep8Naming
class SP_KIT_IMDM_FIND_BY_JSON(BaseProcedure):

    class OutArgs(NamedTuple):
        o_rc: int
        o_err: str
        o_rs: str
        
    class MobileRS(NamedTuple):
        kit: Any
        kit_status_block: dict
        
    # noinspection PyMethodOverriding
    async def __call__(self, connection: Connection, i_json_from_kit: str, check_rc: bool = False) -> tuple[OutArgs, list[MobileRS]]:
        out_args, mobile_rs = await super().__call__(connection, 'sp_kit_imdm_find_by_json', i_json_from_kit , check_rc=check_rc)
        return out_args, mobile_rs


# noinspection PyPep8Naming
class SP_KIT_IMDM_FIND_BY_UDID_FOR_IOS(BaseProcedure):

    class OutArgs(NamedTuple):
        o_rc: int
        o_err: str
        o_rs: str
        
    class KitShortObjRS(NamedTuple):
        mob_id: int
        mob_udid: Any
        mob_imei: Any
        mob_ownership: str
        mob_st_uncontrol: str
        mob_st_connect: str
        mob_os_id: int
        os_version: str
        os_ost_id: int
        
    # noinspection PyMethodOverriding
    async def __call__(self, connection: Connection, i_mob_udid: str, check_rc: bool = False) -> tuple[OutArgs, list[KitShortObjRS]]:
        out_args, kit_short_obj_rs = await super().__call__(connection, 'sp_kit_imdm_find_by_udid_for_ios', i_mob_udid , check_rc=check_rc)
        return out_args, kit_short_obj_rs


# noinspection PyPep8Naming
class SP_KIT_IMDM_FIND_METADATA(BaseProcedure):

    class OutArgs(NamedTuple):
        o_rc: int
        o_err: str
        o_rs: str
        
    class MobileRS(NamedTuple):
        kit: Any
        
    # noinspection PyMethodOverriding
    async def __call__(self, connection: Connection, i_mob_id: int, check_rc: bool = False) -> tuple[OutArgs, list[MobileRS]]:
        out_args, mobile_rs = await super().__call__(connection, 'sp_kit_imdm_find_metadata', i_mob_id , check_rc=check_rc)
        return out_args, mobile_rs


# noinspection PyPep8Naming
class SP_KIT_IMDM_GET(BaseProcedure):

    class OutArgs(NamedTuple):
        o_rc: int
        o_err: str
        o_rs: str
        
    class MobileRS(NamedTuple):
        kit: Any
        
    # noinspection PyMethodOverriding
    async def __call__(self, connection: Connection, i_kit_id: int, check_rc: bool = False) -> tuple[OutArgs, list[MobileRS]]:
        out_args, mobile_rs = await super().__call__(connection, 'sp_kit_imdm_get', i_kit_id , check_rc=check_rc)
        return out_args, mobile_rs


# noinspection PyPep8Naming
class SP_KIT_IMDM_GET_NEXT_COMMAND_FOR_IOS(BaseProcedure):

    class OutArgs(NamedTuple):
        o_rc: int
        o_err: str
        o_rs: str
        
    class CommandRS(NamedTuple):
        command: str
        identifier: str
        
    # noinspection PyMethodOverriding
    async def __call__(self, connection: Connection, i_mob_id: int, check_rc: bool = False) -> tuple[OutArgs, list[CommandRS]]:
        out_args, command_rs = await super().__call__(connection, 'sp_kit_imdm_get_next_command_for_ios', i_mob_id , check_rc=check_rc)
        return out_args, command_rs


# noinspection PyPep8Naming
class SP_KIT_IMDM_GET_SETTINGS(BaseProcedure):

    class OutArgs(NamedTuple):
        o_rc: int
        o_err: str
        o_ams_code: str
        
    # noinspection PyMethodOverriding
    async def __call__(self, connection: Connection, i_kit_id: int, check_rc: bool = False) -> tuple[OutArgs, ]:
        out_args,  = await super().__call__(connection, 'sp_kit_imdm_get_settings', i_kit_id , check_rc=check_rc)
        return out_args, 


# noinspection PyPep8Naming
class SP_KIT_IMDM_IS_SUPERVISED(BaseProcedure):

    class OutArgs(NamedTuple):
        o_rc: int
        o_err: str
        o_supervised: int
        
    # noinspection PyMethodOverriding
    async def __call__(self, connection: Connection, i_mob_id: int, check_rc: bool = False) -> tuple[OutArgs, ]:
        out_args,  = await super().__call__(connection, 'sp_kit_imdm_is_supervised', i_mob_id , check_rc=check_rc)
        return out_args, 


# noinspection PyPep8Naming
class SP_KIT_IMDM_NOT_NOW(BaseProcedure):

    class OutArgs(NamedTuple):
        o_rc: int
        o_err: str
        
    # noinspection PyMethodOverriding
    async def __call__(self, connection: Connection, i_mob_id: int, check_rc: bool = False) -> tuple[OutArgs, ]:
        out_args,  = await super().__call__(connection, 'sp_kit_imdm_not_now', i_mob_id , check_rc=check_rc)
        return out_args, 


# noinspection PyPep8Naming
class SP_KIT_IMDM_SET_OWNERSHIP(BaseProcedure):

    class OutArgs(NamedTuple):
        o_rc: int
        o_err: str
        
    # noinspection PyMethodOverriding
    async def __call__(self, connection: Connection, i_mob_id: int, i_ownership: str, check_rc: bool = False) -> tuple[OutArgs, ]:
        out_args,  = await super().__call__(connection, 'sp_kit_imdm_set_ownership', i_mob_id, i_ownership , check_rc=check_rc)
        return out_args, 


# noinspection PyPep8Naming
class SP_KIT_IMDM_STATUS_CONTROL_OFF(BaseProcedure):

    class OutArgs(NamedTuple):
        o_rc: int
        o_err: str
        
    # noinspection PyMethodOverriding
    async def __call__(self, connection: Connection, i_kit_id: int, i_status_f: str, check_rc: bool = False) -> tuple[OutArgs, ]:
        out_args,  = await super().__call__(connection, 'sp_kit_imdm_status_control_off', i_kit_id, i_status_f , check_rc=check_rc)
        return out_args, 


# noinspection PyPep8Naming
class SP_KIT_SRV_EVENT_ADD_CONTAINER(BaseProcedure):

    class OutArgs(NamedTuple):
        o_rc: int
        o_err: str
        
    # noinspection PyMethodOverriding
    async def __call__(self, connection: Connection, i_srv_ts: datetime, i_mob_id: int, i_mob_ts: datetime, i_container_type: str, check_rc: bool = False) -> tuple[OutArgs, ]:
        out_args,  = await super().__call__(connection, 'sp_kit_srv_event_add_container', i_srv_ts, i_mob_id, i_mob_ts, i_container_type , check_rc=check_rc)
        return out_args, 


# noinspection PyPep8Naming
class SP_KIT_SRV_EVENT_DEL_CONTAINER(BaseProcedure):

    class OutArgs(NamedTuple):
        o_rc: int
        o_err: str
        
    # noinspection PyMethodOverriding
    async def __call__(self, connection: Connection, i_srv_ts: datetime, i_mob_id: int, i_mob_ts: datetime, check_rc: bool = False) -> tuple[OutArgs, ]:
        out_args,  = await super().__call__(connection, 'sp_kit_srv_event_del_container', i_srv_ts, i_mob_id, i_mob_ts , check_rc=check_rc)
        return out_args, 


# noinspection PyPep8Naming
class SP_LICENSE_IMDM_GET(BaseProcedure):

    class OutArgs(NamedTuple):
        o_rc: int
        o_err: str
        o_rs: str
        
    class LicRS(NamedTuple):
        license: Any
        
    # noinspection PyMethodOverriding
    async def __call__(self, connection: Connection, check_rc: bool = False) -> tuple[OutArgs, list[LicRS]]:
        out_args, lic_rs = await super().__call__(connection, 'sp_license_imdm_get',  check_rc=check_rc)
        return out_args, lic_rs


# noinspection PyPep8Naming
class SP_LICENSE_IMDM_GET_ACTIVE_KIT_COUNT(BaseProcedure):

    class OutArgs(NamedTuple):
        o_rc: int
        o_err: str
        o_kit_count: int
        
    # noinspection PyMethodOverriding
    async def __call__(self, connection: Connection, check_rc: bool = False) -> tuple[OutArgs, ]:
        out_args,  = await super().__call__(connection, 'sp_license_imdm_get_active_kit_count',  check_rc=check_rc)
        return out_args, 


# noinspection PyPep8Naming
class SP_LOADER_IMDM_ACCESS(BaseProcedure):

    class OutArgs(NamedTuple):
        o_rc: int
        o_err: str
        
    # noinspection PyMethodOverriding
    async def __call__(self, connection: Connection, i_accesstoken: str, check_rc: bool = False) -> tuple[OutArgs, ]:
        out_args,  = await super().__call__(connection, 'sp_loader_imdm_access', i_accesstoken , check_rc=check_rc)
        return out_args, 


# noinspection PyPep8Naming
class SP_LOADER_IMDM_ADD_BY_CODE(BaseProcedure):

    class OutArgs(NamedTuple):
        o_rc: int
        o_err: str
        o_kit_id: int
        
    # noinspection PyMethodOverriding
    async def __call__(self, connection: Connection, i_accesstoken: str, i_model: str, i_mob_udid: str, i_ser_no: str, i_os: str, check_rc: bool = False) -> tuple[OutArgs, ]:
        out_args,  = await super().__call__(connection, 'sp_loader_imdm_add_by_code', i_accesstoken, i_model, i_mob_udid, i_ser_no, i_os , check_rc=check_rc)
        return out_args, 


# noinspection PyPep8Naming
class SP_LOADER_IMDM_ADD_CODE_4EMP_IOS_LDAP(BaseProcedure):

    class OutArgs(NamedTuple):
        o_rc: int
        o_err: str
        o_token: str
        
    # noinspection PyMethodOverriding
    async def __call__(self, connection: Connection, i_emp_id: int, check_rc: bool = False) -> tuple[OutArgs, ]:
        out_args,  = await super().__call__(connection, 'sp_loader_imdm_add_code_4emp_ios_ldap', i_emp_id , check_rc=check_rc)
        return out_args, 


# noinspection PyPep8Naming
class SP_LOADER_IMDM_ADD_KIT_WITH_OS(BaseProcedure):

    class OutArgs(NamedTuple):
        o_rc: int
        o_err: str
        o_kit_id: int
        
    # noinspection PyMethodOverriding
    async def __call__(self, connection: Connection, i_accesstoken: str, i_ost_platform: str, i_os_version: str, check_rc: bool = False) -> tuple[OutArgs, ]:
        out_args,  = await super().__call__(connection, 'sp_loader_imdm_add_kit_with_os', i_accesstoken, i_ost_platform, i_os_version , check_rc=check_rc)
        return out_args, 


# noinspection PyPep8Naming
class SP_LOADER_IMDM_DEACTIVATE_CODE(BaseProcedure):

    class OutArgs(NamedTuple):
        o_rc: int
        o_err: str
        
    # noinspection PyMethodOverriding
    async def __call__(self, connection: Connection, i_accesstoken: str, check_rc: bool = False) -> tuple[OutArgs, ]:
        out_args,  = await super().__call__(connection, 'sp_loader_imdm_deactivate_code', i_accesstoken , check_rc=check_rc)
        return out_args, 


# noinspection PyPep8Naming
class SP_LOADER_IMDM_FIND_KIT_BY_TOKEN(BaseProcedure):

    class OutArgs(NamedTuple):
        o_rc: int
        o_err: str
        o_mob_id: int
        
    # noinspection PyMethodOverriding
    async def __call__(self, connection: Connection, i_accesstoken: str, check_rc: bool = False) -> tuple[OutArgs, ]:
        out_args,  = await super().__call__(connection, 'sp_loader_imdm_find_kit_by_token', i_accesstoken , check_rc=check_rc)
        return out_args, 


# noinspection PyPep8Naming
class SP_LOADER_LDR_ACCESS(BaseProcedure):

    class OutArgs(NamedTuple):
        o_rc: int
        o_err: str
        
    # noinspection PyMethodOverriding
    async def __call__(self, connection: Connection, i_accesstoken: str, check_rc: bool = False) -> tuple[OutArgs, ]:
        out_args,  = await super().__call__(connection, 'sp_loader_ldr_access', i_accesstoken , check_rc=check_rc)
        return out_args, 


# noinspection PyPep8Naming
class SP_LOADER_LDR_AUTH(BaseProcedure):

    class OutArgs(NamedTuple):
        o_rc: int
        o_err: str
        o_accesstoken: str
        
    # noinspection PyMethodOverriding
    async def __call__(self, connection: Connection, i_code: str, i_deviceid: str, i_osname: str, i_osversion: str, check_rc: bool = False) -> tuple[OutArgs, ]:
        out_args,  = await super().__call__(connection, 'sp_loader_ldr_auth', i_code, i_deviceid, i_osname, i_osversion , check_rc=check_rc)
        return out_args, 


# noinspection PyPep8Naming
class SP_LOGIN_RESULT_IMDM_FAIL(BaseProcedure):

    class OutArgs(NamedTuple):
        o_rc: int
        o_err: str
        
    # noinspection PyMethodOverriding
    async def __call__(self, connection: Connection, i_lres_login: str, check_rc: bool = False) -> tuple[OutArgs, ]:
        out_args,  = await super().__call__(connection, 'sp_login_result_imdm_fail', i_lres_login , check_rc=check_rc)
        return out_args, 


# noinspection PyPep8Naming
class SP_LOGIN_RESULT_IMDM_GET(BaseProcedure):

    class OutArgs(NamedTuple):
        o_rc: int
        o_err: str
        o_rs: str
        
    class LresRS(NamedTuple):
        login_result: Any
        
    # noinspection PyMethodOverriding
    async def __call__(self, connection: Connection, i_lres_login: str, check_rc: bool = False) -> tuple[OutArgs, list[LresRS]]:
        out_args, lres_rs = await super().__call__(connection, 'sp_login_result_imdm_get', i_lres_login , check_rc=check_rc)
        return out_args, lres_rs


# noinspection PyPep8Naming
class SP_LOGIN_RESULT_IMDM_SUCCESS(BaseProcedure):

    class OutArgs(NamedTuple):
        o_rc: int
        o_err: str
        
    # noinspection PyMethodOverriding
    async def __call__(self, connection: Connection, i_lres_login: str, check_rc: bool = False) -> tuple[OutArgs, ]:
        out_args,  = await super().__call__(connection, 'sp_login_result_imdm_success', i_lres_login , check_rc=check_rc)
        return out_args, 


# noinspection PyPep8Naming
class SP_MOB_SCHEDULE_IMDM_SCHEDULE_DEVICE_INFO(BaseProcedure):

    class OutArgs(NamedTuple):
        o_rc: int
        o_err: str
        
    # noinspection PyMethodOverriding
    async def __call__(self, connection: Connection, i_mob_id: int, check_rc: bool = False) -> tuple[OutArgs, ]:
        out_args,  = await super().__call__(connection, 'sp_mob_schedule_imdm_schedule_device_info', i_mob_id , check_rc=check_rc)
        return out_args, 


# noinspection PyPep8Naming
class SP_MOB_SCHEDULE_IMDM_SCHEDULE_MANAGED_APP_LIST(BaseProcedure):

    class OutArgs(NamedTuple):
        o_rc: int
        o_err: str
        
    # noinspection PyMethodOverriding
    async def __call__(self, connection: Connection, i_mob_id: int, check_rc: bool = False) -> tuple[OutArgs, ]:
        out_args,  = await super().__call__(connection, 'sp_mob_schedule_imdm_schedule_managed_app_list', i_mob_id , check_rc=check_rc)
        return out_args, 


# noinspection PyPep8Naming
class SP_MOB_SCHEDULE_IMDM_SCHEDULE_PUSH(BaseProcedure):

    class OutArgs(NamedTuple):
        o_rc: int
        o_err: str
        
    # noinspection PyMethodOverriding
    async def __call__(self, connection: Connection, i_mob_id: int, check_rc: bool = False) -> tuple[OutArgs, ]:
        out_args,  = await super().__call__(connection, 'sp_mob_schedule_imdm_schedule_push', i_mob_id , check_rc=check_rc)
        return out_args, 


# noinspection PyPep8Naming
class SP_MONITOR_DB_UPD_ACTIVITY(BaseProcedure):

    class OutArgs(NamedTuple):
        o_rc: int
        o_err: str
        
    # noinspection PyMethodOverriding
    async def __call__(self, connection: Connection, i_ts: datetime, i_mobileid: int, i_is_online: str, check_rc: bool = False) -> tuple[OutArgs, ]:
        out_args,  = await super().__call__(connection, 'sp_monitor_db_upd_activity', i_ts, i_mobileid, i_is_online , check_rc=check_rc)
        return out_args, 


# noinspection PyPep8Naming
class SP_MONITOR_IMDM_EVENT_START(BaseProcedure):

    class OutArgs(NamedTuple):
        o_rc: int
        o_err: str
        
    # noinspection PyMethodOverriding
    async def __call__(self, connection: Connection, i_ts: datetime, i_mccid: int, i_ts_mcc: datetime, i_mon_ver: str, check_rc: bool = False) -> tuple[OutArgs, ]:
        out_args,  = await super().__call__(connection, 'sp_monitor_imdm_event_start', i_ts, i_mccid, i_ts_mcc, i_mon_ver , check_rc=check_rc)
        return out_args, 


# noinspection PyPep8Naming
class SP_MONITOR_IMDM_GET_CONTAINER_TOKEN(BaseProcedure):

    class OutArgs(NamedTuple):
        o_rc: int
        o_err: str
        o_token: str
        
    # noinspection PyMethodOverriding
    async def __call__(self, connection: Connection, i_kit_id: int, check_rc: bool = False) -> tuple[OutArgs, ]:
        out_args,  = await super().__call__(connection, 'sp_monitor_imdm_get_container_token', i_kit_id , check_rc=check_rc)
        return out_args, 


# noinspection PyPep8Naming
class SP_MONITOR_IMDM_GET_DEVICE_TOKEN(BaseProcedure):

    class OutArgs(NamedTuple):
        o_rc: int
        o_err: str
        o_token: str
        
    # noinspection PyMethodOverriding
    async def __call__(self, connection: Connection, i_kit_id: int, check_rc: bool = False) -> tuple[OutArgs, ]:
        out_args,  = await super().__call__(connection, 'sp_monitor_imdm_get_device_token', i_kit_id , check_rc=check_rc)
        return out_args, 


# noinspection PyPep8Naming
class SP_MONITOR_IMDM_GET_FOR_OS(BaseProcedure):

    class OutArgs(NamedTuple):
        o_rc: int
        o_err: str
        o_res: int
        
    # noinspection PyMethodOverriding
    async def __call__(self, connection: Connection, i_ost_platform: str, i_os_version: str, check_rc: bool = False) -> tuple[OutArgs, ]:
        out_args,  = await super().__call__(connection, 'sp_monitor_imdm_get_for_os', i_ost_platform, i_os_version , check_rc=check_rc)
        return out_args, 


# noinspection PyPep8Naming
class SP_MONITOR_IMDM_SET_MOB_PARAM(BaseProcedure):

    class OutArgs(NamedTuple):
        o_rc: int
        o_err: str
        
    # noinspection PyMethodOverriding
    async def __call__(self, connection: Connection, i_ts: datetime, i_mccid: int, i_ts_mcc: datetime, i_os: str, i_model: str, i_imei: str, i_udid: str, i_ser_no: str, check_rc: bool = False) -> tuple[OutArgs, ]:
        out_args,  = await super().__call__(connection, 'sp_monitor_imdm_set_mob_param', i_ts, i_mccid, i_ts_mcc, i_os, i_model, i_imei, i_udid, i_ser_no , check_rc=check_rc)
        return out_args, 


# noinspection PyPep8Naming
class SP_MONITOR_SRV_EVENT_STRT(BaseProcedure):

    class OutArgs(NamedTuple):
        o_rc: int
        o_err: str
        
    # noinspection PyMethodOverriding
    async def __call__(self, connection: Connection, i_ts: datetime, i_mccid: int, i_ts_mcc: datetime, i_os: str, i_model: str, i_mon_ver: str, i_imei: str, i_udid: str, i_imsi: str, i_iccid: str, i_pno: str, i_roaming: str, check_rc: bool = False) -> tuple[OutArgs, ]:
        out_args,  = await super().__call__(connection, 'sp_monitor_srv_event_strt', i_ts, i_mccid, i_ts_mcc, i_os, i_model, i_mon_ver, i_imei, i_udid, i_imsi, i_iccid, i_pno, i_roaming , check_rc=check_rc)
        return out_args, 


# noinspection PyPep8Naming
class SP_POLICY_IMDM_GET_SUBST_VAL_LIST(BaseProcedure):

    class OutArgs(NamedTuple):
        o_rc: int
        o_err: str
        o_rs: str
        
    class PolValListRS(NamedTuple):
        policy_subst_value: Any
        
    # noinspection PyMethodOverriding
    async def __call__(self, connection: Connection, i_mob_id: int, check_rc: bool = False) -> tuple[OutArgs, list[PolValListRS]]:
        out_args, pol_val_list_rs = await super().__call__(connection, 'sp_policy_imdm_get_subst_val_list', i_mob_id , check_rc=check_rc)
        return out_args, pol_val_list_rs


# noinspection PyPep8Naming
class SP_POLICY_SRV_EVENT_APPLY_ERROR(BaseProcedure):

    class OutArgs(NamedTuple):
        o_rc: int
        o_err: str
        
    # noinspection PyMethodOverriding
    async def __call__(self, connection: Connection, i_ts: datetime, i_mob_id: int, i_tsmobile: datetime, i_pt_internal_name: str, i_policy_name: str, i_policy_value: bytes, i_subst_version: int, i_err_code: int, i_error_msg: str, check_rc: bool = False) -> tuple[OutArgs, ]:
        out_args,  = await super().__call__(connection, 'sp_policy_srv_event_apply_error', i_ts, i_mob_id, i_tsmobile, i_pt_internal_name, i_policy_name, i_policy_value, i_subst_version, i_err_code, i_error_msg , check_rc=check_rc)
        return out_args, 


# noinspection PyPep8Naming
class SP_PROFILE_IMDM_GET(BaseProcedure):

    class OutArgs(NamedTuple):
        o_rc: int
        o_err: str
        o_prof_id: int
        o_prof_identifier: str
        o_ae_aek_id: int
        o_ae_checksum: str
        o_pt_internal_name: str
        o_prof_title: str
        o_prof_description: str
        o_rs: str
        
    class PolicyRS(NamedTuple):
        pol_id: int
        pol_name: str
        pol_pvt_id: str
        pv_value: dict
        pol_is_required: bool
        
    # noinspection PyMethodOverriding
    async def __call__(self, connection: Connection, i_prof_id: int, check_rc: bool = False) -> tuple[OutArgs, list[PolicyRS]]:
        out_args, policy_rs = await super().__call__(connection, 'sp_profile_imdm_get', i_prof_id , check_rc=check_rc)
        return out_args, policy_rs


# noinspection PyPep8Naming
class SP_PROFILE_IMDM_GET_CHECKED(BaseProcedure):

    class OutArgs(NamedTuple):
        o_rc: int
        o_err: str
        o_ae_aek_id: int
        o_ae_checksum: str
        o_pt_internal_name: str
        o_rs: str
        
    class PolicyRS(NamedTuple):
        pol_id: int
        pol_name: str
        pol_pvt_id: str
        pv_value: dict
        pol_is_required: bool
        
    # noinspection PyMethodOverriding
    async def __call__(self, connection: Connection, i_mob_id: int, i_prof_id: int, i_prof_version: int, check_rc: bool = False) -> tuple[OutArgs, list[PolicyRS]]:
        out_args, policy_rs = await super().__call__(connection, 'sp_profile_imdm_get_checked', i_mob_id, i_prof_id, i_prof_version , check_rc=check_rc)
        return out_args, policy_rs


# noinspection PyPep8Naming
class SP_PROFILE_IMDM_GET_IOS_MONITOR_PROFILE(BaseProcedure):

    class OutArgs(NamedTuple):
        o_rc: int
        o_err: str
        o_ae_aek_id: int
        o_ae_checksum: str
        o_subst_version: int
        o_ua_agrm_id: int
        o_ua_task_id: int
        o_rs_ws: str
        o_rs_uid: str
        o_rs_policies: str
        
    class WorkScheduleRS(NamedTuple):
        tcc_start: datetime
        tcc_end: datetime
        
    class UidsRS(NamedTuple):
        app_uid: str
        
    class PolicyRS(NamedTuple):
        pol_id: int
        pol_name: str
        pol_pvt_id: str
        pv_value: dict
        
    # noinspection PyMethodOverriding
    async def __call__(self, connection: Connection, i_mob_id: int, check_rc: bool = False) -> tuple[OutArgs, list[WorkScheduleRS], list[UidsRS], list[PolicyRS]]:
        out_args, work_schedule_rs, uids_rs, policy_rs = await super().__call__(connection, 'sp_profile_imdm_get_ios_monitor_profile', i_mob_id , check_rc=check_rc)
        return out_args, work_schedule_rs, uids_rs, policy_rs


# noinspection PyPep8Naming
class SP_PROFILE_IMDM_GET_SAFELIFE_PROFILE(BaseProcedure):

    class OutArgs(NamedTuple):
        o_rc: int
        o_err: str
        o_rs: str
        
    class PolicyRS(NamedTuple):
        pol_id: int
        pol_name: str
        pol_pvt_id: str
        pv_value: dict
        
    # noinspection PyMethodOverriding
    async def __call__(self, connection: Connection, i_kit_id: int, check_rc: bool = False) -> tuple[OutArgs, list[PolicyRS]]:
        out_args, policy_rs = await super().__call__(connection, 'sp_profile_imdm_get_safelife_profile', i_kit_id , check_rc=check_rc)
        return out_args, policy_rs


# noinspection PyPep8Naming
class SP_PROFILE_IMDM_REGISTER_INSTALL(BaseProcedure):

    class OutArgs(NamedTuple):
        o_rc: int
        o_err: str
        
    # noinspection PyMethodOverriding
    async def __call__(self, connection: Connection, i_mob_id: int, i_ae_aek_id: int, i_ae_checksum: str, i_subst_version: int, i_status: str, i_error_details: str, check_rc: bool = False) -> tuple[OutArgs, ]:
        out_args,  = await super().__call__(connection, 'sp_profile_imdm_register_install', i_mob_id, i_ae_aek_id, i_ae_checksum, i_subst_version, i_status, i_error_details , check_rc=check_rc)
        return out_args, 


# noinspection PyPep8Naming
class SP_PROFILE_IMDM_REGISTER_REMOVE(BaseProcedure):

    class OutArgs(NamedTuple):
        o_rc: int
        o_err: str
        
    # noinspection PyMethodOverriding
    async def __call__(self, connection: Connection, i_mob_id: int, i_ae_aek_id: int, check_rc: bool = False) -> tuple[OutArgs, ]:
        out_args,  = await super().__call__(connection, 'sp_profile_imdm_register_remove', i_mob_id, i_ae_aek_id , check_rc=check_rc)
        return out_args, 


# noinspection PyPep8Naming
class SP_PROFILE_SRV_EVENT_INST_ERR_CLIENT(BaseProcedure):

    class OutArgs(NamedTuple):
        o_rc: int
        o_err: str
        
    # noinspection PyMethodOverriding
    async def __call__(self, connection: Connection, i_ts: datetime, i_mob_id: int, i_tsmobile: datetime, i_profile_id: int, i_profile_version: int, i_subst_version: int, i_err_code: int, i_error_msg: str, check_rc: bool = False) -> tuple[OutArgs, ]:
        out_args,  = await super().__call__(connection, 'sp_profile_srv_event_inst_err_client', i_ts, i_mob_id, i_tsmobile, i_profile_id, i_profile_version, i_subst_version, i_err_code, i_error_msg , check_rc=check_rc)
        return out_args, 


# noinspection PyPep8Naming
class SP_PROFILE_SRV_EVENT_INST_ERR_SUBST(BaseProcedure):

    class OutArgs(NamedTuple):
        o_rc: int
        o_err: str
        
    # noinspection PyMethodOverriding
    async def __call__(self, connection: Connection, i_ts: datetime, i_mob_id: int, i_tsmobile: datetime, i_profile_id: int, i_profile_version: int, i_subst_version: int, i_sub_key: str, i_policy_name: str, i_policy_value: bytes, i_err_code: int, i_error_msg: str, check_rc: bool = False) -> tuple[OutArgs, ]:
        out_args,  = await super().__call__(connection, 'sp_profile_srv_event_inst_err_subst', i_ts, i_mob_id, i_tsmobile, i_profile_id, i_profile_version, i_subst_version, i_sub_key, i_policy_name, i_policy_value, i_err_code, i_error_msg , check_rc=check_rc)
        return out_args, 


# noinspection PyPep8Naming
class SP_PROFILE_SRV_EVENT_INST_ERR_SUBST_RESTR(BaseProcedure):

    class OutArgs(NamedTuple):
        o_rc: int
        o_err: str
        
    # noinspection PyMethodOverriding
    async def __call__(self, connection: Connection, i_ts: datetime, i_mob_id: int, i_tsmobile: datetime, i_profile_id: int, i_profile_version: int, i_policy_id: int, i_subst_version: int, i_policy_value: bytes, i_err_code: int, i_error_msg: str, check_rc: bool = False) -> tuple[OutArgs, ]:
        out_args,  = await super().__call__(connection, 'sp_profile_srv_event_inst_err_subst_restr', i_ts, i_mob_id, i_tsmobile, i_profile_id, i_profile_version, i_policy_id, i_subst_version, i_policy_value, i_err_code, i_error_msg , check_rc=check_rc)
        return out_args, 


# noinspection PyPep8Naming
class SP_PROFILE_SRV_EVENT_INST_OK(BaseProcedure):

    class OutArgs(NamedTuple):
        o_rc: int
        o_err: str
        
    # noinspection PyMethodOverriding
    async def __call__(self, connection: Connection, i_ts: datetime, i_mob_id: int, i_tsmobile: datetime, i_profile_id: int, i_profile_version: int, i_subst_version: int, check_rc: bool = False) -> tuple[OutArgs, ]:
        out_args,  = await super().__call__(connection, 'sp_profile_srv_event_inst_ok', i_ts, i_mob_id, i_tsmobile, i_profile_id, i_profile_version, i_subst_version , check_rc=check_rc)
        return out_args, 


# noinspection PyPep8Naming
class SP_PROFILE_SRV_EVENT_UNINST_ERR_CLIENT(BaseProcedure):

    class OutArgs(NamedTuple):
        o_rc: int
        o_err: str
        
    # noinspection PyMethodOverriding
    async def __call__(self, connection: Connection, i_ts: datetime, i_mob_id: int, i_tsmobile: datetime, i_profile_id: int, i_profile_version: int, i_subst_version: int, i_err_code: int, i_error_msg: str, check_rc: bool = False) -> tuple[OutArgs, ]:
        out_args,  = await super().__call__(connection, 'sp_profile_srv_event_uninst_err_client', i_ts, i_mob_id, i_tsmobile, i_profile_id, i_profile_version, i_subst_version, i_err_code, i_error_msg , check_rc=check_rc)
        return out_args, 


# noinspection PyPep8Naming
class SP_PROFILE_SRV_EVENT_UNINST_OK(BaseProcedure):

    class OutArgs(NamedTuple):
        o_rc: int
        o_err: str
        
    # noinspection PyMethodOverriding
    async def __call__(self, connection: Connection, i_ts: datetime, i_mob_id: int, i_tsmobile: datetime, i_profile_id: int, check_rc: bool = False) -> tuple[OutArgs, ]:
        out_args,  = await super().__call__(connection, 'sp_profile_srv_event_uninst_ok', i_ts, i_mob_id, i_tsmobile, i_profile_id , check_rc=check_rc)
        return out_args, 


# noinspection PyPep8Naming
class SP_PUSH_CLIENTS_IMDM_GET(BaseProcedure):

    class OutArgs(NamedTuple):
        o_rc: int
        o_err: str
        o_rs: str
        
    class PushClientsGetRS(NamedTuple):
        push_clients: Any
        
    # noinspection PyMethodOverriding
    async def __call__(self, connection: Connection, i_psrv_srv_type: str, i_psrv_name: str, i_kit_id: int, i_pcli_pkg_name: str, check_rc: bool = False) -> tuple[OutArgs, list[PushClientsGetRS]]:
        out_args, push_clients_get_rs = await super().__call__(connection, 'sp_push_clients_imdm_get', i_psrv_srv_type, i_psrv_name, i_kit_id, i_pcli_pkg_name , check_rc=check_rc)
        return out_args, push_clients_get_rs


# noinspection PyPep8Naming
class SP_PUSH_CLIENTS_IMDM_INVALID_TOKEN(BaseProcedure):

    class OutArgs(NamedTuple):
        o_rc: int
        o_err: str
        
    # noinspection PyMethodOverriding
    async def __call__(self, connection: Connection, i_psrv_srv_type: str, i_psrv_name: str, i_pkg_name: str, i_token: str, i_detail: str, check_rc: bool = False) -> tuple[OutArgs, ]:
        out_args,  = await super().__call__(connection, 'sp_push_clients_imdm_invalid_token', i_psrv_srv_type, i_psrv_name, i_pkg_name, i_token, i_detail , check_rc=check_rc)
        return out_args, 


# noinspection PyPep8Naming
class SP_PUSH_CLIENTS_IMDM_POLL(BaseProcedure):

    class OutArgs(NamedTuple):
        o_rc: int
        o_err: str
        o_rs: str
        
    class PushClientsListTaskRS(NamedTuple):
        pcli_id: int
        pcli_kit_id: int
        pcli_token: str
        pcli_data: dict
        
    # noinspection PyMethodOverriding
    async def __call__(self, connection: Connection, i_psrv_srv_type: str, i_psrv_name: str, i_pkg_name: str, i_rows_limit: int, check_rc: bool = False) -> tuple[OutArgs, list[PushClientsListTaskRS]]:
        out_args, push_clients_list_task_rs = await super().__call__(connection, 'sp_push_clients_imdm_poll', i_psrv_srv_type, i_psrv_name, i_pkg_name, i_rows_limit , check_rc=check_rc)
        return out_args, push_clients_list_task_rs


# noinspection PyPep8Naming
class SP_PUSH_CLIENTS_IMDM_SET(BaseProcedure):

    class OutArgs(NamedTuple):
        o_rc: int
        o_err: str
        
    # noinspection PyMethodOverriding
    async def __call__(self, connection: Connection, i_psrv_srv_type: str, i_psrv_name: str, i_kit_id: int, i_pcli_pkg_name: str, i_pcli_token: str, i_pcli_data: bytes, check_rc: bool = False) -> tuple[OutArgs, ]:
        out_args,  = await super().__call__(connection, 'sp_push_clients_imdm_set', i_psrv_srv_type, i_psrv_name, i_kit_id, i_pcli_pkg_name, i_pcli_token, i_pcli_data , check_rc=check_rc)
        return out_args, 


# noinspection PyPep8Naming
class SP_SCEP_SETTINGS_IMDM_AUTHENTICATION(BaseProcedure):

    class OutArgs(NamedTuple):
        o_rc: int
        o_err: str
        o_ss_key_size: int
        o_ss_subject_name: str
        o_ss_poll_attempts: int
        o_ss_polling_interval: int
        o_cd_title: str
        o_challenge: str
        o_scep_connection_url: str
        o_ss_encoding_type: str
        o_subject_alternative_name: str
        o_rs: str
        
    class ScepSettingsCertsRS(NamedTuple):
        cert_file_format: str
        cert_password: str
        cert_file: dict
        
    # noinspection PyMethodOverriding
    async def __call__(self, connection: Connection, i_mob_id: int, check_rc: bool = False) -> tuple[OutArgs, list[ScepSettingsCertsRS]]:
        out_args, scep_settings_certs_rs = await super().__call__(connection, 'sp_scep_settings_imdm_authentication', i_mob_id , check_rc=check_rc)
        return out_args, scep_settings_certs_rs


# noinspection PyPep8Naming
class SP_SCEP_SETTINGS_IMDM_AUTHENTICATION_BY_TOKEN(BaseProcedure):

    class OutArgs(NamedTuple):
        o_rc: int
        o_err: str
        o_ss_key_size: int
        o_ss_subject_name: str
        o_ss_poll_attempts: int
        o_ss_polling_interval: int
        o_cd_title: str
        o_challenge: str
        o_scep_connection_url: str
        o_ss_encoding_type: str
        o_subject_alternative_name: str
        o_rs: str
        
    class ScepSettingsCertsRS(NamedTuple):
        cert_file_format: str
        cert_password: str
        cert_file: dict
        
    # noinspection PyMethodOverriding
    async def __call__(self, connection: Connection, i_accesstoken: str, check_rc: bool = False) -> tuple[OutArgs, list[ScepSettingsCertsRS]]:
        out_args, scep_settings_certs_rs = await super().__call__(connection, 'sp_scep_settings_imdm_authentication_by_token', i_accesstoken , check_rc=check_rc)
        return out_args, scep_settings_certs_rs


# noinspection PyPep8Naming
class SP_SCEP_SETTINGS_IMDM_PREPARE(BaseProcedure):

    class OutArgs(NamedTuple):
        o_rc: int
        o_err: str
        o_ss_key_size: int
        o_ss_subject_name: str
        o_ss_poll_attempts: int
        o_ss_polling_interval: int
        o_cd_title: str
        o_challenge: str
        o_scep_connection_url: str
        o_ss_encoding_type: str
        o_subject_alternative_name: str
        o_rs: str
        
    class ScepSettingsCertsRS(NamedTuple):
        cert_file_format: str
        cert_password: str
        cert_file: dict
        
    # noinspection PyMethodOverriding
    async def __call__(self, connection: Connection, i_mob_id: int, i_prof_id: int, i_policy_id: int, check_rc: bool = False) -> tuple[OutArgs, list[ScepSettingsCertsRS]]:
        out_args, scep_settings_certs_rs = await super().__call__(connection, 'sp_scep_settings_imdm_prepare', i_mob_id, i_prof_id, i_policy_id , check_rc=check_rc)
        return out_args, scep_settings_certs_rs


# noinspection PyPep8Naming
class SP_SERVER_CONNECTION_IMDM_GET_CERTIFICATE(BaseProcedure):

    class OutArgs(NamedTuple):
        o_rc: int
        o_err: str
        o_rs: str
        
    class CertificateRS(NamedTuple):
        cert: Any
        
    # noinspection PyMethodOverriding
    async def __call__(self, connection: Connection, i_sc_server_type: str, check_rc: bool = False) -> tuple[OutArgs, list[CertificateRS]]:
        out_args, certificate_rs = await super().__call__(connection, 'sp_server_connection_imdm_get_certificate', i_sc_server_type , check_rc=check_rc)
        return out_args, certificate_rs


# noinspection PyPep8Naming
class SP_SERVER_CONNECTION_IMDM_GET_SERVER_CERT_LIST(BaseProcedure):

    class OutArgs(NamedTuple):
        o_rc: int
        o_err: str
        o_address: str
        o_rs: str
        
    class CertRS(NamedTuple):
        cert: Any
        
    # noinspection PyMethodOverriding
    async def __call__(self, connection: Connection, i_sc_id: int, check_rc: bool = False) -> tuple[OutArgs, list[CertRS]]:
        out_args, cert_rs = await super().__call__(connection, 'sp_server_connection_imdm_get_server_cert_list', i_sc_id , check_rc=check_rc)
        return out_args, cert_rs


# noinspection PyPep8Naming
class SP_SERVER_CONNECTION_IMDM_GET_SERVER_CONNECTION(BaseProcedure):

    class OutArgs(NamedTuple):
        o_rc: int
        o_err: str
        o_rs: str
        
    class ServerConnectionRS(NamedTuple):
        server_connection: Any
        
    # noinspection PyMethodOverriding
    async def __call__(self, connection: Connection, i_sc_server_type: str, check_rc: bool = False) -> tuple[OutArgs, list[ServerConnectionRS]]:
        out_args, server_connection_rs = await super().__call__(connection, 'sp_server_connection_imdm_get_server_connection', i_sc_server_type , check_rc=check_rc)
        return out_args, server_connection_rs


# noinspection PyPep8Naming
class SP_SERVER_LOG_IMDM_ADD(BaseProcedure):

    class OutArgs(NamedTuple):
        o_rc: int
        o_err: str
        
    # noinspection PyMethodOverriding
    async def __call__(self, connection: Connection, i_srvl_record: str, i_sc_id: int, check_rc: bool = False) -> tuple[OutArgs, ]:
        out_args,  = await super().__call__(connection, 'sp_server_log_imdm_add', i_srvl_record, i_sc_id , check_rc=check_rc)
        return out_args, 


# noinspection PyPep8Naming
class SP_SIM_IMDM_EVENT_CHANGE(BaseProcedure):

    class OutArgs(NamedTuple):
        o_rc: int
        o_err: str
        
    # noinspection PyMethodOverriding
    async def __call__(self, connection: Connection, i_ts: datetime, i_mcc: int, i_tsmcc: datetime, i_newimsi: str, i_newiccid: str, i_oldimsi: str, i_oldiccid: str, check_rc: bool = False) -> tuple[OutArgs, ]:
        out_args,  = await super().__call__(connection, 'sp_sim_imdm_event_change', i_ts, i_mcc, i_tsmcc, i_newimsi, i_newiccid, i_oldimsi, i_oldiccid , check_rc=check_rc)
        return out_args, 


# noinspection PyPep8Naming
class SP_SIM_IMDM_GET_SIM_KIT(BaseProcedure):

    class OutArgs(NamedTuple):
        o_rc: int
        o_err: str
        o_rs: str
        
    class SimRS(NamedTuple):
        sim: Any
        
    # noinspection PyMethodOverriding
    async def __call__(self, connection: Connection, i_kit_id: int, check_rc: bool = False) -> tuple[OutArgs, list[SimRS]]:
        out_args, sim_rs = await super().__call__(connection, 'sp_sim_imdm_get_sim_kit', i_kit_id , check_rc=check_rc)
        return out_args, sim_rs


# noinspection PyPep8Naming
class SP_SIM_IMDM_LIST_CORP_KIT(BaseProcedure):

    class OutArgs(NamedTuple):
        o_rc: int
        o_err: str
        o_rs: str
        
    class SimRS(NamedTuple):
        sim: Any
        
    # noinspection PyMethodOverriding
    async def __call__(self, connection: Connection, check_rc: bool = False) -> tuple[OutArgs, list[SimRS]]:
        out_args, sim_rs = await super().__call__(connection, 'sp_sim_imdm_list_corp_kit',  check_rc=check_rc)
        return out_args, sim_rs


# noinspection PyPep8Naming
class SP_SIM_SRV_EVENT_CHANGE(BaseProcedure):

    class OutArgs(NamedTuple):
        o_rc: int
        o_err: str
        
    # noinspection PyMethodOverriding
    async def __call__(self, connection: Connection, i_ts: datetime, i_mcc: int, i_tsmcc: datetime, i_newimsi: str, i_newiccid: str, i_oldimsi: str, i_oldiccid: str, check_rc: bool = False) -> tuple[OutArgs, ]:
        out_args,  = await super().__call__(connection, 'sp_sim_srv_event_change', i_ts, i_mcc, i_tsmcc, i_newimsi, i_newiccid, i_oldimsi, i_oldiccid , check_rc=check_rc)
        return out_args, 


# noinspection PyPep8Naming
class SP_TASK_IMDM_GET_TASK(BaseProcedure):

    class OutArgs(NamedTuple):
        o_rc: int
        o_err: str
        o_rs: str
        
    class TaskRS(NamedTuple):
        task: Any
        
    # noinspection PyMethodOverriding
    async def __call__(self, connection: Connection, i_task_id: int, check_rc: bool = False) -> tuple[OutArgs, list[TaskRS]]:
        out_args, task_rs = await super().__call__(connection, 'sp_task_imdm_get_task', i_task_id , check_rc=check_rc)
        return out_args, task_rs


# noinspection PyPep8Naming
class SP_TASK_IMDM_GET_TASK_BY_KIT_ID(BaseProcedure):

    class OutArgs(NamedTuple):
        o_rc: int
        o_err: str
        o_rs: str
        
    class TaskRS(NamedTuple):
        task: Any
        
    # noinspection PyMethodOverriding
    async def __call__(self, connection: Connection, i_kit_id: int, check_rc: bool = False) -> tuple[OutArgs, list[TaskRS]]:
        out_args, task_rs = await super().__call__(connection, 'sp_task_imdm_get_task_by_kit_id', i_kit_id , check_rc=check_rc)
        return out_args, task_rs


# noinspection PyPep8Naming
class SP_TASK_IMDM_GET_TASK_LIST_BY_KIT_ID(BaseProcedure):

    class OutArgs(NamedTuple):
        o_rc: int
        o_err: str
        o_rs: str
        
    class TaskWithAliasRS(NamedTuple):
        task_id: int
        task_cmd_code: float
        cmd_alias: str
        
    # noinspection PyMethodOverriding
    async def __call__(self, connection: Connection, i_kit_id: int, i_limit: int, check_rc: bool = False) -> tuple[OutArgs, list[TaskWithAliasRS]]:
        out_args, task_with_alias_rs = await super().__call__(connection, 'sp_task_imdm_get_task_list_by_kit_id', i_kit_id, i_limit , check_rc=check_rc)
        return out_args, task_with_alias_rs


# noinspection PyPep8Naming
class SP_TASK_IMDM_UPD_ERROR_WITH_DETAILS(BaseProcedure):

    class OutArgs(NamedTuple):
        o_rc: int
        o_err: str
        
    # noinspection PyMethodOverriding
    async def __call__(self, connection: Connection, i_ts: datetime, i_mobileid: int, i_tsmobile: datetime, i_taskid: int, i_mcc_result: int, i_details: str, check_rc: bool = False) -> tuple[OutArgs, ]:
        out_args,  = await super().__call__(connection, 'sp_task_imdm_upd_error_with_details', i_ts, i_mobileid, i_tsmobile, i_taskid, i_mcc_result, i_details , check_rc=check_rc)
        return out_args, 


# noinspection PyPep8Naming
class SP_TASK_IMDM_UPD_RES(BaseProcedure):

    class OutArgs(NamedTuple):
        o_rc: int
        o_err: str
        
    # noinspection PyMethodOverriding
    async def __call__(self, connection: Connection, i_ts: datetime, i_mobileid: int, i_tsmobile: datetime, i_taskid: int, i_mcc_result: int, check_rc: bool = False) -> tuple[OutArgs, ]:
        out_args,  = await super().__call__(connection, 'sp_task_imdm_upd_res', i_ts, i_mobileid, i_tsmobile, i_taskid, i_mcc_result , check_rc=check_rc)
        return out_args, 


# noinspection PyPep8Naming
class SP_USER_AGREEMENT_IMDM_EVENT_CONFIRM(BaseProcedure):

    class OutArgs(NamedTuple):
        o_rc: int
        o_err: str
        
    # noinspection PyMethodOverriding
    async def __call__(self, connection: Connection, i_ts: datetime, i_mob_id: int, i_mob_ts: datetime, i_confirm_status: int, i_license_id: int, check_rc: bool = False) -> tuple[OutArgs, ]:
        out_args,  = await super().__call__(connection, 'sp_user_agreement_imdm_event_confirm', i_ts, i_mob_id, i_mob_ts, i_confirm_status, i_license_id , check_rc=check_rc)
        return out_args, 


# noinspection PyPep8Naming
class SP_USER_AGREEMENT_IMDM_GET(BaseProcedure):

    class OutArgs(NamedTuple):
        o_rc: int
        o_err: str
        o_rs: str
        
    class UserAgreementRS(NamedTuple):
        user_agreement: Any
        
    # noinspection PyMethodOverriding
    async def __call__(self, connection: Connection, i_agreement_id: int, check_rc: bool = False) -> tuple[OutArgs, list[UserAgreementRS]]:
        out_args, user_agreement_rs = await super().__call__(connection, 'sp_user_agreement_imdm_get', i_agreement_id , check_rc=check_rc)
        return out_args, user_agreement_rs


# noinspection PyPep8Naming
class SP_USER_AGREEMENT_IMDM_GET_LAST(BaseProcedure):

    class OutArgs(NamedTuple):
        o_rc: int
        o_err: str
        o_rs: str
        
    class UserAgreementRS(NamedTuple):
        user_agreement: Any
        
    # noinspection PyMethodOverriding
    async def __call__(self, connection: Connection, check_rc: bool = False) -> tuple[OutArgs, list[UserAgreementRS]]:
        out_args, user_agreement_rs = await super().__call__(connection, 'sp_user_agreement_imdm_get_last',  check_rc=check_rc)
        return out_args, user_agreement_rs


# noinspection PyPep8Naming
class SP_USER_AGREEMENT_SRV_EVENT_CONFIRM(BaseProcedure):

    class OutArgs(NamedTuple):
        o_rc: int
        o_err: str
        
    # noinspection PyMethodOverriding
    async def __call__(self, connection: Connection, i_ts: datetime, i_mob_id: int, i_mob_ts: datetime, i_confirm_status: int, i_license_id: int, check_rc: bool = False) -> tuple[OutArgs, ]:
        out_args,  = await super().__call__(connection, 'sp_user_agreement_srv_event_confirm', i_ts, i_mob_id, i_mob_ts, i_confirm_status, i_license_id , check_rc=check_rc)
        return out_args, 


# noinspection PyPep8Naming
class SP_WS_IMDM_LIST_FOR_KIT(BaseProcedure):

    class OutArgs(NamedTuple):
        o_rc: int
        o_err: str
        o_rs: str
        
    class WsRS(NamedTuple):
        ws: Any
        
    # noinspection PyMethodOverriding
    async def __call__(self, connection: Connection, i_mcc_id: int, check_rc: bool = False) -> tuple[OutArgs, list[WsRS]]:
        out_args, ws_rs = await super().__call__(connection, 'sp_ws_imdm_list_for_kit', i_mcc_id , check_rc=check_rc)
        return out_args, ws_rs


