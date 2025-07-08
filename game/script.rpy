# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

label start:
    # temp values
    default attempts = 0
    default stress = 60
    default stress_amount = 50

    scene white
    # show circle outside at truecenter
    "start"
    # show circle red at beginning
    call screen test

label end:
    "End"

    return
