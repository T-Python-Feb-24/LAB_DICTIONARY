# You can follow the table below:

# | Name    | Number      |
# | -------- | ---------- |
# | Amal     | 0568323222 |
# | Mohammed | 0522222232 |
# | Khadijah | 0532335983 |
# | Abdullah  | 0545341144 |
# | Rawan    | 0545534556 |
# | Faisal   | 0560664566 |
# | Layla    | 0567917077 |
# - If the number exists, print the owner. Otherwise, print "Sorry, the number is not found".
# - If the number is less or more than 10 numbers, print "This is invalid number".
# - If the number contains letters or symbols, print "This is invalid number".

# ## Q2:Write a function that receives a list containing the following numbers : 

phoneBook = { "0568323222": "Amal",
             "0522222232" :"Mohammed",
             "0532335983":"Khadijah",
             "0545341144":"Abdullah",
             "0545534556": "Rawan",
             "0560664566": "Faisal",
             "0567917077" :"Layla" 
             }

phoneInput = input("Enter the phone number")
if not phoneInput.isnumeric() or len(phoneInput)!= 10:
    print ("This is invalid number")
    
else : 
    found = False
    for number, name in phoneBook.items():
        if phoneInput == number : 
            print ('The phone number belongs to : ', name)
            found = True
    if found == False : 
        print("Sorry, the number is not found")

## Q2:Write a function that receives a list containing the following numbers : 
# - [5, 0, 34, 9, 0, 13, 8]
# - rearranges the list so that the zeros are the end of the list, and finally returns the arranged list.

input_list = [5, 0, 34, 9, 0, 13, 8]

def rearrange_zeros(lst):
    non_zeros = [num for num in lst if num != 0]
    zeros = [0] * (len(lst) - len(non_zeros))
    arranged_list = non_zeros + zeros
    return arranged_list

result = rearrange_zeros(input_list)
print(result)

