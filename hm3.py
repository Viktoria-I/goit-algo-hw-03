import datetime as dt
import random
import re
from datetime import datetime as dtdt
import datetime as dt

#First function

def get_days_from_today(date):
    
    enter_date = dt.datetime.strptime(date, '%Y-%m-%d')
    current_date = dt.datetime.today()
    difference = current_date - enter_date
    
    return difference.days


#Second function

def get_numbers_ticket(min, max, quantity):
    
    numbers = []

    if min < max and quantity <= (max - min + 1):

        while len(numbers) < quantity:
            number = random.randint(min, max)
            
            if number not in numbers:
                numbers.append(number)

    numbers.sort()

    return numbers


#Third function

def normalize_phone(phone_number):

    pattern = '[\d]'
    ph_num = re.findall(pattern, phone_number)
    ph_num = ''.join(ph_num)

    if ph_num[0] == '0':
        ph_num = '+38' + ph_num

    elif ph_num[0] == '8':
        ph_num = '+3' + ph_num

    elif ph_num[0] == '3':
        ph_num = '+' + ph_num

    return ph_num


#Fourth function
def get_upcoming_birthdays(users):

    current_year = dt.datetime.now().year

    for user in users:
        b_date_str = user["birthday"]
        month_day = b_date_str[5:]
        b_date = dt.datetime.strptime(f"{current_year}.{month_day}", "%Y.%m.%d").date()

        if b_date < dt.datetime.now().date():
            b_date = dt.datetime.strptime(f"{current_year + 1}.{month_day}", "%Y.%m.%d").date()

        if b_date.weekday() == 5:
            congratulation_date = b_date + dt.timedelta(days=2)
            del user["birthday"]
            user["congratulation_date"] = congratulation_date.strftime("%Y-%m-%d")

        elif b_date.weekday() == 6:
            congratulation_date = b_date + dt.timedelta(days=1)
            del user["birthday"]
            user["congratulation_date"] = congratulation_date.strftime("%Y-%m-%d")

        else:
            congratulation_date = b_date
            del user["birthday"]
            user["congratulation_date"] = congratulation_date.strftime("%Y-%m-%d")

    return users
