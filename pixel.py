
def encrypt(image_path, user_key):
    try:
        fin = open(path, 'rb')                          # open file for reading purposes
        image = fin.read()                              #storing image data in variable "image"
        fin.close()

        image = bytearray(image)                       #converting image into byte array to perform encryption easily on numeric data.

    # performing XOR operations on each value of bytearray
        for index, values in enumerate(image):
            image[index] = values ^ key

        fin = open(path, 'wb')                        # opening file for writing purposes
        fin.write(image)
        fin.close()                                   # writing encrypted data in image
        print("Encryption Done...")
    except Exception:
        print('Error Caught: ', Exception.__name__)

def decrypt(encrypted_image_path, user_key):
    try:
        fin = open(path, 'rb')                          # open file for reading purposes
        image = fin.read()                              #storing image data in variable "image"
        fin.close()

        image = bytearray(image)                       #converting image into byte array to perform encryption easily on numeric data.

    # performing XOR operations on each value of bytearray
        for index, values in enumerate(image):
            image[index] = values ^ key

        fin = open(path, 'wb')                        # opening file for writing purposes
        fin.write(image)
        fin.close()                                   # writing encrypted data in image
        print("decryption Done...")
    except Exception:
        print('Error Caught: ', Exception.__name__)


end = False
while not end:
    user_input = input("Type e for encryption or d for decryption: \n")   # Takes in the user input
    path = input(r'Enter the path of image: ')  # The r means raw strings. it takes \ as literals.   # Takes the path of the image
    key = int(input('Enter the key: '))

    if user_input == 'e':
        print('The path of file: ', path)
        print('The key for encryption: ', key)
        encrypt(image_path=path, user_key=key)

    elif user_input == 'd':
        print('The path of file: ', path)
        print('The key for decryption: ', key)
        decrypt(encrypted_image_path=path, user_key=key)
    retry = input("Type 'yes' to continue, type 'no' to exit. \n").lower()
    if retry == 'no':
        end = True
        print("Have a nice day! Bye..")