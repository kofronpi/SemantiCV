from rdflib import ConjunctiveGraph
menu_item = 0
menu_exp = 0
from cv_ontology import initGraph
from cvdata import addWorkExp
from cvdata import addEdu
from cvdata import addSkill
g = ConjunctiveGraph()
initGraph(g)

from export import exportRDF
from export import exportJSONLD
from export import exportN3
from export import exportTURTLE

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
    if menu_item == 1:addWorkExp()       
    elif menu_item == 2:addEdu()
    elif menu_item == 3:addSkill()
    elif menu_item == 4:
            while menu_exp != 5:
                print("")
                print("---------Export your CV to semantic data :-----------")
                print("1. To RDF")
                print("2. To JSON/LD")
                print("3. To N3")
                print("4. To Turtle")
                print("5. Back")
                try:
                    menu_exp = int(input("Pick an item from the menu: "))
                except ValueError:
                    pass
                if menu_exp == 1:
                    exportRDF()     
                elif menu_exp == 2:
                    exportJSONLD()
                elif menu_exp == 3:
                    exportN3()
                elif menu_exp == 4:
                    exportTURTLE()

 
print("Goodbye! ")



