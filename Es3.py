# Andare a creare una funzioni che si occupi di salvare i dati dell'utente, andare a creare una funzione che si occupi di fare il login dell'utente, 
# Andare a creare un funzioni che modifichi i dati dell'utente solo se questi sono già stati creati  / salvati e solo dopo il login. 
# Andare a creare un menu che concateni le tre funzioni precedenti e permetta di ripetere il ciclo a più utenti diversi.
class User:
  
  def __init__(self, name=None, password=None):
    self.name = name
    self.password = password
    self.allUser = {
        1: {'username': 'ciro', 'password': 'password123'},
        2: {'username': 'anna', 'password': 'securepass'},
        3: {'username': 'marco', 'password': '123456'}
    }
    self.idSession = -1
    
  def login(self):
    usName = input('Inserisci nome utente ---> ')
    usPass = input('Inserisci password ---> ')
    for key, val in self.allUser.items():
      if val["username"] == usName and val["password"] == usPass:
        print(f'Login effettuato con successo, benvenuto {val["username"]}')
        self.idSession = key
        return True
    print('Errore nel login...')
    return False
  
  def update_username(self):
    new_username = input("Inserisci nuovo nome utente ---> ")
    if self.idSession in self.allUser:
      self.allUser[self.idSession]['username'] = new_username
      print(f"Username aggiornato con successo a {new_username}")
    else:
      print("ID non trovato!")
      
  def update_password(self):
    if self.idSession in self.allUser:
      rinsPassword = input('Inserisci la password corrente ---> ')
      if rinsPassword == self.allUser[self.idSession]['password']:
        newPass = input('Inserisci nuova password ---> ')
        self.allUser[self.idSession]['password'] = newPass
        print(f"Password aggiornata con successo")
      else:
        print("Password corrente errata!")
    else:
      print("ID non trovato!")
      
  def change_data(self):
    if self.idSession > -1:
      ch = int(input('--- Menu Modifica Dati --- \n 1) Modifica Username \n 2) Modifica Password \n ---> '))
      match ch:
        case 1:
          self.update_username()
        case 2:
          self.update_password()
        case _:
          print("Scelta non valida!")
    else:
      print('Non sei loggato!')
  
  def print_user_data(self):
    if self.idSession > -1:
      user_data = self.allUser[self.idSession]
      print(f"\nDati utente:\nUsername: {user_data['username']}\nPassword: {user_data['password']}")
    else:
      print("Non sei loggato!")

class Main:
  def __init__(self):
    pass

  def menu(self):
    user = User()
    while True:
      if user.login():
        while True:
          ch = int(input("--- Menu account --- \n 1) Modifica Nome \n 2) Modifica Password \n 3) Visualizza Dati Utente \n 4) Esci \n --->"))
          match ch:
            case 1:
              user.update_username()
            case 2:
              user.update_password()
            case 3:
              user.print_user_data()
            case 4:
              print('Arrivederci....')
              break
            case _:
              print('Scelta non valida!')
          if input('Vuoi fare altro? s/n ---> ').lower().strip() == 'n':
            print('Arrivederci....')
            break
      else:
        if input('Accesso non riuscito, riprovare? s/n ---> ').lower().strip() == 'n':
          print('Arrivederci....')
          break

# Esecuzione del programma
main_menu = Main()
main_menu.menu()


