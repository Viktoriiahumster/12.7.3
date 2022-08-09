def merge_sort (my_numbers, start, end):
    if end - start > 1:
        mid = (start+end) // 2
        merge_sort(my_numbers, start, mid)
        merge_sort(my_numbers, mid, end)
        merge_list(my_numbers, start, mid, end)

def merge_list(my_numbers, start, mid, end):
    left = my_numbers[start : mid]
    right = my_numbers[mid : end]
    k = start
    i = 0
    j = 0
    while start + i < mid and mid + j < end:
        if left[i] <= right[j]:
            my_numbers[k] = left[i]
            i += 1
        else:
            my_numbers[k] = right[j]
            j += 1
        k += 1
    if start + i < mid:
        while k < end:
            my_numbers[k] = left[i]
            i += 1
            k += 1
    else:
        while k < end:
            my_numbers[k] = right[j]
            j += 1
            k += 1

while True:
    try:
        my_numbers = [int(x) for x in input('Введите любую последовательность чисел через пробел: ').split()]
        if all(i is int for i in my_numbers):
            pass
        break
    except ValueError:
        print('Введено неверное значение')

merge_sort(my_numbers, 0, len(my_numbers))

def binary_search(my_numbers, a, left, right):
    if left > right:
        left = 0
        right = len(my_numbers)
        while (right - left > 1):
            i = left + (right - left) // 2
            if a < my_numbers[i]:
                right = i
            else:
                left = i
        b = min([(abs(a - my_numbers[j]), j) for j in (i - 1, i, i + 1)])
        return b[1]
    middle = (right + left) // 2
    if my_numbers[middle] == a:
        result = middle
        return result
    elif a < my_numbers[middle]:
        result = binary_search(my_numbers, a, left, middle-1)
        return result
    else:
        result = binary_search(my_numbers, a, middle+1, right)
        return result

while True:
    try:
        a = int(input('Введите контрольное число: '))
        if a < 0:
            raise Exception
        break
    except ValueError:
        print('Введено неверное значение')
    except Exception:
        print('Введено отрицательное число')

print('Индекс введенного значения или ближайшего наименьшего значения: ', binary_search(my_numbers, a, 0, len(my_numbers)))












