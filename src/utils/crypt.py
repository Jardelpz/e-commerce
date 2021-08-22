import base64


def encrypt(message):
    message_bytes = message.encode()
    encode_64 = base64.b64encode(message_bytes)
    return encode_64.decode('ascii')


def decrypt(message):
    base64_bytes = message.encode('ascii')
    message_bytes = base64.b64decode(base64_bytes)
    return message_bytes.decode('ascii')

