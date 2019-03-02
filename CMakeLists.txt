cmake_minimum_required(VERSION 2.8)

project(projecteuler CXX)

enable_testing()

find_package(Eigen3 REQUIRED)


set(CMAKE_CXX_STANDARD 14)

set(CMAKE_CXX_FLAGS "-O2 -Wall -pedantic")

option(BUILDCPP "option for building cpp solutions" ON)

### build and test c++ files
if(${BUILDCPP})
file(GLOB files e*.cpp) # get files by extension
list(SORT files)
foreach(file ${files}) 
  get_filename_component(f ${file} NAME_WE) # File name without directory or longest extension
  add_executable(${f}.cppout ${file}) # build an exe
  ################# Include Eigen in the files that need it #########
  FILE(READ ${file} TMPTXT)
  STRING(FIND "${TMPTXT}" "Eigen" matchres)
  IF(${matchres} EQUAL -1)
    include_directories(${EIGEN3_INCLUDE_DIR})
  ENDIF()
  ###################################################################
  add_test(NAME cpp_${f} COMMAND ${PROJECT_SOURCE_DIR}/run.sh ${CMAKE_CURRENT_BINARY_DIR}/${f}.cppout
           WORKING_DIRECTORY ${PROJECT_SOURCE_DIR})
endforeach()
endif()

### build and test python files
file(GLOB files e*.py) # get files by extension
list(SORT files)
foreach(file ${files}) 
  get_filename_component(f ${file} NAME_WE) # File name without directory or longest extension
  add_test(NAME py_${f} COMMAND python ${PROJECT_SOURCE_DIR}/pyrun.py ${f}
           WORKING_DIRECTORY ${PROJECT_SOURCE_DIR})
endforeach()


### build and test c++ files
option(BUILDASSEMBLY "option for building assembler solutions" ON)
if(${BUILDASSEMBLY})
enable_language(C ASM)
file(GLOB files e*.s) # get files by extension
list(SORT files)
foreach(file ${files}) 
  get_filename_component(f ${file} NAME_WE) # File name without directory or longest extension
  add_executable(${f}.sout ${file}) # build an exe
  add_test(NAME s_${f} COMMAND ${PROJECT_SOURCE_DIR}/run.sh ${CMAKE_CURRENT_BINARY_DIR}/${f}.sout
           WORKING_DIRECTORY ${PROJECT_SOURCE_DIR})
endforeach()
endif()

# build and test fortran files
option(BUILDFORTRAN "option for building fortran solutions" ON)
if(${BUILDFORTRAN})
enable_language(Fortran)
file(GLOB files e*.f90)
list(SORT files)
foreach(file ${files}) 
  get_filename_component(f ${file} NAME_WE) # File name without directory or longest extension 
  add_executable(${f}.f90out ${file})
  add_test(NAME f90_${f} COMMAND ${PROJECT_SOURCE_DIR}/run.sh ${CMAKE_CURRENT_BINARY_DIR}/${f}.f90out
           WORKING_DIRECTORY ${PROJECT_SOURCE_DIR})
endforeach()
endif()
