import random
random_numbers=[random.randint(1,20) for _ in range(15)]
print(f"original list:{random_numbers}")

Sorted_numbers=sorted(random_numbers)
print(f"sorted in ascending order: {Sorted_numbers}")

Sorted_numbers_desc=sorted(random_numbers,reverse=True)
print(f"sorted in descending order : {Sorted_numbers_desc}")

unique_numbers=list(set(random_numbers))
print(f"list with duplicates removed:{unique_numbers}")