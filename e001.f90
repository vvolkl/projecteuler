
program e001
integer::res
res = 0
do i=1,999
    if ((MOD(i,5).EQ.0) .OR. (MOD(i,3).EQ.0)) then
    res = res + i
    end if
end do
print *,res
PRINT '("",I0)', res
stop
end program e001
