from datetime import datetime

date1 = datetime(2024, 2, 1, 12, 0, 0)
date2 = datetime(2024, 2, 9, 15, 30, 0)

difference_in_seconds = abs((date2 - date1).total_seconds())

print("Difference in seconds:", difference_in_seconds)