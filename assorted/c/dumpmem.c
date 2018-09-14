#include <stdio.h>
#include <sys/mman.h>
#include <stdlib.h>
#include <fcntl.h>
#include <unistd.h>

int debug = 0;

#define dprintf(...) do { if (debug)  fprintf(stderr, __VA_ARGS__);  } while (0)

void write_data(void *addr, off_t offset, int width)
{
    int i;
    unsigned char b = 0;
    printf("Enter data to write (hex, byte by byte, lowest to highest, width: %d)\n", width);
    for (i = 0; i < width; i++) {
        printf("0x%8x: ", offset + i);
        b = 0;
        scanf("%x", &b);
        *(unsigned char *)(addr + i) = b;
    }
}

void read_data(void *addr, off_t offset, int length, int width, int print_offset)
{
    int i;
    for (i = 0; i < length; i = i + width) {
        if (i % 16 == 0) {
            if (print_offset)
                printf("\n0x%016x: ", offset+i);
            else
                printf("\n");
        }
        
        switch (width) {

            case 1:
                printf("0x%02x ", *(unsigned char *)(addr + i)); 
            break;

            case 2:
                printf("0x%04x ", *(unsigned short *)(addr + i)); 
            break;

            case 4:
                printf("0x%08x ", *(unsigned int *)(addr + i)); 
            break;

            case 8:
                printf("0x%016x ", *(unsigned long *)(addr + i)); 
            break;
        }
    }
    printf("\n");
}

int main(int argc, char **argv)
{
    char *file = "/dev/mem";
    int width  = 1;
    off_t old_length = 0;
    off_t old_offset = 0;
  
    int l_flag = 0;
    int o_flag = 0;
    int w_flag = 0;
    int f_flag = 0;
    int c = 0, err = 0;
    extern char *optarg;
    extern int  optind;
    int print_offset = 0;

    static char usage[] = "usage: %s options \n"
                          "        -l length [not used if -w is specified] \n" 
                          "        -o offset [hex] \n" 
                          "        -f file   [optional, defaults to /dev/mem] \n"
                          "        -b width  [optional, values = 1,2,4,8. Defaults to 1] \n"
                          "        -w        [optional, write, Default to read] \n"
                          "        -p        [optional, print offset] \n"
                          "        -d        [debug info] \n";

    while ((c = getopt(argc, argv, "f:l:o:b:dpw")) != -1) {

        switch(c) {

            case 'f':
                file=optarg;
            break;

            case 'l':
                sscanf(optarg, "%d", &old_length);
                l_flag = 1;
            break;

            case 'o':
                sscanf(optarg, "%x", &old_offset);
                o_flag = 1;
            break;

            case 'b':
                sscanf(optarg, "%d", &width);
                if (width != 1 && width != 2 && width != 4 && width != 8)
                    width = 1;
            break;

            case 'w':
                w_flag = 1;
            break;

            case 'p':
                print_offset = 1;
            break;

            case 'd':
                debug = 1;
            break;

            case '?':
                err = 1;
            break;
        }
    }
    
    if (!o_flag) {
        printf(" -o option is missing\n");
        fprintf(stderr, usage, argv[0]);
        exit(EXIT_FAILURE);
    }

    if (!w_flag && !l_flag) {
        printf(" -l/-w option is missing\n");
        fprintf(stderr, usage, argv[0]);
        exit(EXIT_FAILURE);
    }
    
    if (err) {
        printf("Unknown option specified\n");
        fprintf(stderr, usage, argv[0]);
        exit(EXIT_FAILURE);
    }

    if (w_flag) {
        old_length = width;
    }

    if (old_length < width) {
        width = 1;
        dprintf("length specified is less than width, width is now set to : %d\n", width);
    }


    long page_size = sysconf(_SC_PAGE_SIZE);
    off_t offset = (old_offset + (page_size-1)) & ~(page_size-1) - page_size;
    int diff   =  old_offset - offset;
    int length =  old_length + diff;

    if (old_offset % width != 0) {
        dprintf("\nOffset is not a multiple of width, defaulting to width of 1\n\n");
        width = 1;
    }
    int fd = open(file, O_RDONLY); 
    if (fd < 0) {
        printf("Unable to open file : %s \n", file);
        perror("");
        exit(EXIT_FAILURE);
    }

    dprintf("Mapping done from file: %s, offset = 0x%x, length = %ld, width = %d\n", file, offset, length, width);

    void *addr;
    addr = mmap(0, length, PROT_READ, MAP_PRIVATE, fd, offset);
    if (addr == MAP_FAILED) {
        printf("Unable to map the file: %s\n", file);
        perror("");
        exit(EXIT_FAILURE);
    }

    dprintf("Mapped address: %p \n", addr);
  
    addr += diff; /*rebase the addr, to match the offset */

    int i;
    if (w_flag) {
        write_data(addr, old_offset, width);
    }
    else {
        read_data(addr, old_offset, old_length, width, print_offset);
    }
}

