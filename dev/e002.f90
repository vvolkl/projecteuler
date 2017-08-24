
recursive function fibsum(a,b,res,lim) result(k)
! one step of the fibonacci series: add i and j to yield k
! if the new term is even, it is added to 'result'
! if k does not exceed lim, the function proceeds to call itself with the new
! arguments
integer, intent(in) :: a,b,res,lim
integer :: k
! fibonacci sequence
k = a + b
! sum even terms of fibonacci series
if (MOD(k,2) == 0) then
    res = res + a
end if
! recursive part: stop when the fibonacci term value exceeds 4 million
if (k <= lim) then
    ! call fibsum again with the larger two of the three values i,j,k
    if (a < b) then
        k = fibsum(k,b,res2,lim)
    else
        k = fibsum(a,k,res2,lim)
    end if
end if
end function



program e002
implicit none
integer :: fibsum
write(*,"(I10)") fibsum(1,2,2,4000000)
end program
