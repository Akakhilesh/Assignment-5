original_list=[1,2,3,4,5,6,7,8,9,10]
print(f"Original list: {original_list}")

extracted_list=original_list[0:5:1]
print(f"Extracted first five elements: {extracted_list}")

extracted_list.reverse()
print(f"Reverse Extracted list: {extracted_list}")