
function isPalindrome(pal) result(isP)
integer, intent(in):: pal 
integer :: i, len
len = floor(log10(real(pal)))

do i=1,len
write(*,*) i, len-i
end do
isP = i
end function isPalindrome

program e003
implicit none
integer :: res, isPalindrome
res  = isPalindrome(9009)
write(*,*) res 
end program e003
