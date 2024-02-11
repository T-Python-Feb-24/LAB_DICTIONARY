
#number_phone ()
number_phone2 = {
"amal" :"0568323222" ,
"mohammeg" :"0522222232"  ,
 "khadijah" :"0532335983" , 
 "abbullah" :"0545341144" ,
 "rawab" : "0545534556" ,
 "faisal" : "0560664566 ",
  "layla" : "0567917077"
 } 
number_phone2 = input("write number")
if not number_phone2.isdigit() or len (number_phone2) !=10:
    print("sorry the number is not found")
elif number_phone2 in number_phone2 :
    print ("this is invalid number")
else : number_phone2
print("this is invalid number")
#Q2
a  =[5,0,34,9,13,8]
n = len (a)
j = 0
for i in range(n):
    if a[i] != 0:
        a[j], a[i] =a[i] ,a [j]
        j += 1
print(a)