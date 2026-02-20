"""
data_utils.py - A collection of useful data utility functions.
"""

import json
import csv
import os
from datetime import datetime


def read_json(file_path: str) -> dict:
    """Read and parse a JSON file."""
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)


def write_json(data: dict, file_path: str, indent: int = 4) -> None:
    """Write data to a JSON file."""
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=indent)
    print(f"[✓] Data written to {file_path}")


def read_csv(file_path: str) -> list:
    """Read a CSV file and return a list of dictionaries."""
    rows = []
    with open(file_path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            rows.append(dict(row))
    return rows


def write_csv(data: list, file_path: str) -> None:
    """Write a list of dictionaries to a CSV file."""
    if not data:
        print("[!] No data to write.")
        return
    with open(file_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)
    print(f"[✓] Data written to {file_path}")


def flatten_dict(d: dict, parent_key: str = "", sep: str = ".") -> dict:
    """Flatten a nested dictionary."""
    items = {}
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.update(flatten_dict(v, new_key, sep=sep))
        else:
            items[new_key] = v
    return items


def chunk_list(lst: list, chunk_size: int) -> list:
    """Split a list into chunks of a given size."""
    return [lst[i:i + chunk_size] for i in range(0, len(lst), chunk_size)]


def remove_duplicates(lst: list) -> list:
    """Remove duplicates from a list while preserving order."""
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result


def get_timestamp(fmt: str = "%Y-%m-%d %H:%M:%S") -> str:
    """Return the current timestamp as a formatted string."""
    return datetime.now().strftime(fmt)


def file_info(file_path: str) -> dict:
    """Return basic information about a file."""
    if not os.path.exists(file_path):
        return {"error": f"File not found: {file_path}"}
    stat = os.stat(file_path)
    return {
        "name": os.path.basename(file_path),
        "size_bytes": stat.st_size,
        "created": datetime.fromtimestamp(stat.st_ctime).strftime("%Y-%m-%d %H:%M:%S"),
        "modified": datetime.fromtimestamp(stat.st_mtime).strftime("%Y-%m-%d %H:%M:%S"),
        "extension": os.path.splitext(file_path)[1],
    }


if __name__ == "__main__":
    # Example usage
    print("=== Data Utils Demo ===")

    # Timestamp
    print(f"Current Timestamp : {get_timestamp()}")

    # Flatten dict
    nested = {"user": {"name": "Alice", "address": {"city": "NYC", "zip": "10001"}}}
    flat = flatten_dict(nested)
    print(f"Flattened Dict    : {flat}")

    # Chunk list
    numbers = list(range(1, 11))
    chunks = chunk_list(numbers, 3)
    print(f"Chunked List      : {chunks}")

    # Remove duplicates
    dupes = [1, 2, 2, 3, 4, 4, 5]
    unique = remove_duplicates(dupes)
    print(f"Unique List       : {unique}")

    # File info
    info = file_info(__file__)
    print(f"File Info         : {info}")