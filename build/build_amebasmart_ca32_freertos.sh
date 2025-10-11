#!/bin/bash

target=amebasmart_ca32_freertos
build_dir=${target}-out


[[ -d $build_dir ]] && rm -rf $build_dir

#cmake -G Ninja -B ${build_dir} \
cmake -B ${build_dir} \
    -DCMAKE_TOOLCHAIN_FILE=./toolchains/amebasmart_ca32_freertos.toolchain.cmake \
    -DCMAKE_CHIP_TARGET=${target} \
    -DCMAKE_VERBOSE_MAKEFILE=OFF \
    -DBUILD_SHARED_LIBS:BOOL=OFF &&
cmake --build ${build_dir} --parallel $(nproc)
#cmake --build ${build_dir} --target install
