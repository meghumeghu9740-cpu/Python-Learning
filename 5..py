#Tuples
t1=(1,2,3,4,5)
t2=(6,7,8,9,10)
tuples=t1+t2
print("Tuples:",tuples)
#Sets
s1={11,52,3,4,5}  #it is unordered collection of unique elements
s2={4,5,6,7,8}
print("Example of unordered set:",s1)
print("union:",s1|s2)
print("intersection:",s1&s2)
print("difference:",s1-s2)
s1.pop()
print(s1)
