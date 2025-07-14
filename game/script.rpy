# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

label start:
    default previous_attempts = 0
    default status = 0
    default attempts = 0
    default successful_attempts = 0
    default unsuccessful_attempts = 0
    default stress = 60
    default stress_amount = 50

    # Used for debugging size checks
    # default x1 = 0
    # default y1 = 0
    # default x2 = 0
    # default y2 = 0

    scene breathe start
    pause 5.0
    # show breathe bar with moveinright 
    # pause 1.0
    # hide breathe bar with moveoutleft

    $ breathinggameactive = True
    $ Breathing.audioManager()
    $ breathe = Breathing() # class object to call functions
    $ breathe.characterStateChanger() # shows initial face

    show circle red1 at startingPosition

    while attempts < 3:
        $ Breathing.audioManager()
        call screen test
        # pause .55
        hide circle red1
        show circle red1 at startingPosition
        $ attempts += 1

    $ breathe.results()
    $ breathe.ending()
    $ breathinggameactive = False

    jump end

label calm2:
    show bg calm2
    show celia calm2 at still
    show scribble calm2
    return

label calm1:
    show bg calm1
    show celia calm1 at still
    show scribble calm1
    return

label neutral:
    show bg neutral
    show celia neutral at still
    show scribble neutral
    return

label stress1:
    show bg stress1
    show celia stress1 at shake(5, 5)
    show scribble stress1
    return

label stress2:
    show bg stress2
    show celia stress2 at shake(10, 10)
    show scribble stress2
    return

label fail:
    # show celia fail at shake(15, 15)
    # $ quote = "Bad ending."
    scene end failed
    pause 3.0
    jump end

label success:
    # show celia success at still
    # $ quote = "Good ending."
    scene end success
    pause 3.0
    jump end

label perfect:
    # show celia perfect at still
    # $ quote = "Perfect ending."
    scene end perfect
    pause 3.0
    jump end

label end:
    hide circle red
    
    # "[quote]"
    # "Stress: [stress]"

    return

transform startingPosition:
    truecenter
    ypos .8
