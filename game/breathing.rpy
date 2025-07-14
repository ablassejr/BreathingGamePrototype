init python:
    breathinggameactive = False

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
            global successful_attempts
            global attempts

            if successful_attempts >= 3:
                stress += stress_amount*.25
            elif successful_attempts == 2:
                stress +=stress_amount*.50
            elif successful_attempts == 1:
                stress +=stress_amount*.75
            else:
                stress +=stress_amount

            successful_attempts = 0
            attempts = 0
            
            return stress

        def ending(self):
            renpy.music.stop(channel="sound", fadeout=3.0)
            if stress > 100:
                renpy.jump("fail")
            elif status == 3:
                renpy.jump("perfect")
            else:
                renpy.jump("success")

        def timerDisplay():
            return

        @staticmethod
        def audioManager():
            global successful_attempts
            global unsuccessful_attempts
            global stress
            global breathinggameactive

            if not breathinggameactive:
                return

            stageofstress = successful_attempts - unsuccessful_attempts

            if stageofstress == 3:
                renpy.music.play("audio/Heartbeat3.wav", channel="sound", loop=True)
            elif stageofstress == 2:
                renpy.music.play("audio/Heartbeat2.wav", channel="sound", loop=True)
            elif stageofstress == 1:
                renpy.music.play("audio/Heartbeat1.wav", channel="sound", loop=True)
            elif stageofstress == 0:
                renpy.music.play("audio/Heartbeat0.wav", channel="sound", loop=True)
            elif stageofstress == -1:
                renpy.music.play("audio/Heartbeat-1.wav", channel="sound", loop=True)
            elif stageofstress == -2:
                renpy.music.play("audio/Heartbeat-2.wav", channel="sound", loop=True)
            elif stageofstress <= -3:
                renpy.music.play("audio/Heartbeat-3.wav", channel="sound", loop=True)
    
    
