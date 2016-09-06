cmake_minimum_required(VERSION 2.8)

project(projecteuler CXX Fortran)

enable_testing()

#execute_process(COMMAND ../e001 OUTPUT_VARIABLE result)

#add_test(Exampletest ../test_cpp.sh)

message(${PROJECT_SOURCE_DIR})

set(CMAKE_CXX_FLAGS "-std=c++14 -O2 -Wall -pedantic")
file(GLOB files e*.cpp)
list(SORT files)
foreach(file ${files}) 
  get_filename_component(f ${file} NAME_WE)
  add_executable(${f}.cppout ${file})
  add_test(NAME cpp_${f} COMMAND ${PROJECT_SOURCE_DIR}/run.sh ${f}.cpp
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
  add_test(NAME f90_${f} COMMAND ${PROJECT_SOURCE_DIR}/run.sh ${f}.f90
           WORKING_DIRECTORY ${PROJECT_SOURCE_DIR})
endforeach()
