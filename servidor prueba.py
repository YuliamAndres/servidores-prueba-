import socket
import threading
HOST = "0.0.0.0"
PORT = 12345

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

activo = True
def consola():
    global activo

    while activo:
        comando = input(">> ")
        
        if comando.lower() =="apagar":
            print("apagando servidor...")
            activo = False
            server.close()


threading.Thread(target=consola).start()

print ("servidor iniciado")


while activo:
    try:
        cliente, direccion = server.accept()
        print(F"cliente conectado: {direccion}")
        
        cliente.send("Hola".encode())
        cliente.close()

    except:
        break

print ("Servidor apagado")    

