#Q1

def find_owner(phone_number):
    phone_book = {
         "0555502754": "Abdulaziz",
    "0555515532": "Marwan",
    "0544460063": "Ali",
    "0543625757": "Faisal",
    "0566999480": "Rayan",
    "0560001235": "Ahmed",
    "0543588937": "Naif"
    }
    
    if not phone_number.isdigit() or len(phone_number) != 10:
        return "This is an invalid number."
    
    owner = phone_book.get(phone_number)
    
    if owner:
        return owner
    else:
        return "Sorry, the number is not found."


while True:
    phone_number = input("Enter the phone number (or 'e' to exit): ")
    
    if phone_number.lower() == "e":
        break
    
    owner_name = find_owner(phone_number)
    print(owner_name)

#Q2
    
def rearrange_zeros(numbers):
    non_zeros = [num for num in numbers if num != 0]
    zeros = [num for num in numbers if num == 0]
    return non_zeros + zeros

numbers = [5, 0, 34, 9, 0, 13, 8]
arranged_list = rearrange_zeros(numbers)
print(arranged_list)