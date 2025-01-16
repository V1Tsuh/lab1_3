def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # Флаг для отслеживания, произошли ли изменения
        swapped = False
        for j in range(0, n-i-1):
            # Сравниваем соседние элементы
            if arr[j] > arr[j+1]:
                # Меняем их местами, если они в неправильном порядке
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        # Если не было обменов, массив уже отсортирован
        if not swapped:
            break

# Пример использования
if __name__ == "__main__":
    n = int(input("Введите количество чисел для сортировки: "))
    numbers = []

    for _ in range(n):
        num = float(input("Введите число: "))
        numbers.append(num)

    bubble_sort(numbers)

    print("Отсортированные числа по возрастанию:")
    print(numbers)