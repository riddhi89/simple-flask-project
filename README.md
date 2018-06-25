# simple-flask-project
Generate OpenAPI spec from Flask routes:

    
  	python generate_openapi_spec.py
    
View the OpenAPI spec using Swagger-UI:

    docker run --rm -p 9000:8080 --name swagger-ui -e SWAGGER_JSON=/api_docs/openapi.json -v $(PWD)/api_docs:/api_docs swaggerapi/swagger-ui
