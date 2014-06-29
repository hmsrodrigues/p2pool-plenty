from p2pool.bitcoin import networks

PARENT=networks.nets['cryptoescudo']
SHARE_PERIOD=12 # seconds   
CHAIN_LENGTH=24*60*60//12 # shares
REAL_CHAIN_LENGTH=24*60*60//12 # shares
TARGET_LOOKBEHIND=20 # shares
SPREAD=15 # blocks    
IDENTIFIER='1f7c84911f8491c8'.decode('hex')
PREFIX='ce5c1f1f94949191'.decode('hex')
P2P_PORT=8333
MIN_TARGET=0
MAX_TARGET=2**256//2**20 - 1
PERSIST=True
WORKER_PORT=7333
BOOTSTRAP_ADDRS='p2pools.plentygadget.pt p2pools.plentygadget.com 176.111.108.151 87.103.127.26'.split(' ')
ANNOUNCE_CHANNEL='#p2pool-alt'
VERSION_CHECK=lambda v: True
