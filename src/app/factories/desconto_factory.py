from src.app.entities.desconto import (
    DescontoNormal,
    DescontoPremium,
    DescontoVIP,
    IDesconto,
)


class DescontoFactory:
    def __init__(self) -> None:
        self._tipos: dict[str, type[IDesconto]] = {
            "normal": DescontoNormal,
            "vip": DescontoVIP,
            "premium": DescontoPremium,
        }

    def registrar(self, tipo: str, desconto: type[IDesconto]) -> None:
        tipo_normalizado = tipo.strip().lower()
        if not tipo_normalizado:
            raise ValueError("O tipo de desconto não pode ser vazio")
        self._tipos[tipo_normalizado] = desconto

    def criar(self, tipo: str) -> IDesconto:
        tipo_normalizado = tipo.strip().lower()
        try:
            classe_desconto = self._tipos[tipo_normalizado]
        except KeyError:
            raise ValueError("Tipo de desconto inválido") from None
        return classe_desconto()
