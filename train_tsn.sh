#!/usr/bin/env bash

DATASET=$1
MODALITY=$2

TOOLS=/app/lib/caffe-action/build/install/bin
LOG_FILE=/li_wei/AD/code/ad_exp/logs/${DATASET}_${MODALITY}_split1.log
N_GPU=4
MPI_BIN_DIR= #/usr/local/openmpi/bin/


echo "logging to ${LOG_FILE}"

#${MPI_BIN_DIR}mpirun -np $N_GPU \
$TOOLS/caffe train --solver=/li_wei/AD/code/ad_exp/models/${DATASET}/tsn_bn_inception_${MODALITY}_solver.prototxt  \
   --weights=/app/models/bn_inception_${MODALITY}_init.caffemodel 2>&1 | tee ${LOG_FILE}
