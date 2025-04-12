from datetime import datetime

def get_days_from_today(date):
    try:
        date = datetime.strptime(date.replace("-", "."), "%Y.%m.%d")
    except ValueError:
        print("Invalid date formate!")
    else:
        today = datetime.today()
        return (today - date).days
        
print(get_days_from_today("2024-11-03")) 