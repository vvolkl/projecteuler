#!/bin/bash
outfilename=$1
export myanswer=`$outfilename`
number=`echo ${1%.*} | egrep -o [1-9]+`
./projecteuler_check_answer.sh $number $myanswer
