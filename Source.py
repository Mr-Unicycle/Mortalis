import json
from os import system
file_name = "characters.txt"

class Stuff:
    def __init__(self,name,value):
        self.name = name
        self.value = value
    def add_to_val(self,num):
        self.value+=num
    def get_name(self):
        return self.name
    def get_value(self):
        return self.value
class Skill(Stuff):
    def __init__(self,name,value):
        super().__init__(name,value)
class Tool(Stuff):
    def __init__(self,name,value):
        super().__init__(name,value)
class Weapon(Stuff):
    def __init__(self,name,value):
        super().__init__(name,value)
class Ability:
    def __init__(self, name, ab_params):
        self.name = str(name)
        self.skills = []
        for key in ab_params:
            self.skills.append(Skill(name = key, value = ab_params[key]))
        self.skills.sort(key=lambda x: x.value, reverse=True)
class Character:
    def __init__(self,params):
        #Giving the character a name
        self.name = params["Name"]
        #give the character an assigned player
        self.player = params["Player"]
        #initializing and populating the abilities list
        self.abilities = []
        for key in params["Abilities"]:
            self.abilities.append(Ability(name = key, ab_params = params["Abilities"][key]))
        #initialize, populate, and sort the tools list
        self.tools = []
        for key in params["Tools"]:
            self. tools.append(Tool(name = key, value = params["Tools"][key]))
        self.tools.sort(key=lambda x: x.value, reverse=True)
        #initialize, populate, and sort the weapons list
        self.weapons = []
        for key in params["Weapons"]:
            self.weapons.append(Weapon(name = key, value = params["Weapons"][key]))
        self.weapons.sort(key=lambda x: x.value, reverse=True)

    def change_name(self,name):
        self.name = name
    def change_player(self,player):
        self.player=player

characters = []
roster = []

def clear():
    system("cls")

def load():
    f = open(file_name,"r")
    for line in f:
        characters.append(Character(json.loads(line.strip())))
    f.close()
    characters.sort(key = lambda x: x.player)
def save():
    f = open(file_name,"w")
    f.close()
    f = open(file_name,"a")
    for character in characters:
        f.write("{\"Name\":\""+character.name+"\",\"Player\":\""+character.player+"\",\"Abilities\":{")
        ability_num = 0
        for ability in character.abilities:
            if ability_num!=0:
                f.write(",")
            f.write("\""+ability.name+"\":{")
            skill_num=0
            for skill in ability.skills:
                if skill_num!=0:
                    f.write(",")
                f.write(f"\"{skill.name}\":{str(skill.value)}")
                skill_num+=1
            f.write("}")
            ability_num+=1
        f.write("},\"Tools\":{")
        tool_num = 0
        for tool in character.tools:
            if tool_num!=0:
                f.write(",")
            f.write(f"\"{tool.name}:{str(tool.value)}")
            tool_num+=1
        f.write("},\"Weapons\":{")
        weapon_num=0
        for weapon in character.weapons:
            if weapon_num!=0:
                f.write(",")
            f.write(f"\"{weapon.name}:{str(weapon.value)}")
            weapon_num+=1
        f.write("\n")
    f.close()

def validate(string,upper):
    while True:
        try:
            temp = int(input(string))
            if temp>upper or temp<0:
                raise IndexError
            return temp            
        except ValueError:
            print("Pleas input an acceptable value.")
        except IndexError:
            print(f"Please input a number between 0 and {upper}.")

def main_loop():
    while True:
        clear()
        l1 = validate("(0) Make a Roll\t(1) Character Management\t(2) Exit and Save:",2)
        if l1==0:
            while True:
                clear()
                for i in range(len(roster)):
                    print(f"({i}) {characters[roster[i]].name}({characters[roster[i]].player})",end = "\t")
                print(f"({len(roster)}) Back")
                l2 = validate("Which Character?: ", len(roster))
                if l2 == len(roster):
                    break
                clear()
                l3 = validate("(0) Skill\t(1) Weapon\t(2) Tool\t(3) back:",3)
                if l3 == 0:
                    clear()
                    for i in range(len(characters[roster[l2]].abilities)):
                        print(f"({i}) {characters[roster[l2]].abilities[i].name}", end = "\t")
                    l4 = validate("\nWhich ability?: ", len(characters[roster[l2]].abilities)-1)
                    clear()
                    for i in range(len(characters[roster[l2]].abilities[l4].skills)):
                        print(f"({i}) {characters[roster[l2]].abilities[l4].skills[i].name}", end = "\t")
                    l5 = validate("\nWhich skill?: ", len(characters[roster[l2]].abilities[l4].skills)-1)
                    characters[roster[l2]].abilities[l4].skills[l5].add_to_val(1)
                elif l3 == 1:
                    clear()
                    for i in range(len(characters[roster[l2]].weapons)):
                        print(f"({i}) {characters[roster[l2]].weapons[i].name}",end = "\t")
                    l4 = validate("\nWhich Tool?: ", len(characters[roster[l2]].weapons)-1)
                    characters[roster[l2]].weapons[l4].add_to_val(1)
                elif l3 == 2:
                    clear()
                    for i in range(len(characters[roster[l2]].tools)):
                        print(f"({i}) {characters[roster[l2]].tools[i].name}")
                    l4 = validate("Which Tool?: ", len(characters[roster[l2]].tools)-1)
                    characters[roster[l2]].tools[l4].add_to_val(1)
                elif l3 == 3:
                    continue
        elif l1==1:
            while True:
                clear()
                l2 = validate("(0) Add Character\t(1) Remove Character\t(2)Make Character\t(3)Adjust Stats\t(4) Back:", 4)
                if l2 ==0:
                    clear()
                    for i in range(len(characters)):
                        print(f"({i}) {characters[i].name}({characters[i].player})")
                    print(f"({len(characters)}) Back")
                    l3 = validate("Which character?: ",len(characters))
                    if l3 == len(characters):
                        continue
                    roster.append(l3)
                elif l2 == 1:
                    clear()
                    for i in range(len(roster)):
                        print(f"({i}) {characters[roster[i]].name}({characters[roster[i]].player})")
                    print(f"({len(roster)}) Back")
                    l3 = validate("Which character?:", len(roster))
                    if l3 == len(roster):
                        continue
                    roster.pop(l3)
                elif l2 == 2:
                    f = open("empty_character.json","r")
                    characters.append(Character(json.loads(f.readline().strip())))
                    f.close()
                    characters[-1].change_name(input("What is the character's name?:"))
                    characters[-1].change_player(input("Who is the player?:"))
                    input("This character will appear at the end of the character list until the next reload.")
                elif l2 == 3:
                    clear()
                    for i in range(len(roster)):
                        print(f"({i}) {characters[roster[i]].name}({characters[roster[i]].player})")
                    print(f"({len(roster)}) Back")
                    l3 = validate("Which character?:",len(roster))
                    if l3 == len(roster):
                        continue
                    while True:
                        clear()
                        l4 = validate("What would you like to adjust?\n(0) Skill\t(1) Weapon\t(2) Tool\t(3) Back:",3)
                        if l4 == 0:
                            clear()
                            for i in range(len(characters[roster[l3]].abilities)):
                                print(f"({i}) {characters[roster[l3]].abilities[i].name}", end = "\t")
                            l5 = validate("\nWhich Ability?: ",len(characters[roster[l3]].abilities)-1)
                            clear()
                            for i in range(len(characters[roster[l3]].abilities[l5].skills)):
                                print(f"({i}) {characters[roster[l3]].abilities[l5].skills[i].name}",end="\t")
                            l6 = validate("\nWhich skill?: ",len(characters[roster[l3]].abilities[l5].skills)-1)
                            while True:
                                try:
                                    characters[roster[l3]].abilities[l5].skills[l6].add_to_val(int(input(f"{characters[roster[l3]].abilities[l5].skills[l6].name} is currently sitting at {characters[roster[l3]].abilities[l5].skills[l6].value}.\nHow much would you like to add?:")))
                                    break
                                except ValueError:
                                    clear()
                                    print("Please enter and acceptable value.")
                        elif l4 == 1:
                            clear()
                            for i in range(len(characters[roster[l3]].weapons)):
                                print(f"({i}) {characters[roster[l3]].weapons[i].name}", end = "\t")
                            l5 = validate("\nWhich Weapon?: ", len(characters[roster[l3]].weapons)-1)
                            while True:
                                clear()
                                try:
                                    characters[roster[l3]].weapons[l5].add_to_val(int(input(f"{characters[roster[l3]].weapons[l5].name} is currently sitting at {characters[roster[l3]].weapons[l5].value}.\nHow much would you like to add?:")))
                                    break
                                except ValueError:
                                    print("Please enter an acceptable value")
                        elif l4 == 2:
                            clear()
                            for i in range(len(characters[roster[l3]].tools)):
                                print(f"({i}) {characters[roster[l3]].tools[i].name}")
                            l5 = validate("\nWhich tool?: ", len(characters[roster[l3]].tools)-1)
                            while True:
                                clear()
                                try:
                                    characters[roster[l3]].tools[l5].add_to_val(int(input(f"{characters[roster[l3]].tools[l5].name} is currently sitting at {characters[roster[l3]].tools[l5].value}.\nHow much would you like to add?:")))
                                    break
                                except ValueError:
                                    print("Please enter an acceptable value")
                        elif l4 == 3:
                            break
                elif l2 == 4:
                    break
        elif l1==2:
            if input("Are you sure you want to exit? (Type \"Yupperdoodles\")").upper() == "YUPPERDOODLES":
                break

load()
main_loop()
save()