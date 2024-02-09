import os
import yaml
from jsonschema import validate, exceptions


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def yaml_to_properties(data, prefix=""):
    """
    Converts a nested dictionary (YAML) to properties format.
    Returns a list of dictionaries with 'key' and 'value' fields.
    """
    props = []
    for key, value in data.items():
        # Use underscore as the separator for the properties instead of a period
        full_key = f"{prefix}{key}" if not prefix else f"{prefix}_{key}"
        if isinstance(value, dict):
            props.extend(yaml_to_properties(value, full_key))
        elif isinstance(value, list):
            for idx, item in enumerate(value):
                props.extend(yaml_to_properties(item, f"{full_key}_{idx}"))
        else:
            props.append({'key': full_key.replace("-", "_"), 'value': value})
    return props


def add_defaults(data, schema):
    """
    Recursively add default values from schema for missing fields in data.
    """
    if 'properties' in schema:
        for field, attributes in schema['properties'].items():
            # If the field is defined as an object in the schema but missing in data
            if 'properties' in attributes and not data.get(field):
                data[field] = {}

            # If field is missing in data
            if field not in data and 'default' in attributes:
                data[field] = attributes['default']

            # If field is present and has nested schema properties
            if isinstance(data.get(field), dict) and 'properties' in attributes:
                add_defaults(data[field], attributes)


def validate_yaml_against_schema(data, schema_path):
    """
    Validates the provided data against the schema at schema_path.
    If invalid, raises a ValidationError.
    """
    with open(schema_path, 'r') as f:
        schema = yaml.safe_load(f)

    add_defaults(data, schema)
    validate(instance=data, schema=schema)


def main():
    # Read paths from environment variables
    input_yaml_path = os.environ.get('INPUT_PATH')
    output_properties_path = os.environ.get('OUTPUT_PATH')
    schema_path = os.environ.get('SCHEMA_PATH')

    if not input_yaml_path or not output_properties_path or not schema_path:
        raise EnvironmentError("Ensure INPUT_PATH, OUTPUT_PATH, and SCHEMA_PATH environment variables are set")

    with open(input_yaml_path, 'r') as f:
        data = yaml.safe_load(f)

    validate_yaml_against_schema(data, schema_path)

    properties_list = yaml_to_properties(data)

    with open(output_properties_path, "w") as f:
        for prop in properties_list:
            f.write(f"echo \"{prop['key']}={prop['value']}\" >> $GITHUB_OUTPUT\n")
        f.write("#---------------------------------------------------------------\n")
        for prop in properties_list:
            f.write(f"echo \"{prop['key'].upper()}={prop['value']}\" >> $GITHUB_ENV\n")

    print(f"{bcolors.OKGREEN}✅YAML at {input_yaml_path} is valid against the schema {schema_path} {bcolors.ENDC}")
    print(f"{bcolors.OKGREEN}🗃️Properties file has been generated at {output_properties_path} {bcolors.ENDC}")


if __name__ == "__main__":
    main()
