def sort_by_value(marks):
    sorted_dict = {k: v for k, v in sorted(marks.items(), key=lambda item: item[1])}
    print(sorted_dict)

marks = dict(Rahul=86, Ravi=92, Rohit=75, Rajan=79, Ram=92)
sort_by_value(marks)
