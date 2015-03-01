
!program euler001
!call sumDivisibles
!end program euler001
!
!
!

subroutine sumDivisibles(N, res)
implicit none
integer, intent(out):: res
integer:: i 
integer, intent(in):: N
res = 0
do i=1,N
    if ((MOD(i,5).EQ.0) .OR. (MOD(i,3).EQ.0)) then
    res = res + i
    end if
end do
write(*,*)res
end subroutine sumDivisibles
