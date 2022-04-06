from ursina import *
from Pyramid_4 import Piramid_4
from math import acos, degrees


class Area(Ursina):
    def __init__(self):
        super().__init__()
        window.color = color.white
        EditorCamera()
        camera.world_position = (0, 3, 15)
        self.piramid = None
        self.a = None
        self.h = None
        self.d = None
        self.P = None
        self.K = None
        self.PK = None
        self.AK = None
        self.BP = None
        self.txP = None
        self.tP = None
        self.txK = None
        self.tK = None
        self.load_area()

    def load_area(self):
        self.piramid = Piramid_4(40, 20)
        self.piramid.build()
        self.a = self.piramid.a
        self.h = self.piramid.h
        self.d = self.piramid.d

    def etap1(self):
        for i in self.piramid.rs:
            i.color = color.gray
        self.piramid.hp.color = color.gray
        self.piramid.d1.color = color.gray
        self.piramid.d2.color = color.gray
        for i in self.piramid.ts:
            i.color = color.black
        self.P = Entity(model='sphere', color=color.black, scale=0.2, x=self.a / 4, y=self.h / 2,
                        z=self.a / 4)
        self.K = Entity(model='sphere', color=color.black, scale=0.2, x=self.a / 4, y=self.h / 2,
                        z=-self.a / 4)
        self.PK = Entity(model=Cylinder(), color=color.black, scale=(0.1, self.a / 2, 0.1), rotation_x=90,
                         x=self.K.x, y=self.K.y, z=self.K.z)
        AK = (self.d**2 * (0.25 + self.a ** 2 / (2 * self.d ** 2))) ** 0.5
        del_x = degrees(acos(self.h / (2*AK)))
        self.AK = Entity(model=Cylinder(), color=color.black, scale=(0.1, AK, 0.1), rotation_y=71.5, rotation_x=del_x,
                         x=-self.a/2, z=-self.a/2)
        self.BP = Entity(model=Cylinder(), color=color.black, scale=(0.1, AK, 0.1), rotation_y=108.5, rotation_x=del_x,
                         x=-self.a/2, z=self.a/2)
        self.txP = Text(text="P", x=self.a / 4, z=self.a / 4, y=self.h / 2, background=False, parent=scene, scale=50,
                        color=color.red)
        self.tP = Text(text="P", x=self.a / 4, z=self.a / 4, y=self.h / 2, background=False, parent=scene, scale=50,
                       color=color.red, rotation_y=180)
        self.txK = Text(text="K", x=self.a / 4, y=self.h / 2, z=-self.a / 3.73, background=False, parent=scene,
                        scale=50,
                        color=color.red)
        self.tK = Text(text="K", x=self.a / 4, y=self.h / 2, z=-self.a / 4, background=False, parent=scene, scale=50,
                       color=color.red, rotation_y=180)

    def input(self, key):
        super().input(key)
        if key == '1':
            self.etap1()


if __name__ == '__main__':
    area = Area()
    area.run()
