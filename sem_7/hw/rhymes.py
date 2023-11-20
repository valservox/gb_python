stroka = 'за-гад-ка-ра-свет-ка-ра-газ-да-не-на-ма-ли-ва-ла'

def rythm(input_stroka):

    stroka_list = input_stroka.lower().split()

    if len(stroka_list) == 1:
        return print('Количество фраз должно быть больше одной!')

    ans = (list(map(lambda x: sum([1 if i in 'ауоыиэяюёе' else 0 for i in x]),stroka_list)))

    print('Парам пам-пам' if ans.count(ans[0]) == len(ans) else 'Пам парам')

rythm(stroka)