steps = input("Enetr the steps in each day in the month separated by spaces: ")
steps_list = list(map(int, steps.split())) # Here We use the map function to to apply the split function in each step in the list
print (steps_list)
# Here We use the max function to find the max number of steps in the month

max_steps =max(steps_list)
print (f"The maximum number of steps in the month is : {max_steps}")
# Here We use the min function to find the min number of steps in the month

min_steps = min(steps_list)
print (f"The minmum number of steps in the month is : {min_steps}")
# Here We calculate the average number of steps in the month by summing all the steps and dividing by the number of days

average_steps = sum(steps_list) / len(steps_list) # average = sum / length of steps
print (f"Average Daily Step Count: {average_steps:.2f}")
# Here We use the sort function to display the list in descending  order

sorted_steps = sorted(steps_list, reverse=True)
print("Step Counts in Descending Order:")
print (sorted_steps)