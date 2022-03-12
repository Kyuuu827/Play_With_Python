import datetime as dt

# datetime
t1 = dt.datetime.now()
print(t1)
print(t1.strftime("%H시%M분%S초"))
print(t1.weekday()) # 요일 반환 (0:월, 1:화, 2:수, 3:목, 4:금, 5:토, 6:일)
print(t1.date())
print(t1.time())
print(t1)

# timedelta : 기간을 표현
t2 = dt.timedelta(days=5, hours=12, minutes=30)
print(t2)

# datetime & timedelta
today = dt.datetime.today()
diff_days = dt.timedelta(days=5)
print(today + diff_days)

#timezone : 시간대를 표현
KST = dt.timezone(dt.timedelta(hours=9))
korea = dt.datetime(2022, 1, 1, 0, 0, 0, tzinfo=KST)
print(korea)