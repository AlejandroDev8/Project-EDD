import random
import time

def bubble_sort(arr):
  n = len(arr)
  for i in range(n):
    for j in range(0, n-i-1):
      if arr[j] > arr[j+1]:
        arr[j], arr[j+1] = arr[j+1], arr[j]

def insertion_sort(arr):
  for i in range(1, len(arr)):
    key = arr[i]
    j = i-1
    while j >= 0 and key < arr[j]:
      arr[j + 1] = arr[j]
      j -= 1
    arr[j + 1] = key

def quick_sort(arr):
  if len(arr) <= 1:
    return arr
  pivot = arr[len(arr) // 2]
  left = [x for x in arr if x < pivot]
  middle = [x for x in arr if x == pivot]
  right = [x for x in arr if x > pivot]
  return quick_sort(left) + middle + quick_sort(right)

def heap_sort(arr):
  def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and arr[largest] < arr[l]:
      largest = l
    if r < n and arr[largest] < arr[r]:
      largest = r
    if largest != i:
      arr[i], arr[largest] = arr[largest], arr[i]
      heapify(arr, n, largest)
  
  n = len(arr)
  for i in range(n // 2 - 1, -1, -1):
    heapify(arr, n, i)
  for i in range(n-1, 0, -1):
    arr[i], arr[0] = arr[0], arr[i]
    heapify(arr, i, 0)

def generate_random_list(n):
  return [random.randint(0, 1000) for _ in range(n)]

def print_menu():
  print("\nMenu")
  print("Select the sorting algorithm:")
  print("1. Bubble Sort")
  print("2. Insertion Sort")
  print("3. Quick Sort")
  print("4. Heap Sort")
  print("7. Exit")

def execute_algorithm(choice, arr):
  start_time = time.time()
  if choice == 1:
    bubble_sort(arr)
  elif choice == 2:
    insertion_sort(arr)
  elif choice == 3:
    arr = quick_sort(arr)
  elif choice == 4:
    heap_sort(arr)
  end_time = time.time()
  return end_time - start_time

def main():
  while True:
    print_menu()
    choice = int(input("\nEnter your choice: "))
    if choice == 7:
      break
    elif choice in [1, 2 ,3 ,4, 5]:
      # show the algorithm selected
      if choice == 1:
        print("\nYou selected Bubble Sort")
      elif choice == 2:
        print("\nYou selected Insertion Sort")
      elif choice == 3:
        print("\nYou selected Quick Sort")
      elif choice == 4:
        print("\nYou selected Heap Sort")
      n = int(input("\nEnter the size of the list: "))
      arr = generate_random_list(n)
      print("\nOriginal list:", arr)
      time_taken = execute_algorithm(choice, arr)
      print("\nSorted list:", arr)
      print("\nTime taken:", time_taken)

if __name__ == "__main__":
    main()