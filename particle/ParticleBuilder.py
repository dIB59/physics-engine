class ParticleBuilder:
    def __init__(self, x=0, y=0, mass=1, vel_x=0.0, vel_y=0.0):
        self.x = x
        self.y = y
        self.mass = mass
        self.vel_x = vel_x
        self.vel_y = vel_y

    def set_x(self, x):
        self.x = x
        return self

    def set_y(self, y):
        self.y = y
        return self

    def set_mass(self, mass):
        self.mass = mass
        return self

    def set_vel_x(self, vel_x):
        self.vel_x = vel_x
        return self

    def set_vel_y(self, vel_y):
        self.vel_y = vel_y
        return self

    def build(self):
        return ParticleBuilder(self.x, self.y, self.mass, self.vel_x, self.vel_y)


