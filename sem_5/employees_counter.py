def calc_all_count(sp):
    
    res = 0

    for item in sp:

        if isinstance(item,int):
            res += item

        else:
            res += calc_all_count(item)

        return res




count_angola = 18
count_new_york = [20, [10, 7]]
count_chicago = 15
count_usa = [count_new_york,count_chicago ]
count_all = [count_angola, count_usa]

print(count_all)
print(calc_all_count(count_all))