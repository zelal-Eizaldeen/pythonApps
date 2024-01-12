import calendar

print('أهلا وسهلا بك ')
year = int(input('الرجاء إدخال رقم للسنة: '))
month = int(input('الرجاء إدخال رقم للشهر: '))
print(calendar.month(year, month))
print('نتمني لك يوما سعيدا!')