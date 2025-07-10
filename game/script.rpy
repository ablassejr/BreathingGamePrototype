# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

default status = 0

label start:
    # temp values
    default attempts = 0
    default successful_attempts = 0
    default unsuccessful_attempts = 0
    default stress = 60
    default stress_amount = 50
    scene bg gradient
    pause .5
    show breathe bar with moveinright 
    pause 1.0
    hide breathe bar with moveoutleft


    $ breathe = Breathing() # class object to call functions
    $ breathe.characterStateChanger() # shows initial face
    show circle red1 at startingPosition
    while attempts < 3:
        call screen test
        pause .55
        hide circle red1 # hides and shows red circle again so it is above face, can be fixed with layers
        show circle red1 at startingPosition
        $ breathe.characterStateChanger()
        $ attempts += 1
    $ breathe.results()
    $ breathe.ending()


    jump end

label calm2:
    show bg calm2
    show celia calm2
    show scribble calm2
    return

label calm1:
    show bg calm1
    show celia calm1
    show scribble calm1
    return

label neutral:
    show bg neutral
    show celia neutral
    show scribble neutral
    return

label stress1:
    show bg stress1
    show celia stress1
    show scribble stress1
    return

label stress2:
    show bg stress2
    show celia stress2
    show scribble stress2
    return

label fail:
    show celia fail
    $ quote = "Bad ending."
    jump end

label success:
    show celia success
    $ quote = "Good ending."
    jump end

label perfect:
    show celia perfect
    $ quote = "Perfect ending."
    jump end


label end:
    hide circle red
    
    "[quote]"
    "Stress: [stress]"

    return

transform startingPosition:
    truecenter
    ypos .8
