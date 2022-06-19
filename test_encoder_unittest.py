from encoder import encode, decode

import unittest
from hypothesis import given
from hypothesis.strategies import text

class TestEncoding(unittest.TestCase):

    @given(text())
    def test_decode_inverts_encode(self, s):
        self.assertEqual(decode(encode(s)), s)

if __name__ == "__main__":
    unittest.main()
