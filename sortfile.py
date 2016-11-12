import sys

b = sys.argv[1:]

for a in b:
  print a
  with open(a) as f:
    g = map(str.strip, f.readlines())
  
  g = sorted(set(g))
  print ','.join(g)
  with open(a, 'w') as f:
    f.write('\n'.join(g) + '\n')
