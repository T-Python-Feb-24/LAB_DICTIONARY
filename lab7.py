# Q1:Build a phone book program that receives the phone number (Use Input to let the user provide the number), and returns the name of the owner.
my_dic={
    "0552733531":"Amal",
    "0522222232":"Mohammed",
    "0532335983":"Khadijah",
    "0545341144":"Abdullah",
    "0545534556":"Rawan",
    "0560664566":"Faisal",
    "0567917077":"Layla"
    }
# using input 
number=input("Enter the number: ")
'''
If the number exists, print the owner. Otherwise, print "Sorry, the number is not found".
If the number is less or more than 10 numbers, print "This is invalid number".
If the number contains letters or symbols, print "This is invalid number".
'''
if len(number) !=10 or not number.isdigit() :
    print("This is invalid number")

elif number in my_dic:
    print("The owner:",my_dic[number])
else:
        print("Sorry, the number is not found")

# Q2:Write a function that receives a list containing the following numbers :
# [5, 0, 34, 9, 0, 13, 8]
# rearranges the list so that the zeros are the end of the list, and finally returns the arranged list.

def list(my_List:list)->list:
    '''
    rearranges the list so that the zeros are the end of the list, and finally returns the arranged list.
    '''
    my_list.sort(key=lambda x:x==0)
    return my_List
    
my_list=[5, 0, 34, 9, 0, 13, 8]
arranges_list=list(my_list)
print(arranges_list)
