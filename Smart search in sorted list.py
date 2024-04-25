def smart_search_in_sorted_list(k,lst):
    l = len(lst)//2
    if lst[0] == k:
        return True
    elif l == 1:
        return False
    elif lst[l] > k:
        return smart_search_in_sorted_list(k,lst[:l])
    else:
        return smart_search_in_sorted_list(k,lst[l:])