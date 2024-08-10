import random
 
def generate_password(length, user_input):
  # Daftar lengkap characters
  characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-_=+[]{}|;:',.<>?/~`"

  # Menggabungkan input user dengan karakter acak dari daftar characters
  password = user_input
  while len(password) < length:
    password += random.choice(characters)
  
  # Acak kembali hasil password untuk memastikan kerandoman
  password = ''.join(random.sample(password, len(password)))
  return password

def get_user_input():
  # Mengambil input password dari user
  user_input = input("Input the part of your password: ")
  return user_input