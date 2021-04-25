age = input("Are you a cigartte addict older than 75 years old?(can be assigned only True/False)".title().strip())
choronic = input("Do you have a severe choronic disease? (can be assigned only True/False)".title().strip())
imnue = input("Is you imnune system too weak? (can be assigned only True/False) ".title().strip())

if age or cronic or imnue :
    print("You are in risky group")
else :
    print("You are not risky group")    
