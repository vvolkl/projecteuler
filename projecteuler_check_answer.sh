#!/bin/bash

echo 'Project Euler Problem  ' $1

RED='\033[0;31m'
GREEN='\033[0;32m'
NOCOLOR='\033[0m'
STRING_CORRECT=${GREEN}'CORRECT'${NOCOLOR}
STRING_FALSE=${RED}'FALSE'${NOCOLOR}

euler_solution=`grep Answer: ./project_euler.txt 2>/dev/null | sed ''$1'q;d'`
euler_solution=${euler_solution/"Answer: "/}
echo '    ' $euler_solution

my_solution=`echo -n $2 | md5sum`
my_solution=${my_solution/ -/}
echo '    ' $my_solution

printf 'The answer '
printf $2 
printf ' is '
if [ $my_solution == $euler_solution ]
then
printf $STRING_CORRECT
else
printf $STRING_FALSE
printf  '\n'
exit 1
fi
printf '\n'
