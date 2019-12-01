import random
import ast
# import only system from os 
from os import system, name 
  
# import sleep to show output for some time period 
from time import sleep 

# define our clear function 
def clear(): 
  
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 

def czyszczenie(t):
  # sleep for t seconds after printing output 
    sleep(t) 
  
      # now call function we defined above 
    clear() 
while(True):
  while(True):
    
    choice=input("""
    1. Wczytaj tablice z pliku
    2. Stworz nowa tablice
    """)
    czyszczenie(0)
    if choice=="1":
      myFile = open('tablica.txt', 'r')
      lista = ast.literal_eval(myFile.read())
      myFile.close()
      
    elif choice=="2":  
      n=int(input("Podaj rozmiar tablicy: "))
      lista = [None]*n
      a=int(input("Podaj dolna granice elementow tablicy: "))
      z=int(input("Podaj gorna granice elementow tablicy: "))
      for i in range(0,n):
        lista[i]=random.randint(a,z)
        czyszczenie(0)
    else:
      print("Nie ma takiego wyboru w menu")
      czyszczenie(1)
      break
    
    while(True):
      print("Twoja tablica: ")
      print(lista)
      menu=input("""
      1. Wyswietl minimum 
      2. Wyswietl maximum
      3. Wyswietl srednia
      4. Posortuj
      5. Zapisz tablice do pliku
      6. Nowa tablica
      """)
      if menu=="1":
        print("Min: ", min(lista))
        czyszczenie(2)
      elif menu=="2":
        print("Max: ", max(lista))
        czyszczenie(2)
      elif menu=="3": 
        print("Avg: ", (sum(lista)/len(lista)))
        czyszczenie(2)
      elif menu=="4":
        lista.sort()
        print(lista)
        czyszczenie(3)
      elif menu=="5":
        myFile = open('tablica.txt', 'w')
  
        # Print the list to file
        print(lista, file=myFile)
  
        # Close the file
        myFile.close()
        czyszczenie(0)

      elif menu=="6":
        czyszczenie(0)
        break
      else:
        print("Nie ma takiego wyboru w menu")
        czyszczenie(1)
        break