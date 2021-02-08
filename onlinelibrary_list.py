# Programming Task 1
# Author: Stuart Hanson
# Date: 17/01/2021
# Contact: stuart_hanson@outlook.com

# Create a function to read the data from the file "onlinelibrary.txt"
# Arrange this data into a dictionary called "readings"
def read_data(filename):
    d = {}
    with open(filename) as f:
        for line in f:
            (key, val) = line.strip().split(",")
            if key in d:
                d[key].append(val)
            else:
                d[key] = [val]
        return(d)


# Using the data from the "readings" Dictionary the values placed in a list
# The values in the list are converted to INT, averaged, then returned to a new dictionary
# The new Dictionary (avgDict) can now be displayed to the user, while maintaining the raw
# Values in readings, should they be needed.
def get_average_dictionary(readings):
    avgs = []
    avgDict = {}
    for key, value in readings.items():
        avgs = list(map(int, value))
        avgs = sum(avgs) / len(avgs)
        avgDict.update({key:avgs})
    return(avgDict)


# Setup the constant for the input file
FILENAME = "onlinelibrary.txt"


# Create the name function that checks this file has not been imported as a module
if __name__ == "__main__":
    
    # Runs the functions are described above.
    # Any issues with the input file are handled below
    try:
        readings = read_data(FILENAME)
        averages = get_average_dictionary(readings)

        # Loops through the keys in averages, sorted from that with the largest associated value in averages to the lowest
        # - see https://docs.python.org/3.5/library/functions.html#sorted for more details
        for category in sorted(averages, key = averages.get, reverse = True):
            print(category, averages[category])

    # Any issues with the input file are handled here, and the issues displayed to the user.
    except (IOError, ValueError):
        print("Error reading {}".format(FILENAME))
        print("Please ensure the file exists and matches the required format")
        print("(each line should begin with a day name, followed by a comma, followed by a reading value)")
