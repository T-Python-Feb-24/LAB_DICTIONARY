contacats={ "0568323222":"Amal",
"0522222232": "Mohammed",
"0532335983":"Khadijah" ,
"0545341144":"Abdullah",
"0545534556":"Rawan",
"0560664566":"Faisal",
"0567917077":"Layla"}
number=input("Enter the phone number:")
if len (number) !=10:
    print( "This is invalid number")
elif not number.isdigit():
    print("This is invalid number")
elif number in contacats:
        print("Owner:", contacats[number])
else:
    print("Sorry, the number is not found")
def rearrange_list(numbers):
    zeros = []
    others = []
    for num in numbers:
        if num == 0:
            zeros.append(num)
        else:
            others.append(num)
    return others + zeros

number_list = [5, 0, 34, 9, 0, 13, 8]
result = rearrange_list(number_list)
print(result)