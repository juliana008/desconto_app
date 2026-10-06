from src_antigo.controllers.pedido_controller import PedidoController
from src_antigo.database.connection import DatabaseConnection
from src_antigo.models.desconto import DescontoNormal, DescontoPremium, DescontoVIP
from src_antigo.models.pedido import Pedido
from src_antigo.repositories.pedido_repository import PedidoRepository
from src_antigo.services.pedido_service import PedidoService

if __name__=="__main__":
    # Criação de objetos
    database = DatabaseConnection()
    repo = PedidoRepository(database)
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