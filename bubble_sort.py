# Bubble Sort is an algorithm that sorts an array from the lowest value to the highest value.
my_array=[33, 27, 9, 10, 56, 69]
n=len(my_array)
for i in range(n-1):
    for j in range(n-i-1):
        if my_array[j] > my_array[j+1]:
            my_array[j], my_array[j+1] = my_array[j+1], my_array[j]
print("The sorted array is:", my_array)

#The time complexity of the bubble sort algorithm is O(n^2) -
# The algorithm uses two nested loops to iterate through the array, 
# making it quadratic in time complexity.