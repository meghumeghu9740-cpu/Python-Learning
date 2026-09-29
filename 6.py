#Dictionary
Student_details={
    "Meghana G":"AI",
    "Lakshmi KB":"ECE",
    "Arpitha AC":"BCA"
}
print(Student_details)
Student_details["Paavana DG"]="MSC"
print("adding operation:",Student_details)
print("Keys:",Student_details.keys())
print("Values:",Student_details.values())
print("Items:",Student_details.items())
print("Meghana's details:",Student_details.get("Meghana G","Not found"))
print("Kavya's details:",Student_details.get("Kavya DK","Not found"))
print("Updating student details:")
Student_details["Paavana DG"]="BSC"
print(Student_details)
print(type(Student_details))