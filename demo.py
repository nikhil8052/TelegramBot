from global_data import user_selected_exam
from demo1 import fun 

# def foo():
#     foo.counter += 1
#     print(foo.counter)
# foo.counter = 0

if user_selected_exam=="nee":
    user_selected_exam="neet"

if user_selected_exam=="":
    user_selected_exam="Please fill the values "
print(user_selected_exam)

fun()