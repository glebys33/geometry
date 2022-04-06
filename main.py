from ursina import *
from Pyramid_4 import Piramid_4
from math import acos, atan, degrees


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
        self.N = None
        self.PK = None
        self.AK = None
        self.BP = None
        self.SN = None
        self.txP = None
        self.tP = None
        self.txK = None
        self.tK = None
        self.txN = None
        self.tN = None
        self.txT = None
        self.tT = None
        self.load_area()

    def load_area(self):
        self.piramid = Piramid_4(40, 30)
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
        self.N = Entity(model='sphere', color=color.black, scale=0.2, x=self.a / 2)
        del_z = degrees(atan(self.h / (self.a/2)))
        self.SN = Entity(model=Cylinder(), color=color.black, scale=(0.1, (self.d**2 - self.a**2/4)**0.5, 0.1),
                         rotation_z=del_z-90, x=self.a/2)
        self.piramid.rs.append(self.SN)
        self.PK = Entity(model=Cylinder(), color=color.black, scale=(0.1, self.a / 2, 0.1), rotation_x=90,
                         x=self.K.x, y=self.K.y, z=self.K.z)
        self.piramid.rs.append(self.PK)
        AK = (self.d**2 * (0.25 + self.a ** 2 / (2 * self.d ** 2))) ** 0.5
        del_x = degrees(acos(self.h / (2*AK)))
        self.AK = Entity(model=Cylinder(), color=color.black, scale=(0.1, AK, 0.1), rotation_y=71.5, rotation_x=del_x,
                         x=-self.a/2, z=-self.a/2)
        self.piramid.rs.append(self.AK)
        self.BP = Entity(model=Cylinder(), color=color.black, scale=(0.1, AK, 0.1), rotation_y=108.5, rotation_x=del_x,
                         x=-self.a/2, z=self.a/2)
        self.piramid.rs.append(self.BP)
        self.txP = Text(text="P", x=self.a / 4, z=self.a / 3.73, y=self.h / 2, background=False, parent=scene, scale=50,
                        color=color.red)
        self.piramid.ts.append(self.txP)
        self.tP = Text(text="P", x=self.a / 4, z=self.a / 4, y=self.h / 2, background=False, parent=scene, scale=50,
                       color=color.red, rotation_y=180)
        self.piramid.ts.append(self.tP)
        self.txK = Text(text="K", x=self.a / 4, y=self.h / 2, z=-self.a / 3.73, background=False, parent=scene, scale=50,
                        color=color.red)
        self.piramid.ts.append(self.txK)
        self.tK = Text(text="K", x=self.a / 4, y=self.h / 2, z=-self.a / 4, background=False, parent=scene, scale=50,
                       color=color.red, rotation_y=180)
        self.piramid.ts.append(self.tK)
        self.txN = Text(text="N", x=self.a / 2, y=-0.05, background=False, parent=scene, scale=50,
                        color=color.red)
        self.piramid.ts.append(self.txN)
        self.tN = Text(text="N", x=self.a / 2, y=-0.05, background=False, parent=scene, scale=50,
                       color=color.red, rotation_y=180)
        self.piramid.ts.append(self.tN)
        self.txT = Text(text="T", x=self.a / 4 + 0.1, y=self.h/2 + 1, background=False, parent=scene, scale=50,
                        color=color.red)
        self.piramid.ts.append(self.txT)
        self.tT = Text(text="T", x=self.a / 4 + 0.1, y=self.h/2 + 1, background=False, parent=scene, scale=50,
                       color=color.red, rotation_y=180)
        self.piramid.ts.append(self.tT)

    def input(self, key):
        super().input(key)
        if key == '1':
            self.etap1()


if __name__ == '__main__':
    area = Area()
    area.run()
