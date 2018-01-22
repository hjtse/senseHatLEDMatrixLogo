from sense_hat import SenseHat
import time

sense = SenseHat()

g = (255, 180, 0) #gold
w = (255,255,255) #white
e = (0,0,0) #empty
  
pic0 = [
    g,g,g,g,g,e,e,e,
    g,e,e,e,e,e,e,e,
    g,e,g,g,g,e,e,e,
    g,e,e,w,g,w,w,w,
    g,e,e,e,g,w,e,e,
    g,g,g,g,g,w,e,e, 
    e,e,e,e,e,w,e,e,
    e,e,e,e,e,w,e,e
    ]

  
pic1 = [
    g,g,g,g,g,e,e,e,
    e,e,e,e,e,e,e,e,
    e,e,e,e,e,e,e,e,
    e,e,e,e,e,e,e,e,
    e,e,e,e,e,e,e,e,
    e,e,e,e,e,e,e,e,
    e,e,e,e,e,e,e,e,
    e,e,e,e,e,e,e,e,
    ]

pic2 = [
    e,e,e,e,e,e,e,e,
    g,e,e,e,e,e,e,e,
    e,e,e,e,e,e,e,e,
    e,e,e,e,e,e,e,e,
    e,e,e,e,e,e,e,e,
    e,e,e,e,e,e,e,e,
    e,e,e,e,e,e,e,e,
    e,e,e,e,e,e,e,e
    ]

pic3 = [
    e,e,e,e,e,e,e,e,
    e,e,e,e,e,e,e,e,
    g,e,g,g,g,e,e,e,
    e,e,e,e,e,e,e,e,
    e,e,e,e,e,e,e,e,
    e,e,e,e,e,e,e,e,
    e,e,e,e,e,e,e,e,
    e,e,e,e,e,e,e,e
    ]

pic4 = [
    e,e,e,e,e,e,e,e,
    e,e,e,e,e,e,e,e,
    e,e,e,e,e,e,e,e,
    g,e,e,w,g,w,w,w,
    e,e,e,e,e,e,e,e,
    e,e,e,e,e,e,e,e,
    e,e,e,e,e,e,e,e,
    e,e,e,e,e,e,e,e
    ]

pic5 = [
    e,e,e,e,e,e,e,e,
    e,e,e,e,e,e,e,e,
    e,e,e,e,e,e,e,e,
    e,e,e,e,e,e,e,e,
    g,e,e,e,g,w,e,e,
    e,e,e,e,e,e,e,e,
    e,e,e,e,e,e,e,e,
    e,e,e,e,e,e,e,e
    ]

pic6 = [
    e,e,e,e,e,e,e,e,
    e,e,e,e,e,e,e,e,
    e,e,e,e,e,e,e,e,
    e,e,e,e,e,e,e,e,
    e,e,e,e,e,e,e,e,
    g,g,g,g,g,w,e,e,
    e,e,e,e,e,e,e,e,
    e,e,e,e,e,e,e,e
    ]

pic7 = [
    e,e,e,e,e,e,e,e,
    e,e,e,e,e,e,e,e,
    e,e,e,e,e,e,e,e,
    e,e,e,e,e,e,e,e,
    e,e,e,e,e,e,e,e,
    e,e,e,e,e,e,e,e,
    e,e,e,e,e,w,e,e,
    e,e,e,e,e,e,e,e
    ]

pic8 = [
    e,e,e,e,e,e,e,e,
    e,e,e,e,e,e,e,e,
    e,e,e,e,e,e,e,e,
    e,e,e,e,e,e,e,e,
    e,e,e,e,e,e,e,e,
    e,e,e,e,e,e,e,e,
    e,e,e,e,e,e,e,e,
    e,e,e,e,e,w,e,e
    ]



sense.clear


for i in range(10):
    sense.set_pixels(pic1)
    time.sleep(2)
    sense.set_pixels(pic2)
    time.sleep(2)
    sense.set_pixels(pic3)
    time.sleep(2)
    sense.set_pixels(pic4)
    time.sleep(2)
    sense.set_pixels(pic5)
    time.sleep(2)
    sense.set_pixels(pic6)
    time.sleep(2)
    sense.set_pixels(pic7)
    time.sleep(2)
    sense.set_pixels(pic8)
    time.sleep(2)
    


