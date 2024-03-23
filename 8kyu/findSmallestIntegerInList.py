def find_smallest_int(arr):
    # Code here
     for num in arr:
        if num == sorted(arr)[0]:
            return num