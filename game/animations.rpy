init python:
    # gives random offset points on x and y axis so that Celia's shaking is absolutely random
    def shaking(trans, st, at, xbound, ybound):
        trans.xoffset = renpy.random.randint(-xbound, xbound)
        trans.yoffset = renpy.random.randint(-ybound, ybound)
        return None

    # calls the function above, I haven't found a way to make it a single function so this will do for now
    def make_shake(xbound, ybound):
        return lambda trans, st, at: shaking(trans, st, at, xbound, ybound)

transform shake(xbound, ybound):
    xpos 0 # xpos and ypos have to be set to something before transform or Celia will not appear
    ypos 0
    function make_shake(xbound, ybound) # function that takes in parameters of shaking boundaries,
                                            # this allows for more shaking when Celia stress gets worse
    pause 0.05
    repeat

# this transform is needed to undo shake when Celia is calm
transform still():
    xpos 0
    ypos 0
    xoffset 0
    yoffset 0