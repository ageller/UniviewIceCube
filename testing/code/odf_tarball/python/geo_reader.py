from encoder import decode_unsigned
from encoder import decode_float
import sys

FLOAT_SIZE = 8
INT_SIZE = 4
LONG_SIZE = 8

def read(file_handle):
    geo = dict()

    while True :

        data =  file_handle.read( INT_SIZE )
        
        #AMG edit for python 3
        if (data == "" or (sys.version_info > (3, 0) and data.decode("utf-8") == "")): 
            return geo

        string = decode_unsigned( data  )
        om =decode_unsigned(  file_handle.read( INT_SIZE ) )
        x = decode_float( file_handle.read( FLOAT_SIZE ) )
        y = decode_float( file_handle.read( FLOAT_SIZE ) )
        z = decode_float( file_handle.read( FLOAT_SIZE ) )

        geo[(string,om)] = (x,y,z)
