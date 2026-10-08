from src.app.entities.pedido import Pedido
from src.app.entities.desconto import DescontoNormal, DescontoVIP, DescontoPremium
from src.app.gateways.pedido_gateway import IPedidoGateway


class CriarPedido:
    def __init__(self, pedido_gateway: IPedidoGateway):
        self.pedido_gateway = pedido_gateway

    def executar(self, cliente: str, valor_original: float, tipo_desconto: str) -> Pedido:
        tipo = tipo_desconto.lower()

        if tipo == "normal":
            desconto = DescontoNormal()
        elif tipo == "vip":
            desconto = DescontoVIP()
        elif tipo == "premium":
            desconto = DescontoPremium()
        else:
            raise ValueError("Tipo de desconto inválido")

        pedido = Pedido(cliente, valor_original, desconto)
        self.pedido_gateway.salvar(pedido)

        return pedido

    def listar_pedidos(self) -> list[Pedido]:
        return self.pedido_gateway.listar()