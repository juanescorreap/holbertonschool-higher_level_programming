def only_diff_elements(set_1, set_2):
    list_1 = list(set_1)
    list_2 = list(set_2)
    od_set = [i for i in list_1 + list_2 if i not in list_1 or i not in list_2]
    return(set(od_set))