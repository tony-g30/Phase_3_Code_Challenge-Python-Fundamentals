#Merges two dictionaries, summing values of common keys.
def merge_dicts(dict1, dict2):
    merged_dict = dict1.copy()  # Make a copy of dict1 to avoid modifying the original
    for key, value in dict2.items():
        if key in merged_dict:
            merged_dict[key] += value
        else:
            merged_dict[key] = value
    return merged_dict
