import os


def merge(l, r):
    result = []
    i = 0
    j = 0
    while i < len(l) and j < len(r):
        if l[i] <= r[j]:
            result.append(l[i])
            i += 1
        else:
            result.append(r[j])
            j += 1
    result += l[i:]
    result += (r[j:])
    return result


def sort():
    files = os.listdir('input')
    sg_data = []
    for f in files:
        x = sort_data('input/' + f)
        sg_data += x
    data = merge_sort(sg_data)
    save_data(data, 'output/sorted.txt')


def merge_sort(data):
    if len(data) == 1:
        return data
    Mid = int(len(data) / 2)
    l = merge_sort(data[:Mid])
    r = merge_sort(data[Mid:])
    return merge(l, r)


def sort_data(file_path):
    file_input = open(file_path)
    file_list = [int(line) for line in file_input.readlines()]
    sorted = merge_sort(file_list)
    return sorted


def save_data(d, f):
    file_out = open(f, 'w')
    for x in d:
        file_out.write(str(x) + '\n')


sort()
