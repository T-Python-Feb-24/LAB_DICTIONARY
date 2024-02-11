phoneBook:dict = {
    "0568323222" : "Amal" ,
    "0522222232" : "Mohammed" ,
    "0532335983" : "Khadijah" ,
    "0545341144" : "Abdullah" ,
    "0545534556" : "Rawan" ,
    "0560664566" : "Faisal" ,
    "0567917077" : "Layla"
}

#key:str = str(input("Enter the phone number: "))

def search(key:str)-> str:
    """this function take phone numbers and make sure that the numbers are correct."""
    if not str(key).isdigit or len(str(key)) != 10:
        print("The entered number is typed incorrectly.")
    elif key in phoneBook:
        print("The owner of the number is: ", phoneBook[key])
    else:
        print("Sorry, the number is not found.")
    
phoneNumber:str = str(input("Enter the phone number: "))
search(phoneNumber)

listOfNumbers = [5, 0, 34, 9, 0, 13, 8]
def rearrangement(numbers:list)-> list:
    zeros = [x for x in numbers if x == 0]
    notzeros = [x for x in numbers if x != 0]
    return notzeros + zeros

arrangedNumbers = rearrangement(listOfNumbers)
print(arrangedNumbers)