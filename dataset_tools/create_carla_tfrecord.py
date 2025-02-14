from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import hashlib
import glob
import io
import json
import os
import numpy as np
import PIL.Image

import tensorflow as tf

flags = tf.app.flags
tf.flags.DEFINE_string('input_pattern', '',
                       'Carla dataset root folder.')
tf.flags.DEFINE_string('annot_pattern', '',
                       'Pattern matching input images for Carla.')
tf.flags.DEFINE_string('split_type', '',
                       'Type of split: `train`, `test` or `val`.')
tf.flags.DEFINE_string('output_dir', '', 'Output data directory.')

FLAGS = flags.FLAGS


tf.logging.set_verbosity(tf.logging.INFO)

"""Build a TF Record for Carla Semantic Segmentation dataset.  Adapted from Cityscapes version."""

''' 
Usage:
python create_carla_tfrecord.py \
    --input_pattern <rootdir>/train/rgb/*.png \
    --annot_pattern <rootdir>/train/gt/*.png \
    --output_dir  <rootdir>/train \
    --split_type train # must be `train` or `val`

Train: 
python create_carla_tfrecord.py \
    --input_pattern "/home/govvijay/Dropbox/carla_data/datasets/train/rgb/*.png" \
    --annot_pattern "/home/govvijay/Dropbox/carla_data/datasets/train/gt/*.png" \
    --output_dir  "/home/govvijay/Dropbox/carla_data/datasets/train" \
    --split_type train

Val:
python create_carla_tfrecord.py \
    --input_pattern "/home/govvijay/Dropbox/carla_data/datasets/val/rgb/*.png" \
    --annot_pattern "/home/govvijay/Dropbox/carla_data/datasets/val/gt/*.png" \
    --output_dir  "/home/govvijay/Dropbox/carla_data/datasets/val" \
    --split_type val
'''

def _bytes_feature(values):
    return tf.train.Feature(
        bytes_list=tf.train.BytesList(value=[values]))


def _int64_feature(values):
    if not isinstance(values, (tuple, list)):
        values = [values]
    return tf.train.Feature(int64_list=tf.train.Int64List(value=values))


def _open_file(full_path):
    with tf.gfile.GFile(full_path, 'rb') as fid:
        encoded_file = fid.read()
    encoded_file_io = io.BytesIO(encoded_file)
    image = PIL.Image.open(encoded_file_io)
    return image, encoded_file


def create_tf_example(image_path, label_path, image_dir='', is_jpeg=False):
    file_format = 'jpeg' if is_jpeg else 'png'
    full_image_path = os.path.join(image_dir, image_path)
    full_label_path = os.path.join(image_dir, label_path)
    image, encoded_image = _open_file(full_image_path)
    label, encoded_label = _open_file(full_label_path)

    height = image.height
    width = image.width
    if height != label.height or width != label.width:
        raise ValueError('Input and annotated images must have same dims.'
                        'verify the matching pair for {}'.format(full_image_path))

    feature_dict = {
        'image/encoded': _bytes_feature(encoded_image),
        'image/filename': _bytes_feature(
                full_image_path.encode('utf8')),
        'image/format': _bytes_feature(
                file_format.encode('utf8')),
        'image/height': _int64_feature(height),
        'image/width': _int64_feature(width),
        'image/channels': _int64_feature(3),
        'image/segmentation/class/encoded': _bytes_feature(encoded_label),
        'image/segmentation/class/format':_bytes_feature(
                'png'.encode('utf8')),
    }

    example = tf.train.Example(
        features=tf.train.Features(feature=feature_dict))
    return example


def _create_tf_record(images, labels, output_path):
    writer = tf.python_io.TFRecordWriter(output_path)
    for idx, image in enumerate(images):
        if idx % 100 == 0:
            tf.logging.info('On image %d of %d', idx, len(images))
        tf_example = create_tf_example(
            image, labels[idx], is_jpeg=False)
        writer.write(tf_example.SerializeToString())
    writer.close()
    tf.logging.info('Finished writing!')


def main(_):
    assert FLAGS.output_dir, '`output_dir` missing.'
    assert FLAGS.split_type, '`split_type` missing.'
    assert (FLAGS.input_pattern and FLAGS.annot_pattern), \
           'Must specify `input_pattern` and `annot_pattern`.'


    if not tf.gfile.IsDirectory(FLAGS.output_dir):
        tf.gfile.MakeDirs(FLAGS.output_dir)
    train_output_path = os.path.join(FLAGS.output_dir,
        'carla_{}.record'.format(FLAGS.split_type))

    image_filenames = glob.glob(FLAGS.input_pattern)
    annot_filenames = glob.glob(FLAGS.annot_pattern)
    if len(image_filenames) != len(annot_filenames):
        raise ValueError('Supplied patterns do not have image counts.')
    print('Length: ', len(image_filenames), len(annot_filenames))
    
    _create_tf_record(
            sorted(image_filenames),
            sorted(annot_filenames),
            output_path=train_output_path)


if __name__ == '__main__':
    tf.app.run()
