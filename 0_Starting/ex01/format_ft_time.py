import time

current_time = time.time()

timestamp = f"{current_time:,.4f}"
scientific_notation = f"{current_time:.2e}"

formatted_date = time.strftime("%b %d %Y", time.localtime(current_time))

print(f"Seconds since January 1, 1970: {timestamp} or {scientific_notation} in scientific notation")
print(formatted_date)
