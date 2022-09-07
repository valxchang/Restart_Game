# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define m = Character('Me', color= "#14600D")
define a = Character('Aya', color= "#E4411F")
define inn = Character('Innkeeper', color= "#5D270C")
define town = Character('Townsperson', color= "#000000")
define q = Character('???', color = "#000D7D")
define pov = Character("[povname]")
define lady = Character('Restaurant Owner', color = "#8A0870")

# STARTING POINT
# The game starts here in the middle of the forest.
# The player does not remember anything.

label start:

    m "..."
    m "Where am I?"
    m "..."
    m "Who am I?"

    "A silent forest. No birds, no bugs, nothing."
    "Only the distant sound of water."
    
    "You look around. Up, down, left, right."

    m "I only have...these clothes...and this strange...stick. Huh? My cheeks are a bit wet."
    m "Well. It seems like...I have...amnesia."    
    m "I wonder how I ended up here."
    
    jump splitPointTwoAAndB     # The player chooses between 2a and 2b - visiting the town or the mountain.
                
label splitPointTwoAAndB:      # The player chooses between 2a and 2b - visiting the town or the mountain.

    menu:   
        
        "The river's safer. Who knows who lives up there?":
            jump twoA         # The player chooses to visit the town.   
        
        "A short hike's nothing! What if no one lives by the river?":
            jump twoB         # The player chooses to visit the mountain hut.

label twoA:            # The player chooses to visit the town as their first choice.
    
    python:                 # Determines the name of the player.
        
        povname = renpy.input("What is your name?")
        povname = povname.strip()

        if not povname:
             povname = "Sam"
    
    menu:
        "Read the rest of the diary.":  # The player chooses to continue reading their diary.
            $ read_more = True
            jump twoAReadMore
        
        "Don't read the rest of the diary.":    # The player chooses to continue reading their diary.
            $ read_more = False
            jump twoANormalDay

label twoAReadMore:

    jump splitPointThreeAAndC   # The player chooses between 3a and 3c - staying in the town or visiting the mountain.

label twoANormalDay:
    jump splitPointThreeAAndC   # The player chooses between 3a and 3c - staying in the town or visiting the mountain.

label splitPointThreeAAndC:     # The player chooses between 3a and 3c - staying in the town or visiting the mountain.
    
    menu:
        "Stay in Rose Lake. The other townspeople might know more about you." if read_more:
            jump threeAReadMore     # The player chooses to continue living in the town and they chose to read the rest of their diary.
           
        "Stay in Rose Lake. The other townspeople might know more about you." if not read_more:
            jump threeANormalDay
            
        "Visit the witch. She sounds promising.":
            jump threeC         # The player chooses to visit the mountain hut.
            
label threeAReadMore:   # The player chooses to continue living in the town after staying in it for one day.

    jump splitPointThreeA    # The player chooses between staying in the town, going home, or erasing their memories.

label threeANormalDay:
   
    jump splitPointThreeA    # The player chooses between staying in the town, going home, or erasing their memories.

label threeC:   # The player chooses to visit the mountain hut after staying in the town for one day.
        menu:
            "Explore more of your memories.":  # The player chooses to continue exploring their memories.
                $ explore_more = True
                jump threeCExploreMore
            
            "Don't read the rest of the diary.":    # The player chooses to not continue exploring their memories.
                $ explore_more = False
                jump threeCNormalDay

label threeCExploreMore:
    if explore_more and read_more:
        jump splitPointTwoOptions
    else:
        jump splitPointAllOptions

label threeCNormalDay:
    jump splitPointAllOptions

label twoB:         # The player chooses to visit the mountain hut as their first choice.

    python:                 # Determines the name of the player.

        povname = renpy.input("What is your name?")
        povname = povname.strip()

        if not povname:
            povname = "Sam"
    
    menu:
        "Explore more.":
            $ explore_more = True
            jump twoBExploreMore
            
        "Don't explore more.":
            $ explore_more = False
            jump twoBNormalDay

label twoBExploreMore:
    jump splitPointThreeBAndD

label twoBNormalDay:
    jump splitPointThreeBAndD
    
label splitPointThreeBAndD:      # The player chooses between threeD and threeB - visiting the town or staying with Aya.
    menu:
        
        "I want to visit the town.":
            jump threeD
            
        "I want to stay with Aya." if explore_more:
            jump threeBExploreMore
            
        "I want to stay with Aya." if not explore_more:
            jump threeBNormalDay

label threeD:   # The player chooses to visit the town after staying with Aya for one day.
        menu:
            "Read the rest of the diary.":  # The player chooses to continue reading the diary.
                $ read_more = True
                jump threeCExploreMore
            
            "Don't read the rest of the diary.":    # The player chooses to not continue reading the diary.
                $ read_more = False
                jump threeCNormalDay

label threeDReadMore:
    if explore_more and read_more:
        jump splitPointTwoOptions
    else:
        jump splitPointAllOptions

label threeDNormalDay:
    jump splitPointAllOptions

label threeBExploreMore: #PLAYER CHOOSES TO STAY IN THE MOUNTAIN
    
    jump splitPointThreeB

label threeBNormalDay:
    
    jump splitPointThreeB

label splitPointThreeA:         # The final choice available only to players who reach 3a They choose between erasing their memories, living in the town, or returning.
    
    menu: 
        
        "I can't live on knowing that I've done such terrible things.":
            jump restart
            
        "I feel truly alive in this town. I will stay here.":
            jump refresh
            
        "My family needs me. I will return home.":
            jump relive

label splitPointThreeB:         # The final choice available only to players who reach 3b. They choose between erasing their memories, living with Aya, or returning.
    
    menu: 
        
        "I can't live on knowing that I've done such terrible things.":
            jump restart
            
        "Aya's been great company while my memories were gone. I want to stay with her.":
            jump redo
            
        "My family needs me. I will return home.":
            jump relive

label splitPointAllOptions:     # The final choice available only to sane players who explored both areas. They choose between erasing their memories, living in the town or with Aya, and returning.
    
    menu:                   
        
        "I can't live on knowing that I've done such terrible things.":
            jump restart
        
        "Aya's been great company while my memories were gone. I want to stay with her.":
            jump redo
        
        "I feel truly alive in this town. I will stay here.":
            jump refresh
            
        "My family needs me. I will return home.":
            jump relive

label splitPointTwoOptions:     # The final choice available only to insane players. They choose between erasing their memories and returning.
    menu:
        "I can't live on knowing that I've done such terrible things.":
            jump restart
            
        "My family needs me. I will return home.":
            jump relive_lockedup

label restart:          # MC returns to the clearing and erases their memories.
    
    m "I'm sick and tired of living like this! I'm doing it again--I don't care about what happens to me!"
    q "NO! Come back, [povname]!"
    
    "You run off into the forest where you first woke up. Nothing matters anymore."    
    "Reaching the all-too-familiar clearing, you raise the wand up to your forehead."
    
    m "I will always love you, [povname]. Please understand why I'm doing this."    
    m "..."
    
    "You say the spell that will erase your memories, falling to the ground."    
    "A single tear rolls down your cheek."
    "Going, going, gone."    
    "Going, going, gone..."    
    "Going, going..."
    
    m "..."
    m "Where am I?"
    m "..."    
    m "Who am I?"

    "A silent forest. No birds, no bugs, nothing."    
    "Only the distant sound of water."
    
    "{b}Restart Ending{/b}."
    
    return              # Ends the game.

label redo:             # MC decides to live with Aya.
    
    m "Aya, I want to stay with you. Can I?"
    
    "{b}Redo Ending{/b}."
    
    return              # Ends the game.

label refresh:          # MC decides to live in Roselake.
    
    m "Rose Lake is wonderful. I want to stay here."
    
    "{b}Refresh Ending{/b}."
    
    return              # Ends the game.

label relive:           # MC decides to return home with the important person.
    
    m "I'm willing to forgive myself for what I did in the past. I'm going home."
    
    "{b}Relive Ending{/b}."
    
    return              # Ends the game

label relive_lockedup:
    "{b}Hidden Ending 1{/b}."
    return
