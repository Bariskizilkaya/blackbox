# blackbox

# Put a breakpoint by gdb to the function and close the aslr

qemu-x86_64-static -E LD_PRELOAD=./override.so test

sudo chroot . ./qemu-mips-static -g 1234 -E LD_PRELOAD=./override.so -E LD
_DEBUG=all bin/busybox ls

![image](https://github.com/user-attachments/assets/cf64eff2-e703-4db4-af11-bf0214f14b9f)


Use here to symbolize your __uClibc_main fucntion

https://naliferopoulos.github.io/ThinkingInBinary/symbolicating-stripped-elf-files-manually.html

after is normal. Follow here

https://github.com/otsmr/blackbox-fuzzing

somehow libc.so.6 is not supported but native C code works as overriding application.

![image](https://github.com/user-attachments/assets/e70a83ed-fa46-40ff-8171-be5655042e91)

This is how it hits to the __uClibc_main function.

![image](https://github.com/user-attachments/assets/1addf38c-52ed-4096-a0b4-ad4fb584207d)


sudo chroot . ./qemu-mips-static -g 1234 -E LD_PRELOAD=./override.o ./bin/busybox-with-symbols

gdb-multiarch ./bin/busybox-with-symbols
