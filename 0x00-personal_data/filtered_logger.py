import re
from typing import List

def filter_datum(fields: List[str], redaction: str, message: str, separator: str) -> str:
    """Returns the log message obfuscated by replacing values of specified fields."""
    pattern = f"({'|'.join(fields)})=[^\\{separator}]+"
    return re.sub(pattern, lambda m: f"{m.group(1)}={redaction}", message)
