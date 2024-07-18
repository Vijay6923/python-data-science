def list_intersection(lst1,lst2):
    return [x for x in lst1 if x in lst2]

lst1=[1,2,3,4,5]
lst2=[3,4,5,6,7]
intersection=list_intersection(lst1,lst2)
print(f"list 1:{lst1}")
print(f"list 2:{lst2}")
print(f"intersection :{intersection}")