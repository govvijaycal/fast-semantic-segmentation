export CUDA_DEVICE_ORDER=PCI_BUS_ID
export CUDA_VISIBLE_DEVICES=3
python train.py \
    --config_path configs/carla_icnet_resnet_v1_city.config \
    --logdir log \
    --save_interval_secs 3600 \
    --max_checkpoints_to_keep 15
