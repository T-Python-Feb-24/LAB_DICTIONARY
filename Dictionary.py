'''
Q1:Build a phone book program that receives the phone number (Use Input to let the user provide the number), 
and returns the name of the owner. You can follow the table below:
-----------------------
Name	Number
Amal	0568323222
Mohammed	0522222232
Khadijah	0532335983
Abdullah	0545341144
Rawan	0545534556
Faisal	0560664566
Layla	0567917077
------------------------
If the number exists, print the owner. Otherwise, print "Sorry, the number is not found".
If the number is less or more than 10 numbers, print "This is invalid number".
If the number contains letters or symbols, print "This is invalid number".
'''
def get_name(phone):
    phone_book = {
        "0568323222": "Amal",
        "0522222232": "Mohammed",
        "0532335983":  "Khadijah",
        "0545341144": "Abdullah",
        "0545534556": "Rawan",
        "0560664566": "Faisal",
        "0567917077": "Layla",
    }
    if not phone.isdigit() or len(phone) != 10:
        return "This is an invalid number"
    
    name = phone_book.get(phone)   
    if name != None:
        return name
    else:
        return "Sorry, the number is not found"

search = input("Enter the phone number: ")

result = get_name(search)
print("Name: ",result)

'''
Q2:Write a function that receives a list containing the following numbers : [5, 0, 34, 9, 0, 13, 8]
rearranges the list so that the zeros are the end of the list, and finally returns the arranged list.
'''
def rearranges_list(lst:list):
    result = []
    count = 0
    for i in lst:
        if i ==0:
            count += 1
        else:
            result.append(i)
    result += [0]* count
    return result

sort_num:list = [5, 0, 34, 9, 0, 13, 8]
print("Before: ",sort_num)
result = rearranges_list(sort_num)
print("After: ", result)