from random import choice as chc
import os


def readfile(file):
  with open(os.path.join(base, file)) as f:
    return filter(lambda x: x and not x.startswith('#'),
      map(lambda x: (x.split('#')[0] if '#' in x else x).strip(), f.readlines()))

def gen():
    return chc(nam) + ' Threw a really ' + chc(ver) + ' ' + chc(adv)  + ' ' + chc(obj)


base = os.path.split(__file__)[0]

ver  = readfile('verbs.txt');
adv  = readfile('adverb.txt');
obj  = readfile('object.txt');
nam  = readfile('names.txt');
if __name__ == '__main__':
    while not raw_input():
        print gen()
