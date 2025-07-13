# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.




# The game starts here.

# label start2:
#     "this is after the minigame ends with a previous stress level of 60 and a potential increase of 50"
#     "So in the following choose how you did"

#     default Minigame_ending = False
#     default attempts = 0
#     default stress = 60
#     default stress_amount = 50

# menu:
#     "Perfect Success":
#         $attempts +=3
#         jump results
#     "Success":
#         $attempts +=1
#         jump results
#     "Failure":
#         jump results

# label results:
#     if attempts == 3:
#         scene bg prefect
#         $stress += stress_amount*.25
#         "Im okay"
    
#     elif attempts == 2:
#         scene bg success
#         $stress +=stress_amount*.50
#         "Im a o..okay"

#     elif attempts == 1:
#         scene bg success
#         $stress +=stress_amount*.75
#         "Im o..okay"

#     else:
#         scene bg failure
#         $stress +=stress_amount
#         "o..oh no..."

# label ending:

#     if stress > 100:
#         $Minigame_ending = True

#     if Minigame_ending == True:
#         "bad ending"
#     else:
#         "Good Ending"


#     return
