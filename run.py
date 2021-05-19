from huffman import HuffmanCoding
import sys


path = input("please enter the file's directory: \n")

h = HuffmanCoding(path)


while 1:
    comp_decomp = input(
        "please enter 1 for compressing \n2 for decompressing\n3 to exit the program: \n")
    if comp_decomp == '1':
        output_path = h.compress()
        print("Compressed file path: " + output_path)
    elif comp_decomp == '2':
        decom_path = h.decompress(output_path)
        print("Decompressed file path: " + decom_path)
    elif comp_decomp == '3':
        sys.exit()
    else:
        print("please enter the correct input")
