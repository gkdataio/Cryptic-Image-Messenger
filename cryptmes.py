import random
from PIL import Image

def create_permutation(length, seed):
    indices = list(range(length))
    random.seed(seed)
    random.shuffle(indices)
    return indices

def invert_permutation(permutation):
    inverse = [0] * len(permutation)
    for i, p in enumerate(permutation):
        inverse[p] = i
    return inverse

def apply_permutation(message, permutation):
    permuted_message = [''] * len(message)
    for i, char in enumerate(message):
        permuted_message[permutation[i]] = char
    return ''.join(permuted_message)

def message_to_image(message, image_path):
    pixels = [ord(char) for char in message]
    size = int((len(pixels) ** 0.5) + 1)
    image = Image.new('L', (size, size), 0)
    image.putdata(pixels + [0] * ((size * size) - len(pixels)))
    image.save(image_path)
    return image_path

def image_to_message(image_path):
    image = Image.open(image_path)
    pixels = list(image.getdata())
    message = ''.join(chr(pixel) for pixel in pixels if pixel != 0)
    return message

def main():
    action = input("Do you want to encrypt a new message or decrypt an existing image? (encrypt/decrypt): ")
    if action == 'encrypt':
        message = input("Enter your message: ")
        seed = random.randint(0, 2**32 - 1)
        permutation = create_permutation(len(message), seed)
        encrypted_message = apply_permutation(message, permutation)
        image_path = message_to_image(encrypted_message, 'encrypted_message.png')
        print(f"Seed: {seed}, Encrypted Message: {encrypted_message}, Image: {image_path}")

    elif action == 'decrypt':
        image_path = input("Enter the path to the encrypted image: ")
        seed = int(input("Enter the seed used for encryption: "))
        retrieved_message = image_to_message(image_path)
        permutation = create_permutation(len(retrieved_message), seed)
        inverse_permutation = invert_permutation(permutation)
        decrypted_message = apply_permutation(retrieved_message, inverse_permutation)
        print("Decrypted Message:", decrypted_message)

if __name__ == "__main__":
    main()
