import struct

ELF_MAGIC_OFFSET   = 0
ELF_MAGIC_BYTES    = [0x7f, ord('E'), ord('L'), ord('F')]
ELF_CLASS_OFFSET   = 4
ELF_CLASS_BYTES    = [2]
ELF_EI_DATA_OFFSET = 5
ELF_EI_DATA_BYTES  = [1]
ELF_ENTRY_OFFSET   = 24
ELF_ENTRY_BYTES    = [0x70, 0x1b, 0x40, 0, 0, 0, 0, 0]  # call _start
# ELF_ENTRY_BYTES    = [0x90, 0x16, 0x40, 0, 0, 0, 0, 0]  # call main
# ELF_ENTRY_BYTES    = [0xa0, 0x1c, 0x40, 0, 0, 0, 0, 0]  # call call_me
