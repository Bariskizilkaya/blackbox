//gcc override.c -o override.so -shared -fPIC -ldl

#define _GNU_SOURCE
#include <stdio.h>
#include <dlfcn.h>

// Declare the original __libc_start_main function signature
typedef int (*libc_start_main_t)(int (*main)(int, char**, char**), int, char**,
                                 void (*init)(void), void (*fini)(void),
                                 void (*rtld_fini)(void), void*);

// Override __libc_start_main
int __libc_start_main(int (*main)(int, char**, char**), int argc, char** argv,
                      void (*init)(void), void (*fini)(void),
                      void (*rtld_fini)(void), void* stack_end) {
    printf("Custom __libc_start_main called!\n");

    // Correctly call func1
void (*func1)() = (void (*)())0x4000001151;
    if (func1) {
        printf("Calling func1 from the binary...\n");
        func1();  // Call func1
    } else {
        printf("func1 not found!\n");
    }

    // Call the original __libc_start_main to proceed with normal execution
    libc_start_main_t original_start_main = (libc_start_main_t)dlsym(RTLD_NEXT, "__libc_start_main");
    return original_start_main(main, argc, argv, init, fini, rtld_fini, stack_end);
}
