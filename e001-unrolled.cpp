#include "stdio.h"

int main() {
  int result = 0;
  int  i = 0;
  while (i < 990) {
    result += 7 * i + 60;
    i += 15;
  }
  result += 3983;
  printf("%d\n",result);
  return 0;
}

