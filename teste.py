""" numPedidos = int(input())
pedidos = dict()
todos_pedidos = list()
for i in range(1, numPedidos + 1):
    prato = input()
    calorias = int(input())
    ehVegano = False
    
    vegano = str(input()).lower()
    if vegano == 's':
     veg = "(Vegano)-"
    elif vegano == 'n':
     veg ="(Nao-vegano)-"
    
    pedidos["prato:"]= prato
    pedidos["vegano:"]= veg
    pedidos["calorias:"]= calorias
    
    todos_pedidos.append(pedidos)

for p in todos_pedidos:
    
    for x in p:
      print(f'Pedido: {todos_pedidos.index(p)+1}',end="")
      print(x.get('')) """
     
                



