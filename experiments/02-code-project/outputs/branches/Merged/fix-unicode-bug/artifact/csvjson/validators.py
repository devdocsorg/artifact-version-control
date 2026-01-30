"""Input validation for csvjson — backward-compatibility shim.

Import from the new modules directly:
  - csvjson.schema_validators (validate_file_path, validate_csv_structure)
  - csvjson.type_validators (validate_output_format, validate_delimiter)
"""

from csvjson.schema_validators import validate_file_path, validate_csv_structure
from csvjson.type_validators import validate_output_format, validate_delimiter

SUPPORTED_FORMATS = ["json", "jsonl", "yaml"]

__all__ = [
    "validate_file_path",
    "validate_csv_structure",
    "validate_output_format",
    "validate_delimiter",
    "SUPPORTED_FORMATS",
]
