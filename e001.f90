
program euler001
implicit none
integer:: res, i
res = 0
do i=1,999
    if ((MOD(i,5).EQ.0) .OR. (MOD(i,3).EQ.0)) then
    res = res + i
    end if
end do
write(*,*)res
stop
end program euler001
