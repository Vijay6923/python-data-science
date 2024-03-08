# bool_true=True
# print("type of true:",type(bool_true))
# name1="Alice"
# name2="Bob"
# is_equal=name1==name2
# print(is_equal)
try:
    numerator=int(input("enter the numerator: "))
    denominator=int(input("enter the denominator: "))
    result=numerator/denominator
    print(result)
except ZeroDivisionError as zero_division_error:
    print("Error:",zero_division_error)
