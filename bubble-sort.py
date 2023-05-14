#!/usr/bin/env python
# coding: utf-8

# Criando um algoritmo de bubble sort para ordenar de forma CRESCENTE uma lista com números embaralhados

# In[6]:


lista1 = [25, 12, 7, 2, 45, 34, 1, 5, 3, 54, 37]

def bubble_sort(arr):
    # define o tamanho da lista
    n = len(lista1)
    
    # 1º loop percorre a lista por inteiro
    for i in range(n):
        
        # 2º loop evita que o item atual se compare com ele mesmo
        for j in range(0, n-i-1):
            
            # verifica se o item atual é maior que o próximo item, ou seja, se o item com índice +1 em relação ao item atual
            if arr[j] > arr[j+1]:
                
                # se o item atual for maior que o próximo item (o que tem índice +1), eles trocam de lugar
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

print(bubble_sort(lista1))


# Perceba que para trocar de lugar os itens dentro da lista, o que é feito é a troca de lugar entre as etiquetas que acessam
# os itens da lista, através do índice

# In[ ]:




