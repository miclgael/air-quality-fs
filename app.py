
def read_data(filename):

  def colorize(text, msg_type="error"):
    if msg_type == "error" or msg_type == None:
      start = "\u001b[31mError:" # <- ANSI for "red"
    elif msg_type == 'warning' or msg_type == "warn": 
      start = "\u001b[33mWarning:" # <- ANSI for "red"
    elif msg_type == "success": 
      start = "\u001b[32mSuccess!" # <- ANSI for "red"
    end = "\033[0m"  # <- ANSI for "normal"
    return "{} {} {}".format(start,text,end)

  data_file = open(filename,'r')
  lines = data_file.readlines()
  output = {}
  for (index, line) in enumerate(lines):
    ## Check for formatting error (comma-space)
    if (', ' in line):
      print(colorize('Please check formatting! Linter (comma-space) expected "," but found ", " in file "./{1}", line {0}'.format(index+1, filename), 'warn'
      ))
      line = line.replace(", ", ",") # auto-fix space.
   
    line = line.replace('\n', '') # remove extraneous new lines
    line = line.split(',') # split into key / value pairs
    
    try:
      location = str(line[0])
      value = float(line[1])
    except ValueError as error:
      print(colorize('Please check formatting! ', 'error'))
      print(colorize(error, 'error'))

    if location in output:
      prev = output[location][0]
      print(location)
      print(value)
      print(prev)
      new = [value, prev]
      output[location] = new
    else:
      output[location] = [value]
      
  data_file.close()
  return output

def get_average_dictionary(readings):
  return {}

FILENAME = 'days.txt'

print(read_data(FILENAME))




# if __name__ == "__main__":
#   try:
#     readings = read_data(FILENAME)
#     averages = get_average_dictionary(readings)

#     # Loops through the keys in averages, sorted from that with the largest associated value in averages to the lowest - see https://docs.python.org/3.5/library/functions.html#sorted for details
#     for location in sorted(averages, key = averages.get, reverse = True):
#       print(location, averages[location])

#   except (IOError, ValueError):
#     print("Error reading {}".format(FILENAME))
#     print("Please ensure the file exists and matches the required format")
#     print("(each line should begin w`ith a location name, followed by a comma, followed by an AQI reading)")