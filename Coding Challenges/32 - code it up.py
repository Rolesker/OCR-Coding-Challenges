#pretty much the same thing as challenge 13 but sure
#this kind of breaks since this encodes to values larger than ascii allows
#wasnt too sure if i should add wrapping around to fix this because then it would have been literally the same as challenge 13
def encode(string,factor):
    output=""
    for i in string:
        output+=chr(ord(i)+factor)
    return output

def decode(string,factor):
    output=""
    for i in string:
        output+=chr(ord(i)-factor)
    return output

print(encode("aaaaaa",25))
print(decode("zzzzzz",25))
