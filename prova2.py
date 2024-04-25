estoqueProdutos = []
pedidosPendentes = []
vendasRealizadas = []

def adicionarProduto(novoProduto): 
    if type(novoProduto) != str:
        print('Error: apenas strings podem ser adicionadas')
    else: estoqueProdutos.append(novoProduto) 
    
    print("estoque atual", estoqueProdutos)
    
def removerProduto(produtoRemovido): 
    if produtoRemovido not in estoqueProdutos: 
        print('Produto nao encontrado')
    else: estoqueProdutos.remove(produtoRemovido) 
    
    print("estoque atual", estoqueProdutos)

def adicionarPedido(novoPedido):
    if novoPedido in estoqueProdutos:
        
        pedidosPendentes.append(novoPedido)
        
        print("Produto", novoPedido,"adicionado a lista de pedidos")
        print(pedidosPendentes)
    else:
        print("O produto", novoPedido, "nao esta disponivel no estoque")
        
def processarCompra():
        compra = pedidosPendentes.pop(0)
        vendasRealizadas.append(compra)
        estoqueProdutos.remove(compra)
        
        print('Compra realizada')
    
def desfazerCompra():
        compra = vendasRealizadas.pop()
        estoqueProdutos.append(compra)
        
        print('Compra desfeita')

print('Metodo para adicionar produto na lista de estoque')
print("Estoque", estoqueProdutos)        
adicionarProduto('banana')
adicionarProduto('alface')
adicionarProduto('pepino')
adicionarProduto('carne')
adicionarProduto('frango')
adicionarProduto('peixe')
adicionarProduto(10)

print('---------------------------------------------------------------------------')

print('Metodo para remover produto da lista de estoque')
print('Estoque', estoqueProdutos)
removerProduto('banana')
removerProduto('alface')
removerProduto('abacate')

print('---------------------------------------------------------------------------')

print('Metodo para adicionar novo pedido de compra')
print("pedidos atualmente pendentes", pedidosPendentes)
adicionarPedido('pepino')
print("pedidos atualmente pendentes", pedidosPendentes)
adicionarPedido('carne')
print("pedidos atualmente pendentes", pedidosPendentes)
adicionarPedido('peixe')
print("pedidos atualmente pendentes", pedidosPendentes)
adicionarPedido('frango')
print("pedidos atualmente pendentes", pedidosPendentes)
adicionarPedido('banana')
print("pedidos atualmente pendentes", pedidosPendentes)

print('---------------------------------------------------------------------------')

print('Metodo para processar pedido de compra')
print('Estoque:', estoqueProdutos,'Pedido pendentes:', pedidosPendentes, 'Vendas realizadas', vendasRealizadas)
processarCompra()
print('Estoque:', estoqueProdutos,'Pedido pendentes:', pedidosPendentes, 'Vendas realizadas', vendasRealizadas)
processarCompra()
print('Estoque:', estoqueProdutos,'Pedido pendentes:', pedidosPendentes, 'Vendas realizadas', vendasRealizadas)
processarCompra()
print('Estoque:', estoqueProdutos,'Pedido pendentes:', pedidosPendentes, 'Vendas realizadas', vendasRealizadas)


print('---------------------------------------------------------------------------')

print('Metodo para desfazer compra')
print("vendas realizadas:", vendasRealizadas,'Estoque:' , estoqueProdutos)
desfazerCompra()
print("vendas realizadas:", vendasRealizadas,'Estoque:' , estoqueProdutos)
desfazerCompra()
print("vendas realizadas:", vendasRealizadas,'Estoque:' , estoqueProdutos)

print('---------------------------------------------------------------------------')

print("Resultado final:", "Estoque:", estoqueProdutos, "Pedentes:", pedidosPendentes, "Vendas:", vendasRealizadas)
