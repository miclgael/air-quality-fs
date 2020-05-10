
def read_data(filename):

  def colorize(text, msg_type="error"):
    if msg_type == "error":
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
      print(colorize('Please check formatting! Linter `comma-space` expected "," but found ", " in file "./{1}", line {0}'.format(index+1, filename), 'warn'
      ))
      line = line.replace(", ", ",") # auto-fix space.
   
    line = line.replace('\n', '') # remove extraneous new lines
    line = line.split(',') # split into key / value pairs
    location = str(line[0])
    
    try:
      value = float(line[1])
    except ValueError as error:
      value = 0.0 ## Nullify the result.
      error = str(error).split('float: ')
      print(colorize('Please check formatting! Result invalid due to poor formatting.\nLinter `value-is-float` expected FLOAT but found STRING {0} in file "./{2}", line {1}'.format(error[1],index+1,filename), 'error'))

    if location in output:
      prev = output[location]
      # print(location)
      # print(prev)
      # print(value)
      prev.append(value)
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