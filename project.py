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