USER_DETAILS_SCHEMA = {
	"type": "object",
	"required": ["name", "email"],
	"properties": {
		"name": {"type": "string", "example": "John Doe"},
		"email": {"type": "string", "format": "email", "example": "john.doe@gmail.com"},
		"age": {"type": "integer", "example": "30"}
	}
}


USERS_LIST_SCHEMA = {
	"type": "object",
	"required": ["users"],
	"properties": {
		"users": {
			"type": "array",
			"items": USER_DETAILS_SCHEMA
		}
	}
}


USER_GET_SCHEMA = {
	"type": "object",
	"required": ["user"],
	"properties": {
		"user": USER_DETAILS_SCHEMA
	}
}
