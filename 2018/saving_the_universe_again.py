def calc_damage(instrs):
  damage = 0
  beam = 1

  for i in range(len(instrs)):
    if instrs[i] == 'S':
      damage += beam
    elif instrs[i] == 'C':
      beam *= 2

  return damage

t = int(input('')) # read a line with a single integer
for case in range(1, t + 1):
  shield, robot_instrs = input().split(" ")
  shield = int(shield)
  robot_instrs = list(robot_instrs)

  swap_count = 0

  while shield < calc_damage(robot_instrs):
    is_changed = False
    for i in range(len(robot_instrs) - 1):
      if robot_instrs[i] == 'C' and robot_instrs[i+1] == 'S':
        robot_instrs[i], robot_instrs[i+1] = robot_instrs[i+1], robot_instrs[i]
        swap_count += 1
        is_changed = True
        if shield >= calc_damage(robot_instrs):
          break
    if is_changed == False:
      swap_count = 'IMPOSSIBLE'
      break

  print("Case #{}: {}".format(case, swap_count))
