import socket
import sys

MASK_ERRORS = True

HAARCASCADES_DIR = '/usr/local/metaLayer-objectdetection-face/resources'

#ERROR MESSAGES
ERROR_NOIMAGE = { 'status':'failed', 'code':101, 'error':'The required POST field \'image\' was not supplied' }
ERROR_IMAGEERROR = { 'status':'failed', 'code':102, 'error':'The image supplied could not be ready by the system' }

if socket.gethostname() == 'matt-griffiths':
    MASK_ERRORS = False
    HAARCASCADES_DIR = '/home/matt/code/metaLayer/objectdetection-face/resources'