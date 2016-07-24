#include <stdio.h>
#include <stdlib.h>


int readWriteTextFile(char* filename) {
    FILE *ptr_file;
    char buf[1000];
    ptr_file =fopen(filename,"a+");
    if (!ptr_file)
	    return 1;
    while (fgets(buf,1000, ptr_file)!=NULL)
	    printf("%s",buf);
    fputs("This line was appended to the file by a program!\n", ptr_file);
    fclose(ptr_file);
    return 0;
}

 
int main( int argc, char** argv) {
  printf("Hello World! \n");
  printf("reading contents of a text file... \n");
  readWriteTextFile("testtext.txt");
  return 0;
}

