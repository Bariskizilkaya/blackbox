# blackbox

# Put a breakpoint by gdb to the function and close the aslr

qemu-x86_64-static -E LD_PRELOAD=./override.so test

sudo chroot . ./qemu-mips-static -g :1234 -E LD_PRELOAD=./override.so -E LD
_DEBUG=all bin/busybox ls

![image](https://github.com/user-attachments/assets/cf64eff2-e703-4db4-af11-bf0214f14b9f)
