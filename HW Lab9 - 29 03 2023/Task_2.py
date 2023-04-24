# Задача 2. Да се напише програма, която да създаде множество от множества, което да
# съдържа: А - B, B, B-A, A-B + B-A, A & B, A | B, където A и B са два списъка, чиито
# елементи се въвеждат от клавиатурата.

List_A = [1,2,3,4]
List_B = [4,5,6]

union_sets = set()

Set_A = set(List_A)
Set_B = set(List_B)

# print(Set_B)

union_sets = (Set_A - Set_B),Set_B,(Set_B - Set_A),((Set_A - Set_B)|(Set_B - Set_A)),(Set_A & Set_B),(Set_A|Set_B)

z=(Set_B - Set_A)

print(z)

print(f'обединеното множество е {union_sets}')

