chars = ['ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz']

def caesar (offset, sentence):    
    for i in range(len(sentence)):
        char = sentence[i]
        
        if (char.upper()):
            return ''.join(chr((ord(char) - 97 + offset) % 26 + 97) for char in sentence)
        



if __name__ == '__main__':
    print(caesar(3, "abc")) # def
    print(caesar(2, "alta")) # cnvc
    print(caesar(10, "alterraacademy")) # kvdobbkkmknowi
    print(caesar(1, "abcdefghijklmnopqrstuvwxyz")) # bcdefghijklmnopqrstuvwxyza
    print(caesar(1000, "abcdefghijklmnopqrstuvwxyz")) # mnopqrstuvwxyzabcdefghijkl