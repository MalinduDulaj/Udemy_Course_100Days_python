alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction= input("Type 'encode' to encrypt,type 'decode' to decrypt: \n").lower()
text=input("Type your message:\n").lower()
shift=int(input("Type the shift number:\n"))


def caesar(original_text,shift_amount,encode_or_decode):
    output_text = ""

    for letter in original_text:

        if encode_or_decode == "decode":
            shift_amount *= -1

        shifed_position = alphabet.index(letter) - shift_amount
        shifed_position %= len(alphabet) 
        output_text += alphabet[shifed_position]

    print(f"here is the encode resalt: {output_text}")

caesar(original_text=text,shift_amount=shift,encode_or_decode=direction)
