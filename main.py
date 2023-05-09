import functions, time

start = time.time()
print(functions.WeightedRandom({"obj":2,"obj2":3,"obj3":5}))
print(time.time()-start)