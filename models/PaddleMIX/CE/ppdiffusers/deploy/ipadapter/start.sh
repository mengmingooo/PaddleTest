#!/bin/bash

cur_path=$(pwd)
echo ${cur_path}

work_path1=${root_path}/PaddleMIX/ppdiffusers/deploy/sd15
echo ${work_path1}

log_dir=${root_path}/deploy_log

if [ ! -d "$log_dir" ]; then
    mkdir -p "$log_dir"
fi

/bin/cp -rf ./* ${work_path1}/
exit_code=0

cd ${work_path1}

bash sd15_export.sh
exit_code=$(($exit_code + $?))

bash sd15_infer.sh
exit_code=$(($exit_code + $?))


work_path2=${root_path}/PaddleMIX/ppdiffusers/deploy/sdxl
echo ${work_path2}

/bin/cp -rf ./* ${work_path2}/

cd ${work_path2}

bash sdxl_export.sh
exit_code=$(($exit_code + $?))

bash sdxl_infer.sh
exit_code=$(($exit_code + $?))


echo exit_code:${exit_code}
exit ${exit_code}
