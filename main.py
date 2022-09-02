def count_batteries_by_usage(cycles):
    high=0
    medium=0
    low=0
    for i in range (0,6):      #In this for loop we count the number of low,medium and high values and return it 
        if cycles[i]<400:                     
            low+=1
        elif (cycles[i]>400 and cycles[i]<919):
            medium+=1
        elif cycles[i]>=920:
            high+=1

    return {"low":low,"medium":medium,'High':high}

def test_bucketing_by_number_of_cycles():
  print("Counting batteries by usage cycles...\n");
  counts = count_batteries_by_usage([100, 300, 500, 600, 900, 1000])  # counts =print(count_batteries_by_usage([100, 300, 500, 600, 900, 1000])) will return the dict containing the values 
  print("Done counting :)")


if __name__ == '__main__':
  test_bucketing_by_number_of_cycles()
