#while loop
is_failed=True
i=1
while is_failed:
    print(f"Attempt {i}")
    i+=1
    if i==10:
        break
#Example   
is_passed=True
j=2
while is_passed:
 if j%2!=0:
   j+=1
   continue
 print("display even number")
 print(f"attempt {j}")
 j+=1
 if j>10:
    break 

 

       
   

