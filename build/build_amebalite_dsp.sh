#!/bin/bash

target=amebalite_dsp

configurations=(HIFI5_PROD_1123_asic_UPG HIFI5_PROD_1123_asic_wUPG)
export XTENSA_TOOLS_VERSION=RI-2021.8-linux
export XTENSA_BASE=/opt/xtensa/XtDevTools/install

for config in ${configurations[@]}
do
    build_dir=${target}-out/${config}
    [[ -d $build_dir ]] && rm -rf $build_dir
    export XTENSA_CORE=${config}

    cmake -B ${build_dir} \
    -DCMAKE_TOOLCHAIN_FILE=./toolchains/amebalite_dsp.toolchain.cmake \
    -DCMAKE_CHIP_TARGET=${target} \
    -DCMAKE_VERBOSE_MAKEFILE=OFF \
    -DBUILD_SHARED_LIBS:BOOL=OFF &&

    cmake --build ${build_dir} --parallel $(nproc)
done




#cmake -G Ninja -B ${build_dir} \
#cmake --build ${build_dir} --target install
