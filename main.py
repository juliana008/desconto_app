from src.app.adapters.controllers.pedido_controller import PedidoController
from src.app.frameworks.database.memory_database import MemoryDatabase
from src.app.adapters.repositories.memory_pedido_repository import MemoryPedidoRepository
from src.app.use_cases.criar_pedido import CriarPedido


if __name__ == "__main__":
    database = MemoryDatabase()
    criar_pedido_gateway = MemoryPedidoRepository(database)
    criar_pedido_use_case = CriarPedido(criar_pedido_gateway)
    controller = PedidoController(criar_pedido_use_case)

    controller.criar_pedido("vitin", 100, "normal")
    controller.criar_pedido("atilario", 200, "vip")
    controller.criar_pedido("pepivis", 300, "premium")

    print("Pedidos registrados:")
    for pedido in controller.listar_pedidos():
        print(pedido)