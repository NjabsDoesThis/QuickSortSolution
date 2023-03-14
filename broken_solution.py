def quick_sort(numbers):
   quick_sort_helper(numbers, 0, len(numbers)-1)

def quick_sort_helper(numbers, first, last):
   if first<last:

       splitpoint = partition(numbers, first, last)

       quick_sort_helper(numbers, first, splitpoint-1)
       quick_sort_helper(numbers, splitpoint+1, last)


def partition(numbers, first, last):
   pivotvalue = numbers[first]

   leftmark = first+1
   rightmark = last

   done = False

   """
   With the way the while-loop was initially structured,
   'done' could never be True because the rightmark 
   was always greater than the leftmark.
   """
   while not done:

       while leftmark <= rightmark and numbers[leftmark] <= pivotvalue:
            # Left-mark should only increment by 1
           leftmark += 1

       while numbers[rightmark] >= pivotvalue and rightmark >= leftmark:
            # Right-mark should only decrement by 1
           rightmark -= 1
        # Removed -1 from the if-statement below
       if rightmark < leftmark:
           done = True
       else:
           temp = numbers[leftmark]
           numbers[leftmark] = numbers[rightmark]
           numbers[rightmark] = temp

   temp = numbers[first]
   numbers[first] = numbers[rightmark]
   numbers[rightmark] = temp

   return rightmark

numbers = [54, 26, 93, 17, 77, 31, 44, 55, 20]
print("Before Sort: {}".format(numbers))
quick_sort(numbers)
print("After Sort: {}".format(numbers))

