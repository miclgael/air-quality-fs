
def read_data(filename):
  data_file = open(filename,'r')
  lines = data_file.readlines()
  output = []
  for line in lines:
    line=line.replace('\n', '')
    output.append(line)
  data_file.close()
  return output


def get_average_dictionary(readings):
  return {}

FILENAME = '/home/michael/studies/python_assignment2/days.txt'

if __name__ == "__main__":
  try:
    readings = read_data(FILENAME)
    averages = get_average_dictionary(readings)

    # Loops through the keys in averages, sorted from that with the largest associated value in averages to the lowest - see https://docs.python.org/3.5/library/functions.html#sorted for details
    for location in sorted(averages, key = averages.get, reverse = True):
      print(location, averages[location])

  except (IOError, ValueError):
    print("Error reading {}".format(FILENAME))
    print("Please ensure the file exists and matches the required format")
    print("(each line should begin with a location name, followed by a comma, followed by an AQI reading)")