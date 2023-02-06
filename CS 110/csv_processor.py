###
### Author: Derek Tominaga
### Descripton: This program reads a csv file and determines
### min, max, or average of a column.
###

def open_read(file_name):
    """
    This fucntion takes one parameter to read the csv and
    convert the values from strings to floats and add
    them to a list that is returned
    file_name = a string that is the name of a  file.
    """
    data_list = []
    data = open(file_name, "r")
    for line in data:
        list_from_line = line.strip("\n").split(",")
        float_list = []
        for i in range(len(list_from_line)):
            float_list.append(float(list_from_line[i]))
        data_list.append(float_list)
    return data_list
def operation_print(operation, column_value, csv_data):
    """
    This function takes 3 parameters to determine
    the max, min, or average of an indicated "column"
    operation = string indicating the action taken
    column_value = int value indicating what column to look at
    csv_data = 2D list of the data from the file
    """
    value_printed = csv_data[0][column_value]
    if operation == "min":
        for index in range(0, len(csv_data)):
            if csv_data[index][column_value] < value_printed:
                value_printed = csv_data[index][column_value]
        print("The minimum value in column " + str(column_value + 1) +
        " is: " + str(value_printed))
    if operation == "max":
        for index in range(0, len(csv_data)):
            if csv_data[index][column_value] > value_printed:
                value_printed = csv_data[index][column_value]
        print("The maximum value in column " + str(column_value + 1) +
        " is: " + str(value_printed))
    if operation == "avg":
        average_value = 0.0
        average_count = 0.0
        for index in range(0, len(csv_data)):
            average_value += csv_data[index][column_value]
            average_count += 1
        average_value = float(average_value/average_count)
        print("The average for column " + str(column_value + 1) + " is: "
        + str(average_value))
def main():
    file_name = input("Enter CSV file name:\n")
    csv_data = open_read(file_name)
    column_value = (int(input("Enter column number:\n")) - 1)
    operation = input("Enter column operation:\n")
    operation_print(operation, column_value, csv_data)
main()