"""Discord timestamp as a one-liner

Condenses the script in the main.py file into one line.

Usage: python ./one_liner.py "1970-01-01T00:00:00"
"""

import sys
from datetime import datetime

if __name__ == "__main__":
    print(f"<{int(datetime.fromisoformat(sys.argv[1]).timestamp())}:F>")
