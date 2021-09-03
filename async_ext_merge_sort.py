import os
import asyncio


async def merge(l, r):
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


async def sort():
    files = os.listdir('input')
    tasks = []
    for f in files:
        tasks.append(asyncio.create_task(sort_data('./input/' + f)))

    sg_data = []
    for task in tasks:
        sg_data += await task

    data = await merge_sort(sg_data)
    await save_data(data, 'output/async_sorted.txt')


async def merge_sort(data):
    if len(data) == 1:
        return data
    Mid = int(len(data) / 2)
    l = await merge_sort(data[:Mid])
    r = await merge_sort(data[Mid:])
    result = merge(l, r)
    a = await result
    return a


async def sort_data(file_path):
    file_input = open(file_path)
    file_list = [int(line) for line in file_input.readlines()]
    sorted = await merge_sort(file_list)
    return sorted


async def save_data(d, f):
    file_out = open(f, 'w')
    for x in d:
        file_out.write(str(x) + '\n')


loop = asyncio.get_event_loop()
try:
    loop.run_until_complete(sort())
finally:
    loop.close()
