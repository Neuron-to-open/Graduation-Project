from cryptography.fernet import Fernet


def generate_key():
    """
    生成加密密钥。

    该函数无参数。

    返回:
        bytes: 生成的加密密钥，为bytes类型。
    """
    key = Fernet.generate_key()  # 生成Fernet加密密钥
    print("生成的key" , key)
    print(type(key))
    return key


# 生成加密密钥的函数已经提供，以下为对具体加密和解密过程的函数定义

def encrypt_id(key, id):
    """
    使用给定的密钥对消息进行加密。

    参数:
    key: 用于加密的密钥，必须是Fernet可以接受的格式。
    message: 需要加密的消息，字符串形式。

    返回值:
    返回加密后消息的字节编码形式。
    """
    # 初始化加密套件
    cipher_suite = Fernet(key)

    # 将消息字符串转换为字节序列以进行加密
    byte_id = id.encode()

    # 加密消息
    encrypted_id = cipher_suite.encrypt(byte_id)

    # 将加密后的消息编码为字符串后返回
    return encrypted_id.decode()


def decrypt_id(key, encrypted_id):
    """
    使用给定的密钥对加密的消息进行解密。

    参数:
    key: 用于解密的密钥，必须是Fernet可以接受的格式。
    encrypted_message: 需要解密的消息，字符串形式。

    返回值:
    返回解密后的消息字符串。
    """
    # 初始化解密套件
    cipher_suite = Fernet(key)

    # 将加密的消息字符串转换为字节序列以进行解密
    encrypted_id_bytes = encrypted_id.encode()

    # 解密消息
    decrypted_id = cipher_suite.decrypt(encrypted_id_bytes)

    # 将解密后的消息字节序列解码为字符串后返回
    return decrypted_id.decode()



generate_key()