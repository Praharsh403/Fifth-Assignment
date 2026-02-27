numbers = [1,2,3,4,5,6,7,8,9,10]

"""Problem Statement: Write a Python program that:
1.   Creates a list of numbers from 1 to 10.
2.   Extracts the first five elements from the list.
3.   Reverses these extracted elements.
4.   Prints both the extracted list and the reversed list
"""

extracted = numbers[0:5]       #extracts the fist five elements through slicing method
print(f"Original list:", numbers)
print(f"Extracted first five elements:", extracted)
reversed = extracted[::-1]     #creates a reversed copy hence not affecting the original.
print(f"Reversed extracted elements:", reversed)

"""The output provides the desired result with original, first five extracted and reversed of extracted elements.\n
"""