from password import passwordGenerator
 
def user_input_the_password():
  global user_input, length
  try:
    length = int(input("Input the length of password characters you want: "))
    if length < 1:
      print("Password length must bigger than 0")
      return
    
    while True:
      user_input = passwordGenerator.get_user_input()
      if len(user_input) > length:
        print(f"\nYour password character more than {length}")
      else: break
  except ValueError:
    raise ValueError;

def show_results():
  while True:
    password = passwordGenerator.generate_password(length, user_input)
    print(f"Generate result: {password}\n");
    generate_again = input("Generate again? [y/n] ")
    match generate_again:
      case "y" | "yes" | "Y" | "Yes" | "YES": return show_results()
      case _: break

if __name__ == '__main__':
  user_input_the_password()