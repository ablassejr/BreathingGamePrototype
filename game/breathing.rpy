init python:

    class Breathing:

        def characterStateChanger():
            return

        def results(result):
            if attempts == 3:
                scene bg prefect
                $stress += stress_amount*.25
            elif attempts == 2:
                scene bg success
                $stress +=stress_amount*.50
            elif attempts == 1:
                scene bg success
                $stress +=stress_amount*.75
            else:
                scene bg failure
                $stress +=stress_amount
            result == stress
            return result

        

        def ending(ending):
            default Minigame_ending = False
            if stress > 100:
                $Minigame_ending = True

            if Minigame_ending == True:
                return "bad ending"
            else:
                return "Good Ending"


        def timerDisplay():
            return

        def audioManager():
            return
