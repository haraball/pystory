import unittest


from .pystory import (
    is_int,
    parse_pystory,
)


class TestPystory(unittest.TestCase):

    def test_is_int(self):
        assert is_int(3)
        assert is_int('carrot') == False

    def test_parse_pystory(self):
        pass
