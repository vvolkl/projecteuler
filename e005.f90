program e005
implicit none

integer*8 :: i, check
logical :: done
i = 23 

write(*,*) 'smallest number that is evenly divisible by all numbers 1-20'
do while (.NOT. done) 
    i = i + 1
    done = .TRUE.
    !write(*,*) i, done
    factors: do check = 2,20
        !write(*,*) i / REAL(check)
        if (i / DBLE(check) > i / check ) then
            done = .FALSE.
            exit factors
        end if 
    end do factors
end do
write(*,*) (i / REAL(check) > i / check ), done
write(*,*) i / check, i / real(check)
write(*,*) i
end program e005

