init python:
    import pygame

    class IncreaseCircle(renpy.Displayable):
        delayTime = 0.5  # Reset delay time in seconds        
        def __init__(self, image, difficulty=0.5):
            super(IncreaseCircle, self).__init__()
            self.start_image = Image(image)  # Convert string to Image displayable
            self.xysize = [0, 0]
            self.rate = 0.0
            self.last_st = 0.0
            self.difficulty = difficulty
            self.reset_timer = 0.0  # Marker for reset delay
            
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

            return None

    config.layers.append("top")



screen test(difficulty=0.5):
    add IncreaseCircle ("circle blue.svg", difficulty) at startingPosition
    add TargetBand ("circle red.png") at startingPosition
    