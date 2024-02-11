# Q1:Build a phone book program that receives the phone number
# (Use Input to let the user provide the number), and returns the name of the owner.

person_info: dict = {
    "0568323222": "amal",
    "0568323222": "Amal",
    "0522222232": "Mohammed",
    "0532335983": "Khadijah",
    "0545341144": "Abdullah",
    "0545534556": "Rawan",
    "0560664566": "Faisal",
    "0567917077": "Layla",
}


def phone_book(phone_dict: dict) -> None:
    while True:
        phone: str = input(
            "enter phone number to see the ownar name of exist or (q) to skip:\n")
        if phone == "q":
            return None
        elif (not phone.isdigit() or len(phone) != 10):
            print("This is invalid number.please enter only numbers of 10 characters")

        else:
            print(f"The ownar of the phone \"{phone}\" is \
{person_info.get(phone, "Sorry, the number is not found")}")
            break

# function for Q2


def rearranges(nums: list) -> list:
    zeros: list = []
    new_list: list = []
    for num in nums:
        if num == 0:
            zeros.append(0)
        else:
            new_list.append(num)
    return new_list+zeros


# call for phone book function
phone_book(person_info)

# Q2:Write a function that receives a list containing the following numbers :
inputList: list[int] = [5, 0, 34, 9, 0, 13, 8]
print(rearranges(inputList))
