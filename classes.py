from pyray import * 
import math
# This is where you put classes 

class Guy:
    def __init__(self, pos_vec : Vector2, dir_vec : Vector2):
        self.pos_vec = pos_vec
        self.dir_vec = dir_vec
        self.i= 0
        self.texture = load_texture("data/gfx/sleigh.png")
    def update(self):
        self.i += 1
        self.pos_vec = vector2_add(self.pos_vec, self.dir_vec)
        self.pos_vec.x = math.sin(self.i/60) * 100
    def draw(self):
        draw_texture_v(self.texture, self.pos_vec, WHITE)

class Present:
    def __init__(self, pos_vec: Vector2, dir_vec: Vector2):
        self.pos_vec = pos_vec
        self.dir_vec = dir_vec
        self.collrec = Rectangle(0, 0, 0, 0)
    def update(self):
        self.pos_vec = vector2_add(self.pos_vec, self.dir_vec)
        self.collrec = Rectangle(self.pos_vec.x, self.pos_vec.y, 20, 20)
    def draw(self):
        draw_rectangle_v(self.pos_vec, Vector2(20, 20), YELLOW)

class House:
    def __init__(self, pos_vec: Vector2, dir_vec: Vector2):
        self.pos_vec = pos_vec
        self.dir_vec = dir_vec
        self.texture = load_texture("data/gfx/house.png")
        self.delivered = False
    def update(self):
        self.pos_vec = vector2_add(self.pos_vec, self.dir_vec)
        self.collrec = Rectangle(self.pos_vec.x, self.pos_vec.y, self.texture.width, self.texture.height)

    def draw(self):
        draw_texture_v(self.texture, self.pos_vec, WHITE)