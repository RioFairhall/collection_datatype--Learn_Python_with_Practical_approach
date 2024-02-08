# '''Let's learn about Tuple in Python'''

#creating a List & trying to change its any item value
shopping_list= ["Milk", "Soap","Coffee Powder"]
print("Before changing value:", shopping_list)
shopping_list[1] = "Sugar"
print("After chaning soap to sugar:",shopping_list)


#doing same but in tuple
shopping_list_1= ("Bread", "Sugar")
try:
    shopping_list_1[1] = "Butter"
    print("After chaning soap to sugar:",shopping_list)
    
except:
   print("Tuple does not allowed to change the value") 
   
   

#But, why we use Tuple? -> if it does not allow to change item's value
print(type(("HELLO", "everyone!")))

person1 = ("Aadhaar_Number", 452100231111)
print(person1)

person2 = {
    "Name": "Pranay",
    "Mobile": "iPhone15_Pro_Max",
    "IMEI" : (8024512041, 8024512050)
}

# person2["IMEI"][8024512041] = 708045140
# print("Change Sucessfully")
# print(person2)
    
# trying to change IMEI value of Mobile which belongs to person2
try:
    person2["IMEI"][8024512041] = 708045140
    print("Change Sucessfully")
    print(person2)
except:
    print("You can not change Tuple value")
    