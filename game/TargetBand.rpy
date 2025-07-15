init python:
  class TargetBand(renpy.Displayable):
    def __init__(self, image):
      super(TargetBand, self).__init__()  # Initialize the parent class
      self.start_image = Image(image)  # Convert string to Image displayable
      # Default target size
      self.xysize = [.36, .36]  # Default size for the target band

    def render(self, width=0, height=0, st=0, at=0):
      # Render the image displayable
      child_render = renpy.render(self.start_image, width, height, st, at)
      cw, ch = child_render.get_size()
      self.xysize = [cw, ch]  # Update target size based on rendered image
                                # The line above will not work for the IncreaseCircle parameter. I don't
                                # believe it gets to this line before passing through the size. It would be 
                                # better for it to be simply a global variable instead, but the size is so large
                                # compared to the blue circle that it I believe it would be pointless. We need to
                                # talk in more detail about this. -Christian
    
      rv = renpy.Render(cw, ch)
      rv.blit(child_render, (0, 0))
      return rv
