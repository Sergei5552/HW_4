length_set_1_2 = input('Введите количество элементов первого и второго множества через пробел: ').split()
set_1_2 = [set(), set()]
j = 0

while j < 2:
    for i in range(int(length_set_1_2[j])):
        set_1_2[j].add(int(input(f"Введите элемент множества {j + 1}: ")))
    j += 1

print(*sorted(list(set_1_2[0].intersection(set_1_2[1]))))

