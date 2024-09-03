#Sorts a list of tuples by age in ascending order.

def sort_by_age(list_of_tuples):
    return sorted(list_of_tuples, key=lambda x: x[1])
