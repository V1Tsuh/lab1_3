def bubble_sort(arr, ascending=True):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            # Сравниваем элементы в зависимости от направления сортировки
            if (ascending and arr[j] > arr[j+1]) or (not ascending and arr[j] < arr[j+1]):
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break

# Пример использования
if __name__ == "__main__":
    n = int(input("Введите количество чисел для сортировки: "))
    numbers = []

    for _ in range(n):
        num = float(input("Введите число: "))
        numbers.append(num)

    direction = input("Введите направление сортировки (введите 'asc' для возрастания или 'desc' для убывания): ").strip().lower()

    if direction == 'asc':
        bubble_sort(numbers, ascending=True)
        print("Отсортированные числа по возрастанию:")
    elif direction == 'desc':
        bubble_sort(numbers, ascending=False)
        print("Отсортированные числа по убыванию:")
    else:
        print("Неверное направление сортировки. Пожалуйста, введите 'asc' или 'desc'.")
        exit()

    print(numbers)