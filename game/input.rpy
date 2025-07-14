
init python:
    import pygame

    class IncreaseCircle(renpy.Displayable):
        delayTime = 0.5  # Reset delay time in seconds        
        def __init__(self, image, targetSize, difficulty=0.5):
            super(IncreaseCircle, self).__init__()
            self.start_image = Image(image)  # Convert string to Image displayable
            self.xysize = [0, 0]
            self.rate = 0.0
            # The beginning state of when the spacebar begins to be held
            self.start_st = 0
            self.last_st = 0  # Initialize this
            # Total time the space bar is being held
            self.total_time = 0.0
            # Delay for resetting the image - start at 0.0, not 0.5
            self.reset_timer = 0.0
            self.difficulty = difficulty
            self.targetSize = targetSize  # Target size to compare against
        # Renders the image onto the screen
        def render(self,width,height,st,at):
            # Handle growth when spacebar is held
            if self.rate != None and self.start_st != None:
                # Will calculate how long the spacebar has been held
                time_held = st - self.start_st
                # The time held is added to the total amount of time it is held
                total_time = self.total_time + time_held
            else:
                total_time = self.total_time
                
            if self.reset_timer == 0.0:
                self.xysize[0] = self.rate * total_time
                self.xysize[1] = self.rate * total_time

            # Transforms the image into new size
            t = Transform(self.start_image, xanchor=0.5, yanchor=0.5, xysize=self.xysize)
            child_render = renpy.render(t, 1080, height, st, at) 
            cw, ch = child_render.get_size()
            rv = renpy.Render(cw, ch)
            rv.blit(child_render, (0, 0))
            if self.rate:
                renpy.redraw(self, 0)


            return rv

        def event(self, ev, x, y, st):
            RATE = self.difficulty
            if ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_SPACE:
                    self.rate = RATE
                    self.start_st = st  # Set start time when key is pressed
                    self.last_st = st
                    renpy.redraw(self, 0)
                    raise renpy.IgnoreEvent()
            elif ev.type == pygame.KEYUP:
                if ev.key == pygame.K_SPACE:
                    if self.start_st is not None:
                        # Getting the time
                        self.total_time += st - self.start_st
                        self.start_st = None
                        global status # ensure to declare you are using the global variable
                        global attempts
                        global successful_attempts
                        breathe = Breathing()
                        inputWindow = 100  # Define the input window size
                        if abs(self.xysize[0] - self.targetSize[0]) < inputWindow and abs(self.xysize[1] - self.targetSize[1]) < inputWindow:
                            status += 1
                            successful_attempts += 1
                            renpy.show("images/circles/circle green.svg")
                            breathe.characterStateChanger()
                            return
                        else:
                            status -= 1
                            breathe.characterStateChanger()
                            return
                    self.rate = 0
                    raise renpy.IgnoreEvent()

screen test:
    add TargetBand("images/circles/circle green.svg") at startingPosition as target
    add IncreaseCircle("images/circles/circle blue.svg", target.xysize, 0.5) at startingPosition