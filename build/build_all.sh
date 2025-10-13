#!/bin/bash
set -e

#build all targets supported 
DIR=`dirname $0`


echo x86_linux tflm building..
$DIR/build_x86_linux.sh

echo amebadplus_km4 tflm building..
$DIR/build_amebadplus_km4.sh

echo amebalite_dsp tflm building..
$DIR/build_amebalite_dsp.sh

echo amebasmart_ca32_freertos tflm building..
$DIR/build_amebasmart_ca32_freertos.sh

echo amebasmart_ca32_linux tflm building..
$DIR/build_amebasmart_ca32_linux.sh
