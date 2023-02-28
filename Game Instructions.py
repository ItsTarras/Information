"""At the end of every "Page" function, reset the coordinate variable to "menu" to reactivate the menu option"""




def art_direction():
    """Art direction page command"""
    print(("-" * 40), "\n Welcome to the Art Direction Page!")
    print("-" * 40)
    
    """Opens the file for Art Direction."""
    filename = open("C:/Users/Lenovo/Desktop/Art_Direction.txt")
    content = filename.readlines()
    for lines in content:
        lines = lines.strip("\n")
        print(lines)
    
    """Gives them time to read"""
    input("\nType anything to continue... ")
    print("\n")
    """Returns the variable to go to the menu."""
    return "menu"          
    

def menu(command_list, possible_pages):
    """Menu Command"""
    print("\nContents:\n")
    
    """Prints lines of contents."""
    for index in range(len(command_list)):
        print(f"Page {index + 1}: {command_list[index]}")
    
    """Asks the user to input the page they want to go to."""
    coordinate = input("\nEnter the page you would like to go to, or type exit to leave: ")
    
    if coordinate.lower() == "exit":
        return coordinate
    """Tells them off if the number isn't numeric, or can't go to the number."""
    while (coordinate.isnumeric() == False and coordinate != "exit") or (str(coordinate) not in possible_pages and coordinate != "exit"):
        coordinate = input("Please enter a valid number, or type exit: ")
    
    return coordinate

def game_concept():
    """Command for the game concept to print out."""
    print(("-" * 40), "\n Welcome to the Game Concept page!")
    print("-" * 40)
    
    """Opens the file for Art Direction."""
    filename = open("C:/Users/Lenovo/Desktop/Game_Concept.txt")
    content = filename.readlines()
    for lines in content:
        lines = lines.strip("\n")
        print(lines)
    
    """Gives them time to read"""
    input("\nType anything to continue... ")
    print("\n")
    """Returns the variable to go to the menu."""
    return "menu"              
    
def main_character():
    print(("-" * 40), "\n Welcome to the Main Character page!")
    print("-" * 40)
    
    """Opens the file for Art Direction."""
    filename = open("C:/Users/Lenovo/Desktop/Main_Character.txt")
    content = filename.readlines()
    for lines in content:
        lines = lines.strip("\n")
        print(lines)
    
    """Gives them time to read"""
    input("\nType anything to continue... ")
    print("\n")
    """Returns the variable to go to the menu."""
    return "menu"          

def storyline():
    print(("-" * 40), "\n Welcome to the Storyline page!")
    print("-" * 40)
    
    """Opens the file for Art Direction."""
    filename = open("C:/Users/Lenovo/Desktop/Game_Story.txt")
    content = filename.readlines()
    for lines in content:
        lines = lines.strip("\n")
        print(lines)
    
    """Gives them time to read"""
    input("\nType anything to continue... ")
    print("\n")
    """Returns the variable to go to the menu."""
    return "menu"          

def main():
    """Creates an unordered set."""
    unordered_set = set()
    
    """Creates an empty list to sort contents to."""
    command_list = []
    possible_pages = []
    """Add Pages to this set."""
    unordered_set.add(("Art Direction", "Main Character", "Game Concept", "Storyline"))
    
    """Sorts the set into alphabetical order."""
    for tup in unordered_set:
        for item in tup:
            command_list.append(item)
            command_list = sorted(command_list)
    
    """The program is running"""
    exit = False
    
    """Creates a list of possible pages to look at."""
    for index in range(len(command_list)):
        possible_pages.append(str(index + 1))    
    
    """Starts on page 1"""
    coordinate = "menu"
    
    """While the program has not been exited"""
    while exit == False:
        
        """Page 1 commands:"""
        while coordinate == "menu":
            coordinate = menu(command_list, possible_pages)
            """While on the Art Direction Page (1)"""
            
            if coordinate == "1":
                coordinate = art_direction()
            
            if coordinate == "2":
                coordinate = game_concept()
                
            if coordinate == "3":
                coordinate = main_character()
            
            if coordinate == "4":
                coordinate = storyline()
            
            if coordinate == "exit":
                exit = True
                print("Goodbye!")
                
main()