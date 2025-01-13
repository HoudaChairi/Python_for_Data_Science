
import time
"""
This script gets the current time and formats it in different ways:
- Seconds since January 1, 1970, with decimals and scientific notation.
- Current date in a readable format (e.g., "Jan 13 2025").
"""
current_time = time.time()

timestamp = f"{current_time:,.4f}"

scientific_notation = f"{current_time:.2e}"

formatted_date = time.strftime("%b %d %Y", time.localtime(current_time))

print(f"Seconds since January 1, 1970: {timestamp} or {scientific_notation}\
      in scientific notation")

print(formatted_date)
