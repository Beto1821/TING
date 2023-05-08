from collections import deque
from ting_file_management.abstract_queue import AbstractQueue


class Queue(AbstractQueue):
    def __init__(self):
        # https://docs.python.org/3.11/library/collections.html#collections.deque
        # utilizando deque para implementar a fila.
        self.queue = deque()

    def __len__(self):
        # retorna o tamanho atual da fila, que é o tamanho da deque.
        return len(self.queue)

    def enqueue(self, value):
        # adiciona um elemento no final da deque
        self.queue.append(value)

    def dequeue(self):
        # remove e retorna o elemento que está no início da deque
        return self.queue.popleft()

    def search(self, index):
        # recebe um índice como parâmetro e retorna o elemento da fila
        # que está no índice especificado.
        if index < 0 or index >= len(self):
            raise IndexError("Índice Inválido ou Inexistente")
        return self.queue[index]
