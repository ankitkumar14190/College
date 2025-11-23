dict1={'StdNo.':532,'StuName':'Naveen','StuAge':21,'StuCity':'Hyderabad'}
print("\n Dictionary is:",dict1)
print("\n Student Name is:",dict1['StuName'])
print("\n Student City is:",dict1['StuCity'])
print("\n All keys in Dictionary")
for x in dict1:
    print(x)
print("\n All Values in Dictionary")
for x in dict1:
    print(dict1[x])
dict1["Phno."]=85457854
print("\n Updated Dictionary is:",dict1)
dict1["StuName"]="Madhu"
print("\n Updated Dictionary is:",dict1)
dict1.pop("StuAge")
print("\n Updated Dictionary is:",dict1)
print("Length of Dictionary is:",len(dict1))
dict2=dict1.copy()
