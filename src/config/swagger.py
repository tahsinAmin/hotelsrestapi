template = {
    "swagger": "2.0",
    "info": {
        "title": "Bookmarks API",
        "description": "API for hotels",
        "contact": {
            "responsibleOrganization": "W3 Engineers Ltd.",
            "responsibleDeveloper": "Muhammad Tahsin Amin",
            "email": "tahsin@w3engineers.com",
            "url": "https://github.com/tahsinAmin",
        },
        "termsOfService": "https://github.com/tahsinAmin/hotelsrestapi#readme",
        "version": "1.0"
    },
    "basePath": "/api/v1",  # base bash for blueprint registration
    "schemes": [
        "http",
        "https"
    ],
    "securityDefinitions": {
        "Bearer": {
            "type": "apiKey",
            "name": "Authorization",
            "in": "header",
            "description": "JWT Authorization header using the Bearer scheme. Example: \"Authorization: Bearer {token}\""
        }
    },
}

swagger_config = {
    "headers": [
    ],
    "specs": [
        {
            "endpoint": 'apispec',
            "route": '/apispec.json',
            "rule_filter": lambda rule: True,  # all in
            "model_filter": lambda tag: True,  # all in
        }
    ],
    "static_url_path": "/flasgger_static",
    "swagger_ui": True,
    "specs_route": "/"
}