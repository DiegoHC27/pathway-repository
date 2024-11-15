"""
When you physically exercise to strengthen your heart, you
should maintain your heart rate within a range for at least 20
minutes. To find that range, subtract your age from 220. This
difference is your maximum heart rate per minute. Your heart
simply will not beat faster than this maximum (220 - age).
When exercising to strengthen your heart, you should keep your
heart rate between 65% and 85% of your heart’s maximum rate.
"""
age = int(input("Please enter your age: "))
max_hr_per_minute = (220-age)
av_min_hr = max_hr_per_minute*.65
av_max_hr = max_hr_per_minute*.85

print(f"When you exercise to strengthen your heart, you should keep your heart rate between {av_min_hr:.2f} and {av_max_hr:.2f} beats per minute.")