alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction= input("Type 'encode' to encrypt,type 'decode' to decrypt: \n").lower()
text=input("Type your message:\n").lower()
shift=int(input("Type the shift number:\n"))

#Create a function called 'encrypt' that takes 'original_text' and 'shift_amount'as 2 inputs.
def encrypt(original_text,shift_amount):
    cipher_text = ""

    for letter in original_text:
        shifed_position = alphabet.index(letter) + shift_amount
        shifed_position %= len(alphabet) 
        cipher_text += alphabet[shifed_position]

    print(f"here is the encode resalt: {cipher_text}")


#Cread function called 'decrypt()' that takes 'original_text' and 'shift_amount'as 2 inputs.
    
def decrypt(original_text,shift_amount):
    output_text = ""

    for letter in original_text:
        shifed_position = alphabet.index(letter) - shift_amount
        shifed_position %= len(alphabet) 
        output_text += alphabet[shifed_position]

    print(f"here is the encode resalt: {output_text}")

def caesar(original_text,shift_amount,encode_or_decode):
    output_text = ""

    for letter in original_text:
        shifed_position = alphabet.index(letter) - shift_amount
        shifed_position %= len(alphabet) 
        output_text += alphabet[shifed_position]

    print(f"here is the encode resalt: {output_text}")

decrypt(original_text=text,shift_amount=shift)
encrypt(original_text=text,shift_amount=shift)