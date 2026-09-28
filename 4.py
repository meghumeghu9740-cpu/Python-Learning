#lists
items=["phone","keyboard","mouse","bluetooth"]
print("Entered items:",items)
items.pop()
print("poped last item:",items)
items.pop(0)
print("poped first item:",items)
items.append("bluetooth")
print("add item:",items)
items.insert(0,"phone")
print("inserted item:",items)
Numbers=[100,400,200,700,300]
sorted_numbers=sorted(Numbers)
print("sorted numbers in acsending order:",sorted_numbers)
sorted_numbers.reverse()
print("sorted numbers in descending order:",sorted_numbers)
print("length of items:",len(items))
print("length of sorted_numbers:",len(sorted_numbers))
#slicing
print("slicing items and sorted_numbers:")
print(items[0:3])
print(sorted_numbers[-2])
print(sorted_numbers[0::2])

