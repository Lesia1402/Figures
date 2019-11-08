#draw

import turtle as tl
# Dasha
class Square:
  
  
   def show(self):
        tl.up()
        tl.goto(self.x, self.y)
        tl.color(self.color)
        tl.down()
        tl.fillcolor(self.color)
        tl.begin_fill()
        for _ in range (4):
            tl.forward(self.size)
            tl.left(90)
        tl.end_fill()
        
        
 class Triangle:
    # Lesia
    def __init__(self, x, y, size, color):
        self.x = x
        self.y = y
        self.size = size
        self.color = color
     
        
    def show(self):
        tl.up()
        tl.goto(self.x, self.y)
        tl.color(self.color)
        tl.down()
        tl.fillcolor(self.color)
        tl.begin_fill()
        for _ in range (3):
            tl.forward(self.size)
            tl.left(120)
        tl.end_fill()
        
        
 
  

class Parallelogram:
    def __init__(self, x, y, size, length, color, angle):
        self.x = x
        self.y = y
        self.size = size
        self.color = color
        self.angle = angle
        self.length = length
    def show(self):
        tl.up()
        tl.goto(self.x, self.y)
        tl.color(self.color)
        tl.down()
        tl.fillcolor(self.color)
        tl.begin_fill()
        for _ in range (2):
            tl.forward(self.size)
            tl.left(self.angle)
            tl.forward(self.length)
            tl.left(180-self.angle)
        tl.end_fill()
        




#f1 = Parallelogram( 0, 0, 100, 110, "red", 45)
#f1.show()

#f2 = Triangle(0, 60, 60, "black")
#f2.show()

f3= Square( 0, 0, 150, "yellow")
f3.show()

f2 = Triangle(-10, 150, 170, "green")
f2.show()



tl.mainloop()
