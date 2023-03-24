import json
import jsonschema

with open('ExpectedSchema.json', 'r') as f:
    ExpectedSchema=json.load(f)
with open('ActualJsonResponse.json','r') as f:
    ActualJsonResponse = json.load(f)
# Define the JSON schema you want to validate against
schema = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "age": {"type": "integer"}
    },
    "required": ["name", "age"]
}

# Parse the response JSON string into a Python object
response_json = '{"name": "John Doe", "age": 30}'
response_obj = json.loads(response_json)

# Validate the response object against the schema
jsonschema.validate(instance=ActualJsonResponse, schema=ExpectedSchema)
