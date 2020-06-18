
program e002
integer::a
integer::b
integer::res
res = 0
a = 1
b = 1
do while ((a .LT. 4000000) .AND.(b .LT. 4000000))
  a = a + b
  if (MOD(a,2) .EQ. 0) then
    res = res + a
  end if
  b = a + b
  if (MOD(b,2) .EQ. 0) then
    res = res + b
  end if
end do
print *,res
end program e002
