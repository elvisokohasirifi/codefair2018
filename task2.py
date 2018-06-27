import sys
from datetime import*
def run(a, b):
  mainStart = datetime.now()
  sample = open(a, "r", encoding='utf-8-sig')
  partial = open(b, "r", encoding='utf-8-sig')

  file = open("task2_result-sample_partial_time_series1.txt", "w")

  countries = {} # stores concatenation (separated by commas) of country, indicator and locality as keys. Its values are a list of values that correspond to that country, locality and indicator. 
  alls = {} # stores the concatenation (separated by commas) of country, indicator, locality and value as keys. Its values are a list of dates correspoding to that country, locality, indicator and value
  listP = []
  for item in partial.readlines():
    listP.append(int(item))

  sample.readline()

  for line in sample.readlines():
    country, locality, indicator, d, v = line.split(",")
    if (country + "," + locality + "," + indicator + "," + str(int(v))) in alls:
      alls[country + "," + locality + "," + indicator + "," + str(int(v))].append(d)
    else:
      alls[country + "," + locality + "," + indicator + "," + str(int(v))] = [d]
      
    if (country + "," + locality + "," + indicator) in countries:
      countries[country + "," + locality + "," + indicator].append(int(v))
    else:
      countries[country + "," + locality + "," + indicator] = [int(v)]

  # this loop finds the concatenation (separated by commas) of country, indicator and locality (as key) whose value (a list) contains all the values in the partial time series data
  for key in countries:
    set1 = set(countries[key])
    set2 = set(listP)
    if set2.issubset(set1):
      print("The data is related to", key.split(",")[0], "and the locality is", key.split(",")[1], file = file)      
      print("The indicator is", key.split(",")[2], file = file)
      print("The starting date is", alls[key + "," + str(listP[0])][0], file = file)

  mainEnd = datetime.now()
  print("The runtime for the entire program is", (mainEnd - mainStart).total_seconds() * 1000, "milliseconds", file = file)
if __name__ == "__main__":
    a = sys.argv[1]
    b = sys.argv[2]
    run(a, b)
