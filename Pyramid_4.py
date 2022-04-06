from ursina import *
from math import atan, degrees


class Piramid_4(Ursina):
    def __init__(self, a=20, h=15, r_color=color.gray, d_color=color.gray, h_color=color.gray):
        self.a = a # длина стороны квадрата
        self.h = h # длинна высоты
        self.r_color = r_color # цвет рёбер
        self.d_color = d_color # цвет диогоналей
        self.h_color = h_color # цвет высоты
        self.rs = [] # диогонали
        self.d1 = None # 1-я диогональ
        self.d2 = None # 2-я диогональ
        self.hp = None # высота
        self.d = None

    def build(self):
        # основание
        r = Entity(model=Cylinder(), color=self.r_color, scale=(0.1, self.a, 0.1), rotation_x=90, x=-10, z=-10)
        self.rs.append(r)
        r = Entity(model=Cylinder(), color=self.r_color, scale=(0.1, self.a, 0.1), rotation_x=90, rotation_y=90,
                   x=-10, z=-10)
        self.rs.append(r)
        r = Entity(model=Cylinder(), color=self.r_color, scale=(0.1, self.a, 0.1), rotation_x=90, rotation_y=90,
                   x=-10, z=10)
        self.rs.append(r)
        r = Entity(model=Cylinder(), color=self.r_color, scale=(0.1, self.a, 0.1), rotation_x=90, x=10, z=-10)
        self.rs.append(r)

        # диогонали
        self.d1 = Entity(model=Cylinder(), color=self.d_color, scale=(0.1, self.a*2**0.5, 0.1), rotation_x=90,
                         rotation_y=45 ,x=-10, z=-10)
        self.d2 = Entity(model=Cylinder(), color=self.d_color, scale=(0.1, self.a*2**0.5, 0.1), rotation_x=90,
                         rotation_y=-45 ,x=10, z=-10)

        # высота
        self.hp = Entity(model=Cylinder(), color=self.h_color, scale=(0.1, self.h, 0.1))

        # ребра
        self.d = (self.h**2 + self.a**2/2)**0.5 # длина ребра
        del_x = 90 - degrees(atan(2*self.h / (self.a*2**0.5)))
        r = Entity(model=Cylinder(), color=self.r_color, scale=(0.1, self.d, 0.1), x=-10, z=-10, rotation_x=del_x,
                   rotation_y=45)
        self.rs.append(r)
        r = Entity(model=Cylinder(), color=self.r_color, scale=(0.1, self.d, 0.1), x=-10, z=10, rotation_x=-del_x,
                   rotation_y=-45)
        self.rs.append(r)
        r = Entity(model=Cylinder(), color=self.r_color, scale=(0.1, self.d, 0.1), x=10, z=-10, rotation_x=del_x,
                   rotation_y=-45)
        self.rs.append(r)
        r = Entity(model=Cylinder(), color=self.r_color, scale=(0.1, self.d, 0.1), x=10, z=10, rotation_x=-del_x,
                   rotation_y=45)
        self.rs.append(r)

    def off_all(self):
        for i in self.rs:
            i.disable()
        self.hp.disable()
        self.d1.disable()
        self.d2.disable()

    def off_h(self):
        self.hp.disable()

    def off_ds(self):
        self.d1.disable()
        self.d2.disable()

    def off_d1(self):
        self.d1.disable()

    def off_d2(self):
        self.d2.disable()

    def off_rs(self):
        for i in self.rs:
            i.disable()

    def on_all(self):
        for i in self.rs:
            i.enable()
        self.hp.enable()
        self.d1.enable()
        self.d2.enable()

    def on_h(self):
        self.hp.enable()

    def on_ds(self):
        self.d1.enable()
        self.d2.enable()

    def on_d1(self):
        self.d1.enable()

    def on_d2(self):
        self.d2.enable()

    def on_rs(self):
        for i in self.rs:
            i.enable()
