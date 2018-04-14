# Input do usuário
str = input("Insira um número: ")

# We need to know how many characters are in the string so we can place a "pointer" in the middle
string_size = len(str)

if string_size % 2 != 0:
    stop = int((string_size - 1)/2)
else:
    stop = int(string_size/2)
    
# Checking all numbers
for i in (0,stop):
    if str[i] != str[string_size-i-1]:
        print("Não é palíndromo")
        break