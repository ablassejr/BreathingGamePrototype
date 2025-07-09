init python:
  class TargetBand(renpy.Displayable):
    def __init__(self, image):
      super(TargetBand, self).__init__()  # Initialize the parent class
      self.start_image = Image(image)  # Convert string to Image displayable
      
    def render(self, width=0, height=0, st=0, at=0):
      # Render the image displayable
      child_render = renpy.render(self.start_image, width, height, st, at)
      cw, ch = child_render.get_size()
      rv = renpy.Render(cw, ch)
      rv.blit(child_render, (0, 0))
      return rv

      return None