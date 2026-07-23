from praktikum.bun import Bun

class TestBun:

    # получить название булки
    def test_bun_get_name_returns_correctly_value(self):
        bun = Bun('Флюоресцентная булка R2-D3', 988)
        assert bun.get_name() == 'Флюоресцентная булка R2-D3'

     # получить цену булки
    def test_price_get_name_returns_correctly_value(self):
        bun = Bun('Краторная булка N-200i', 1255)
        assert bun.get_price() == 1255
        