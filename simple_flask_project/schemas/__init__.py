from simple_flask_project.schemas import user_schema


GLOBAL_SCHEMA_MAP = {
	'list_all_users': user_schema.USERS_LIST_SCHEMA,
	'get_user_details': user_schema.USER_GET_SCHEMA
}
