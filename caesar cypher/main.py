alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd',
    'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
    't', 'u', 'v', 'w', 'x', 'y', 'z'
]

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
def decrypt(encoded_text, shift_amount):
  decoded_text = ""
  for char in encoded_text:
      position = alphabet.index(char)
      new_position = position - shift_amount
      if new_position < 0:
          new_position = len(alphabet) - 1 + new_position
      decoded_text += alphabet[new_position]
  print(f"The decoded text is: {decoded_text}")
def encrypt(plain_text,shift_amount):
  message=""
  end_of_list=len(alphabet)-1
  for char in plain_text:
    ind=alphabet.index(char)
    if ind==end_of_list:
      ind=0
      shift_amount-=1
    new_position=ind+shift_amount
    if new_position>len(alphabet):
      new_position-=len(alphabet)
    new_char=alphabet[new_position]
    message+=new_char
  print(message)
if direction == "encode":
    encrypt(plain_text=text, shift_amount=shift)
else:
    decrypt(encoded_text=text, shift_amount=shift)
