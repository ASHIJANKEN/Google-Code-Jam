from math import sqrt, cos, sin, radians

def detect_error(list):
  error = 'OK';
  for i in range(len(list) - 1):
    if list[i] > list[i + 1]:
      error = i
      break;
  return error

t = int(input('')) # read a line with a single integer

for case in range(1, t + 1):
  area = float(input(''))
  angle = 0;
  max_angle = 90
  found = False

  while angle < max_angle:
    if area - 0.000001 < sqrt(2) * cos(radians(angle)) <  area +  0.000001:
      found = True
      break

    angle += 1

  if found == False:
    angle = 0
    while angle < max_angle:
      if area - 0.000001 < sqrt(2) * cos(radians(angle)) <  area +  0.000001:
        break

      angle += 0.000001

  red_angle = angle + 45

  red_y = 0.5 * sin(radians(red_angle))
  red_x = 0.5 * cos(radians(red_angle))

  blue_angle = angle - 45

  blue_y = 0.5 * sin(radians(blue_angle))
  blue_x = 0.5 * cos(radians(blue_angle))


  print("Case #{}:".format(case))
  print("{} {} {}".format(red_y, red_x, 0))
  print("{} {} {}".format(blue_y, blue_x, 0))
  print("{} {} {}".format(0, 0, 0.5))
