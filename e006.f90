program e006
implicit none

integer*8 :: i,squaresum, sumsquares
squaresum = 0
sumsquares = 0
do  i=1,100 
    sumsquares = sumsquares + i * i
    squaresum = squaresum + i
end do
squaresum  = squaresum * squaresum
write(*,*) squaresum - sumsquares
end program e006
