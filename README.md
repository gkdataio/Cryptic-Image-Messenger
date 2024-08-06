# Cryptic Image Messenger

Cryptic Image Messenger is a Python script that encrypts a message by permuting its characters based on a seed and then encodes the encrypted message into an image. It also allows for the decryption of the message from the image using the same seed.

## Features

- **Encryption**: Permutes the characters of a message and encodes it into an image.
- **Decryption**: Extracts the permuted message from the image and reverts it to the original message using the seed.
- **Seed-Based Security**: Uses a seed for generating the permutation, ensuring that only those with the seed can decrypt the message.

## Requirements

- Python 3.x
- Pillow (PIL) library

You can install the required library using pip:
```bash
pip install pillow
