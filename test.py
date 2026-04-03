from calendar_gen import month_calendar, format_month, weekday, easter, days_in_month
assert weekday(2026, 3, 29) == 6  # Sunday
cal = month_calendar(2026, 3)
assert cal[0][6] == 1  # March 2026 starts on Sunday
assert sum(1 for w in cal for d in w if d>0) == 31
text = format_month(2026, 3)
assert "March 2026" in text
assert days_in_month(2024, 2) == 29
e = easter(2026)
assert e == (2026, 4, 5)  # Easter 2026
e2 = easter(2024)
assert e2 == (2024, 3, 31)
print("calendar_gen tests passed")
