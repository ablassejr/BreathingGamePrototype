init python:

    class Breathing:

        def characterStateChanger(state):

            if status >= 2:
                renpy.call("calm2")
            elif status == 1:
                renpy.call("calm1")
            elif status == 0:
                renpy.call("neutral")
            elif status == -1:
                renpy.call("stress1")
            else:
                renpy.call("stress2")
            return

        def results(self):
            global stress

            if successful_attempts >= 3:
                stress += stress_amount*.25
            elif successful_attempts == 2:
                stress +=stress_amount*.50
            elif successful_attempts == 1:
                stress +=stress_amount*.75
            else:
                stress +=stress_amount
            
            return stress

        def ending(self):
            if stress > 100:
                renpy.jump("fail")
            elif status == 3:
                renpy.jump("perfect")
            else:
                renpy.jump("success")

        def timerDisplay():
            return

        def audioManager():
            global successful_attempts
            global unsuccessful_attempts
            stageofstress = 0
            breathingingameactive == True
            global stress
            
            
            while breathingingameactive == True:

                stageofstress == successful_attempts - unsuccessful_attempts
            #zen audio
                while stageofstress == 3:
                    return

            #good audio
                while stageofstress == 2:
                    return

            # normal audio
                while stageofstress == 1:
                    return

            # mixed audio
                while stageofstress == 0:
                    return

            # bad audio
                while stageofstress == -1:
                    return

            # turmoil audio
                while stageofstress == -2:
                    return

            # panicked audio
                while stageofstress == -3:
                    return

                if attempts == 3:
                    breathingingameactive = False
                    return
            return


            # ending audio
            if stress >= 100:
                return
            else:
                return

    
            return
