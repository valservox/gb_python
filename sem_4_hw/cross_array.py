var1 = '5 5'
var2 = '10 20 30 40 50'
var3 = '10 20 30 40 50'

var2_set = set(var2.split())
var3_set = set(var3.split())

ans_arr = sorted(var2_set & var3_set)

ans = ''

for i in ans_arr:
    ans += i + ' '
    
print(ans[:-1])