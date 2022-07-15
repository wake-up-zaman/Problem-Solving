Seconds=int(input(""))
Hours=int(Seconds/3600)
Remaining_Seconds1=Seconds-Hours*3600
Minutes=int(Remaining_Seconds1/60)
Remaining_Seconds2=Remaining_Seconds1-Minutes*60
print(f'{Hours}:{Minutes}:{Remaining_Seconds2}')