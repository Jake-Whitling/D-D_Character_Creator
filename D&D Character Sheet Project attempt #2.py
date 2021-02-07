import random
#Global Values
Race_Choices = ['Human', 'Half-Elf', 'Mountain Dwarf', 'Hill Dwarf', 'High Elf', 'Wood Elf', 'Drow', 'Half-Orc', 'Tiefling', 'Dragonborn', 'Rock Gnome', 'Forest Gnome', 'Stout Halfling', 'Lightfoot Halfling']
Class_Choices = ['Barbarian', 'Bard', 'Cleric', 'Druid', 'Fighter', 'Monk', 'Paladin', 'Ranger', 'Rogue', 'Sorcerer', 'Warlock', 'Wizard']

Selected_Races = random.choice(Race_Choices)
Selected_Classes = random.choice(Class_Choices)

st_score = str(random.randint(3,18))
dx_score = str(random.randint(3,18))
cn_score = str(random.randint(3,18))
ws_score = str(random.randint(3,18))
int_score = str(random.randint(3,18))
cha_score = str(random.randint(3,18))

#skill_score = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30']
#skill_modifier = ['-5', '-4', '-4', '-3', '-3', '-2', '-2', '-1', '-1', '0', '0', '+1', '+1', '+2', '+2', '+3', '+3', '+4', '+4', '+5', '+5', '+6', '+6', '+7', '+7', '+8', '+8', '+9', '+9', '+10']

Ability_Score_Modifiers = {'1' : '-5', '2' : '-4', '3' : '-4', '4' : '-3', '5' : '-3', '6' : '-2', '7' : '-2', '8' : '-1', '9' : '-1', '10' : '0', '11' : '0', '12' : '+1', '13' : '+1', '14' : '+2', '15' : '+2', '16' : '+3', '17' : '+3', '18' : '+4', '19' : '+4', '20' : '+5', '21' : '+5', '22' : '+6', '23' : '+6', '24' : '+7', '25' : '+7', '26' : '+8', '27' : '+8', '28' : '+9', '29' : '+9', '30' : '+10'}

# Print Prompt to Enter First Name and Last Name
firstname=input('Please choose a First Name : ')
lastname=input('Please choose a Last Name : ')

print(firstname, lastname)
#Print Selected Race from List
def race_generator():
    print(Selected_Races)

#Print Selected Class from List
def class_generator():
    print(Selected_Classes)

#Random Number Generator for Stats (6 values from 1 - 18)
def stat_generator():
    print('--------------Ability Scores--------------')
    #Strength Score
    print(st_score)

    #Racial Bonuses
    if Selected_Races == 'Human':
        st_bonus = str(1)
        strength = str(int(st_score)+int(st_bonus))
    elif Selected_Races == 'Mountain Dwarf' :
        st_bonus = str(2)
        strength = str(int(st_score)+int(st_bonus))
    elif Selected_Races == 'Dragonborn' :
        st_bonus = str(2)
        strength = str(int(st_score)+int(st_bonus))
    elif Selected_Races == 'Half-Orc' :
        st_bonus = str(2)
        strength = str(int(st_score)+int(st_bonus))
    else:
        strength = (st_score)
    #Modifier Code
    for key in Ability_Score_Modifiers:
        if key == strength:
            print("Strength Score of {} Grants a modifier of {}".format(strength, Ability_Score_Modifiers[strength]))
        else:
            pass
    print("------------------------")

    #Dexterity Score
    print(dx_score)
    #RaceBonuses
    if Selected_Races == 'Human':
        dx_bonus = str(1)
        dexterity = str(int(dx_score)+int(dx_bonus))
    elif Selected_Races == 'High Elf' :
        dx_bonus = str(2)
        dexterity = str(int(dx_score)+int(dx_bonus))
    elif Selected_Races == 'Wood Elf' :
        dx_bonus = str(2)
        dexterity = str(int(dx_score)+int(dx_bonus))
    elif Selected_Races == 'Drow' :
        dx_bonus = str(2)
        dexterity = str(int(dx_score)+int(dx_bonus))
    elif Selected_Races == 'Forest Gnome' :
        dx_bonus = str(1)
        dexterity = str(int(dx_score)+int(dx_bonus))
    elif Selected_Races == 'Stout Halfling' :
        dx_bonus = str(2)
        dexterity = str(int(dx_score)+int(dx_bonus))
    elif Selected_Races == 'Lightfoot Halfling' :
        dx_bonus = str(2)
        dexterity = str(int(dx_score)+int(dx_bonus))
    else:
        dexterity = (dx_score)
    #Modifier Code
    for key in Ability_Score_Modifiers:
        if key == dexterity:
            print("dexterity Score of {} Grants a modifier of {}".format(dexterity, Ability_Score_Modifiers[dexterity]))
        else:
            pass
    print("------------------------")

    #Constitution Score
    print(cn_score)
    #RaceBonuses
    if Selected_Races == 'Human':
        cn_bonus = str(1)
        constitution = str(int(cn_score)+int(cn_bonus))
    elif Selected_Races == 'Hill Dwarf' :
        cn_bonus = str(2)
        constitution = str(int(cn_score)+int(cn_bonus))
    elif Selected_Races == 'Mountain Dwarf' :
        cn_bonus = str(2)
        constitution = str(int(cn_score)+int(cn_bonus))
    elif Selected_Races == 'Half-Orc' :
        cn_bonus = str(1)
        constitution = str(int(cn_score)+int(cn_bonus))
    elif Selected_Races == 'Stout Halfling' :
        cn_bonus = str(1)
        constitution = str(int(cn_score)+int(cn_bonus))
    elif Selected_Races == 'Rock Gnome' :
        cn_bonus = str(1)
        constitution = str(int(cn_score)+int(cn_bonus))
    else:
        constitution = (cn_score)
    #Modifier Code
    for key in Ability_Score_Modifiers:
        if key == constitution:
            print("constitution Score of {} Grants a modifier of {}".format(constitution, Ability_Score_Modifiers[constitution]))
        else:
            pass
    print("------------------------")
    
    #Wisdom Score
    print(ws_score)
    #RaceBonuses
    if Selected_Races == 'Human':
        ws_bonus = str(1)
        wisdom = str(int(ws_score)+int(ws_bonus))
    elif Selected_Races == 'Hill Dwarf' :
        ws_bonus = str(2)
        wisdom = str(int(ws_score)+int(ws_bonus))
    elif Selected_Races == 'Wood Elf' :
        ws_bonus = str(2)
        wisdom = str(int(ws_score)+int(ws_bonus))
    else:
        wisdom = (ws_score)
    #Modifier Code
    for key in Ability_Score_Modifiers:
        if key == wisdom:
            print("wisdom Score of {} Grants a modifier of {}".format(wisdom, Ability_Score_Modifiers[wisdom]))
        else:
            pass
    print("------------------------")
    
    #Intelligence Score
    print(int_score)
    #RaceBonuses
    if Selected_Races == 'Human':
        int_bonus = str(1)
        intelligence = str(int(int_score)+int(int_bonus))
    elif Selected_Races == 'Rock Gnome' :
        int_bonus = str(2)
        intelligence = str(int(int_score)+int(int_bonus))
    elif Selected_Races == 'Forrest Gnome' :
        int_bonus = str(2)
        intelligence = str(int(int_score)+int(int_bonus))
    elif Selected_Races == 'High Elf' :
        int_bonus = str(1)
        intelligence = str(int(int_score)+int(int_bonus))
    elif Selected_Races == 'Tiefling' :
        int_bonus = str(1)
        intelligence = str(int(int_score)+int(int_bonus))
    else:
        intelligence = (int_score)
    #Modifier Code
    for key in Ability_Score_Modifiers:
        if key == intelligence:
            print("intelligence Score of {} Grants a modifier of {}".format(intelligence, Ability_Score_Modifiers[intelligence]))
        else:
            pass
    print("------------------------")
   
    #Charisma Score
    print(cha_score)
    #RaceBonuses
    if Selected_Races == 'Human':
        cha_bonus = str(1)
        charisma = str(int(cha_score)+int(cha_bonus))
    elif Selected_Races == 'Half-Elf' :
        cha_bonus = str(2)
        charisma = str(int(cha_score)+int(cha_bonus))
    elif Selected_Races == 'Drow' :
        cha_bonus = str(1)
        charisma = str(int(cha_score)+int(cha_bonus))
    elif Selected_Races == 'Dragonborn' :
        cha_bonus = str(1)
        charisma = str(int(cha_score)+int(cha_bonus))
    elif Selected_Races == 'Lightfoot Halfling' :
        cha_bonus = str(1)
        charisma = str(int(cha_score)+int(cha_bonus))
    elif Selected_Races == 'Tielfing' :
        cha_bonus = str(2)
        charisma = str(int(cha_score)+int(cha_bonus))
    else:
        charisma = (cha_score)
    #Modifier Code
    for key in Ability_Score_Modifiers:
        if key == charisma:
            print("charisma Score of {} Grants a modifier of {}".format(charisma, Ability_Score_Modifiers[charisma]))
        else:
            pass
    print("------------------------")

def main():
    race_generator()
    class_generator()
    stat_generator()


main()
