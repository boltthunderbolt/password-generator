import random

# Kamus leetspeak untuk mengganti karatkter tertentu dengan angka
leet_dict = {
  'a': '4', 'A': '4',
  'e': '3', 'E': '3',
  'i': '1', 'I': '1',
  'o': '0', 'O': '0',
  's': '5', 'S': '5',
  't': '7', 'T': '7'
}

def replace_with_leetspeak(user_input):
  # Mengganti beberapa karakter dalam input user dengan angka menggunakan kamus leetspeak
  leet_input = ''.join([leet_dict[char] if char in leet_dict else char for char in user_input])
  return leet_input

def generate_password(length, user_input):
  # Daftar lengkap characters
  characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-_=+[]{}|;:',.<>?/~`"

  # Ganti beberapa karakter dalam input user dalam bentuk angka untuk memperkuat password
  leet_input = replace_with_leetspeak(user_input)
  # Password yang telah diubah menjadi leetspeak
  password = leet_input

  # Menggabungkan input user dengan karakter acak dari daftar characters
  # Tambahkan karakter acak jika user menentukan panjang karakter lebih dari password
  while len(password) < length:
    password += random.choice(characters)
  
  # Acak kembali hasil password untuk memastikan kerandoman
  password = ''.join(random.sample(password, len(password)))
  return password

def get_user_input():
  # Mengambil input password dari user
  user_input = input("Input the part of your password: ")
  return user_input