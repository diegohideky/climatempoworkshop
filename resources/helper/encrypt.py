# encoding=utf8
import sys

reload(sys)
sys.setdefaultencoding('utf8')

from Crypto.Cipher import AES
import base64

# the block size for the cipher object; must be 16, 24, or 32 for AES
BLOCK_SIZE = 32

# the character used for padding--with a block cipher such as AES, the value
# you encrypt must be a multiple of BLOCK_SIZE in length.  This character is
# used to ensure that your value is always a multiple of BLOCK_SIZE
PADDING = '{'

# one-liner to sufficiently pad the text to be encrypted
pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * PADDING

# one-liners to encrypt/encode and decrypt/decode a string
# encrypt with AES, encode with base64
EncodeAES = lambda c, s: base64.b64encode(c.encrypt(pad(s)))
DecodeAES = lambda c, e: c.decrypt(base64.b64decode(e)).rstrip(PADDING)

# generate a random secret key
# secret = os.urandom(BLOCK_SIZE)
secret = 'serginhoserginho'

# create a cipher object using the random secret
cipher = AES.new(secret)


def encode(senha):
    return EncodeAES(cipher, senha)


def decode(senha):
    return DecodeAES(cipher, senha)