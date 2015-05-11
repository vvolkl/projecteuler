function euler003() result(factor) 
implicit none
double precision:: input, factor
input  = 600851475143.0D+0
factor = 2.0D+0
do while (input > 1)
    !write(*,*)factor, tmp
    if (MOD(input, factor)  < 1e-18) then
        input = input / factor
        write(*,*) input, factor
    end if 
        factor = factor + 1
end do
end function euler003

program e003
implicit none
external :: euler003
integer:: res
res = euler003()
end program e003


