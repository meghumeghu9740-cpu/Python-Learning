#example of if-else-elif
time=int(input("enter time:"))
if time==8:
    print("it's breakfast time.")
elif time==13:
    print("it's lunch time.")
elif time==15:
    print("it's dinner time.")
else:
    print("it's not meal time.")

#another example of if-else-elif
gender=input("enter gender:")
age=int(input("enter age:"))
if gender=="female":
    print("ticket is free")
else:
    if age<5:
      print("ticket is free")
    elif age<12:
      print("you get child discount")
    elif age>60:
        print("you get senior citizen discount")
    else:
        print("you pay full amt")



