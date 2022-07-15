value=int(input(""))
year=int(value/365)
Remain_days=value%365
month=int(Remain_days/30)
Remain_days2=Remain_days%30
print(f"{year} ano(s)")
print(f"{month} mes(es)")
print(f"{Remain_days2} dia(s)")