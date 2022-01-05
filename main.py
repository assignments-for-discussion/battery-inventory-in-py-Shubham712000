
def count_batteries_by_usage(cycles):
  return {
    "lowCount": 0,
    "mediumCount": 0,
    "highCount": 0
  }


def test_bucketing_by_number_of_cycles():
  lowCount=0,mediumCount=0,highCount=0
  print("Counting batteries by usage cycles...\n");
  arr=[100, 300, 500, 600, 900, 1000]
  for i in range(0,len(arr)):
      if arr[i]<400:
          lowCount=lowCount+1
      elif 400<=arr[i]<919:
          mediumCount=mediumCount+1
      else:
          highCount=highCount+1
  return lowCount,mediumCount,highCount


if __name__ == '__main__':
  test_bucketing_by_number_of_cycles()
