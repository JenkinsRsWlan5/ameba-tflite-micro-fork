#!/bin/bash

target=amebalite_km4
build_dir=${target}-out


#[[ -d $build_dir ]] && rm -rf $build_dir

#cmake -G Ninja -B ${build_dir} \
cmake -B ${build_dir} \
    -DCMAKE_TOOLCHAIN_FILE=./toolchains/amebalite_km4.toolchain.cmake \
    -DCMAKE_CHIP_TARGET=${target} \
    -DCMAKE_VERBOSE_MAKEFILE=ON \
    -DBUILD_SHARED_LIBS:BOOL=OFF &&
cmake --build ${build_dir} --parallel $(nproc)
#cmake --build ${build_dir} --target install
