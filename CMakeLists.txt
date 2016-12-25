cmake_minimum_required(VERSION 2.8)

project(projecteuler CXX Fortran)

enable_testing()

#set(CMAKE_MODULE_PATH ${CMAKE_CURRENT_SOURCE_DIR}/cmake)
#find_package(GMP REQUIRED)
find_package(Eigen3 REQUIRED)

set(CMAKE_CXX_FLAGS "-std=c++14 -O2 -Wall -pedantic")
file(GLOB files e*.cpp)
list(SORT files)
foreach(file ${files}) 
  get_filename_component(f ${file} NAME_WE)
  add_executable(${f}.cppout ${file})
  ################# Include Eigen in the files that need it #########
  FILE(READ ${file} TMPTXT)
  STRING(FIND "${TMPTXT}" "Eigen" matchres)
  IF(${matchres} EQUAL -1)
    include_directories(${EIGEN3_INCLUDE_DIR})
  ENDIF()
  ###################################################################
  add_test(NAME cpp_${f} COMMAND ${PROJECT_SOURCE_DIR}/run.sh build/${f}.cppout
           WORKING_DIRECTORY ${PROJECT_SOURCE_DIR})
endforeach()

file(GLOB files e*.py)
list(SORT files)
foreach(file ${files}) 
  get_filename_component(f ${file} NAME_WE)
  add_test(NAME py_${f} COMMAND python ${PROJECT_SOURCE_DIR}/pyrun.py ${f}
           WORKING_DIRECTORY ${PROJECT_SOURCE_DIR})
endforeach()


file(GLOB files e*.f90)
list(SORT files)
foreach(file ${files}) 
  get_filename_component(f ${file} NAME_WE)
  add_executable(${f}.f90out ${file})
  add_test(NAME f90_${f} COMMAND ${PROJECT_SOURCE_DIR}/run.sh build/${f}.f90out
           WORKING_DIRECTORY ${PROJECT_SOURCE_DIR})
endforeach()
