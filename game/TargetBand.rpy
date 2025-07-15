init python:
  class TargetBand(renpy.Displayable):
    def __init__(self, image, x_size, y_size):
      super(TargetBand, self).__init__()  # Initialize the parent class
      self.start_image = Image(image)  # Convert string to Image displayable
      # Default target size
      self.xysize = [x_size, y_size]  # Default size for the target band
    #   global x2
    #   x2 = x_size

    def render(self, width=0, height=0, st=0, at=0):
      # Transforms the image into the random size given in the constructor. Also need this 
      #   to add the anchors to the image. Without them it would become unaligned as it grows smaller/bigger.
      t = Transform(self.start_image, xanchor=0.5, yanchor=0.5, xysize=self.xysize)

      # Render the image displayable
      child_render = renpy.render(t, width, height, st, at)
      cw, ch = self.xysize
      self.xysize = [cw, ch]  # Update target size based on rendered image
                                # The line above will not work for the IncreaseCircle parameter. I don't
                                # believe it gets to this line before passing through the size. It would be 
                                # better for it to be simply a global variable instead, but the size is so large
                                # compared to the blue circle that it I believe it would be pointless. We need to
                                # talk in more detail about this. -Christian
      global target_x, target_y
      target_x = cw / 1080
      target_y = ch / 1080
    
      rv = renpy.Render(cw, ch)
      rv.blit(child_render, (0, 0))
      return rv