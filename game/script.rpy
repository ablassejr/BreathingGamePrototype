# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

default status = 0
init image backgroundCircle = "circle blue.svg" # Background circle image
label start:
    # temp values
    default attempts = 0
    default successful_attempts = 0
    default stress = 60
    default stress_amount = 50
    scene white
    "start"

    $ breathe = Breathing() # class object to clal functions
    $ breathe.characterStateChanger() # shows inital face
    show backgroundCircle at startingPosition
    while attempts < 3:
        call screen test()
        hide backgroundCircle # hides and shows red circle again so it is above face, can be fixed with layers
        show backgroundCircle at startingPosition # maybe should be solid and use a green band(hollow circle) to represent success window
        $ attempts += 1

    $ breathe.results() 


    jump end

label happy:
    show face happy
    return

label smile:
    show face smile
    return

label straight:
    show face straight
    return

label frown:
    show face frown
    return

label cry:
    show face cry
    return

label end:
    hide circle red
    $ quote = breathe.ending()
    "[quote]"
    "Stress: [stress]"

    return

transform startingPosition:
    truecenter
    ypos .8
