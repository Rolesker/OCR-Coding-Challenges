def encode(string,key):
    output=""
    for i in string:
        original_ascii=ord(i)
        final_ascii=original_ascii+key
        if (65<=original_ascii<=90 and final_ascii>90) or (97<=original_ascii<=122 and final_ascii>122):
            final_ascii-=26
        output+=chr(final_ascii)
    return output

def decode(string,key):
    output=""
    for i in string:
        original_ascii=ord(i)
        final_ascii=original_ascii-key
        if (65<=original_ascii<=90 and final_ascii<65) or (97<=original_ascii<=122 and final_ascii<97):
                final_ascii+=26
        output+=chr(final_ascii)
    return output

while True:
    print("-----------------------------------------")
    operation=input("Are you encoding or decoding? ")
    input_str=input("Enter string ")
    input_factor=int(input("Enter key "))
    if operation=="encoding":
        result=encode(input_str,input_factor)
    else:
        result=decode(input_str,input_factor)
    print(result)
    print()
    
    
