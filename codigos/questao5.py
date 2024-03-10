# Escreva um programa que inverta os caracteres de um string.

# IMPORTANTE:
# a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
# b) Evite usar funções prontas, como, por exemplo, reverse;

def inverter(s):
  invertido = ''
  for i in range(len(s) -1, -1, -1): invertido += s[i]
  return invertido

string = 'Larissa'
print(f'String invertida da palavra {string}:',inverter(string))