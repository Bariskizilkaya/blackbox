#Executable to library
import struct

def modify_elf_type(filename, new_type):
    with open(filename, "r+b") as f:
        f.seek(0x10)  # Seek to e_type field
        f.write(struct.pack(">H", new_type))  # Write new e_type as big-endian 16-bit value
        print(f"Updated ELF type to: {hex(new_type)} (DYN)")

# Change EXEC (0x0002) to DYN (0x0003)
modify_elf_type("libfuzz.so", 0x0003)
