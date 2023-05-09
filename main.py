import functions

dict = {
  "obj":2,
  "obj2":3,
  "obj3":5
}

print(*functions.WeightedRandom(dict))