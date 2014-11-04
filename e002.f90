
recursive function fibsum(i,j, res) result(k)
integer, intent(in) :: i,j,res
integer :: k, res2
! fibonacci sequence
k = i + j
! sum even terms of fibonacci series
if (MOD(k,2) == 0) then
    res2 = res + k
else 
    res2 = res
end if
! where are you now
write(*,*) k, res2
! recursive part: stop when the fibonacci term value exceeds 4 million
if (k <= 4000000) then
    ! call fibsum again with the larger two of the three values i,j,k
    if (i < j) then
        k = fibsum(k,j,res2)
    else
        k = fibsum(i,k,res2)
    end if
else ! we are done, write result 
    write(*,*) res2
end if
end function



program e002
implicit none
integer :: fibsum
write(*,*) fibsum(1,2,2)
end program
