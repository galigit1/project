from asyncio.windows_events import NULL
import math
import sys
from unittest.util import _MAX_LENGTH
from xmlrpc.client import MAXINT

neutral = True

def do_turn(pw):
    if len(pw.my_fleets()) >= 1:
        return

    if len(pw.my_planets()) == 0:
        return

    if (neutral):
        attack_closest_natural(pw)
        neutral = False
    
    else:
        attack_anemy_natural(pw)
        neutral = True        

    '''
    if len(pw.neutral_planets()) >= 1:
        dest = pw.neutral_planets()[0]
    else:
        if len(pw.enemy_planets()) >= 1:
            dest = pw.enemy_planets()[0]

    source = pw.my_planets()[0]
    
    num_ships = source.num_ships() / 2
    pw.debug('Num Ships: ' + str(num_ships))

    pw.issue_order(source, dest, num_ships)
    '''

def attack_closest_natural(pw):
    src = pw
    dst = cloasest_natural(pw)
    num_ships = src.num_ships() / 2
    pw.debug('Num Ships: ' + str(num_ships))

    pw.issue_order(src, dst, num_ships)
    
def avg_growth_natural(pw):
    planets = pw.planets()
    num = 0
    for planet in planets:
        num += planet.growth_rate()
    avg = num/(len(planets))
    return avg

def above_avg_list(pw):
    planets = pw.planets()
    list_planets = []
    for planet in planets:
        if planet.growth_rate() > avg_growth_natural():
            list_planets.append(planet)
    return list_planets


def cloasest_natural(pw):
    planets = above_avg_list(pw)
    closest = NULL
    min_length = sys.maxsize
    length = 0
    for planet in planets:
        length = pw.total_trip_length(planet)
        if length < min_length:
            closest = planet
            min_length = length

    return closest

def attack_anemy_natural(pw):
    pass
