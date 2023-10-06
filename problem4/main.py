def find_max_sum_sub_array(k, arr):
    max_jumlah = 0
    total = sum(arr[:k])
    for i in range (len(arr)):
        start_idx = i
        end_idx = i +k
        total = sum(arr[start_idx : end_idx])
        max_jumlah = (max(max_jumlah, total))
    return max_jumlah
if __name__ == '__main__':
    print(find_max_sum_sub_array(3, [2, 1, 5, 1, 3, 2])) # 9
    print(find_max_sum_sub_array(2, [2, 3, 4, 1, 5])) # 7
    print(find_max_sum_sub_array(2, [2, 1, 4, 1, 1])) # 5
    print(find_max_sum_sub_array(3, [2, 1, 4, 1, 1])) # 7
    print(find_max_sum_sub_array(4, [2, 1, 4, 1, 1])) # 8