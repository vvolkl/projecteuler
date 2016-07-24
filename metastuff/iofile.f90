program iocheck
CHARACTER(10) :: buffer
open(15, file="testtext.txt") 
read(15,*) buffer
write(*,*) buffer

end program iocheck
