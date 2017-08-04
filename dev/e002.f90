
recursive function fibsum(i,j,res,lim) result(k)
! one step of the fibonacci series: add i and j to yield k
! if the new term is even, it is added to 'result'
! if k does not exceed lim, the function proceeds to call itself with the new
! arguments
integer, intent(in) :: i,j,res,lim
integer :: k, res2, cache1
! fibonacci sequence
k = i + j
! sum even terms of fibonacci series
if (MOD(k,2) == 0) then
    res2 = res + k
else 
    res2 = res
end if
! where are you now
!write(*,*) k, res2
! recursive part: stop when the fibonacci term value exceeds 4 million
if (k <= lim) then
    ! call fibsum again with the larger two of the three values i,j,k
    if (i < j) then
        k = fibsum(k,j,res2,lim)
    else
        k = fibsum(i,k,res2,lim)
    end if
!else ! we are done, write result 
!  k = res2 - k
    !write(*,*) res2
end if
end function



program e002
implicit none
integer :: fibsum
write(*,"(I10)") fibsum(1,2,2,4000000)
end program
