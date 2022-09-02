def count_batteries_by_usage(cycles):
    high=0
    medium=0
    low=0
    for i in range (0,6):
        if cycles[i]<400:
            low+=1
        elif (cycles[i]>400 and cycles[i]<919):
            medium+=1
        elif cycles[i]>=920:
            high+=1
    print(low)
    print(medium)
    print(high)
    
    return

def test_bucketing_by_number_of_cycles():
  print("Counting batteries by usage cycles...\n");
  counts = count_batteries_by_usage([100, 300, 500, 600, 900, 1000])
  print("Done counting :)")


if __name__ == '__main__':
  test_bucketing_by_number_of_cycles()
