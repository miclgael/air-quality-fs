def colorize(text, msg_type="error"):
    """Changes the colour of the given string.

       @credit: https://stackoverflow.com/a/33206814
       (I needed to look up a chart to get the ANSI codes)

    Arguments:
        text {str} -- The text you want to change

    Keyword Arguments:
        msg_type {str} -- a keyword uses to choose a colour (default: {"error"})

    Returns:
        {str} -- The same text, in a different colour
    """
    if msg_type == "error":
        start = "\u001b[31mError:"   # ANSI for "red"
    elif msg_type == 'warning' or msg_type == "warn": 
        start = "\u001b[33mWarning:" # ANSI for "yellow"
    elif msg_type == "success": 
        start = "\u001b[32mSuccess!" # ANSI for "green"
    end = "\033[0m"                  # ANSI for "normal"
    return "{} {} {}".format(start,text,end)

def read_data(filename):
    """Opens the file with the given name. Returns a dictionary where the keys are the location names in the file and the values are a list of the AQI readings.

    Arguments:
        filename {str} -- the given filename eg. 'readings.txt'

    Returns:
        dict -- eg. { "location-name": [AQI_reading_1, AQI_reading_2], ... }
    """
    try: 
        data_file = open(filename,'r')
        lines = data_file.readlines()
        output = {}
        if len(lines) == 0:
            print(colorize('{} exists, but is empty!'.format(filename)))
            exit

        for (index, line) in enumerate(lines):
            # Check for formatting error (comma-space)
            if (', ' in line):
                print(colorize('Please check formatting!\n      Linter: `comma-space` expected "," but found ", " in file "./{1}", line {0}'.format(index+1, filename), 'warn'
                ))
                line = line.replace(", ", ",") # auto-fix space.
    
            line = line.replace('\n', '') # remove extraneous new lines
            line = line.split(',') # split into key / value pairs
            location = str(line[0]) # always coerce to string
      
            try:
                value = float(line[1])

            except IndexError as error:
                value = None ## Nullify the result.
                print(colorize('The results have been invalidated due to poor formatting.\n       Linter: `value-is-missing` expected Float but found Nothing! in file "./{1}", line {0}'.format(index+1,filename)))

            except ValueError as error:
                value = None ## Nullify the result.
                error = str(error).split('float: ')
                print(colorize('The results have been invalidated due to poor formatting.\n       Linter: `value-is-float` expected Float but found String {0} in file "./{2}", line {1}'.format(error[1],index+1,filename), 'error'))

            # Warn if no location given
            if location == '':
                location = 'Unknown Location' # Set _something_ and continue
                print(colorize('Please check formatting! Linter: `no-location-name` expected a location name given, but found "" file "./{1}", line {0}'.format(index+1, filename), 'warn'
                ))
                pass

            # Throw out result if no value given
            if value == None:
                pass # Drop the whole line from output
            else:
                if location in output:
                ## handle duplicate location eg 'Mallowbeach' already exists
                    prev = output[location]
                    prev.append(value)
                else:
                ## unique location, set up as initial value
                    output[location] = [value]
                    
        data_file.close()
        return output

    except IOError:
        print(colorize('Error reading {0}\nPlease ensure the file exists and matches the required format\n(each line should begin with a location name, followed by a comma, followed by an AQI reading'.format(FILENAME)))
        pass


def get_average_dictionary(readings):
    """returns a dictionary with the same keys as the parameter, but with the average value of the AQI readings rather than the list of individual readings.

    Arguments:
        readings {dict} -- eg. { "location-name": [AQI_reading_1, AQI_reading_2], ... }

    Returns:
        {dict} -- eg. { "location-name": "average-reading" }
    """
    try: 
        for value in readings:
            ## Do the average calculation for each entry
            readings[value] = sum(readings[value]) / len(readings[value])
        return readings
    except TypeError:
        print(colorize('file exists, but it''s empty!'))
        return {}

FILENAME = "readings.txt"

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