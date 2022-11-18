def BubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


if __name__ == '__main__':
    n = int(input("Enter the number of elements in the array: "))
    arr = []
    print("Enter the elements: ")
    for i in range(0, n):
        arr.append(int(input()))
    BubbleSort(arr)
    print("After Sorting: ")
    for i in range(len(arr)):
        print("% d" % arr[i])