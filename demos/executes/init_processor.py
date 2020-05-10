#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: wensong

import os
import sys
import tensorflow as tf
import numpy as np


class InitProcessor(object):
    '''nlp分类器初始化
    '''
    def __init__(self):
        self.name = "INIT"

    def execute(params):
        '''初始化参数，使用tf的flags定义
        '''
        # 当前路径
        current_path = os.getcwd()
        # 样本集合相关参数
        tf.flags.DEFINE_float(
            "dev_sample_percentage", .1,
            "Percentage of the training data to use for validation")
        tf.flags.DEFINE_string(
            "positive_data_file",
            current_path + "../corpus/rt-polaritydata/rt-polarity.pos",
            "Data source for the positive data.")

        tf.flags.DEFINE_string(
            "negative_data_file",
            current_path + "../corpus/rt-polaritydata/rt-polarity.neg",
            "Data source for the negative data.")

        # 分类器公共参数
        tf.flags.DEFINE_integer(
            "emb_size", 128, "Dimensionality of word embedding (default: 128)")
        tf.flags.DEFINE_integer("max_seq_len", 1024,
                                "max len of input seq(default: 1024)")

        # TextCNN相关参数
        tf.flags.DEFINE_string("filter_sizes", "2,3,4,5",
                               "TextCNN filter sizes (default: '2,3,4,5')")
        tf.flags.DEFINE_integer(
            "num_filters", 128,
            "Number of filters per filter size (default: 128)")

        # 训练相关参数
        tf.flags.DEFINE_integer("batch_size", 64, "Batch Size (default: 64)")
        tf.flags.DEFINE_integer("num_epochs", 100,
                                "Number of training epochs (default: 100)")
        tf.flags.DEFINE_float("keep_prob", 0.5,
                              "Dropout keep probability (default: 0.5)")
        tf.flags.DEFINE_float("l2_reg_lambda", 0.0,
                              "L2 regularization lambda (default: 0.0)")
        tf.flags.DEFINE_integer(
            "evaluate_every", 100,
            "Evaluate model on dev set after this many steps (default: 100)")
        tf.flags.DEFINE_integer(
            "checkpoint_every", 100,
            "Save model after this many steps (default: 100)")
        tf.flags.DEFINE_integer("num_checkpoints", 5,
                                "Number of checkpoints to store (default: 5)")

        #  设备及日志相关
        tf.flags.DEFINE_boolean(
            "allow_soft_placement", True,
            "Allow device soft device placement")  # 如果指定设备不存在，tf自动分配设备
        tf.flags.DEFINE_boolean("log_device_placement", False,
                                "Log placement of ops on devices")  # 是否打印备份日志

        # 返回参数
        return tf.flags.FLAGS
