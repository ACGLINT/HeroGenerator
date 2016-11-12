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

prefs   = readfile('prefs.txt')
things  = readfile('things.txt')
classes = readfile('classes.txt')
weapons = readfile('weapons.txt')
weaponp = readfile('weaponprefix.txt')
attack1 = readfile('attack1.txt')
attack2 = readfile('attack2.txt')
talentp = readfile('talentp.txt')
talents = readfile('talents.txt')


def gen():
  return (c(name()) + ', the ' + chc(prefs) + ' ' + chc(classes) + ' of ' + chc(prefs) + ' ' + chc(things) + '\n' +
        'Weapon: ' + c(chc(weaponp)) + ' ' + c(chc(weapons)) + '\n' +
        'Attack: ' + c(chc(attack1)) + ' ' + c(chc(attack2)) + '\n' +
        'Talent: ' + c(chc(talentp)) + ' ' + c(chc(talents)))

if __name__ == '__main__':
    while not raw_input():
        print gen()
