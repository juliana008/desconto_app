from src.controllers.pedido_controller import PedidoController
from src.repositories.pedido_repository import PedidoRepository
from src.services.pedido_service import PedidoService
from src.database.connection import DatabaseConnection
from src.models.pedido import Pedido
from src.models.desconto import DescontoVIP, DescontoNormal, DescontoPremium




if __name__=="__main__":
    # Criação de objetos
    database = DatabaseConnection()
    repo = PedidoRepository(database)
    repo = PedidoRepository()
    service = PedidoService(repo)
    controller = PedidoController(service)
    
    # Criando um pedido com desconto
    
    pedido1 = Pedido("Jonso", DescontoNormal())
    pedido1.valor_original = 100.0 # Definindo o valor original do pedido
    
    pedido2 = Pedido("Vitin", DescontoVIP())
    pedido2.valor_original = 100.0 # Definindo o valor original do pedido
    
    pedido3 = Pedido("Titila", DescontoPremium())
    pedido3.valor_original = 100.0 # Definindo o valor original do pedido
    
        
    # Salvamento dos pedidos no repositório
    controller.adicionar_pedido(pedido1)
    controller.adicionar_pedido(pedido2)
    controller.adicionar_pedido(pedido3)
    
    # Processando os pedidos
    controller.processar_pedidos()