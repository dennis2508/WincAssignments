# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

# Add your code after this line

def greet(name, greeting = ("Hello, <name>!")):
    x = greeting.replace("<name>",name)
    return x

x = greet("Bob", )
print(x)

body = dict(
    sun = 274.0,
    jupiter = 24.9,
    neptune = 11.2,
    saturn = 10.4,
    earth = 9.8,
    uranus = 8.9,
    venus = 8.9,
    mars = 3.7,
    mercury = 3.7,
    moon = 1.6,
    pluto = 0.6
)
G = 6.674*(10**-11)

def force(mass = float, planet = "earth"):
    y = body[planet]
    x = mass * y
    return x

print(force(11.3,"venus"))

def pull(mass1, mass2, distance):
    x = G * ((mass1*mass2)/(distance**2))
    return x

x = pull(0.1, 5.972*10**24 , 6371*10**3)
print(x)
y = pull(1,1,2)
print(y)