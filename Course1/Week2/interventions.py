def merge_sort(list, inversions):
    if len(list) > 1:
        mid = len(list)/2
        left = list[:mid]
        right = list[mid:]
        
        # recursive call on both halves
        leftInput = merge_sort(left, inversions)
        rightInput = merge_sort(right, inversions)
        
        left = leftInput[0]
        right = rightInput[0]
        
        # Adding inversions on both sides
        inversions = leftInput[1] + rightInput[1]
        
        # initializing sub-lists indices
        i, j = 0, 0
        
        #initializing main list index
        k = 0
        
        # Sorting and merging the two sub lists
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                list[k] = left[i]
                i += 1
            else:
                list[k] = right[j]
                j += 1
                inversions = inversions + mid - i
            k += 1
        
        # Merging the remaining items in the lists
        while i < len(left):
            list[k] = left[i]
            #inversions += len(right)
            i += 1
            k += 1
        
        while j < len(right):
            list[k] = right[j]
            j += 1
            k += 1
         
    return list, inversions

with open ('integers.txt') as f:
    lines = f.readlines()
    integers = [int(x) for x in lines]
#integers = [13,15,16,4,7,9,80, 3]
output = merge_sort(integers, 0)

print ("Sorted array: ", output[0])
print ("inversions: ", output[1])






