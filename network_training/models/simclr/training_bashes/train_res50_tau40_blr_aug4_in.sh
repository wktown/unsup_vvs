TPU_NAME=$1
DATA_DIR=gs://full_size_imagenet/tfrs/
MODEL_DIR=gs://cx_visualmaster/simclr_blr_aug4_tau40
TPU_ZONE=$2

python run.py --train_mode=pretrain \
  --train_batch_size=256 --train_epochs=100 \
  --learning_rate=0.6 --weight_decay=1e-6 --temperature=0.4 \
  --dataset=imagenet2012 --image_size=224 --eval_split=validation \
  --data_dir=$DATA_DIR --model_dir=$MODEL_DIR \
  --use_tpu=True --tpu_name=$TPU_NAME --train_summary_steps=0 --tpu_zone $TPU_ZONE \
  --num_transforms 4

FIT_MODEL_DIR=${MODEL_DIR}_fit
python run.py --mode=train_then_eval --train_mode=finetune \
  --fine_tune_after_block=4 --zero_init_logits_layer=True \
  --variable_schema='(?!global_step|(?:.*/|^)LARSOptimizer|head)' \
  --global_bn=False --optimizer=momentum --learning_rate=0.1 --weight_decay=1e-6 \
  --train_epochs=90 --train_batch_size=4096 --warmup_epochs=0 \
  --dataset=imagenet2012 --image_size=224 --eval_split=validation \
  --data_dir=$DATA_DIR --model_dir=$FIT_MODEL_DIR --checkpoint=$MODEL_DIR \
  --use_tpu=True --tpu_name=$TPU_NAME --train_summary_steps=0 --tpu_zone $TPU_ZONE
