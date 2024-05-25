import random
import time

def bubble_sort(arr):
  n = len(arr)
  for i in range(n):
    for j in range(0, n-i-1):
      if arr[j] > arr[j+1]:
        arr[j], arr[j+1] = arr[j+1], arr[j]

def generate_random_list(n):
  return [random.randint(0, 50) for _ in range(n)]

def print_menu():
  print("\nMenu")
  print("Select the sorting algorithm:")
  print("1. Bubble Sort")
  print("7. Exit")

def execute_algorithm(choice, arr):
  start_time = time.time()
  if choice == 1:
    bubble_sort(arr)
  end_time = time.time()
  return end_time - start_time

def main():
  while True:
    print_menu()
    choice = int(input("\nEnter your choice: "))
    if choice == 7:
      break
    elif choice == 1:
      n = int(input("\nEnter the size of the list: "))
      arr = generate_random_list(n)
      print("\nOriginal list:", arr)
      time_taken = execute_algorithm(choice, arr)
      print("\nSorted list:", arr)
      print("\nTime taken:", time_taken)

if __name__ == "__main__":
    main()