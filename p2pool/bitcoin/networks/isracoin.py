import os
import platform

from twisted.internet import defer

from .. import data, helper
from p2pool.util import pack

P2P_PREFIX='cfbdbe9c'.decode('hex')
        P2P_PORT=4331
        ADDRESS_VERSION=102
        RPC_PORT=3331
        RPC_CHECK=defer.inlineCallbacks(lambda bitcoind: defer.returnValue(
            'isracoinaddress' in (yield bitcoind.rpc_help()) and
            not (yield bitcoind.rpc_getinfo())['testnet']
        ))
        SUBSIDY_FUNC=lambda height: 50*100000000 >> (height + 1)//840000
        POW_FUNC=lambda data: pack.IntType(256).unpack(__import__('ltc_scrypt').getPoWHash(data))
        BLOCK_PERIOD=150 # s
        SYMBOL='ISR'
		CONF_FILE_FUNC=lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'isracoin') if platform.system() == 'Windows'
        else os.path.expanduser('~/Library/Application Support/isracoin/') if platform.system() == 'Darwin'
        else os.path.expanduser('/home/administrator/.isracoin'), 'isracoin.conf')
        BLOCK_EXPLORER_URL_PREFIX='http://bexplorer.israelcoin.org/block/'
        ADDRESS_EXPLORER_URL_PREFIX='http://bexplorer.israelcoin.org/address/'
        TX_EXPLORER_URL_PREFIX='http://bexplorer.israelcoin.org/tx/'
        SANE_TARGET_RANGE=(2**256//1000000000 - 1, 2**256//1000 - 1)
        DUMB_SCRYPT_DIFF=2**16
        DUST_THRESHOLD=1e8