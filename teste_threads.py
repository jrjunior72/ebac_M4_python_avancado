import threading
import time

def tarefa(nome):
    for i in range(3):
        print(f'{nome} - execução {i+1}')
        time.sleep(1)

# Cria duas threads
t1 = threading.Thread(target=tarefa, args=('Thread 1' ,))
t2 = threading.Thread(target=tarefa, args=('Thread 2' ,))

# Inicia as threads
t1.start()
t2.start()

# Aguarda as threads terminarem
t1.join()
t2.join()

print('Finalizado com sucesso')