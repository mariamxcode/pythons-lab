
def temperature_conversion(value):
    temprature = ""
    for character in value:
        if character == "C" or character == "F":
            continue
        temprature+=character
        
        
    if "F" in value:
        celsius = (int(temprature)*(9/5)) + 32
        if celsius < 50:
            return "Cold Advisory"
        else:
            return "Heat Alert"
     
    else:
        fahrenheit = (int(temprature)-32) * (5/9)
        if fahrenheit< 50:
            return "Cold Advisory"
        else:
            return "Heat Alert"
       
 
print(temperature_conversion("50F"))
    
        
