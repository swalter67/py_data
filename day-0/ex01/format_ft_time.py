import time
from datetime import datetime

# Current date and time -> floating-point number
current_time = time.time()

# Specific date
current_date = datetime.fromtimestamp(current_time)

print(f"Seconds since January 1, 1970: {current_time:,.4f}\
      or {current_time:.2e} in scientific notation")
print(current_date.strftime("%b %d %Y"))
