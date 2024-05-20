from typing import List, Optional
from models.cliente import Cliente
from models.produto import Produto
from pydantic import BaseModel


class PedidoBase(BaseModel):
    codigo: str
    id_cliente: int
    produtos: List[int]


class Pedido(PedidoBase):
    id: Optional[int] = None

    class Config:
        from_attributes = True


class PedidoCompleto(Pedido):
    cliente: Cliente
    status: str
    produtos: List[Produto]