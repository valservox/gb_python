'''
Задача №33. Решение в группах
Хакер Василий получил доступ к классному журналу и
хочет заменить все свои минимальные оценки на
максимальные. Напишите программу, которая
заменяет оценки Василия, но наоборот: все
максимальные – на минимальные.

Input: 5 -> 1 3 3 3 4
Output: 1 3 3 3 1
'''

def change_scores(scores_list: list, ind: int):

    max_score = max(scores_list)
    min_score = min(scores_list)
    
    if ind == len(scores_list):
        return
    
    if scores_list[ind] == max_score:
        scores_list[ind] = min_score

    change_scores(scores_list,ind + 1)

input_list = [1, 3, 3, 3, 4]

print(f'Before: {input_list}')
change_scores(input_list,0)
print(f'After: {input_list}')