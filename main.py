import random
from cmp import *


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


def search_max(arr_p: list, used_ind):
    _max = -1
    _max_index = -1
    for i in range(len(arr_p)):
        if arr_p[i] > _max and i not in used_ind:
            _max = arr_p[i]
            _max_index = i
    return _max_index


def search_min(arr_p: list, used_ind):
    _min = 999
    _min_index = -1
    for i in range(len(arr_p)):
        if arr_p[i] < _min and i not in used_ind:
            _min = arr_p[i]
            _min_index = i
    return _min_index


def check_delta(arr_p: list, delta):
    used_ind = []
    ind = -1
    _max_ind = search_max(arr_p, used_ind)
    if arr_p[_max_ind] < delta:
        ind = _max_ind
    return ind


cnt_processors = int(input("Enter count of processors: "))
m = int(input("Enter value of tasks: "))
a = int(input("Enter value from: "))
b = int(input("Enter value to: "))

print()
print("#######################CMP#########################")
print()

T = []

for i in range(m):
    T.append(random.randint(a, b))

T.sort(reverse=True)

print("T:", T)

arr_processors_sort_down = []

for i in range(cnt_processors):
    arr_processors_sort_down.append([])

for i in range(len(T)):
    index = minimal_load_processor(arr_processors_sort_down)
    arr_processors_sort_down[index].append(T[i])

_max = sum_of_processor(arr_processors_sort_down[0])
for i in range(len(arr_processors_sort_down)):
    if sum_of_processor(arr_processors_sort_down[i]) > _max:
        _max = sum_of_processor(arr_processors_sort_down[i])
    print(f"p{i + 1} =", arr_processors_sort_down[i], "Sum:", sum_of_processor(arr_processors_sort_down[i]))
print("Max:", _max)

while True:
    print()
    print("################################################")
    print()
    max_p = arr_processors_sort_down[max_load_processor(arr_processors_sort_down)]
    min_p = arr_processors_sort_down[minimal_load_processor(arr_processors_sort_down)]
    print(f"Max: p{max_load_processor(arr_processors_sort_down) + 1}")
    print(f"Min: p{minimal_load_processor(arr_processors_sort_down) + 1}")

    delta = sum(max_p) - sum(min_p)
    print(f"delta = {delta}")
    index = check_delta(max_p, delta)
    if index == -1:
        break
    else:
        print(f"index = {index}")
        min_p.append(max_p[index])
        max_p.pop(index)
    for i in range(len(arr_processors_sort_down)):
        print(f"p{i + 1} =", arr_processors_sort_down[i], "Sum:", sum(arr_processors_sort_down[i]))

delta = 999

_max_proc = []
_min_proc = []
all_ind = []
_min_ind = 0
_max_ind = 0
flag = True
while flag:

    _sum_min = 999
    _sum_max = -1
    used_ind_min = []
    used_ind_max = []

    for i in range(len(arr_processors_sort_down)):
        if sum(arr_processors_sort_down[i]) < _sum_min:
            _sum_min = sum(arr_processors_sort_down[i])
            _min_proc = arr_processors_sort_down[i]
    for i in range(len(arr_processors_sort_down)):
        if sum(arr_processors_sort_down[i]) > _sum_max:
            _sum_max = sum(arr_processors_sort_down[i])
            _max_proc = arr_processors_sort_down[i]

    for i in range(len(arr_processors_sort_down)):
        print(f"p{i + 1} =", arr_processors_sort_down[i], "Sum:", sum(arr_processors_sort_down[i]))

    print(f"Max = {_sum_max}")
    print(f"Min = {_sum_min}")

    print(f"Max_proc = {_max_proc}")
    print(f"Min_proc = {_min_proc}")

    delta = _sum_max - _sum_min
    if delta <= 1:
        break

    while True:
        print(f"delta = {delta}")
        _min_ind = search_min(_min_proc, used_ind_min)
        _max_ind = search_max(_max_proc, used_ind_max)
        print(f"_min_ind: {_min_ind}")
        print(f"_max_ind: {_max_ind}")
        if _min_ind == -1 or _max_ind == -1:
            break
        if _min_ind in used_ind_min or _max_ind in used_ind_max:
            continue
        else:
            used_ind_min.append(_min_ind)
            used_ind_max.append(_max_ind)
            print(f"used_ind_min: {used_ind_min}")
            print(f"used_ind_max: {used_ind_max}")

        print(f"_max: {_max_proc[_max_ind]}, _min: {_min_proc[_min_ind]}")

        if (_max_proc[_max_ind] - _min_proc[_min_ind]) < delta and (_max_proc[_max_ind] > _min_proc[_min_ind]):
            print(f"{_max_proc[_max_ind] - _min_proc[_min_ind]} < {delta}")
            _max_proc[_max_ind], _min_proc[_min_ind] = _min_proc[_min_ind], _max_proc[_max_ind]
            flag = True
            break
        else:
            print(
                f"{_max_proc[_max_ind] - _min_proc[_min_ind]} >= {delta} or {_max_proc[_max_ind]} < {_min_proc[_min_ind]}")
            flag = False

print(f"Max_proc = {_max_proc}")
print(f"Min_proc = {_min_proc}")
print(f"delta = {delta}")

for i in range(len(arr_processors_sort_down)):
    print(f"p{i + 1} =", arr_processors_sort_down[i], "Sum:", sum(arr_processors_sort_down[i]))


print()
print("#######################RANDOM#########################")
print()

T = []

for i in range(m):
    T.append(random.randint(a, b))


print("T:", T)

arr_processors_sort_down = []

for i in range(cnt_processors):
    arr_processors_sort_down.append([])

for i in range(len(T)):
    index = minimal_load_processor(arr_processors_sort_down)
    arr_processors_sort_down[index].append(T[i])

_max = sum_of_processor(arr_processors_sort_down[0])
for i in range(len(arr_processors_sort_down)):
    if sum_of_processor(arr_processors_sort_down[i]) > _max:
        _max = sum_of_processor(arr_processors_sort_down[i])
    print(f"p{i + 1} =", arr_processors_sort_down[i], "Sum:", sum_of_processor(arr_processors_sort_down[i]))
print("Max:", _max)

while True:
    print()
    print("################################################")
    print()
    max_p = arr_processors_sort_down[max_load_processor(arr_processors_sort_down)]
    min_p = arr_processors_sort_down[minimal_load_processor(arr_processors_sort_down)]
    print(f"Max: p{max_load_processor(arr_processors_sort_down) + 1}")
    print(f"Min: p{minimal_load_processor(arr_processors_sort_down) + 1}")

    delta = sum(max_p) - sum(min_p)
    print(f"delta = {delta}")
    index = check_delta(max_p, delta)
    if index == -1:
        break
    else:
        print(f"index = {index}")
        min_p.append(max_p[index])
        max_p.pop(index)
    for i in range(len(arr_processors_sort_down)):
        print(f"p{i + 1} =", arr_processors_sort_down[i], "Sum:", sum(arr_processors_sort_down[i]))

delta = 999

_max_proc = []
_min_proc = []
all_ind = []
_min_ind = 0
_max_ind = 0
flag = True
while flag:

    _sum_min = 999
    _sum_max = -1
    used_ind_min = []
    used_ind_max = []

    for i in range(len(arr_processors_sort_down)):
        if sum(arr_processors_sort_down[i]) < _sum_min:
            _sum_min = sum(arr_processors_sort_down[i])
            _min_proc = arr_processors_sort_down[i]
    for i in range(len(arr_processors_sort_down)):
        if sum(arr_processors_sort_down[i]) > _sum_max:
            _sum_max = sum(arr_processors_sort_down[i])
            _max_proc = arr_processors_sort_down[i]

    for i in range(len(arr_processors_sort_down)):
        print(f"p{i + 1} =", arr_processors_sort_down[i], "Sum:", sum(arr_processors_sort_down[i]))

    print(f"Max = {_sum_max}")
    print(f"Min = {_sum_min}")

    print(f"Max_proc = {_max_proc}")
    print(f"Min_proc = {_min_proc}")

    delta = _sum_max - _sum_min
    if delta <= 1:
        break

    while True:
        print(f"delta = {delta}")
        _min_ind = search_min(_min_proc, used_ind_min)
        _max_ind = search_max(_max_proc, used_ind_max)
        print(f"_min_ind: {_min_ind}")
        print(f"_max_ind: {_max_ind}")
        if _min_ind == -1 or _max_ind == -1:
            break
        if _min_ind in used_ind_min or _max_ind in used_ind_max:
            continue
        else:
            used_ind_min.append(_min_ind)
            used_ind_max.append(_max_ind)
            print(f"used_ind_min: {used_ind_min}")
            print(f"used_ind_max: {used_ind_max}")

        print(f"_max: {_max_proc[_max_ind]}, _min: {_min_proc[_min_ind]}")

        if (_max_proc[_max_ind] - _min_proc[_min_ind]) < delta and (_max_proc[_max_ind] > _min_proc[_min_ind]):
            print(f"{_max_proc[_max_ind] - _min_proc[_min_ind]} < {delta}")
            _max_proc[_max_ind], _min_proc[_min_ind] = _min_proc[_min_ind], _max_proc[_max_ind]
            flag = True
            break
        else:
            print(
                f"{_max_proc[_max_ind] - _min_proc[_min_ind]} >= {delta} or {_max_proc[_max_ind]} < {_min_proc[_min_ind]}")
            flag = False

print(f"Max_proc = {_max_proc}")
print(f"Min_proc = {_min_proc}")
print(f"delta = {delta}")

for i in range(len(arr_processors_sort_down)):
    print(f"p{i + 1} =", arr_processors_sort_down[i], "Sum:", sum(arr_processors_sort_down[i]))

print()
print("#######################DOWN#########################")
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

delta = 999

_max_proc = []
_min_proc = []
all_ind = []
_min_ind = 0
_max_ind = 0
flag = True
while flag:

    _sum_min = 999
    _sum_max = -1
    used_ind_min = []
    used_ind_max = []

    for i in range(len(arr_processors)):
        if sum(arr_processors[i]) < _sum_min:
            _sum_min = sum(arr_processors[i])
            _min_proc = arr_processors[i]
    for i in range(len(arr_processors)):
        if sum(arr_processors[i]) > _sum_max:
            _sum_max = sum(arr_processors[i])
            _max_proc = arr_processors[i]

    for i in range(len(arr_processors)):
        print(f"p{i + 1} =", arr_processors[i], "Sum:", sum(arr_processors[i]))

    print(f"Max = {_sum_max}")
    print(f"Min = {_sum_min}")

    print(f"Max_proc = {_max_proc}")
    print(f"Min_proc = {_min_proc}")

    delta = _sum_max - _sum_min
    if delta <= 1:
        break

    while True:
        print(f"delta = {delta}")
        _min_ind = search_min(_min_proc, used_ind_min)
        _max_ind = search_max(_max_proc, used_ind_max)
        print(f"_min_ind: {_min_ind}")
        print(f"_max_ind: {_max_ind}")
        if _min_ind == -1 or _max_ind == -1:
            break
        if _min_ind in used_ind_min or _max_ind in used_ind_max:
            continue
        else:
            used_ind_min.append(_min_ind)
            used_ind_max.append(_max_ind)
            print(f"used_ind_min: {used_ind_min}")
            print(f"used_ind_max: {used_ind_max}")

        print(f"_max: {_max_proc[_max_ind]}, _min: {_min_proc[_min_ind]}")

        if (_max_proc[_max_ind] - _min_proc[_min_ind]) < delta and (_max_proc[_max_ind] > _min_proc[_min_ind]):
            print(f"{_max_proc[_max_ind] - _min_proc[_min_ind]} < {delta}")
            _max_proc[_max_ind], _min_proc[_min_ind] = _min_proc[_min_ind], _max_proc[_max_ind]
            flag = True
            break
        else:
            print(
                f"{_max_proc[_max_ind] - _min_proc[_min_ind]} >= {delta} or {_max_proc[_max_ind]} < {_min_proc[_min_ind]}")
            flag = False

print(f"Max_proc = {_max_proc}")
print(f"Min_proc = {_min_proc}")
print(f"delta = {delta}")

for i in range(len(arr_processors)):
    print(f"p{i + 1} =", arr_processors[i], "Sum:", sum(arr_processors[i]))


print()
print("#######################UP#########################")
print()

T = []

for i in range(m):
    T.append(random.randint(a, b))

T.sort()
print("T:", T)

arr_processors_sort_down = []

for i in range(cnt_processors):
    arr_processors_sort_down.append([])

for i in range(len(T)):
    index = minimal_load_processor(arr_processors_sort_down)
    arr_processors_sort_down[index].append(T[i])

_max = sum_of_processor(arr_processors_sort_down[0])
for i in range(len(arr_processors_sort_down)):
    if sum_of_processor(arr_processors_sort_down[i]) > _max:
        _max = sum_of_processor(arr_processors_sort_down[i])
    print(f"p{i + 1} =", arr_processors_sort_down[i], "Sum:", sum_of_processor(arr_processors_sort_down[i]))
print("Max:", _max)

while True:
    print()
    print("################################################")
    print()
    max_p = arr_processors_sort_down[max_load_processor(arr_processors_sort_down)]
    min_p = arr_processors_sort_down[minimal_load_processor(arr_processors_sort_down)]
    print(f"Max: p{max_load_processor(arr_processors_sort_down) + 1}")
    print(f"Min: p{minimal_load_processor(arr_processors_sort_down) + 1}")

    delta = sum(max_p) - sum(min_p)
    print(f"delta = {delta}")
    index = check_delta(max_p, delta)
    if index == -1:
        break
    else:
        print(f"index = {index}")
        min_p.append(max_p[index])
        max_p.pop(index)
    for i in range(len(arr_processors_sort_down)):
        print(f"p{i + 1} =", arr_processors_sort_down[i], "Sum:", sum(arr_processors_sort_down[i]))

delta = 999

_max_proc = []
_min_proc = []
all_ind = []
_min_ind = 0
_max_ind = 0
flag = True
while flag:

    _sum_min = 999
    _sum_max = -1
    used_ind_min = []
    used_ind_max = []

    for i in range(len(arr_processors_sort_down)):
        if sum(arr_processors_sort_down[i]) < _sum_min:
            _sum_min = sum(arr_processors_sort_down[i])
            _min_proc = arr_processors_sort_down[i]
    for i in range(len(arr_processors_sort_down)):
        if sum(arr_processors_sort_down[i]) > _sum_max:
            _sum_max = sum(arr_processors_sort_down[i])
            _max_proc = arr_processors_sort_down[i]

    for i in range(len(arr_processors_sort_down)):
        print(f"p{i + 1} =", arr_processors_sort_down[i], "Sum:", sum(arr_processors_sort_down[i]))

    print(f"Max = {_sum_max}")
    print(f"Min = {_sum_min}")

    print(f"Max_proc = {_max_proc}")
    print(f"Min_proc = {_min_proc}")

    delta = _sum_max - _sum_min
    if delta <= 1:
        break

    while True:
        print(f"delta = {delta}")
        _min_ind = search_min(_min_proc, used_ind_min)
        _max_ind = search_max(_max_proc, used_ind_max)
        print(f"_min_ind: {_min_ind}")
        print(f"_max_ind: {_max_ind}")
        if _min_ind == -1 or _max_ind == -1:
            break
        if _min_ind in used_ind_min or _max_ind in used_ind_max:
            continue
        else:
            used_ind_min.append(_min_ind)
            used_ind_max.append(_max_ind)
            print(f"used_ind_min: {used_ind_min}")
            print(f"used_ind_max: {used_ind_max}")

        print(f"_max: {_max_proc[_max_ind]}, _min: {_min_proc[_min_ind]}")

        if (_max_proc[_max_ind] - _min_proc[_min_ind]) < delta and (_max_proc[_max_ind] > _min_proc[_min_ind]):
            print(f"{_max_proc[_max_ind] - _min_proc[_min_ind]} < {delta}")
            _max_proc[_max_ind], _min_proc[_min_ind] = _min_proc[_min_ind], _max_proc[_max_ind]
            flag = True
            break
        else:
            print(
                f"{_max_proc[_max_ind] - _min_proc[_min_ind]} >= {delta} or {_max_proc[_max_ind]} < {_min_proc[_min_ind]}")
            flag = False

print(f"Max_proc = {_max_proc}")
print(f"Min_proc = {_min_proc}")
print(f"delta = {delta}")

for i in range(len(arr_processors_sort_down)):
    print(f"p{i + 1} =", arr_processors_sort_down[i], "Sum:", sum(arr_processors_sort_down[i]))