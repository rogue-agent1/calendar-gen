#!/usr/bin/env python3
"""Calendar generator. Zero dependencies."""

def is_leap(y): return y%4==0 and (y%100!=0 or y%400==0)
def days_in_month(y, m):
    return [0,31,29 if is_leap(y) else 28,31,30,31,30,31,31,30,31,30,31][m]

def weekday(y, m, d):
    """Zeller's formula. 0=Mon, 6=Sun."""
    if m < 3: m += 12; y -= 1
    q = d; k = y%100; j = y//100
    h = (q + (13*(m+1))//5 + k + k//4 + j//4 - 2*j) % 7
    return (h + 5) % 7  # convert to Mon=0

def month_calendar(y, m):
    first = weekday(y, m, 1)
    days = days_in_month(y, m)
    weeks = []; week = [0]*first
    for d in range(1, days+1):
        week.append(d)
        if len(week) == 7: weeks.append(week); week = []
    if week: week.extend([0]*(7-len(week))); weeks.append(week)
    return weeks

def format_month(y, m):
    names = ["","January","February","March","April","May","June","July","August","September","October","November","December"]
    lines = [f"    {names[m]} {y}", "Mo Tu We Th Fr Sa Su"]
    for week in month_calendar(y, m):
        lines.append(" ".join(f"{d:2d}" if d else "  " for d in week))
    return "\n".join(lines)

def year_calendar(y):
    return "\n\n".join(format_month(y, m) for m in range(1, 13))

def easter(y):
    """Computus algorithm."""
    a=y%19; b=y//100; c=y%100; d=b//4; e=b%4
    f=(b+8)//25; g=(b-f+1)//3; h=(19*a+b-d-g+15)%30
    i=c//4; k=c%4; l=(32+2*e+2*i-h-k)%7
    m=(a+11*h+22*l)//451; month=(h+l-7*m+114)//31; day=(h+l-7*m+114)%31+1
    return y, month, day

if __name__ == "__main__":
    print(format_month(2026, 3))
