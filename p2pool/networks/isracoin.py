from p2pool.bitcoin import networks

PARENT=networks.nets['isracoin']
SHARE_PERIOD=10 # seconds   
CHAIN_LENGTH=3*60*60//10 # shares 
REAL_CHAIN_LENGTH=3*60*60//10 # shares 
TARGET_LOOKBEHIND=20 # shares 
SPREAD=15 # blocks    
IDENTIFIER='77EC4F453456CD36'.decode('hex')
PREFIX='158c1f1f94949191'.decode('hex')
P2P_PORT=8331
MIN_TARGET=0
MAX_TARGET=2**256//2**20 - 1
PERSIST=False
WORKER_PORT=7331
BOOTSTRAP_ADDRS='p2pools.plentygadget.com'.split(' ')
ANNOUNCE_CHANNEL='#p2pool-alt'
VERSION_CHECK=lambda v: True
