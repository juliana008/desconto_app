import pytest

from src.app.adapters.repositories.memory_pedido_repository import (
    MemoryPedidoRepository,
)
from src.app.entities.desconto import (
    DescontoNormal,
    DescontoPremium,
    DescontoVIP,
    IDesconto,
)
from src.app.dtos.criar_pedido_input_dto import CriarPedidoInputDTO
from src.app.factories.desconto_factory import DescontoFactory
from src.app.frameworks.database.memory_database import MemoryDatabase
from src.app.use_cases.criar_pedido import CriarPedido


@pytest.fixture
def desconto_vip() -> DescontoVIP:
    return DescontoVIP()


@pytest.fixture
def criar_pedido() -> CriarPedido:
    database = MemoryDatabase()
    gateway = MemoryPedidoRepository(database)
    return CriarPedido(gateway)


def test_desconto_normal_calcula_dez_porcento() -> None:
    desconto = DescontoNormal()

    assert desconto.calcular(100) == 10


def test_desconto_vip_calcula_vinte_porcento(
    desconto_vip: DescontoVIP,
) -> None:
    assert desconto_vip.calcular(200) == 40


@pytest.mark.parametrize(
    ("valor", "valor_esperado"),
    [(100, 30), (200, 60), (300, 90)],
)
def test_desconto_premium_calcula_trinta_porcento(
    valor: float,
    valor_esperado: float,
) -> None:
    desconto = DescontoPremium()

    assert desconto.calcular(valor) == valor_esperado


def test_tipo_desconhecido_gera_erro(criar_pedido: CriarPedido) -> None:
    input_dto = CriarPedidoInputDTO("Cliente", 100, "desconhecido")

    with pytest.raises(ValueError, match="Tipo de desconto inválido"):
        criar_pedido.executar(input_dto)


def test_novo_desconto_pode_ser_registrado_sem_alterar_o_caso_de_uso() -> None:
    class DescontoEstudante(IDesconto):
        def calcular(self, valor: float) -> float:
            return valor * 0.05

    factory = DescontoFactory()
    factory.registrar("estudante", DescontoEstudante)
    gateway = MemoryPedidoRepository(MemoryDatabase())
    criar_pedido = CriarPedido(gateway, factory)

    resultado = criar_pedido.executar(
        CriarPedidoInputDTO("Estudante", 100, " ESTUDANTE ")
    )

    assert resultado.valor_desconto == 5
    assert resultado.valor_final == 95
    assert resultado.tipo_desconto == " ESTUDANTE "
