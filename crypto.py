import random
import string

# Liste des caracteres  
symbols = list(string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation + ' ' + '”' + '“') * 2
random.shuffle(symbols)

SIZE = 20
matrix = [[''] * SIZE for _ in range(SIZE)]

# Remplissage sequentiel
index = 0
for i in range(SIZE):
  for j in range(SIZE):  
    if index < len(symbols):
      matrix[i][j] = symbols[index]
      index += 1
    else:
      index = 0

# Mappings  
mappings = {}
for i in range(SIZE):
  for j in range(SIZE):
     mappings.setdefault(matrix[i][j], []).append((i,j))
     
# Affichage matrice
def displayMatrice():
  print("\nMatrice:")
  for row in matrix:
    print(row)
      
# Chiffrement
def encrypt(msg):

  cipher = ""

  for char in msg:

    x, y = random.choice(mappings[char])

    # Longueur x
    x_len = len(str(x))
    cipher += str(x_len)
    
    # Valeur x
    cipher += str(x)

    # Longueur y 
    y_len = len(str(y))
    cipher += str(y_len)

    # Valeur y
    cipher += str(y)

  return cipher

# Déchiffrement
def decrypt(cipher):

  msg = ""

  i = 0
  while i < len(cipher):

    # Longueur x
    x_len = int(cipher[i])

    # Coord x
    x = cipher[i+1 : i+1+x_len]  

    # Longueur y
    i += 1 + x_len
    y_len = int(cipher[i])

    # Coord y 
    y = cipher[i+1 : i+1+y_len]

    # Caractère
    i += 1 + y_len
    msg += matrix[int(x)][int(y)]

  return msg
  
# Tests 
# Encryption/Decryption functions 

while True:

  print("What do you want to do?")
  print("1. Encrypt a message")
  print("2. Decrypt a message")
  print("3. Display the matrix")
  print("4. Quit")
  
  choice = input("> ")
  
  if choice == '1':
    msg = input("Message to encrypt: ")
    print("Encrypted:", encrypt(msg))

  elif choice == '2':
   
    cipher = input("Message to decrypt: ")
    print("Decrypted:", decrypt(cipher))
  
  elif choice == '3':
    print("Here is the matrix : ")
    displayMatrice()

  elif choice == '4':
    print("Goodbye!")
    break
  
  else:
    print("Invalid choice")