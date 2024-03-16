import random


def minimal_load_processor(arr_processors: list):
    _min = 0
    index = 0
    min_load_processor = sum(arr_processors[0])
    for i in range(len(arr_processors)):
        if sum(arr_processors[i]) < min_load_processor:
            min_load_processor = sum(arr_processors[i])
            index = i
    return index


def max_load_processor(arr_processors: list):
    _min = 0
    index = 0
    max_load_processor = sum(arr_processors[0])
    for i in range(len(arr_processors)):
        if sum(arr_processors[i]) > max_load_processor:
            max_load_processor = sum(arr_processors[i])
            index = i
    return index


def search_max(arr_p: list):
    _max = -1
    _max_index = -1
    for i in range(len(arr_p)):
        if arr_p[i] > _max:
            _max = arr_p[i]
            _max_index = i
    return _max_index


def search_min(arr_p: list):
    _min = -1
    _min_index = -1
    for i in range(len(arr_p)):
        if arr_p[i] < _min:
            _min = arr_p[i]
            _min_index = i
    return _min_index


def check_delta(arr_p: list, delta):
    ind = -1
    _max_ind = search_max(arr_p)
    if arr_p[_max_ind] < delta:
        ind = _max_ind
    return ind


cnt_processors = int(input("Enter count of processors: "))
m = int(input("Enter value of tasks: "))
a = int(input("Enter value from: "))
b = int(input("Enter value to: "))

T = []

for i in range(m):
    T.append(random.randint(a, b))

print()
print("################################################")
print()

print("T:", T)

arr_processors = []

for i in range(cnt_processors):
    arr_processors.append([])

j = 0

while j < len(T):
    i = random.randint(0, cnt_processors - 1)
    arr_processors[i].append(T[j])
    j += 1

for i in range(len(arr_processors)):
    _sum_max = -1
    _sum_min = 999
    print(f"p{i + 1} =", arr_processors[i], "Sum:", sum(arr_processors[i]))

while True:
    print()
    print("################################################")
    print()
    max_p = arr_processors[max_load_processor(arr_processors)]
    min_p = arr_processors[minimal_load_processor(arr_processors)]
    print(f"Max: p{max_load_processor(arr_processors) + 1}")
    print(f"Min: p{minimal_load_processor(arr_processors) + 1}")

    delta = sum(max_p) - sum(min_p)
    print(f"delta = {delta}")
    index = check_delta(max_p, delta)
    if index == -1:
        break
    else:
        print(f"index = {index}")
        min_p.append(max_p[index])
        max_p.pop(index)
    for i in range(len(arr_processors)):
        print(f"p{i + 1} =", arr_processors[i], "Sum:", sum(arr_processors[i]))

_sum_max = -1
_sum_min = 999

_max_proc = []
_min_proc = []
for i in range(len(arr_processors)):
    if sum(arr_processors[i]) > _sum_max:
        _sum_max = sum(arr_processors[i])
        _max_proc = arr_processors[i]

for i in range(len(arr_processors)):
    if sum(arr_processors[i]) < _sum_max:
        _sum_min = sum(arr_processors[i])
        _min_proc = arr_processors[i]

for i in range(len(arr_processors)):
    print(f"p{i + 1} =", arr_processors[i], "Sum:", sum(arr_processors[i]))

print(f"Max = {_sum_max}")
print(f"Min = {_sum_min}")

print(f"Max_proc = {_max_proc}")
print(f"Min_proc = {_min_proc}")

delta = _sum_max - _sum_min

print(f"delta = {delta}")

if _max_proc[search_max(_max_proc)] - _min_proc[search_min(_min_proc)] < delta:
    print(f"{_max_proc[search_max(_max_proc)] - _min_proc[search_min(_min_proc)]} < {delta}")
    buble = _max_proc[search_max(_max_proc)]
    _max_proc[search_max(_max_proc)] = _min_proc[search_min(_min_proc)]
    _min_proc[search_min(_min_proc)] = buble
else:
    print(f"{_max_proc[search_max(_max_proc)] - _min_proc[search_min(_min_proc)]} >= {delta}")


print(f"Max_proc = {_max_proc}")
print(f"Min_proc = {_min_proc}")

for i in range(len(arr_processors)):
    print(f"p{i + 1} =", arr_processors[i], "Sum:", sum(arr_processors[i]))

