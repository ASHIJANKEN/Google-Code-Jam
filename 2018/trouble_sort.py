def detect_error(list):
  error = 'OK';
  for i in range(len(list) - 1):
    if list[i] > list[i + 1]:
      error = i
      break;
  return error

t = int(input('')) # read a line with a single integer
cases = []

for case in range(t):
  cases.append([int(input('')), input('')])
  cases[case][1] = [int(s) for s in cases[case][1].split(" ")]

for case in range(len(cases)):
  done = False
  while not done:
    done = True
    for i in range(cases[case][0]-2):
      if cases[case][1][i] > cases[case][1][i+2]:
        done = False
        cases[case][1][i], cases[case][1][i+2] = cases[case][1][i+2], cases[case][1][i] 

  print("Case #{}: {}".format(case+1, detect_error(cases[case][1])))
