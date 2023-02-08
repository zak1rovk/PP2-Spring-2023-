def unique_elements(list):
    new_list=[]
    for i in range(len(list)):
        if list[i] not in new_list:
            new_list.append(list[i])
    return new_list