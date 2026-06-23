from ursina import *
import math

app = Ursina()

window.title = "Interactive Solar System"

Sky(texture='textures/space.jpg')
EditorCamera()

DirectionalLight()
AmbientLight(color=color.rgba(180,180,180,0.6))


class Planet(Entity):
    def __init__(self, texture, orbit_radius, orbit_speed, scale):
        super().__init__(
            model='sphere',
            texture=texture,
            scale=scale
        )

        self.orbit_radius = orbit_radius
        self.orbit_speed = orbit_speed
        self.base_speed = orbit_speed      # NEW
        self.angle = 0

    def update(self):
        self.angle -= self.orbit_speed * time.dt

        self.x = math.cos(math.radians(self.angle)) * self.orbit_radius
        self.z = math.sin(math.radians(self.angle)) * self.orbit_radius

        self.rotation_y += 30 * time.dt


# ---------------- Sun ----------------

sun = Entity(
    model='sphere',
    texture='textures/2k_sun.jpg',
    scale=2.5
)

# --------------- Planets -------------

mercury = Planet('textures/2k_mercury.jpg',3,60,0.20)
venus = Planet('textures/2k_venus.jpg',4,45,0.35)
earth = Planet('textures/2k_earth.jpg',5.5,35,0.38)
mars = Planet('textures/2k_mars.jpg',7,28,0.30)
jupiter = Planet('textures/2k_jupiter.jpg',9,20,0.80)

saturn = Planet('textures/2k_saturn.jpg',12,16,0.70)

saturn_ring = Entity(
    parent=saturn,
    model='quad',
    texture='textures/saturn_ring.png',
    scale=4,
    rotation_x=90,
    double_sided=True
)

uranus = Planet('textures/2k_uranus.jpg',15,12,0.55)
neptune = Planet('textures/2k_neptune.jpg',18,10,0.55)


# ---------- Speed Control ----------

speed_multiplier = 1.0

speed_text = Text(
    text="Speed: 1.0x",
    position=(-0.85,0.45),
    scale=1.2,
    background=True
)

controls = Text(
    text=(
        "Controls\n"
        "Right Mouse : Rotate Camera\n"
        "Mouse Wheel : Zoom\n"
        "+ / - : Change Speed"
    ),
    position=(-0.85, 0.15),
    scale=0.9,
    background=True
)


def input(key):
    global speed_multiplier

    if key == '+':
        speed_multiplier += 0.2

    elif key == '-':
        speed_multiplier = max(0.2, speed_multiplier - 0.2)

    planets = [
        mercury, venus, earth, mars,
        jupiter, saturn, uranus, neptune
    ]

    for planet in planets:
        planet.orbit_speed = planet.base_speed * speed_multiplier


# ---------- Update ----------

def update():

    speed_text.text = f"Speed: {speed_multiplier:.1f}x"

    sun.rotation_y += 10 * time.dt

    mercury.update()
    venus.update()
    earth.update()
    mars.update()
    jupiter.update()
    saturn.update()
    uranus.update()
    neptune.update()


app.run()