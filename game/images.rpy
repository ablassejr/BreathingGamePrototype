image bg gradient = Movie(size=(1920, 1080), channel="movie_dp", play="images/bg white gradient.webm")

image circle red1 = Image("circles/circle red.svg")
image circle green1 = Image("circles/circle green.svg")

#bg
image bg calm1 = im.Scale("bg/bg calm 1.png", 1920, 1080)
image bg calm2 = im.Scale("bg/bg calm 2.png", 1920, 1080)
image bg neutral = im.Scale("bg/bg default.png", 1920, 1080)
image bg stress1 = im.Scale("bg/bg stress 1.png", 1920, 1080)
image bg stress2 = im.Scale("bg/bg stress 2.png", 1920, 1080)

#scribbles
image scribble calm1 = im.Scale("scribbles/scribbles calm 1.png", 1920, 1080)
image scribble calm2 = im.Scale("scribbles/scribbles calm 2.png", 1920, 1080)
image scribble neutral = im.Scale("scribbles/scribbles default.png", 1920, 1080)
image scribble stress1 = im.Scale("scribbles/scribbles stress 1.png", 1920, 1080)
image scribble stress2 = im.Scale("scribbles/scribbles stress 2.png", 1920, 1080)
image breathe bar = im.Scale("bar.png", 1920, 1080)

#character
image celia calm1 = im.Scale("character/sprite calm 1.png", 1920, 1080, ypos=1.10)
image celia calm2 = im.Scale("character/sprite calm 2.png", 1920, 1080, ypos=1.10)
image celia neutral = im.Scale("character/sprite default.png", 1920, 1080, ypos=1.10)
image celia stress1 = im.Scale("character/sprite stress 1.png", 1920, 1080, ypos=1.0)
image celia stress2 = im.Scale("character/sprite stress 2.png", 1920, 1080, ypos=1.0)
image celia success = im.Scale("character/sprite success.png", 1920, 1080, ypos=1.0)
image celia fail = im.Scale("character/sprite fail.png", 1920, 1080, ypos=1.0)
image celia perfect = im.Scale("character/sprite perfect 2.png", 1920, 1080, ypos=1.0)