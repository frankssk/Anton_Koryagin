import sys
from time import perf_counter

start = perf_counter()
src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
result = []

seen_scr = set(src)
print(src)
print(seen_scr)
for number in src:
    if number in seen_scr:
        result.append(number)
        seen_scr.discard(number)
print(result)
print(sys.getsizeof(result))
print(perf_counter() - start)
