import time

def bubble_sort(arr):
    n = len(arr)
    start_time = time.time()

    for i in range(n):
        swapped = False

        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True

        if not swapped:
            break

    end_time = time.time()
    return arr, end_time - start_time

def insertion_sort(arr):
    n = len(arr)
    start_time = time.time()

    for i in range(1, n):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    end_time = time.time()
    return arr, end_time - start_time

def print_iterations(arr, sort_type):
    print(f"\nIterasi pertama ({sort_type}):")
    print(arr[:5])
    print("\nIterasi terakhir:")
    print(arr[-5:])

def print_execution_time(time_taken, sort_type):
    print(f"\nWaktu komputasi pengurutan ({sort_type}): {time_taken:.6f} detik")

def print_before_after(arr, sort_type):
    print(f"\nSebelum pengurutan ({sort_type}):")
    print(arr)
    print("\nSetelah pengurutan:")
    print(arr)

def analyze_algorithm():
    arr = [12, 99, 62, 15, 20, 95, 39, 48, 3, 24, 8, 43, 74, 19, 97, 33, 49, 68, 55, 33, 90, 90, 7, 26, 85, 46, 39, 40, 9,
           36, 60, 64, 89, 31, 25, 71, 21, 23, 63, 84, 32, 5, 3, 44, 21, 10, 21, 17, 50, 2, 36, 53, 79, 54, 19, 88, 1, 32,
           31, 15, 6, 3, 1, 40, 22, 43, 18, 1, 77, 9, 59, 40, 7, 41, 81]

    print("Sebelum pengurutan:")
    print(arr)

    choice = input("\nPilih pengurutan (bubble/insertion): ")

    if choice.lower() == "bubble":
        sorted_arr, time_taken = bubble_sort(arr)
        print_before_after(sorted_arr, "Bubble Sort")
        print_iterations(sorted_arr, "Bubble Sort")
        print_execution_time(time_taken, "Bubble Sort")
    elif choice.lower() == "insertion":
        sorted_arr, time_taken = insertion_sort(arr)
        print_before_after(sorted_arr, "Insertion Sort")
        print_iterations(sorted_arr, "Insertion Sort")
        print_execution_time(time_taken, "Insertion Sort")
    else:
        print("Pilihan tidak valid. Silakan pilih bubble atau insertion.")

def continue_program():
    choice = input("\nLanjutkan program? (y/n): ")
    if choice.lower() == "y":
        analyze_algorithm()
        continue_program()
    else:
        print("Program selesai.")

analyze_algorithm()
continue_program()