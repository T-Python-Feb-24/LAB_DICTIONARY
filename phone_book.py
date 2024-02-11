phone_book_dic ={
    "0568323222":"Amal",
    "0522222232":"Mohammed",
    "0532335983":"Khadijah",
    "0545341144":"Abdullah",
    "0545534556":"Rawan",
    "0560664566":"Faisal",
    "0567917077":"Layla"
}
#######################################

#######################################
#Entering the the number by the user 
InputNumber = input("enter the number -> ")
#######################################
#Check if the length of the number less or more than 10 and if it contine any symbol.
symbol = "~!@#$%^&*()_-+=}]{[|\;:\|<>.,/?`"
if len(InputNumber) != 10 or any(char in symbol for char in InputNumber):
    print("This is an invalid number.")
#######################################
#Serach if the number in the list.
else:
    if InputNumber in phone_book_dic:
        print(f" Here -> {phone_book_dic[InputNumber]}")
        
    else:
        print("Sorry, the number is not found")
        
######################################
print("-"*50)
######################################
def rearrange (zero_arrange):
    Notzero = [num for num in zero_arrange if num != 0]
    Azero = [num for num in zero_arrange if num == 0]
    return Notzero + Azero
number_list=[5, 0, 34, 9, 0, 13, 8] 
arranged_list = rearrange(number_list)
print(arranged_list)