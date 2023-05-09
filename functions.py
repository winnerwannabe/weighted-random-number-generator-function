import random, inspect

def WeightedRandom(d, ammount = 1, ShowList = False, ShowChance = False): #weighted random number generator. uses random, and inspect(imported to the file where you use it, not here). dict must be a dictionary with it's values all being integers. you must put inspect.currentframe() for argument 2, "frameinfo".
  
  TotalChances = [] #do not touch these two lines.
  chosen = []
  frameinfo = inspect.getframeinfo(inspect.currentframe().f_back)

  if not isinstance(d, dict):
    exit("argument 1 is not a dictionary. Please change it to a dictionary. (file: "+str(frameinfo.filename)+", line "+str(frameinfo.lineno)+")")

  for i in d.values():
    if not isinstance(i, int):
      exit("argment 1 contains a value that is not an iteger. Please make sure all values in argument 1 are itegers.(file: "+str(frameinfo.filename)+", line "+str(frameinfo.lineno)+")")

  if not isinstance(ammount, int):
    exit("Argument 2 is not an integer. Please make argument 2 an integer.(file: "+str(frameinfo.filename)+", line "+str(frameinfo.lineno)+")")
  
  for i in d:#goes through every item in dict
    if isinstance(d[i],int):#determins if the item in dict that the code is currently looking at is an integer
      for x in range(d[i]):#adds the item in dict to a list an amount of times equivelent to it's value in the dictionary
        TotalChances.append(i)
        
    else:#if the item in dict that the code is not an integer, it closes the program
      exit("\""+str(i)+"\"in argument 1 is not a integer. please change all values of the dictionary you used to an integer. (file: "+str(frameinfo.filename)+", line "+str(frameinfo.lineno)+")")
  for i in range(ammount):
    chosen.append(*random.choices(TotalChances))

  if ShowChance:
    print(*TotalChances, sep=", ")
  if ShowList:
    print("chance per point: " + "%.2f"%(1/sum(d.values())))#prints % chance of selecting an item for every point the item has
  return(chosen)#prints the result