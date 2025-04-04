# Andare a creare un sistema ripetibile che si occupa di gestire la lunghezza delle stringhe e salvarle, 
# l'utente potrà continuare a inserire dati finché la stringa inserita e più lunga della precedente, alla fine stamperà 
# l'insieme delle stringhe date in input divise da virgole e quante stringhe ha inserito.

class World:
  
  def __init__(self):
    self.strList = []

  def insert(self):
    while True:
      input_str = input("Inserisci una stringa ---> ")
      
      # Se la lista è vuota, accetta qualsiasi stringa come primo inserimento
      if len(self.strList) == 0:
        self.strList.append(input_str)
      elif len(input_str) > len(self.strList[-1]):  # Verifica se la stringa è più lunga della precedente
        self.strList.append(input_str)
      else:
        print("La parola inserita è più corta della precedente, fine programma")
        break
    self.print_all_str()
    print(f"Hai inserito {len(self.strList)} stringe")

  def print_all_str(self):
    print("Le stringhe inserite sono:")
    for s in self.strList:
      print(f"{s}, ")

# Creazione dell'oggetto e utilizzo
world = World()
world.insert()  

