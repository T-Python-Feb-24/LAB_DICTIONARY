phone_book={"0568323222":"Amal","0522222232":"Mohamed","0532335983":"Khadigah",
           "0545341144":"Abdullah"," 0545534556":"Rawan","0560664566":"Faisal","0567917077":"Layla"}
phone_number=input("Enter ur number phone:")

if phone_number in phone_book:
    print("owners:" , phone_book[phone_number])
else:
    print("Sorry, the number is not found")

if not phone_number.isdigit() or len(phone_number) !=10:
 print("This is invalid number")

 if not phone_number.isnumeric():
    print("This is invalid number")
  


 #  Q2:Write a function that receives a list containing the following numbers : 
def list_zero(lst):
  non_zero= [num for num in lst if num !=0]
  zero =[num for num in lst if num ==0] 
  return non_zero + zero
list= [5, 0, 34, 9, 0, 13, 8]
arranged = list_zero(list)
print(arranged)

#or another solution Q2:
list= [5, 0, 34, 9, 0, 13, 8]
list.sort(reverse=-1)
print(list)


         

     

