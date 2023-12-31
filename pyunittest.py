import unittest
import string

def encrypt(message,shift):
    abc = string.ascii_letters + string.punctuation + string.digits + " "
    encrypted_message = "".join([abc[abc.find(char) + shift] if len(abc) > (abc.find(char) + 1) else abc[0] for index,char in enumerate(message)])
    print(encrypted_message)
    return encrypted_message


class TestEncryption(unittest.TestCase):
    
    def setUp(self):
        self.my_message = "I am Vincent!! 55"
        self.shift = 2
        
    def test_inputType(self):
        self.assertIsInstance(self.my_message,str)
    
    def test_inputExists(self):
        self.assertIsNotNone(self.my_message)
    
        
    def test_functionReturnsSomething(self):
        self.assertIsNotNone(encrypt(self.my_message,self.shift))
        
    def test_lengthIO(self):
        self.assertEqual(len(self.my_message), len(encrypt(self.my_message,self.shift)))
        
    def test_differentIO(self):
        self.assertNotIn(self.my_message,encrypt(self.my_message,self.shift))
        
    def test_outputType(self):
        self.assertIsInstance(encrypt(self.my_message,self.shift),str)
        
    def test_shiftedCipher(self):
        abc = string.ascii_letters + string.punctuation + string.digits + " "
        encrypted_message = "".join([abc[abc.find(char) + self.shift] if len(abc) > (abc.find(char) + 1) else abc[0] for index,char in enumerate(self.my_message)])
        print(encrypted_message)
        self.assertEqual(encrypted_message,encrypt(self.my_message,self.shift))
        
    
    
    
if __name__ == "__main__":
    unittest.main()