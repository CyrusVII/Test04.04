# Crea un sistema ripetibile che si occupi di dividere su tre possibili liste i tipi basilari di dato che riceve in entrata. 
# Deve poter stampare una lista singola o tutte.  Si deve ripetere X volte definite all'inizio dall'utente

#definizione classe
class TipiBasilari:
  def __init__(self):
    self.n_int = []
    self.n_float = []
    self.boolean = []
    self.str = []
    
  #prendiamo l input dell utente e smistiamo
  def take_input(self):
    roll = int(input("Quanti volte vuoi inserire i dati---> "))
    for _ in range(roll):
      dato = input("Inserisci il dato ---> ")
      #controlli per definire la variabile
      if dato.isdigit():
        self.n_int.append(int(dato))
      elif dato.count('.') == 1:
        self.n_float.append(float(dato))
      elif dato.lower().strip() in ['true','false']:
        self.boolean.append(dato.lower().strip() == 'true')
      else:
        self.str.append(dato)
        
  #def di print
  def print_all_date(self):
      # Stampa tutte le liste
      print("Interi:", self.n_int)
      print("Float:", self.n_float)
      print("Booleani:", self.boolean)
      print("Stringhe:", self.str)
 
#funzione per il main     
def main():
  tB = TipiBasilari()
  # Crea un'istanza della classe TipiBasilari
  tipi = TipiBasilari()
  tipi.take_input()  # Permette di inserire i dati

  while True:
    print("\n--- Menu --- \n 1) Stampa lista degli interi \n2) Stampa lista dei float \n 3) Stampa lista dei booleani \n 4) Stampa lista delle stringhe \n 5) Stampa tutte le liste \n 6) Uscita")
    ch = int(input("---> "))
    match ch:
      case 1:
        print("Interi:", tipi.n_int)
      case 2:
        print("Float:", tipi.n_float)
      case 3:
        print("Booleani:", tipi.boolean)
      case 4:
        print("Stringhe:", tipi.str)
      case 5:
        tipi.print_all_date()  
      case 6:
        print("Uscita...")
        break
      case _:
        print("Opzione non valida. Riprova.")
    if input('Vuoi uscire? s/n ---> ').lower().strip() == 's':
      break
#avvio programma
main()

