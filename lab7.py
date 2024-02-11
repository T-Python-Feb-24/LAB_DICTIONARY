# Q1:Build a phone book program that receives the phone number (Use Input to let the user provide the number), and returns the name of the owner. 

phone_numbers = {
    "0568323222": "Amel",
    "0522222232": "Mohammed",
    "0532335983": "Khadijah",
    "0545341144": "Abdullah",
    "0545534556": "Rawan",
    "0560664566": "Faisal",
    "0567917077": "Layla"
}

# Prompt user for input
x = input("Enter The Phone Number: ")

#- If the number exists, print the owner. Otherwise, print "Sorry, the number is not found".
#- If the number is less or more than 10 numbers, print "This is invalid number".
#- If the number contains letters or symbols, print "This is invalid number".

if len(x) == 10 and x.isdigit():
    # Look for the number in the phone_numbers dictionary
    if x in phone_numbers:
        print("The owner:", phone_numbers[x])
    else:
        print("Sorry, the number is not found.")
else:
    # Input is invalid if it doesn't meet the length and digit-only criteria
    print("This is an invalid number.")

    
#Q2:Write a function that receives a list containing the following numbers : 
def move_zeros_to_end(lst):
    return sorted(lst, key=lambda x: x == 0)


numbers = [5, 0, 34, 9, 0, 13, 8]

arranged_list = move_zeros_to_end(numbers)
print(arranged_list)

