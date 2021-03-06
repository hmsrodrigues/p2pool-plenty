import os
import platform

from twisted.internet import defer

from .. import data, helper
from p2pool.util import pack


P2P_PREFIX='fbc0b6db'.decode('hex')
P2P_PORT=4333
ADDRESS_VERSION=28
RPC_PORT=3333
RPC_CHECK=defer.inlineCallbacks(lambda bitcoind: defer.returnValue(
           'cryptoescudoaddress' in (yield bitcoind.rpc_help()) and       
            not (yield bitcoind.rpc_getinfo())['testnet']   
        ))
SUBSIDY_FUNC=lambda height: 600*10000000
POW_FUNC=lambda data: pack.IntType(256).unpack(__import__('ltc_scrypt').getPoWHash(data))
BLOCK_PERIOD=120 # s
SYMBOL='CESC'
CONF_FILE_FUNC=lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'cryptoescudo') if platform.system() == 'Windows'
                else os.path.expanduser('~/Library/Application Support/cryptoescudo/') if platform.system() == 'Darwin'
                else os.path.expanduser('/home/administrator/.cryptoescudo'), 'cryptoescudo.conf')
BLOCK_EXPLORER_URL_PREFIX='http://cryptexplorer.com/block/'
ADDRESS_EXPLORER_URL_PREFIX='http://cryptexplorer.com/address/'
TX_EXPLORER_URL_PREFIX='http://cryptexplorer.com/tx/'
SANE_TARGET_RANGE=(2**256//1000000000 - 1, 2**256//1000 - 1)
DUMB_SCRYPT_DIFF=2**16
DUST_THRESHOLD=1e8
