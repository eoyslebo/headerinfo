#/usr/bin/python
from sys import argv
from struct import *

structure_gif = [
("3s", "GIF"),
("3s", "87a or 89a"),
("H", "<Logical Screen Width>"),
("H", "<Logical Screen Height>"),
("B", "Global Color Table Flag (GCTF)"),
("B", "<Background Color Index>"),
("B", "<Pixel Aspect Ratio>"),
("3B", "<Global Color Table(0..255 x 3 bytes) if GCTF is one>"),
]

structure_mbr_partition = [
("1B", "status (0x80 = bootable (active), 0x00 = non-bootable, other = invalid )"),
("1B", "CHS Head"),
("1B", "sector in bits 5-0. 7-6 are high bits of cylinder"),
("1B", "bits 7-0 of cylinder"),
("1B", "Partition type"),
("1B", "CHS head"),
("1B", "sector in bits 5-0. bits 7-6 are high bits of cylinde"),
("1B", "bits 7-0 of cylinder"),
("4B", "LBA of first absolute sector in the partition"),
("4B", "Number of sectors in partition"),
]

structure_mbr = [
("440x", "code area"),
("4B", "disk sinature (optional)"),
("2B", "Usually nulls"),
] + structure_mbr_partition + structure_mbr_partition + structure_mbr_partition + structure_mbr_partition + [
#("64x", "Table of primary partitions"),
("2B", "MBR signature"),
]

structure = structure_mbr
#structure = structure_gif



with open(argv[1], mode='rb') as file:
    offset = 0
    for pattern, description in structure:
        chunksize = calcsize (pattern)
        chunk = file.read(chunksize)
        tuple = unpack_from (pattern, chunk)

        print str(hex(offset)) + "\t" + description
        for i in tuple:
            if type(i) == int:
                print "  " + str(i) + "\t" + str(hex(i)) + "\t" + str(bin(i))
            else:
                print "  " + i
        offset += chunksize
        print
