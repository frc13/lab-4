# Ədədi massiv yaratmaq
initial_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Fayl adını təyin etmək
file_name = "numbers.txt"

# Faylı yaratmaq və ədədləri yazmaq
with open(file_name, 'w') as file:
    for number in initial_numbers:
        file.write(str(number) + '\n')

# Fayldan ədədləri oxumaq və cüt nömrələri 2 dəfə artırmaq
new_numbers = []
with open(file_name, 'r') as file:
    for line in file:
        number = int(line.strip())
        if number % 2 == 0:
            number *= 2
        new_numbers.append(number)

# Yeni fayla yazmaq
new_file_name = "new_numbers.txt"
with open(new_file_name, 'w') as new_file:
    for number in new_numbers:
        new_file.write(str(number) + '\n')

# Ədədi orta hesablamaq
average = sum(new_numbers) / len(new_numbers)

# Nəticəni çap etmək
print(f"Yeni ədəd massivi: {new_numbers}")
print(f"Ədədi orta: {average}")