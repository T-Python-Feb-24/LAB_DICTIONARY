#number_phone ()
number_phone2 = {
"0568323222" :"amal" ,
"0522222232" :"mohamme"  ,
 "0532335983" :"khadijah" , 
 "0545341144" :"abbullah" ,
 "0545534556" : "rawab" ,
 "0560664566" : "faisal ",
  "0567917077" : "layla"
}
userPhone = input("write number")
if not userPhone.isdigit() or len (userPhone) !=10:
    print("sorry the number is invalid")
elif number_phone2.get(userPhone)== None:
    print('not found')
else:
    print('this phone number belong to: ',number_phone2.get(userPhone))
#Q2
a  =[5,0,34,9,13,8]
n = len (a)
j = 0 
for i in range(n):
    if a[i] != 0:
        a[j], a[i] =a[i] ,a [j]
        j += 1
print(a)