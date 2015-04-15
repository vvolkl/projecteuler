
subroutine multiplesum_bruteforce(lim, res)
implicit none
integer,intent(out):: res
integer,intent(in):: lim
integer::  i
res = 0
do i=1,lim
    if ((MOD(i,5).EQ.0) .OR. (MOD(i,3).EQ.0)) then
    res = res + i
    end if
end do
end subroutine multiplesum_bruteforce 

subroutine multiplesum_smart(lim, res)
implicit none
integer,intent(out):: res
integer,intent(in):: lim
integer::  i
res = 0
! sum all multiples of three below lim
do i=3,lim,3
    res = res + i
end do
! sum all multiples of five below lim
do i=5,lim,5
    res = res + i
end do
! we counted multiples of fifteen twice -- subtract once
do i=15,lim,15
    res = res - i
end do
end subroutine multiplesum_smart


program e001
integer::res
call multiplesum_smart(999, res)
write(*,*)res
stop
end program e001
