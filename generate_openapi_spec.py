import json
import os

from apispec import APISpec, utils
from apispec.ext.flask import flaskpath2swagger

from simple_flask_project.app import app
from simple_flask_project.schemas import GLOBAL_SCHEMA_MAP


spec = APISpec(
    title='Users API',
    version='1.0.0',
    plugins=('apispec.ext.flask',),
    openapi_version='3.0.0',
    security=[],
    components={}
)


for r in app.url_map.iter_rules():
    view = app.view_functions.get(r.endpoint)
    operations = utils.load_operations_from_docstring(view.__doc__)
    path = flaskpath2swagger(r.rule)

    if not operations:
        continue

    for verb in operations:
        resp = operations.get(verb).get('responses')
        for status in resp:
            val = resp.get(status)
            content = resp.get(status).get('schema')
            if content:
                # Check if mapping is present in global schema map
                if GLOBAL_SCHEMA_MAP.get(content):
                    val.update({
                        'content': {
                            'application/json': {
                                'schema': GLOBAL_SCHEMA_MAP[content]
                            }
                        }
                    })
                else:
                    print("Mapping missing for the schema = ", content)

                val.pop('schema')

    spec.add_path(path=path, operations=operations)

    if not os.path.exists('api_docs/'):
        os.makedirs('api_docs')

    with open('api_docs/openapi.json', 'w') as openapi_json_file:
        json.dump(spec.to_dict(), openapi_json_file, indent=4, sort_keys=True)
