#include <stdio.h>
#include <stdlib.h>
#include <errno.h>
#include <fcntl.h>
#include <unistd.h>
#include <string.h>
 
#define print_error \
    do { \
        fprintf(stderr, "Error at line %d, file %s (%d) [%s]\n", \
        __LINE__, __FILE__, errno, strerror(errno)); exit(1); \
    } while(0)
 
int main(int argc, char **argv)
{
        char buf[1024];
        ssize_t len;
        int fd;
    /*char *filename;
 
    if(argc < 2) {
        fprintf(stderr, "\nUsage:\t%s { sysfs file }\n", argv[0]);
        exit(1);
    }
*/ 
  //  filename = argv[1]; /* accept argument 1 as filename */

        bool found = false;
	string cwd = getcwd(buf, 1024);
	int count = 0;
	int len = strlen(cwd);
	for(int i=0; i<len; i++)
		if(strcmp(cwd[i], "/") == 0 ) count += 1;
	while(true){
		if( count > 0){
		       	chdir("..");
			count -= 1; }
		chdir("/sys/class/net/");

	}
	fd = open(filename, O_RDONLY);
        if (fd < 0) {
        fprintf(stderr, "open %s: %s\n", filename, strerror(errno));
        print_error;
        }
 
        len = read(fd, buf, sizeof(buf)-1);
        if (len < 0) {
                fprintf(stderr, "read %s: %s", filename, strerror(errno));
        print_error;
        }
 
        buf[len] = 0;
     
    printf("%s : %s\n", filename, buf);
 
#if 0
    printf("bufferlen is %d\n", strlen(buf));
#endif
         
    close(fd);
    return 0;
}

