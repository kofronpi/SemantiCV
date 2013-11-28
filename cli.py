from rdflib import ConjunctiveGraph
from cv_ontology import initGraph
from cvdata import addWorkExp
from cvdata import addEdu
from cvdata import addSkill
from export import exportN3
from export import exportNT
from export import exportTRIG
from export import exportTURTLE

menu_item = 0
menu_exp = 0
g = ConjunctiveGraph()
initGraph(g)


print(" #####                                       #####  #     #") 
print("#     # ###### #    #   ##   #    # ##### # #     # #     #")
print("#       #      ##  ##  #  #  ##   #   #   # #       #     #") 
print(" #####  #####  # ## # #    # # #  #   #   # #       #     #")
print("      # #      #    # ###### #  # #   #   # #        #   #")  
print("#     # #      #    # #    # #   ##   #   # #     #   # #")   
print(" #####  ###### #    # #    # #    #   #   #  #####     #") 

while menu_item != 5:
    print("--------------------")
    print("1. Add a work experience section to your CV")
    print("2. Add an education record to your CV")
    print("3. Add a skill to your CV")
    print("4. Export your CV to semantic formats")
    print("5. Quit SemantiCV")
    try:
        menu_item = int(input("Pick an item from the menu: "))
    except ValueError:
        pass
    if menu_item == 1: g=addWorkExp(g)       
    elif menu_item == 2:addEdu()
    elif menu_item == 3:addSkill()
    elif menu_item == 4:
            while menu_exp != 5:
                print("")
                print("---------Export your CV to semantic data :-----------")
                print("1. To N3")
                print("2. To NT")
                print("3. To TRIG")
                print("4. To Turtle")
                print("5. Back")
                try:
                    menu_exp = int(input("Pick an item from the menu: "))
                except ValueError:
                    pass
                if menu_exp == 1:
                    exportN3(g)     
                elif menu_exp == 2:
                    exportNT(g)
                elif menu_exp == 3:
                    exportTRIG(g)
                elif menu_exp == 4:
                    exportTURTLE(g)

 
print("Goodbye! ")



