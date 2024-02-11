def Mobiles_book (Usermobile):
    Mobiles:dict={"0568323222": "Amal" ,
              "0952222232": "Mohammed",
              "0567345673" :"Khalid",
              "0546777899":"Abdullah",
            "0543225678" :"Rawan" ,
              "05546774320": "Faisal",
              "05466873221":"Layla",
                }
    num = Mobiles.get(Usermobile)
    if num is not None:
              print(f"The owner is : {Mobiles.get(Usermobile)}")
    elif num is None:
         print("Sorry, the number is not found")
         
        
    while num is None:
          if Usermobile !=10 or not Usermobile.isdigit() :
               print("This is invalid number")
               break
          else:
                 print("Sorry, the number is not found")
                 break

Usermobile:str=str(input("Please enter mobile number : "))

#Q2
listOfnumbers=[5, 0, 34, 9, 0, 13, 8]

def Q ():
   listOfnumbers.sort(reverse=True)
   return listOfnumbers


print(Mobiles_book(Usermobile))
print(Q())