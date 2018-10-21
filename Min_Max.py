def min_max(input_dict):
    value_dict=[]
    for row in ex_dict:
        value_dict.append(input_dict[row])
    value_sorted=sorted(value_dict)
    min_value=value_sorted[0]
    max_value=value_sorted[-1]
    max_min={"min:":min_value,"max:":max_value}
    return max_min
min_max(ex_dict)
