import math

def dig_sum(x):
  out = 0
  string = str(x)
  for char in string:
    out += int(char)
  return out

max_sum = 0
for a in range(2,100):
  local_max  = max(map(dig_sum, [a**b for b in range(2,101)]))
  if local_max >= max_sum:
    max_sum = local_max

print(max_sum)
