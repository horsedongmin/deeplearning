#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: wensong

import tensorflow as tf
from .tf_base_layer import TFBaseLayer


class TFSoftAttLayer(TFBaseLayer):
    '''soft attention层封装
    softmax求出attention score后，对隐层进行软加权。
    '''
    def __init__(self, in_hidden, attention_size):
        '''初始化

        Args:
            in_hidden: 需要进行软加权的隐层
            attention_size: attention权重矩阵宽度
        '''
        # 父类初始化
        TFBaseLayer.__init__(self)
        # 当前层参数
        self.in_hidden = in_hidden
        self.in_hidden_size = in_hidden.get_shape()[-1]
        self.attention_size = attention_size

    def layer(self):
        """返回soft-attention后的向量表示
        输入Shape为[Batch, TimeStep, In_Hidden_Size]

        Returns:
            返回shape为[Batch, In_Hidden_Size]
        """
        # 初始化att参数
        att_w = tf.get_variable(
            "attention_weight",
            shape=[self.hidden_size, self.attention_size],
            initializer=tf.contrib.layers.xavier_initializer())
        att_b = tf.get_variable(
            "attention_bias",
            shape=[self.attention_size],
            initializer=tf.contrib.layers.zeros_initializer())
        att_u = tf.get_variable(
            "attention_u",
            shape=[self.attention_size],
            initializer=tf.contrib.layers.zeros_initializer())

        # 非线性转换
        # [B, T, H] dot [H, A] = [B, T, A]
        att_v = tf.tanh(tf.tensordot(self.in_hidden, att_w, axes=1) + att_b)

        # [B, T, A] dot [A] = [B, T]
        att_vu = tf.tensordot(att_v, att_u, axes=1, name='attention_vu')

        # attention score, [B, T]
        att_alpha = tf.nn.softmax(att_vu, name='attention_alpha')

        # expand to: [B, T] -> [B, T, 1]
        att_expand = tf.expand_dims(att_alpha, -1)
        # 注意是点乘: [B, T, H] * [B, T, 1] = [B, T, H]
        att_ah = self.in_hidden * att_expand
        # reduce_sum, axis=1: [B, T, H] -> [B, H]
        self.output = tf.reduce_sum(att_ah, axis=1)

        # [Batch, In_Hidden_Size]
        return self.output
