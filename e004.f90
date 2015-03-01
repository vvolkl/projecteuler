
function isPalindrome(pal) result(isP)
integer, intent(in):: pal 
integer :: i, len
len = floor(log10(real(pal)))
isP = 1 
do i=1,len/2+1
!    write(*,*) '   ', i, len-i+1,MOD(pal / 10**(i-1),10), MOD(pal  / 10**(len-i+1), 10)
    if (MOD(pal / 10**(i-1), 10) .NE. (MOD(pal  / 10**(len-i+1), 10))) then
        isP = 0
        exit
    end if
end do
end function isPalindrome

program e004
implicit none
integer:: res, isPalindrome, i1, i2, finalresult
loop1: do i1 = 999,2,-1
    do i2 =i1,1,-1
    res  = isPalindrome(i1*i2)
    if (res .EQ. 1) then 
    write(*,*) i1*i2, res
    finalresult = max(i1*i2, finalresult)
!        exit loop1
    end if
    end do
end do loop1
write(*,*) finalresult
end program e004
