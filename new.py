#1
number = input("Enter the phone number: ")
phone_book = {
    "0568323222": "Amal",
    "0522222232": "Mohammed",
    "0532335983": "Khadijah",
    "0545341144": "Abdullah",
    "0545534556": "Rawan",
    "0560664566": "Faisal",
    "0567917077": "Layla"
}


if number in phone_book:
    print("owners:" , phone_book[number])
else:
    print("Sorry, the number is not found")

if not number.isdigit() or len(number) !=10:
 print("This is invalid number")

 if not number.isnumeric():
    print("This is invalid number")

#Q2

def rearrange_list(lst):
    non_zeros = [x for x in lst if x != 0]
    zeros = [x for x in lst if x == 0]
    return non_zeros + zeros

numbers =  [5, 0, 34, 9, 0, 13, 8]
arranged_numbers = rearrange_list(numbers)
print(arranged_numbers)