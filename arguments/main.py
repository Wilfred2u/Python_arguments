# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

# Add your code after this line


def greet(name, greeting='Hello, <name>!'):
    say_hello = greeting.replace('<name>', name)
    print(say_hello)
    return say_hello


greet('Doc')
greet('Bob', 'What\'s up, <name>!')


planets = {
    'mercury': 3.7,
    'venus': 8.9,
    'earth': 9.8,
    'moon': 1.6,
    'mars': 3.7,
    'jupiter': 23.1,
    'saturn': 9.0,
    'uranus': 8.7,
    'neptune': 11.0,
    'pluto': 0.7,
}


def force(mass, body='earth'):
    gravity = planets.get(body)
    planet_force = mass * gravity
    print(planet_force)
    return planet_force


force(5.97 * 10**24)
force(1898*10**24, body='jupiter')


def pull(m1, m2, d):
    g = 6.674*10**-11
    attraction = (g * (m1 * m2)) / d**2
    print(attraction)
    return (attraction)


pull(800, 1500, 3)
pull(0.1, 5.972*10**24, 6.371*10**6)
