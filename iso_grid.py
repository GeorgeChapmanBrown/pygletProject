import pyglet
import math
import numpy as np
ball_image = pyglet.image.load('Assets\\\\BeachBall.png')
slider_image = pyglet.image.load('Assets\\\\WhiteNeonSliderBorder.png')
slider_sprite = pyglet.sprite.Sprite(img=slider_image)

ball_sequence=pyglet.image.ImageGrid(ball_image, 1,12,column_padding=30)
ball_anim=pyglet.image.Animation.from_image_sequence(ball_sequence[0:11],0.1)
ball_anim_reverse=pyglet.image.Animation.from_image_sequence(ball_sequence[11:0:-1],0.1)

window = pyglet.window.Window(resizable=True,width=1300)
sprite2 = pyglet.sprite.Sprite(img=ball_anim,x=0,y=10)

spriteForward = pyglet.sprite.Sprite(img=ball_anim,x=10,y=10)
spriteReverse = pyglet.sprite.Sprite(img=ball_anim_reverse,x=10,y=10)

circumference=ball_sequence.height/2  *math.pi
distincePerFrame=circumference/12
sliderWidth=915


#10 pixel by 10 pixel boundries with a 2/1 ratio

lineRatio=1/2

[50*i for i in range[]]

windowStart=[100,100]
windowSize=[500,500]
numberOfGrids=50









def on_mouse_press(x, y, button, modifiers):
    print(x)

def on_mouse_release(x, y, button, modifiers):
    print(x)



@window.event
def on_mouse_drag(x, y, dx, dy, buttons, modifiers):
    window.clear()
    slider_sprite.draw()
    if (x-dx>spriteForward.x and x-dx<spriteForward.x+spriteForward.width):
        if(y-dy>spriteForward.y and y-dy<spriteForward.y+spriteForward.height):

            x-=spriteForward.width/2
            y-=spriteForward.height/2
            if(x>sliderWidth):
                x=sliderWidth
            if(x<10):
                x=10
            spriteForward.x=x
            curFrame=np.digitize([x%circumference],boundries)
            print(curFrame)
            spriteForward.image=ball_sequence[curFrame[0]]

    spriteForward.draw()


@window.event
def on_draw():
    '''
    window.clear()
    slider_sprite.draw()

    spriteForward.draw()

    if sprite2.x==0:
        spriteForward.x = spriteForward.x + 25
    else:
        spriteForward.x = spriteForward.x - 25
    if (spriteForward.x >= 905):
        sprite2.x = 1
        spriteForward.image=ball_anim_reverse
    if (spriteForward.x <= 10):
        sprite2.x = 0
        spriteForward.image=ball_anim
    '''


pyglet.app.run()