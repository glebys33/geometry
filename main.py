import colorama
from ursina import *
from Pyramid_4 import Piramid_4
from math import acos, degrees


class Area(Ursina):
    def __init__(self):
        super().__init__()
        window.color = color.white
        Entity(model='quad', color=color.light_gray, scale=200, y=-5, rotation_x=90, texture='white_cube',
               texture_scale=(200, 200))
        EditorCamera()
        camera.world_position = (0, 0, 15)
        self.load_area()

    def load_area(self):
        self.piramid = Piramid_4()
        self.piramid.build()
        self.a = self.piramid.a
        self.h = self.piramid.h
        self.d = self.piramid.d

    def etap1(self):
        self.P = Entity(model='sphere', color=color.black, scale=0.2, x=self.a / 4, y=self.h / 2,
                        z=self.a / 4)
        self.K = Entity(model='sphere', color=color.black, scale=0.2, x=self.a / 4, y=self.h / 2,
                        z=-self.a / 4)
        self.PK = Entity(model=Cylinder(), color=color.black, scale=(0.1, self.a / 2, 0.1), rotation_x=90,
                         x=self.K.x, y=self.K.y, z=self.K.z)
        AK = (self.d**2 * (0.25 + self.a ** 2 / (2 * self.d ** 2))) ** 0.5
        del_x = degrees(acos(self.h / (2*AK)))
        self.AK = Entity(model=Cylinder(), color=color.black, scale=(
        0.1, AK, 0.1), rotation_y=71.5, rotation_x=del_x, x=-10, z=-10)

    def input(self, key):
        super().input(key)
        if key == '1':
            self.etap1()
        elif key == '=':
            self.AK.rotation_x -= 1
        elif key == 'q':
            self.AK.rotation_y += 1
        elif key == 'a':
            self.AK.rotation_y -= 1


if __name__ == '__main__':
    area = Area()
    area.run()
