def sum_of_processor(p):
    return sum(p)


def minimal_load_processor(arr_processors: list):
    _min = 0
    index = 0
    min_load_processor = sum_of_processor(arr_processors[0])
    for i in range(len(arr_processors)):
        if sum_of_processor(arr_processors[i]) < min_load_processor:
            min_load_processor = sum_of_processor(arr_processors[i])
            index = i
    return index


def minimal_load_processor_hdmt(arr_processors: list, start, end):
    index = 0
    min_load_processor = sum_of_processor(arr_processors[0])
    for i in range(start, end):
        if sum_of_processor(arr_processors[i]) < min_load_processor:
            min_load_processor = sum_of_processor(arr_processors[i])
            index = i
    return index
