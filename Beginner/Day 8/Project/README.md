# Caesar Cipher

### Instructions

- Caeser Cipher performs two operations

  1. Text Encryption
  2. Text Decryption

- For the 'encrypt' operation, It shifts each letter of the 'text' _forwards_ in the alphabet by the shift amount and prints the encrypted text.

```py
plain_text = "good morning"
encrypted_text = "jrrg pruqlqj"
```

- For the 'decrypt' operation, It shifts each letter of the 'text' _backwards_ in the alphabet by the shift amount and prints the decrypted text.

```py
encrypted_text = "jrrg pruqlqj"
decrypted_text = "good morning"
```

- Checks if the user wanted to encrypt or decrypt the message by checking the 'direction' variable input.

### Example Output

```js
Type 'encode' to encrypt, type 'decode' to decrypt:
> encode
Type your message:
> hello
Type the shift number:
> 19
The encoded text is: axeeh
```

```js
Type 'encode' to encrypt, type 'decode' to decrypt:
> decode
Type your message:
> axeeh
Type the shift number:
> 19
The decoded text is: hello
```

- It will ask the user if they want to restart the cipher program?
- e.g. Do you wish to continue? "yes" or "no":

### Example Output

```
 ,adPPYba,  ,adPPYYba,   ,adPPYba,  ,adPPYba,  ,adPPYYba,  8b,dPPYba,
a8"     ""  ""     `Y8  a8P_____88  I8[    ""  ""     `Y8  88P'   "Y8
8b          ,adPPPPP88  8PP"         `"Y8 ba,  ,adPPPPP88  88
"8a,   ,aa  88,    ,88  "8b,   ,aa  aa    ]8I  88,    ,88  88
 `"Ybbd8"'  `"8bbdP"Y8   `"Ybbd8"'  `"YbbdP"'  `"8bbdP"Y8  88

             88               88
             ""               88
                              88
 ,adPPYba,   88  8b,dPPYba,   88,dPPYba,    ,adPPYba,  8b,dPPYba,
a8"     ""   88  88P'    "8a  88P'    "8a  a8P_____88  88P'   "Y8
8b           88  88       d8  88       88  8PP"        88
"8a,   ,aa   88  88b,   ,a8"  88       88  "8b,   ,aa  88
 `"Ybbd28"'  88  88`YbbdP"'   88       88   `"Ybbd8"'  88
                 88
                 88
```

```js
Type 'encode' to encrypt, type 'decode' to decrypt:
> encode
Type your message:
> hello world
Type the shift number:
> 8
The encoded message is: pmttw ewztl

Do you wish to continue? "yes" or "no":> yes
Type 'encode' to encrypt, type 'decode' to decrypt:
> decode
Type your message:
> pmttw ewztl
Type the shift number:
> 8
The decoded message is: hello world

Do you wish to continue? "yes" or "no":> no
Goodbye
```

OBS.: `>` represents input
