# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

init python:
    # Have to import pygame to check for spacebar is held down
    import pygame

    # Class for the increasing circle
    class IncreaseCircle(renpy.Displayable):
        def __init__(self,image):
            super(renpy.Displayable,self).__init__()
            # Image that will be increased
            self.start_image = image
            # Size of the image
            self.xysize = [0, 0]
            # Rate image size will increase
            self.rate = 0.0
            # The beginning state of when the spacebar begins to be held
            self.start_st = None
            # Total time the space bar is being held
            self.total_time = 0.0

        # Renders the image onto the screen
        def render(self,width,height,st,at):
            # If rate if above 0 and the beginning state is already intialized
            if self.rate and self.start_st is not None:
                # Will calculate how long the spacebar has been held
                time_held = st - self.start_st
                # The time held is added to the total amount of time it is held
                total_time = self.total_time + time_held
            else:
                total_time = self.total_time

            # Use total_time to determine the image size. Using time instead of difference
            #   in states like the previous iterations allows the circle to expand linearly.
            self.xysize[0] = self.rate * total_time
            self.xysize[1] = self.rate * total_time

            # Transforms the image into new size
            t = Transform(self.start_image, xanchor=0.5, yanchor=0.5, xysize=self.xysize)

            # Renders child with the transform
            #   The first 1080 is Width and the second 1080 is height.
            #   If left to there default values (1920, 1080) the image would be stretched
            child_render = renpy.render(t, 1080, height, st, at)

            # Gets width and height of child rendering
            cw, ch = child_render.get_size()

            # Renders the image based on width and height of child rendering
            rv = renpy.Render(cw, ch)

            # Draws the image onto the screen
            rv.blit(child_render, (0,0))

            # If the rate is not zero, will redraw itself
            if self.rate:
                renpy.redraw(self, 0)

            return rv

        # Handles the spacebar
        def event(self, ev, x, y, st):

            # How fast size increases.
            RATE = .2

            # If spacebar is pressed down, will start to increase image
            if ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_SPACE and self.rate == 0:
                    self.rate = RATE
                    # Initializes the beginning state
                    self.start_st = st
                    renpy.redraw(self, 0)
                    raise renpy.IgnoreEvent()
            # If spacebar is no longer being pressed, will stop the image
            elif ev.type == pygame.KEYUP:
                if ev.key == pygame.K_SPACE:
                    if self.start_st is not None:
                        # Getting the time
                        self.total_time += st - self.start_st
                        self.start_st = None
                        # Checks to see if the red circle is within the black circle using time
                        #   Issue with this is that if the rate changes then the time will also have to change
                        #   At least it works for now though
                        if self.total_time > 2.18 and self.total_time < 2.60:
                            # I have it return the time so that I can get a general guideline how how long
                            #   it takes for the red circle to overlap the black circle.
                            renpy.call("success", self.total_time)
                            return
                        else:
                            renpy.call("failure", self.total_time)
                            return
                    self.rate = 0
                    raise renpy.IgnoreEvent()

            return None

screen test:
    add IncreaseCircle("circle red.png") at truecenter

label start:

    scene white
    show circle outside at truecenter
    "start"
    # show circle red at beginning
    call screen test
    jump end

    label success(time):
        
        "I made it!"
        "[time]"
        return

    label failure(time):
    
        "I failed!"
        "[time]"
        return


label end:
    "End"

    return
