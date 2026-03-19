# Задача 2.
# Создать класс. Очередь на структуре данных двусвязный список.
#
#
#
# class Node:
#     """
#     Вспомогательный класс для узлов списка
#     """
#     def __init__(self, data):
#         self.data = data  # храним информацию
#         self.nref = None  # ссылка на следующий узел
#         self.pref = None  # Ссылка на предыдущий узел
#
#
# class Queue:
#     """
#     Основной класс
#     """
#
#     def __init__(self):
#         self.start = None  # ссылка на начало очереди
#         self.end = None  # ссылка на конец очереди
#
#     def pop(self):
#         """
#         возвращаем элемент val из начала списка с удалением из списка
#         """
#         pass
#         return val
#
#     def push(self, val):
#         """
#         добавление элемента val в конец списка
#         """
#         pass
#
#     def insert(self, n, val):
#         """
#         вставить элемент val между элементами с номерами n-1 и n
#         """
#         pass
#
#     def print(self):
#         """
#         вывод на печать содержимого очереди
#         """
#         pass
class Node:
    """
    Вспомогательный класс для узлов двусвязного списка.
    Каждый узел хранит данные и ссылки на следующий и предыдущий узлы.
    """
    def __init__(self, data):
        self.data = data      # данные узла
        self.nref = None      # ссылка на следующий узел
        self.pref = None      # ссылка на предыдущий узел


class Queue:
    """
    Основной класс для очереди, реализованной на двусвязном списке.
    В очереди доступ к элементам осуществляется по принципу FIFO (первым пришёл — первым вышел).
    """
    def __init__(self):
        self.start = None     # ссылка на начало очереди (первый элемент)
        self.end = None       # ссылка на конец очереди (последний элемент)

    def pop(self):
        """
        Удаляет и возвращает первый элемент очереди.
        Если очередь пуста, возвращает None.
        """
        if self.start is None:
            return None                 # очередь пуста
        val = self.start.data
        self.start = self.start.nref    # перемещаем начало на следующий узел
        if self.start is not None:
            self.start.pref = None      # у нового начала нет предыдущего
        else:
            self.end = None              # очередь стала пустой
        return val

    def push(self, val):
        """
        Добавляет новый элемент val в конец очереди.
        """
        new_node = Node(val)
        if self.end is None:
            # очередь пуста — новый элемент становится и началом, и концом
            self.start = new_node
            self.end = new_node
        else:
            new_node.pref = self.end
            self.end.nref = new_node
            self.end = new_node

    def insert(self, n, val):
        """
        Вставляет элемент val на позицию n (нумерация с 0).
        Элемент оказывается между элементами с индексами n-1 и n.
        При n=0 вставляет в начало, при n=длина_очереди — в конец.
        """
        new_node = Node(val)

        # Вставка в начало (n == 0)
        if n == 0:
            new_node.nref = self.start
            if self.start is not None:
                self.start.pref = new_node
            self.start = new_node
            if self.end is None:          # очередь была пуста
                self.end = new_node
            return

        # Ищем элемент, который сейчас находится на позиции n
        current = self.start
        index = 0
        while current is not None and index < n:
            current = current.nref
            index += 1

        # Если n больше длины очереди, вставляем в конец
        if current is None:
            if self.end is not None:
                self.end.nref = new_node
                new_node.pref = self.end
                self.end = new_node
            else:
                # очередь пуста (n > 0 быть не может, но обработаем)
                self.start = new_node
                self.end = new_node
        else:
            # Вставка перед current (между его предыдущим и самим current)
            prev = current.pref
            new_node.pref = prev
            new_node.nref = current
            if prev is not None:
                prev.nref = new_node
            current.pref = new_node

    def print(self):
        """
        Выводит содержимое очереди на печать от начала к концу.
        """
        current = self.start
        elements = []
        while current is not None:
            elements.append(str(current.data))
            current = current.nref
        print(" -> ".join(elements))
