gpu=$1
split=$2
for rep in 0 1 2
do
    python fit_neural_data.py --gpu ${gpu} \
        --load_setting_func v1v2_setting.cate_res18_v1v2_bwd_to_be_filled \
        --expId cate_e69_bal_bwd_sp${split}_${rep} \
        --v1v2_folder /mnt/fs4/chengxuz/v1v2_related/tfrs_balance/ \
        --which_split split_${split}

    python fit_neural_data.py --gpu ${gpu} \
        --load_setting_func v1v2_setting.cate_res18_v1v2_bbwd_to_be_filled \
        --expId cate_e69_bal_bbwd_sp${split}_${rep} \
        --v1v2_folder /mnt/fs4/chengxuz/v1v2_related/tfrs_balance/ \
        --which_split split_${split}

    for layer in 1 2 3 4 5
    do
        python fit_neural_data.py --gpu ${gpu} \
            --load_setting_func v1v2_setting.cate_res18_v1v2_e${layer}_to_be_filled \
            --expId cate_e${layer}_bal_sp${split}_${rep} \
            --v1v2_folder /mnt/fs4/chengxuz/v1v2_related/tfrs_balance/ \
            --which_split split_${split}
    done
done
