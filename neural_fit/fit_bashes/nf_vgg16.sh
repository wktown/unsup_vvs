python fit_neural_data.py \
    --whichopt 1 --weight_decay 1e-3 \
    --expId new_vgg16_wf --gpu 8 \
    --loadexpId inst_infant_18_fx --cacheDirPrefix /mnt/fs4/chengxuz \
    --cacheDirName neural_fitting_inst \
    --it_nodes encode_[4:1:13] \
    --v4_nodes encode_[4:1:13] --batchsize 64 --loadport 27009 \
    --tpu_flag 1 --fre_valid 160 --fre_metric 160 \
    --rp_sub_mean 1 --div_std 1 \
    --network_func get_vgg16 \
    --ckpt_file /mnt/fs4/chengxuz/tpu_ckpts/vgg16/model.ckpt-610549 \
    --use_dataset_inter \ 
    --train_num_steps 635576