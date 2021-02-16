import random
#Racial Constants
HUMAN = "Human"
HALF_ELF ="Half-Elf"
MOUNTAIN_DWARF = "Mountain Dwarf"
HILL_DWARF = "Hill Dwarf"
HIGH_ELF = "High_Elf"
WOOD_ELF = "Wood Elf"
DROW = "Drow"
HALF_ORC = "Half-Orc"
TIEFLING = "Tiefling"
DRAGONBORN = "Dragonborn"
ROCK_GNOME = "Rock Gnome"
FOREST_GNOME = "Forest Gnome"
STOUT_HALFLING = "Stout Halfling"
LIGHTFOOT_HALFLING = "Lightfoot Halfling"

BARBARIAN = "Barabrian"
BARD = "Bard"
CLERIC = "Cleric"
DRUID = "Druid"
FIGHTER = "Fighter"
MONK = "Monk"
PALADIN = "Paladin"
RANGER = "Ranger"
ROGUE = "Rogue"
SORCERER = "Sorcerer"
WARLOCK = "Warlock"
WIZARD = "Wizard"

Race_Choices = [HUMAN, HALF_ELF, MOUNTAIN_DWARF, HILL_DWARF, HIGH_ELF, WOOD_ELF, DROW, HALF_ORC, TIEFLING, DRAGONBORN, ROCK_GNOME, FOREST_GNOME, STOUT_HALFLING, LIGHTFOOT_HALFLING]
Class_Choices = [BARBARIAN, BARD, CLERIC, DRUID, FIGHTER, MONK, PALADIN, RANGER, ROGUE, SORCERER, WARLOCK, WIZARD]


st_score = str(random.randint(3,18))
dx_score = str(random.randint(3,18))
cn_score = str(random.randint(3,18))
int_score = str(random.randint(3,18))
ws_score = str(random.randint(3,18))
cha_score = str(random.randint(3,18))

#skill_score = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30']
#skill_modifier = ['-5', '-4', '-4', '-3', '-3', '-2', '-2', '-1', '-1', '0', '0', '+1', '+1', '+2', '+2', '+3', '+3', '+4', '+4', '+5', '+5', '+6', '+6', '+7', '+7', '+8', '+8', '+9', '+9', '+10']

Ability_Score_Modifiers = {'1' : '-5', '2' : '-4', '3' : '-4', '4' : '-3', '5' : '-3', '6' : '-2', '7' : '-2', '8' : '-1', '9' : '-1', '10' : '0', '11' : '0', '12' : '+1', '13' : '+1', '14' : '+2', '15' : '+2', '16' : '+3', '17' : '+3', '18' : '+4', '19' : '+4', '20' : '+5', '21' : '+5', '22' : '+6', '23' : '+6', '24' : '+7', '25' : '+7', '26' : '+8', '27' : '+8', '28' : '+9', '29' : '+9', '30' : '+10'}

# Print Prompt to Enter First Name and Last Name
firstname=input('Please choose a First Name : ')
lastname=input('Please choose a Last Name : ')
Selected_Race=input('Please choose your Race : ')
Selected_Class=input('Please choose your Class : ')
print(firstname, lastname)
#Print Selected Race from List
def race_generator():
    print(Selected_Race)

#Print Selected Class from List
def class_generator():
    print(Selected_Class)

#Random Number Generator for Stats (6 values from 1 - 18)
def stat_generator():
    print('--------------Ability Scores--------------')
   separation = "------------------------"
    #New Racial Bonuses
    if Selected_Race == HUMAN:
        st_bonus = 1
        strength = str(int(st_score)+int(st_bonus))
        dx_bonus = 1
        dexterity = str(int(dx_score)+int(dx_bonus))
        cn_bonus = 1
        constitution = str(int(cn_score)+int(cn_bonus))
        int_bonus = 1
        intelligence = str(int(int_score)+int(int_bonus))
        ws_bonus = 1
        wisdom = str(int(ws_score)+int(ws_bonus))
        cha_bonus = 1
        charisma = str(int(cha_score)+int(cha_bonus))
    
    elif Selected_Race == HALF_ELF:
        ws_bonus = 2
        wisdom = str(int(ws_score)+int(ws_bonus))
        
    elif Selected_Race == MOUNTAIN_DWARF:
        st_bonus = 2
        strength = str(int(st_score)+int(st_bonus))
        cn_bonus = 2
        constitution = str(int(cn_score)+int(cn_bonus))
        
    elif Selected_Race == HILL_DWARF:
        ws_bonus = 1
        wisdom = str(int(ws_score)+int(ws_bonus))
        cn_bonus = 2
        constitution = str(int(cn_score)+int(cn_bonus))
        
    elif Selected_Race == HIGH_ELF:
        int_bonus = 1
        intelligence = str(int(int_score)+int(int_bonus))
        dx_bonus = 2
        dexterity = str(int(dx_score)+int(dx_bonus)) 
        
    elif Selected_Race == WOOD_ELF:
        ws_bonus = 1
        wisdom = str(int(ws_score)+int(ws_bonus))
        dx_bonus = 2
        dexterity = str(int(dx_score)+int(dx_bonus))
        
    elif Selected_Race == DROW:
        cha_bonus = 1
        charisma = str(int(cha_score)+int(cha_bonus))
        dx_bonus = 2
        dexterity = str(int(dx_score)+int(dx_bonus)) 
    
    elif Selected_Race == HALF_ORC:
        st_bonus = 2
        strength = str(int(st_score)+int(st_bonus))
        cn_bonus = 1
        constitution = str(int(cn_score)+int(cn_bonus)) 
    
    elif Selected_Race == TIEFLING:
        cha_bonus = 2
        charisma = str(int(cha_score)+int(cha_bonus))
        int_bonus = 1
        intelligence = str(int(int_score)+int(int_bonus))
    
    elif Selected_Race == DRAGONBORN:
        st_bonus = 2
        strength = str(int(st_score)+int(st_bonus))
        cha_bonus = 1
        charisma = str(int(cha_score)+int(cha_bonus))
    
    elif Selected_Race == ROCK_GNOME:
        int_bonus = 2
        intelligence = str(int(int_score)+int(int_bonus))
        cn_bonus = 1
        constitution = str(int(cn_score)+int(cn_bonus))
    
    elif Selected_Race == FOREST_GNOME:
        int_bonus = 2
        intelligence = str(int(int_score)+int(int_bonus))
        dx_bonus = 1
        dexterity = str(int(dx_score)+int(dx_bonus))
    
    elif Selected_Race == STOUT_HALFLING:
        cn_bonus = 1
        constitution = str(int(cn_score)+int(cn_bonus))
        dx_bonus = 2
        dexterity = str(int(dx_score)+int(dx_bonus))
    
    elif Selected_Race == LIGHTFOOT_HALFLING:
        cha_bonus = 1
        charisma = str(int(cha_score)+int(cha_bonus))
        dx_bonus = 2
        dexterity = str(int(dx_score)+int(dx_bonus))
    
    #Strength Score
    print(st_score)

    
    #Modifier Code
    for key in Ability_Score_Modifiers:
        if key == strength:
            print("Strength Score of {} Grants a modifier of {}".format(strength, Ability_Score_Modifiers[strength]))
        else:
            pass
    print("------------------------")

   
    else:
        dexterity = (dx_score)
    #Modifier Code
    for key in Ability_Score_Modifiers:
        if key == dexterity:
            print("dexterity Score of {} Grants a modifier of {}".format(dexterity, Ability_Score_Modifiers[dexterity]))
        else:
            pass
    print("------------------------")

    #Modifier Code
    for key in Ability_Score_Modifiers:
        if key == constitution:
            print("constitution Score of {} Grants a modifier of {}".format(constitution, Ability_Score_Modifiers[constitution]))
        else:
            pass
    print("------------------------")
    
    
    #Modifier Code
    for key in Ability_Score_Modifiers:
        if key == wisdom:
            print("wisdom Score of {} Grants a modifier of {}".format(wisdom, Ability_Score_Modifiers[wisdom]))
        else:
            pass
    print("------------------------")
    
   
    #Modifier Code
    for key in Ability_Score_Modifiers:
        if key == intelligence:
            print("intelligence Score of {} Grants a modifier of {}".format(intelligence, Ability_Score_Modifiers[intelligence]))
        else:
            pass
    print("------------------------")
   
    
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
