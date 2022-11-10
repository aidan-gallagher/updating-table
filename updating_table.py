#!/usr/bin/env python3

import sys
import time
from typing import List, Tuple
from random import randrange
from tabulate import tabulate


def get_data() -> List[Tuple[str, int, float]]:
    """Stub function to return fake data"""
    return [("Data 1", randrange(100), randrange(100)),
            ("Data 2", randrange(100), randrange(100)),
            ("Data 3", randrange(100), randrange(100))]


while(True):
    try:
        # Get data and convert it to pretty tabular format
        data = get_data()
        formatted_table = tabulate(
            data,
            headers=["Column A", "Column B", "Column C"],
            tablefmt="github")

        print(formatted_table)

        # Move the cursor to the top of the table
        # Plus 2 to account for the header + header seperator lines.
        # Note if you choose a different tablefmt this value might have to change.
        length = len(data) + 2
        print(f"\u001b[{length}A", end='')

        time.sleep(1)

    except KeyboardInterrupt:
        # Catch ^C so it doesn't print traceback.
        # Move cursor back to the bottom of the terminal
        print(f"\u001b[{length}B", end='')
        sys.exit(0)
