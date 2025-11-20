from datetime import datetime, timedelta

def add_days_to_date(start_time:datetime,end_time:datetime):
    total=timedelta()
    current_time=start_time

    while current_time < end_time:
        midnight = datetime(current_time.year, current_time.month, current_time.day,0,0,0)
        next_midnight = midnight + timedelta(hours=6)
        day_end = datetime(current_time.year,current_time.month,current_time.day,23,59,59)

        start=max(current_time,next_midnight)
        end=min(end_time,day_end)

        if start < end:
            total += (end - start)

        current_time = midnight + timedelta(days=1)

    return total

formate = "%Y-%m-%d %H:%M"

start_input = input("Enter start time (YYYY-MM-DD HH:MM): ")
end_input = input("Enter end time (YYYY-MM-DD HH:MM): ")

start_time=datetime.strptime(start_input,formate)
end_time=datetime.strptime(end_input, formate)

active_duration = add_days_to_date(start_time, end_time)

print("Active duration excluding night (12AM to 6Am):", active_duration)





