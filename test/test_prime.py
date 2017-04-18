import unittest
from app.prime import primes


class TddPrimes(unittest.TestCase):
    def setUp(self):
        self.primes = primes()
        
    def test_negative_numbers(self):
        self.assertRaises(ValueError, self.primes.primes, -10)

                
    def test_that_one_never_appears_in_list(self):
        for number in self.primes:
            self.assertFalse(number == 1)    
            
    def test_primes_not_int(self):
        self.assertRaises(TypeError, self.primes.primes, 10.5)
        self.assertRaises(TypeError, self.primes.primes, 'string')
                
    def test_that_return_type_is_list(self):
        self.assertIsInstance(self.primes, list) 
            
    def test_negative_numbers(self):
        for number in self.primes:
            self.assertGreater(number, 0)
            
    def test_primes_method_returns_zero_and_one(self):
        self.assertEqual([], self.primes.primes(1))
        self.assertEqual([], self.primes.primes(0))


if __name__ == '__main__':
    unittest.main()