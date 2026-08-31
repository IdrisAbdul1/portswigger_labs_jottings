import hashlib
import base64

file_path = '/home/phantomMenace/portswigger_labs/Authentication/password.txt'

try:
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            password = line.strip()
            
            if password:
                hash_object = hashlib.md5(password.encode('utf-8'))
                
                hash_hex = f"carlos:{hash_object.hexdigest()}"
                text_byte = hash_hex.encode("utf-8")
                encoded_byte = base64.b64encode(text_byte)
                encoded_text = encoded_byte.decode("utf-8")
                print(encoded_text)
                
except FileNotFoundError:
    print(f"The file {file_path} was not found.")


# password = "peter"
# hash_object = hashlib.md5(password.encode('utf-8'))
# hash_hex = f"wiener:{hash_object.hexdigest()}"

# original_text  = hash_hex
# # Convert string to bytes, then encode
# text_bytes = original_text.encode("utf-8")
# encoded_bytes = base64.b64encode(text_bytes)
# # Convert bytes back to a readable string
# encoded_text = encoded_bytes.decode("utf-8")

# print(encoded_text)