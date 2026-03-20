import sys 

arr = []
for i in range(1, len(sys.argv)):
    arr.append(int(sys.argv[i]))
print('Исходный массив:', arr)
sum_even = 0
i = 0
while i < len(arr):
    if i % 2 == 0:
        sum_even += arr[i]
    i += 1
print('Сумма четных индексов:', sum_even)

multi = 1
i = 1
while i < len(arr):
    multi *= arr[i]
    i += 2   # Сразу переходим к следующему нечетному индексу
print('Произведение нечетных индексов:', multi)

min_index = 0
max_index = 0
i = 1

while i < len(arr):
    if arr[i] < arr[min_index]:
        min_index = i
    if arr[i] > arr[max_index]:
        max_index = i
    i += 1

temp = arr[min_index]
arr[min_index] = arr[max_index]
arr[max_index] = temp

print('Массив после замены min и max:', arr)