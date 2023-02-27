import random
import string

def password_generador(len_pass=8):
    ascii_options = string.ascii_letters
    number_options = string.digits
    punt_options = string.punctuation
    options = ascii_options + number_options + punt_options

    senha_usuario = ""
    for i in range(0, len_pass):
        digit = random.choice(options)
        if digit not in senha_usuario:
            senha_usuario += digit
    
    return senha_usuario

choise_user = input('Quantos digitos na senha?')           

if choise_user.isdigit():
    choise_user = int(choise_user)
else:
    print('Entrada inválida!')    
    quit()

response = password_generador(len_pass = choise_user)    
print(f'Senha gerada:\n{response}')