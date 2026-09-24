from src.models.desconto import DescontoVIP, DescontoNormal, DescontoPremium
from src.models.pedido import Pedido
from src.services.pedido_servico import PedidoService

if __name__=="__main__":
    
    servico = PedidoService()
    
    """criando pedidos e aplicando descontos"""
    pedido1 = Pedido("Cliente A", DescontoNormal())
    pedido1.valor_original = 100.0 # Definindo o valor original do pedido
    
    pedido2 = Pedido("Cliente B", DescontoVIP())
    pedido2.valor_original = 200.0 # Definindo o valor original do pedido
    
    pedido3 = Pedido("Cliente C", DescontoPremium())
    pedido3.valor_original = 300.0 # Definindo o valor original do pedido
    
    # Criar pedidos, aplicar descontos e processar os pedidos
       
    servico.adicionar_pedido(pedido1)
    servico.adicionar_pedido(pedido2)
    servico.adicionar_pedido(pedido3)
    
    servico.processar_pedidos()