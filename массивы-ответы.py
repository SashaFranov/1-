def main():
    task5()



def task5():
    # Найти минимальное и максимальное числа в массиве. Вывести их значения и индексы.

    print("Задание 5")
    arr = [1, 3, 2, 4, 6, 0, 10]
    # print(f"Минимальное: {min(arr)}")
    # print(f"Максимальное: {max(arr)}")

    min_num = arr[0]
    max_num = arr[0]
    min_ind = 0
    max_ind = 0

    for i in range(len(arr)):
        if arr[i] < min_num:
            min_num = arr[i]
            min_ind = i
        if arr[i] > max_num:
            max_num = arr[i]
            max_ind = i

    print(f"Минимальное: {min_num}, индекс: {min_ind}")
    print(f"Максимальное: {max_num}, индекс: {max_ind}")


main()
