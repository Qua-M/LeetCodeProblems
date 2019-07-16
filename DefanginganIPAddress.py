class Solution:
    def defangIPaddr(self, address):
        address = address.replace('.', '[.]')
        return address
