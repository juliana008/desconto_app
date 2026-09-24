from src.models.desconto import DescontoVIP
from src.models.pedido import Pedido
from src.services.pedido_servico import PedidoService
if __name__=="__main__":
    pedido = Pedido("Leonardo", DescontoVIP())
    pedido_servico = PedidoService()
    
    valor_final = pedido.valor_final(100)
    
    pedido_servico.adicionar_pedido(pedido)
    pedido_servico.processar_pedidos()