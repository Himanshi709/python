import datetime
year=int(input("enter your birth year = "))
month=int(input("enter your birth month = "))
date=int(input("enter your birth date = "))
birthdate=datetime.datetime(year,month,date)
current_date= datetime.datetime.now()
days_old= current_date - birthdate
print("you are {} days old".format(days_old))
