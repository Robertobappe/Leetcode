# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Passo 1: Criar um nó "dummy" (sentinela)
        # Este nó é um truque comum para simplificar a lógica,
        # pois nos dá um ponto de partida fixo para a nova lista mesclada.
        # O valor do nó não importa, pois ele não fará parte da lista final.
        dummy = ListNode()

        # Passo 2: Criar um ponteiro 'current' (atual)
        # Este ponteiro vai ser usado para construir a nova lista mesclada.
        # Ele sempre apontará para o último nó que foi adicionado à lista mesclada.
        current = dummy

        # Passo 3: Iterar enquanto houver nós em ambas as listas (list1 e list2)
        # Comparamos os valores dos nós atuais e adicionamos o menor à nossa nova lista.
        while list1 is not None and list2 is not None:
            if list1.val <= list2.val:
                # Se o valor de list1 for menor ou igual ao de list2,
                # anexamos o nó de list1 à lista mesclada.
                current.next = list1
                # E então avançamos o ponteiro de list1 para o próximo nó.
                list1 = list1.next
            else:
                # Caso contrário, o valor de list2 é menor,
                # então anexamos o nó de list2 à lista mesclada.
                current.next = list2
                # E avançamos o ponteiro de list2 para o próximo nó.
                list2 = list2.next

            # Em ambos os casos, depois de anexar um nó,
            # precisamos mover o ponteiro 'current' para o nó que acabamos de adicionar.
            # Isso garante que 'current' esteja sempre no último nó da lista mesclada,
            # pronto para anexar o próximo.
            current = current.next

        # Passo 4: Anexar os nós restantes (se houver)
        # Após o loop principal, uma das listas (ou ambas) pode ter se esgotado.
        # Se list1 ainda tiver nós, significa que todos os seus valores restantes
        # são maiores que os de list2 (que já foram adicionados),
        # então podemos simplesmente anexá-los ao final da nossa lista mesclada.
        if list1 is not None:
            current.next = list1
        # O mesmo se aplica a list2. Se list2 ainda tiver nós, anexamos eles.
        elif list2 is not None:
            current.next = list2

        # Passo 5: Retornar a cabeça da lista mesclada
        # Lembre-se que 'dummy' foi um nó sentinela. A verdadeira cabeça
        # da nossa lista mesclada é o nó que 'dummy.next' aponta.
        return dummy.next