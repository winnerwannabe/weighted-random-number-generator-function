import random, inspect

def WeightedRandom(dict, chosen = 1, ShowList = False, ShowChance = False):
  frameinfo = inspect.getframeinfo(inspect.currentframe().f_back)
  if not isinstance(dict, type({})):
    exit("argument 1 is not a dictionary. Please change it to a dictionary. (file: "+str(frameinfo.filename)+", line "+str(frameinfo.lineno)+")")

  print()
  for i in dict.values():
    if not isinstance(i, int):
      exit("argment 1 contains a value that is not an iteger. Please make sure all values in argument 1 are itegers.")
  if not isinstance(chosen, int):
    exit("Argument 2 is not an integer. Please make argument 2 an integer.")
  randomList = random.choices(list(dict.keys()), weights=(dict.values()), k = chosen)
  if ShowList:
    print(list(dict.keys()))
  if ShowChance:
    print("chance per point: " + "%.2f"%(1/sum(dict.values())))
  return(randomList)
    