init python:
    import pygame

    class IncreaseCircle(renpy.Displayable):
        delayTime = 0.5  # Reset delay time in seconds        
        def __init__(self, image, targetSize, difficulty=0.5):
            super(IncreaseCircle, self).__init__()
            self.start_image = Image(image)  # Convert string to Image displayable
            self.xysize = [0, 0]
            self.rate = 0.0
            self.last_st = 0.0
            self.difficulty = difficulty
            self.reset_timer = 0.0  # Marker for reset delay
            self.targetSize = targetSize  # Target size for the circle   
            # The beginning state of when the spacebar begins to be held
            self.start_st = None
            # Total time the space bar is being held
            self.total_time = 0.0
            # Delay for resetting the image
            self.reset_timer = 0.5         
        def render(self, width, height, st, at):
            if self.reset_timer > 0:
                if st - self.reset_timer >= self.delayTime:  # Target reset delay
                    self.xysize = [0, 0]
                    self.last_st = st
                    self.reset_timer = 0.0
                    
            # Only grow if not in reset mode
            if self.reset_timer == 0.0:
                self.xysize[0] += self.rate * (st - self.last_st)
                self.xysize[1] += self.rate * (st - self.last_st)
                
            self.last_st = st

           
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

            # Transforms the image into new size
            t = Transform(self.start_image, xanchor=0.5, yanchor=0.5, xysize=self.xysize)
            child_render = renpy.render(t, 1080, height, st, at) 
            cw, ch = child_render.get_size()
            rv = renpy.Render(cw, ch)
            rv.blit(child_render, (0, 0))

            if self.rate != 0 or self.reset_timer > 0:
                renpy.redraw(self, 0)

            return rv

        def event(self, ev, x, y, st):
            RATE = self.difficulty
            if ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_SPACE:
                    self.rate = RATE
                    self.last_st = st
                    renpy.redraw(self, 0)
                    raise renpy.IgnoreEvent()
            elif ev.type == pygame.KEYUP:
                if ev.key == pygame.K_SPACE:
                    if self.rate == RATE:
                        self.rate = 0
                        self.reset_timer = st 
                        renpy.redraw(self, 0)
                        raise renpy.IgnoreEvent()
                    
                    inputWindow = 10
                    if abs(self.xysize[0] - self.targetSize[0]) < inputWindow and abs(self.xysize[1] - self.targetSize[1]) < inputWindow:
                        global status
                        global successful_attempts
                        global attempts
                        status += 1
                        successful_attempts += 1
                        if status > 3:
                            status = 3
                    else:
                        status -= 1
                        if status < -1:
                            status = -1
                    
                    Breathing.characterStateChanger()
                    attempts += 1
                    if attempts >= 3:
                        Breathing.results()

            return None

screen test:
    add TargetBand("circles/circle green.svg") at startingPosition as target
    add IncreaseCircle("circles/circle blue.svg", target.xysize, 0.5) at startingPosition