# LAB_DICTIONARY


# Q1:Build a phone book program that receives the phone number 
# (Use Input to let the user provide the number), and returns the name 
# of the owner. 

phone_book = {
    "0568323222": "Amal",
    "0522222232": "Mohammed",
    "0532335983": "Khadijah",
    "0545341144": "Abdullah",
    "0545534556": "Rawan",
    "0560664566": "Faisal",
    "0567917077": "Layla"
}

number = input("Enter the phone number: ")

if len(number) != 10 or not number.isdigit():
    print("This is an invalid number.")
else:
    owner = phone_book.get(number)
    if owner:
        print("Owner:", owner)
    else:
        print("Sorry, the number is not found.")



#Q2:Write a function that receives a list containing the following numbers : 
# - [5, 0, 34, 9, 0, 13, 8]
# - rearranges the list so that the zeros are the end of the list, 
# and finally returns the arranged list.

def rearrange_list(lst):
    non_zeros = [x for x in lst if x != 0]
    zeros = [x for x in lst if x == 0]
    return non_zeros + zeros

numbers =  [5, 0, 34, 9, 0, 13, 8]
arranged_numbers = rearrange_list(numbers)
print(arranged_numbers)