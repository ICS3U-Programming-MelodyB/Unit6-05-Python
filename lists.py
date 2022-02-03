#!/usr/bin/env python3

# Created by: Melody Berhane
# Created on: Feb. 2, 2022
# This program uses a while loop to collect input
# from the user. It then calls a function calculate
# the average of the input.


# function calculates the min value in the list of elements
def calc_average(marks):
    counter = 0
    sum = 0
    average = 0

    for counter in range(len(marks)):
        sum += marks[counter]

    if len(marks) == 0:
        return average
    else:
        average = sum / len(marks)
        return average


# get input from user and checks for invalid input
def main():

    # declaring variable
    marks_list = []
    temp_mark = None

    # display opening message to console
    print("This program will calculate the average of all the user's marks.")
    print("")

    # gets input from user and adds it to end of list
    while temp_mark != "-1":
        temp_mark = input("Please enter a mark, or -1 to stop: ")
        try:
            mark_int = int(temp_mark)
            if mark_int < -1:
                print("{} is not between 0 and 100." .format(temp_mark))
                continue
            marks_list.append(mark_int)
        except Exception:
            print("{} is not a number." .format(temp_mark))

    # removes -1 from the list
    marks_list.pop()
    # assigns variable to function call
    average_user = calc_average(marks_list)
    # displays results to user
    print("")
    print("For the list of marks: {}" .format(marks_list))
    print("The average is {:,.2f}%" .format(average_user))


if __name__ == "__main__":
    main()
