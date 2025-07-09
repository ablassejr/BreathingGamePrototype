init python:

    class Breathing:

        def characterStateChanger(state):

            if status >= 2:
                renpy.call("happy")
            elif status == 1:
                renpy.call("smile")
            elif status == 0:
                renpy.call("straight")
            elif status == -1:
                renpy.call("frown")
            else:
                renpy.call("cry")
            return

        def results(self):
            global stress

            if successful_attempts >= 3:
                #scene bg prefect
                stress += stress_amount*.25
            elif successful_attempts == 2:
                #scene bg success
                stress +=stress_amount*.50
            elif successful_attempts == 1:
                #scene bg success
                stress +=stress_amount*.75
            else:
                #scene bg failure
                stress +=stress_amount
            
            return stress

        def ending(self):
            if stress > 100:
                return "Bad ending"
            elif status == 3:
                return "Perfect ending"
            else:
                return "Good ending"

        def timerDisplay():
            return

        def audioManager():
            return
