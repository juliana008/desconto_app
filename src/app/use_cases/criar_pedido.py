from src.app.entities.pedido import Pedido
from src.app.factories.desconto_factory import DescontoFactory
from src.app.gateways.pedido_gateway import IPedidoGateway
from src.app.dtos.criar_pedido_input_dto import CriarPedidoInputDTO
from src.app.dtos.criar_pedido_output_dto import CriarPedidoOutputDTO


class CriarPedido:
    def __init__(
        self,
        pedido_gateway: IPedidoGateway,
        desconto_factory: DescontoFactory | None = None,
    ):
        self.pedido_gateway = pedido_gateway
        self.desconto_factory = desconto_factory or DescontoFactory()

    def executar(self, input_dto:CriarPedidoInputDTO) -> CriarPedidoOutputDTO:
        tipo_desconto = input_dto.tipo_desconto.lower().strip()
        desconto = self.desconto_factory.criar(tipo_desconto)

        pedido = Pedido(input_dto.cliente, input_dto.valor_original, desconto)
        self.pedido_gateway.salvar(pedido, tipo_desconto)

        return CriarPedidoOutputDTO(
            cliente=input_dto.cliente,
            valor_original=input_dto.valor_original,
            valor_desconto=pedido.valor_desconto(),
            valor_final=pedido.valor_final(),
            tipo_desconto=input_dto.tipo_desconto
        )

    def listar_pedidos(self) -> list[CriarPedidoOutputDTO]:
        pedidos=self.pedido_gateway.listar()
        
        lista_dto=[]
        
        for registro in pedidos:
            pedido=registro["pedido"]
            dto=CriarPedidoOutputDTO(
                cliente=pedido.cliente,
                valor_original=pedido.valor_original,
                valor_desconto=pedido.valor_desconto(),
                valor_final=pedido.valor_final(),
                tipo_desconto=registro["tipo_desconto"]
            )
            lista_dto.append(dto)
        
        return lista_dto