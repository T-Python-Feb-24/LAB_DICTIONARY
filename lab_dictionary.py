# Q1.
print("\n")
print("-------------------------- Phone Book Program --------------------------")

def number_isfound(phone_number):
    '''Check and print if the phone number is found in the phone book of not '''
    if phone_number in phone_book:
        print(f"The phone number is found.The owner is: {phone_book[phone_number]}.")
    else:    
        print("Sorry, the phone number is not found.")   
         
phone_book = {
    "0568323222":"Amal", 
    "0522222232":"Mohammed", 
    "0532335983":"Khadijah", 
    "0545341144":"Abdullah", 
    "0545534556":"Rawan", 
    "0560664566":"Fasial", 
    "0567917077":"Layla"
    }
# Start the phone book program
while True:
    input_number = input("Enter the phone number that you want to search about: ")
    if len(input_number) == 10 and input_number.isdigit():
        number_isfound(input_number)
        break
    else:
        print("This is invalid phone number,try again!\nNOTE: The phone number have to consist of ONLY 10 digits,letters and symbols are NOT allowed.")

# Q2.
print("\n")
print("-------------------------- Rerange List Program --------------------------")
def rerange_list(number_list):
    '''This function reranges the list to move the zeros to the end of the list'''
    temp_list = number_list [:]
    length_list = len(temp_list)
    for i in range(length_list):
        for j in range(0, length_list-i-1): 
            # Swap if and only if the current element equal 0 and the next element not equal 0  
            if temp_list[j] == 0 and temp_list[j+1] != 0:
                temp_list[j], temp_list[j+1] = temp_list[j+1], temp_list[j]
    return temp_list

# Start the rerange list program
unarranged_list = [5, 0, 34, 9, 0, 13, 8]
arranged_list = rerange_list(unarranged_list)

print(f"The unarranged list: {unarranged_list}")
print(f"The arranged list: {arranged_list}")