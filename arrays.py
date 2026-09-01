# Algorithm: Find The Lowest Value in an Array

my_array=[5, 2, 9, 1, 5, 6]
min_val=my_array[0]
for i in my_array:
    if i < min_val:
        min_val = i
print("The lowest value in the array is:", min_val)

#Time Complexity: O(n) - The algorithm iterates through the entire array once, making it linear in time complexity. 
  
  #Similarly, we can find the highest value in an array using a similar approach.
  #by just changing the comparison operator from '<' to '>' in the if statement.