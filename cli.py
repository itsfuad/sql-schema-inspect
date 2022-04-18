#!/usr/bin/env python3
"""Command-line interface for sql-schema-inspect."""
import argparse
import json
import sys
from sql_schema_inspect import analyze

def main(argv=None):
    parser = argparse.ArgumentParser(description='Extract SQLite CREATE TABLE statements into a schema overview')
    parser.add_argument('path', help='Input data file, or - for standard input')
    parser.add_argument('--pretty', action='store_true', help='Indent JSON output')
    args = parser.parse_args(argv)
    if args.path == '-':
        data = sys.stdin.read()
    else:
        with open(args.path, encoding='utf-8') as f:
            data = f.read()
    print(json.dumps(analyze(data), sort_keys=True, indent=2 if args.pretty else None))
    return 0

if __name__ == '__main__':
    sys.exit(main())
