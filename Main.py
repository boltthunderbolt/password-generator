from password import user
from time import sleep 

def main():
  user.user_input_the_password()
  user.show_results()
  menu()

def menu():
  menu_program = input("Want to generate another password? [y / n] : ")
  while True:
    match menu_program:
      case "y" | "yes" | "Y" | "Yes" | "YES":
        print('\n' * 100);
        return main()
      case "n" | "no" | "N" | "No" | "NO":
        sleep(3)
        print('\n' * 100, "Program stopped")
        break

if __name__ == '__main__':
  main()