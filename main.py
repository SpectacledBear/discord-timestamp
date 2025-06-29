"""Discord timestamp script

To convert an ISO datetime string to a Discord timestamp.

Usage: python ./main "1970-01-01T00:00:00"

You can specify a timezone by adding the timezone offset. For example,
"1970-01-01T00:00:00-00:00"
"""

import sys
from datetime import datetime, timezone


def get_datetime_arg():
    """Parses argument and gives a hint if the argument is not present.

    Returns:
        The commandline argument.

    Raises:
        IndexError: If argument is not present.
    """
    try:
        arg = sys.argv[1]

        return arg
    except IndexError:
        print("Error: No ISO date was provided as an argument.")
        return None


def get_iso_datetime(iso_datetime_str):
    """Get ISO datetime from a datetime argument.

    Args:
        iso_datetime_str: The commandline argument, which is expected to be an ISO datetime string.

    Returns:
        A datetime variable. None if the argument is not a datetime value.

    Raises:
        ValueError: The iso_datetime_str is not a valid datetime string.
    """
    # From https://stackoverflow.com/a/61569783
    try:
        parsed_datetime = datetime.fromisoformat(
            iso_datetime_str.replace("Z", "+00:00")
        )

        if parsed_datetime.tzinfo is None:
            parsed_datetime = parsed_datetime.astimezone(
                timezone.utc
            )  # local time preserved
            # parsed_datetime = parsed_datetime.replace(tzinfo=timezone.utc)  # converted to UTC

        return parsed_datetime
    except ValueError:
        print("Error: Could not format datetime correctly.")
        return None


def convert_datetime_to_discord_datetime(base_datetime):
    """Displays Discord timestamps for the given datetime variable.

    Args:
        base_datetime: A datetime variable based on the commandline ISO datetime argument.
    """
    epoch_time = int(base_datetime.timestamp())

    print(f"Long Date/Time: {base_datetime.strftime("%A, %B %d, %Y at %I:%M %p")}")
    print(f"<t:{epoch_time}:F>")
    print(f"Short Date/Time: {base_datetime.strftime("%B %d, %Y at %I:%M %p")}")
    print(f"<t:{epoch_time}:f>")
    print(f"Long Date: {base_datetime.strftime("%B %d, %Y")}")
    print(f"<t:{epoch_time}:D>")
    print(f"Short Date: {base_datetime.strftime("%m/%d/%y")}")
    print(f"<t:{epoch_time}:d>")
    print(f"Long Time: {base_datetime.strftime("%I:%M:%S %p")}")
    print(f"<t:{epoch_time}:T>")
    print(f"Short Time: {base_datetime.strftime("%I:%M %p")}")
    print(f"<t:{epoch_time}:t>")
    print('Relative Time: (for example: "in 7 days")')
    print(f"<t:{epoch_time}:R>")


if __name__ == "__main__":
    datetime_arg = get_datetime_arg()

    if datetime_arg is not None:
        iso_datetime = get_iso_datetime(datetime_arg)

        if iso_datetime is not None:
            convert_datetime_to_discord_datetime(iso_datetime)
        else:
            print("Error: No ISO date found, so not proceeding.")
