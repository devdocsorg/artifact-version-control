"""Command-line interface for csvjson."""

import argparse
import sys

from csvjson.converter import convert_csv_to_json
from csvjson.validators import validate_file_path, validate_output_format
from csvjson.formatters import format_output


def create_parser():
    """Create the argument parser."""
    parser = argparse.ArgumentParser(
        prog="csvjson",
        description="Convert CSV files to JSON format.",
    )
    parser.add_argument(
        "input",
        help="Path to the input CSV file",
    )
    parser.add_argument(
        "-o", "--output",
        help="Path to the output file (default: stdout)",
        default=None,
    )
    parser.add_argument(
        "-f", "--format",
        help="Output format: json (default), jsonl",
        choices=["json", "jsonl"],
        default="json",
    )
    parser.add_argument(
        "--pretty",
        help="Pretty-print JSON output",
        action="store_true",
    )
    parser.add_argument(
        "--delimiter",
        help="CSV delimiter character (default: comma)",
        default=",",
    )
    return parser


def main(argv=None):
    """Main entry point."""
    parser = create_parser()
    args = parser.parse_args(argv)

    # Validate inputs
    errors = validate_file_path(args.input)
    if errors:
        for err in errors:
            print(f"Error: {err}", file=sys.stderr)
        return 1

    format_errors = validate_output_format(args.format)
    if format_errors:
        for err in format_errors:
            print(f"Error: {err}", file=sys.stderr)
        return 1

    # Convert
    try:
        records = convert_csv_to_json(args.input, delimiter=args.delimiter)
    except Exception as e:
        print(f"Error converting file: {e}", file=sys.stderr)
        return 1

    # Format output
    output_text = format_output(records, fmt=args.format, pretty=args.pretty)

    # Write output
    if args.output:
        with open(args.output, "w") as f:
            f.write(output_text)
        print(f"Written to {args.output}")
    else:
        print(output_text)

    return 0


if __name__ == "__main__":
    sys.exit(main())
