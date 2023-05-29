class SuperStr(str):

    def isRepeatance(self, s0):
        if ((type(s0) != str) or not s0 or (len(self) % len(s0) != 0)):
            return False
        elif (len(self) % len(s0) == 0):
            return True

    def isPalindrom(self):
        if (self == ''.join(reversed(self))):
            return True
        else:
            return False

print("  Tests:")
s = SuperStr("123123123123")
print(s.isRepeatance("123")) # True
print("  =============")
print(s.isRepeatance("123123")) # True
print("  =============")
print(s.isRepeatance("123123123123")) # True
print("  =============")
print(s.isRepeatance("12312")) # False
print("  =============")
print(s.isRepeatance(123)) # False
print("  =============")
print(s.isPalindrom()) # False
print("  =============")
print(s) # 123123123123 (строка)
print("  =============")
print(int(s)) # 123123123123 (целое число)
print("  =============")
print(s + "qwe") # 123123123123qwe
print("  =============")
p = SuperStr("123_321")
print(p.isPalindrom()) # True