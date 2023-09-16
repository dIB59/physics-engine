class Particle:
    def __init__(self, x: int, y: int, mass: int, vel_x: float, vel_y: float):
        self.x = x
        self.y = y
        self.mass = mass
        self.vel_x = vel_x
        self.vel_y = vel_y

    def update_position(self, dt: float):
        self.x += self.vel_x * dt
        self.y += self.vel_y * dt

    def get_position(self) -> (int, int):
        return self.x, self.y

    def get_mass(self) -> int:
        return self.mass

    def get_velocity(self) -> (float, float):
        return self.vel_x, self.vel_y

    def set_velocity(self, vel_x: float, vel_y: float):
        self.vel_x = vel_x
        self.vel_y = vel_y

