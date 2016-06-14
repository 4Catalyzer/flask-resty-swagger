"""This script makes some pretty strong assumptions on the structure of the
service:
  - there are `views` and `schemas` modules imported in the main module,
    containing respectively the views and the schemas of the app
"""

import json
import inspect
import sys

from apispec import APISpec
from flask_resty.view import ApiView
from marshmallow import Schema


def generate_specs(module_name):
    module = import_service_module(module_name)
    service_name = ''.split('.')[-1]

    ctx = module.app.test_request_context()
    ctx.push()
    spec = APISpec(
        title=service_name,
        version='1.0.0',
        plugins=('apispec.ext.marshmallow', 'flask_resty.spec'))

    schemas = get_subclasses(module.schemas, Schema)
    for schema in schemas:
        spec.definition(prettify_schema_name(schema), schema=schema)

    for view in get_subclasses(module.views, ApiView):
        try:
            spec.add_path(view=view, tag=True)
        except KeyError:
            pass  # means that the view is not registered. move along

    return json.dumps(spec.to_dict(), indent=2)


def import_service_module(module_name):
    sys.path.insert(0, '.')
    module = __import__(module_name, fromlist='*')
    return module


def prettify_schema_name(schema):
    name = schema.__name__
    return name[:-6] if name.lower()[-6:] == 'schema' else name


def get_subclasses(module, sup_cls):
    return [cls for name, cls in inspect.getmembers(module)
            if inspect.isclass(cls) and issubclass(cls, sup_cls)
            and inspect.getmodule(cls) == module]
