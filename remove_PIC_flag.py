import struct

def modify_elf_flags(filename, new_flags):
    with open(filename, "r+b") as f:
        f.seek(0x24)  # Seek to e_flags
        f.write(struct.pack(">I", new_flags))  # Write new e_flags as big-endian integer
        print(f"Updated e_flags to: 0x{new_flags:X}")

def zero_out_section(filename, section_name):
    with open(filename, "r+b") as f:
        f.seek(0)  # Reset file position
        data = f.read()

        # Find section (naive search, better with pyelftools)
        index = data.find(section_name.encode())
        if index != -1:
            print(f"Zeroing out {section_name} section...")
            f.seek(index)
            f.write(b'\x00' * len(section_name))  # Overwrite name
        else:
            print(f"Section {section_name} not found.")

# Remove PIC (0x8) and CPIC (0x1000) again
new_flags = 0x00
#new_flags = original_flags & ~(0x8 | 0x1000)

# Apply changes
modify_elf_flags("login", new_flags)
zero_out_section("login", ".dynamic")
zero_out_section("login", ".got")
