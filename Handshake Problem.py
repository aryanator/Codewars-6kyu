
import math
def get_participants(handshakes):
    a=math.ceil((1+8*handshakes)**0.5)
    return math.ceil((1+a)/2)
