
# This file is part of Scapy
# Copyright (C) 2007, 2008, 2009 Arnaud Ebalard
# 2015, 2016 Maxence Tury
# This program is published under a GPLv2 license

"""
TLS ciphers.
"""


class CipherError(Exception):
    """
    Raised when .decrypt() or .auth_decrypt() fails.
    """
    pass


# We have to keep these imports below CipherError definition
# in order to avoid circular dependencies.
from scapy.layers.tls.crypto.cipher_aead import tls_aead_cipher_algs
from scapy.layers.tls.crypto.cipher_block import tls_block_cipher_algs
from scapy.layers.tls.crypto.cipher_stream import tls_stream_cipher_algs

tls_cipher_algs = {}
tls_cipher_algs.update(tls_block_cipher_algs)
tls_cipher_algs.update(tls_stream_cipher_algs)
tls_cipher_algs.update(tls_aead_cipher_algs)
