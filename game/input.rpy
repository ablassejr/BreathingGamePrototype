init python:
    status = 0 

    # Have to import pygame to check for spacebar is held down
    import pygame

    # Class for the increasing circle
    class IncreaseCircle(renpy.Displayable):
        def __init__(self,image, targetSize, difficulty=0.5):
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

            self.reset_timer = 0.0
            self.difficulty = difficulty
            self.targetSize = targetSize  # Target size to compare against

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
            if self.reset_timer == 0.0:
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
            RATE = self.difficulty

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
                        global status # ensure to declare you are using the global variable
                        global attempts
                        global successful_attempts
                        breathe = Breathing()
                        inputWindow = .03

                        # Used for debugging size checks
                        # global x1
                        # global y1
                        # global x2
                        # global y2
                        # x1 = self.xysize[0]
                        # y1 = self.xysize[1]
                        # x2 = self.targetSize[0]
                        # y2 = self.targetSize[1]

                        if abs(self.xysize[0] - self.targetSize[0]) < inputWindow and abs(self.xysize[1] - self.targetSize[1]) < inputWindow: ## change to size
                            status += 1
                            successful_attempts += 1
                            # renpy.show("circle green1")
                            breathe.characterStateChanger()
                            return
                        else:
                            status -= 1
                            breathe.characterStateChanger()
                            return
                    self.rate = 0
                    raise renpy.IgnoreEvent()

            return None

screen test:
    add TargetBand("images/circles/circle green.svg") at startingPosition as target
    add IncreaseCircle("circles/circle blue.svg", target.xysize, 0.2) at startingPosition