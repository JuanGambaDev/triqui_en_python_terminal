#Importamos libreria random
import random
import string

#Creamos un diccionario para nuestro tablero de juego
mi_tablero = {
  '7':' ', '8':' ', '9':' ',
  '4':' ', '5':' ', '6':' ',
  '1':' ', '2':' ', '3':' '
}

juego_finalizado = False

#imprimimos el tablero
def imprimir_tablero(tablero):
  print("_______")
  print("|" + tablero["7"] + "|" + tablero["8"] + "|" + tablero["9"] + "|")
  print("+-+-+-+")
  print("|" +tablero["4"] + "|" + tablero["5"] + "|" + tablero["6"]+ "|")
  print("+-+-+-+")
  print("|" +tablero["1"] + "|" + tablero["2"] + "|" + tablero["3"]+ "|")
  print("–––––––")

def imprimir_mensaje_ganador(turno, perdedor):
  print("El jugardor " + perdedor + " ha perdido.")
  print(" **** " + "El jugador " + turno + "  ha ganado. ****")

def mensaje_reiniciar():
  reiniciar = input("¿Desea jugar una partida nueva?(si/no): ")

  if reiniciar == "si" or reiniciar == "si":
      for key in mi_tablero:
          mi_tablero[key] = " "
      multijugador()
  else:
    mostrar_menu()

def multijugador():
  turno = "x"
  contador = 0
  perdedor = turno

  for i in range(10):
    imprimir_tablero(mi_tablero)
    print("Es tu turno, " + "jugador " + turno + ", ¿a que lugar desea moverse?")

    movimiento = input()

    if mi_tablero[movimiento] == ' ':
      mi_tablero[movimiento] = turno
      contador += 1
    else:
      print("Ese lugar ya esta lleno.\n a que lugar desea mover?")
      continue

    if contador >= 5:
      # Horizontales
      # Linea superior
      if mi_tablero['7'] == mi_tablero['8'] == mi_tablero['9'] != ' ':
        imprimir_tablero(mi_tablero)
        imprimir_mensaje_ganador(turno,perdedor)
        mensaje_reiniciar()
        break

      # Linea de la mitad
      elif mi_tablero['4'] == mi_tablero['5'] == mi_tablero['6'] != ' ':
        imprimir_tablero(mi_tablero)
        imprimir_mensaje_ganador(turno,perdedor)
        mensaje_reiniciar()
        break

      # Linea inferior
      elif mi_tablero['1'] == mi_tablero['2'] == mi_tablero['3'] != ' ':
        imprimir_tablero(mi_tablero)
        imprimir_mensaje_ganador(turno,perdedor)
        mensaje_reiniciar()
        break

      # Verticales
      # Linea izquierda
      elif mi_tablero['1'] == mi_tablero['4'] == mi_tablero['7'] != ' ':
        imprimir_tablero(mi_tablero)
        imprimir_mensaje_ganador(turno,perdedor)
        mensaje_reiniciar()
        break

      # Linea centrañ
      elif mi_tablero['2'] == mi_tablero['5'] == mi_tablero['8'] != ' ':
        imprimir_tablero(mi_tablero)
        imprimir_mensaje_ganador(turno,perdedor)
        mensaje_reiniciar()
        break

      # Linea derecha
      elif mi_tablero['3'] == mi_tablero['6'] == mi_tablero['9'] != ' ':
        imprimir_tablero(mi_tablero)
        imprimir_mensaje_ganador(turno,perdedor)
        mensaje_reiniciar()
        break

      # Diagonales
      # Izquierda a derecha
      elif mi_tablero['7'] == mi_tablero['5'] == mi_tablero['3'] != ' ': # diagonal 1
        imprimir_tablero(mi_tablero)
        imprimir_mensaje_ganador(turno,perdedor)
        mensaje_reiniciar()
        break

      # Derecha a izquierda
      elif mi_tablero['1'] == mi_tablero['5'] == mi_tablero['9'] != ' ': # diagonal 2
        imprimir_tablero(mi_tablero)
        imprimir_mensaje_ganador(turno,perdedor)
        mensaje_reiniciar()
        break

    if contador == 9:
      print("\nGame Over.\n")
      print("!Es un empate!")
      mensaje_reiniciar()
      break

    # Cambiar de jugador cada movimiento.
    if turno == "x":
      turno = "O"
    else:
        turno = 'x'

    if turno == "x":
      perdedor = "O"
    else:
      perdedor = "x"
  
def quien_comienza():
  # Elije al azar que jugador comienza.
  if random.randint(0, 1) == 0:
    return 'computador'
  else:
    return 'jugador'  


def definir_ganador(mi_tablero):
  #condicionales para ganar
  return mi_tablero['7'] == mi_tablero['8'] == mi_tablero['9'] != ' ' or mi_tablero['4'] == mi_tablero['5'] == mi_tablero['6'] != ' ' or mi_tablero['1'] == mi_tablero['2'] == mi_tablero['3'] != ' ' or mi_tablero['1'] == mi_tablero['4'] == mi_tablero['7'] != ' ' or mi_tablero['2'] == mi_tablero['5'] == mi_tablero['8'] != ' ' or mi_tablero['3'] == mi_tablero['6'] == mi_tablero['9'] != ' ' or mi_tablero['7'] == mi_tablero['5'] == mi_tablero['3'] != ' ' or mi_tablero['1'] == mi_tablero['5'] == mi_tablero['9'] != ' '
  
def quienComienza():
  # Elije al azar que jugador comienza.
  if random.randint(0, 1) == 0:
    return 'la computadora'
  else:
    return 'el jugador'  

def jugada_computador():
  posibilidades =['1','2','3','4','5','6','7','8','9']
  jugada_compu = random.choice(posibilidades)
  return jugada_compu


def hay_espacio(tablero,jugada): 
  if tablero[jugada] == ' ':
    return True
  else:
    return False

def contra_compu():
  """creo dos variable vacias haciendo refencia a quienes vas a jugar que va a hacer el usuario (jugador) y el computador (cpu)"""
  jugador = " "
  cpu = " "

  #permitimos que el usuario elija la letra con la que va a jugar.
  print("escoja la letra con la que desea jugar (x/o)")
  letra_escogida = input()
  if letra_escogida == "x":
    jugador = "x"
    cpu = "o"
  else:
    jugador = "o"
    cpu = "x"  
  print("Tu ficha de juego será: " + jugador)

  turno = quien_comienza()
  juego_en_curso = True
  
  while juego_en_curso:
    #turno del jugador
    #imprimimos tablero y preguntamos donde desea jugar  
    if turno == "el jugador":
      print("jugador " + jugador +", elija la casilla donde desea jugar (1-9):")
      movimiento = input()
      if mi_tablero[movimiento] == ' ':
        mi_tablero[movimiento] = jugador
        imprimir_tablero(mi_tablero)
        print(jugador + " has jugado")
      else:
        print("+++Esa casilla ya esta llena+++")
        continue
      if definir_ganador(mi_tablero):
        print(jugador + " has ganado")
        juego_en_curso = False
      else:
          if hay_espacio(mi_tablero,movimiento):
            imprimir_tablero(mi_tablero)
            print('¡Es un empate!')
            break
  
          else:
            turno= "el computador"

    #turno computador
    else:
      turno == "el computador"
      jugada_compu = jugada_computador()
      
      if mi_tablero[jugada_compu] == ' ':
        mi_tablero[jugada_compu] = cpu
        imprimir_tablero(mi_tablero)   
        print("CPU ha jugado")
        if definir_ganador(mi_tablero):
          imprimir_tablero(mi_tablero)
          print("la CPU ha ganado")
          juego_en_curso = False
        else:
          if hay_espacio(mi_tablero,jugada_compu):
            imprimir_tablero(mi_tablero)
            print('¡Es un empate!')
            break
          
          else:
            turno= "el jugador"
    
  else: 
    mensaje_reiniciar()
    

#Creamos el mensaje de bienvenida y las instrucciones
def mensaje_bienvenida():
  print('''
   _______________________________________________
  |Bienvenidos al juego triqui                    |
  |Presentado por:Juan Sebastian Gamba Jacomussi  |
  |_______________________________________________|
  ''')
  print("¿Como funciona el juego?                                   El tablero está numerado como el teclado numérico del teclado. Y así, un jugador puede hacer su movimiento en el tablero de juego ingresando el número desde el teclado numérico.")

  print("_______")
  print("|" + "7" + "|" + "8" + "|" + "9" + "|")
  print("+-+-+-+")
  print("|" + "4" + "|" + "5" + "|" + "6" + "|")
  print("+-+-+-+")
  print("|" + "1" + "|" + "2" + "|" + "3" + "|")
  print("–––––––")

#Creamos el menu y sus opciones
def mostrar_menu():
  print("Seleccione un modo de juego")
  print("1.- Jugar con un compañero")
  print("2.- Jugar con la CPU")
  print("3.- Salir")

  opc = int(input("Elija una opción (1-3): "))

  #Jugar con un compañero
  if opc == 1:
    multijugador()
    
  #Jugar contra la CPU
  elif opc == 2:
    contra_compu()

  # Salir de la aplicación
  elif opc == 3:
    print("--> Fin")
    print("")
    exit()

def init():
  mensaje_bienvenida()
  mostrar_menu()

if __name__ == "__main__":
  init()
