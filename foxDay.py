import pandas as pd 
from matplotlib import pyplot as plt

def monthPlinko(month):
   if month == 'January':
      return 1
   elif month == 'February':
      return 2
   elif month == 'March':
      return 3
   elif month == 'April':
      return 4
   elif month == 'May':
      return 5
   elif month == 'June':
      return 6
   
def reverseMonthPlinko(month):
   if month == 1:
      return 'January'
   elif month == 2:
      return 'February'
   elif month == 3:
      return 'March'
   elif month == 4:
      return 'April'
   elif month == 5:
      return 'May'
   elif month == 6:
      return 'June'
   
def weekdayPlinko(weekday):
   if weekday == 'Monday':
      return 1
   elif weekday == 'Tuesday':
      return 2
   elif weekday == 'Wednesday':
      return 3
   elif weekday == 'Thursday':
      return 4
   elif weekday == 'Friday':
      return 5
   
def reverseWeekdayPlinko(weekday):
   if weekday == 1:
      return 'Monday'
   elif weekday == 2:
      return 'Tuesday'
   elif weekday == 3:
      return 'Wednesday'
   elif weekday == 4:
      return 'Thursday'
   elif weekday == 5:
      return 'Friday'

def main():
  df = pd.read_excel('FoxyDayPredictor/foxDays.xlsx', engine='openpyxl')
  fox = df.values.tolist()
  foxDay = {}
  weekday = 0
  month = 0
  date = 0
  counter = 0

  #turn the list into a dictionary, categorized by year
  for day in fox:
      year = day[0]
      day2 = day[1].replace(",","")
      foxDay[year] = day2.split()

  for year in foxDay:
     x = weekdayPlinko(foxDay[year][0])
    # print(isinstance(x, NoneType))
     if x is None:
      continue
     weekday = weekday + x
     
     y = monthPlinko(foxDay[year][1])
    # print(isinstance(x, NoneType))
     if y is None:
      continue
     month = month + y

     y = monthPlinko(foxDay[year][1])
    # print(isinstance(x, NoneType))
     if y is None:
      continue
     date = date + int(foxDay[year][2])

     counter += 1
  weekday = int(weekday / counter) - 1
  month = int(month / counter)
  date = int(date / counter)
  weekdate2 = reverseWeekdayPlinko(weekday)
  month2 = reverseMonthPlinko(month)
  print("Fox Day 2025 will be on ", weekdate2, ", ", month2, " ", date)

  
main()