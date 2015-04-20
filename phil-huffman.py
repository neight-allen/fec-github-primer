def most_classes(in_dict):
    t0 = 0
    return_value = ""
    for teacher in in_dict:
        if len(in_dict[teacher]) > t0:
            t0 = len(in_dict[teacher])
            return_value = teacher
    return return_value


def function(in_dict):
    return len(in_dict)


def stats(in_dict):
    return_list = []
    for teacher in in_dict:
        return_list.append([teacher, len(in_dict[teacher])])
    return return_list


def courses(in_dict):
    out_list = []
    for teacher in in_dict:
        for class1 in in_dict[teacher]:
            if class1 not in out_list:
                out_list.append(class1)
    return out_list
