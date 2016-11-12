from random import choice as chc, randint as rnd
import os


def name():
    r = rnd(3, 6)
    s = rnd(0, 1)
    d = []
    for x in xrange(r):
        if x & 1 == s:
            d.append(chc(k))
        else:
            d.append(chc(v))
    return ''.join(d)

def readfile(file):
  with open(os.path.join(base, file)) as f:
    return filter(lambda x: x and not x.startswith('#'),
      map(lambda x: (x.split('#')[0] if '#' in x else x).strip(), f.readlines()))

c = str.capitalize


k = 'z,x,w,v,t,s,r,q,p,n,m,l,k,j,h,g,f,d,c,b'.split(',')
v = 'a,e,i,o,u,y'.split(',')

base = os.path.split(__file__)[0]

feel   = readfile('feel.txt') # emotions
mob = readfile('mob.txt') # monsters npcs w/e
weapons = readfile('weapons.txt') #
weaponp = readfile('weaponprefix.txt') #
talentp = readfile('eventp.txt') #
events = readfile('events.txt') #


def gen():
  return (c + chc(events) + 'You encounter '(name()) + ', a very ' + chc(feel) + ' ' + chc(mob) + ' wielding a ' +chc(weaponprefix.txt) + ' ' + chc(weapons) + '\n' +

if __name__ == '__main__':
    while not raw_input():
        print gen()
