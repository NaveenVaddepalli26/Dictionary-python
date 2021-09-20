# Python Program to Check if a Given Key Exists in a Dictionary or Not

dict = {"Name":"Naveen","age":23,"branch":"MSc","location":"Hyd"}
key = input("Enter a key:")
if key in dict.keys():
    print("The key is present and the value is:",dict[key])
else:
    print("Key is not present")
