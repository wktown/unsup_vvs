python train_combinet.py \
    --expId depth_res50 --dataconfig dataset_config_pbr.cfg \
    --batchsize 64 --valinum 200 --whichopt 1 \
    --init_lr 0.1 --valdconfig dataset_config_pbr.cfg \
    --valid_first 0 --pathconfig depth_resnet50_up4.cfg \
    --nport 27001 --withclip 0 --fre_filter 20018 --fre_valid 20018 \
    --ignorebname_new 0 --init_type variance_scaling_initializer \
    --cacheDirPrefix gs://cx_visualmaster/ --namefunc tpu_combine_tfutils_depth \
    --weight_decay 1e-4 --with_feat 0 --tpu_flag 1 --tpu_task depth \
    --sm_loaddir gs://siming-dataset-1/pbrnet/ \
    --sm_loaddir2 gs://siming-dataset-1/ --depth_zip 1 "$@"
