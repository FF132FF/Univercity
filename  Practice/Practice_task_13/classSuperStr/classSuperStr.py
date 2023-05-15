class SuperStr(str):

    def is_repeatance(self, s0):
        if ((type(s0) != str) or not s0 or (len(self) % len(s0) != 0)):
            return False
        elif (len(self) % len(s0) == 0):
            return True

    def is_palindrom(self):
        if (self == ''.join(reversed(self))):
            return True
        else:
            return False

print("  Tests:")
s = SuperStr("123123123123")
print(s.is_repeatance("123")) # True
print("  =============")
print(s.is_repeatance("123123")) # True
print("  =============")
print(s.is_repeatance("123123123123")) # True
print("  =============")
print(s.is_repeatance("12312")) # False
print("  =============")
print(s.is_repeatance(123)) # False
print("  =============")
print(s.is_palindrom()) # False
print("  =============")
print(s) # 123123123123 (строка)
print("  =============")
print(int(s)) # 123123123123 (целое число)
print("  =============")
print(s + "qwe") # 123123123123qwe
print("  =============")
p = SuperStr("123_321")
print(p.is_palindrom()) # True