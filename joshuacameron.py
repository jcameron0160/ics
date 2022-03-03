notDone = True
allCharacters = []
while notDone :
    charList =[]
    name = input('name: ')
    charList.append(name)
    profession = input('class: ')
    charList.append(profession)
    level = input('level: ')
    charList.append(level)
    allCharacters.append(charList)
    print(f"""
    name: {name}
    class: {profession}
    level: {level}""")



    answer = input("Do you want out? ")
    if answer == "Y":
       notDone = False

    else:
       print("ok we go again")
print(allCharacters)



   

    
