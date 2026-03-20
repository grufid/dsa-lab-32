import sys

# Считываем массив
arr = [int(sys.argv[i]) for i in range(1, len(sys.argv))]
print('Исходный массив:', arr)

# Сумма четных индексов 
sum_even = 0
i = 0
while i < len(arr):
    sum_even += arr[i]
    i += 2
print('Сумма элементов с четными номерами:', sum_even)

# Произведение нечетных индексов 
multi = 1
i = 1
while i < len(arr):
    multi *= arr[i]
    i += 2
print('Произведение элементов с нечетными номерами:', multi)

# Замена min и max
min_i = arr.index(min(arr))
max_i = arr.index(max(arr))
arr[min_i], arr[max_i] = arr[max_i], arr[min_i]

print('Массив после замены min и max:', arr)
