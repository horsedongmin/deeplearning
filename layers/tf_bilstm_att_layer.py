#!/usr/bin/env python
# coding: utf-8
# @author: wensong

import tensorflow as tf
from .tf_base_layer import TFBaseLayer
from .tf_soft_att_layer import TFSoftAttLayer


class TFBILSTMAttLayer(TFBaseLayer):
    '''多层bi-lstm加attention层封装
    底层可以多个双向lstm，顶层是SoftAttention加权隐层表示。
    '''
    def __init__(self, in_hidden, hidden_sizes, attention_size, keep_prob):
        '''Bi-LSTM-ATTENTION初始化

        Args:
            in_hidden: 输入层
            hidden_sizes: 多层BILSTM中每层隐层维数大小
            attention_size: 注意力矩阵宽度
            keep_prob: 多层lstm之间dropout输出时激活概率
        '''
        # 父类初始化
        TFBaseLayer.__init__(self)
        # 当前layer参数
        self.in_hidden = in_hidden
        self.hidden_sizes = hidden_sizes
        self.att_size = attention_size
        self.keep_prob = keep_prob

    def layer(self):
        '''多层bilstm-attention Layer隐层表示

        Returns:
            返回经过BILSTM-ATTENTION后的隐层表示，shape为[Batch, In_Hidden_Size]
        '''
        layer_hidden = self.in_hidden
        # 定义双向LSTM的模型结构
        with tf.name_scope("BILSTM_Layer"):
            # n个双层lstm
            for idx, hidden_size in enumerate(self.hidden_sizes):
                with tf.name_scope("BILSTM" + str(idx)):
                    # forward LSTM
                    fw_lstm_cell = tf.nn.rnn_cell.DropoutWrapper(
                        tf.nn.rnn_cell.LSTMCell(num_units=hidden_size,
                                                state_is_tuple=True),
                        output_keep_prob=self.keep_prob)
                    # backward LSTM
                    bw_lstm_cell = tf.nn.rnn_cell.DropoutWrapper(
                        tf.nn.rnn_cell.LSTMCell(num_units=hidden_size,
                                                state_is_tuple=True),
                        output_keep_prob=self.keep_prob)

                    # outputs: (output_fw, output_bw)
                    # 其中两个元素的维度都是[batch_size, max_time, hidden_size],
                    outputs, current_state = tf.nn.bidirectional_dynamic_rnn(
                        fw_lstm_cell,
                        bw_lstm_cell,
                        layer_hidden,  # 第一层输入是word_emb，第二层输入是上一层双向的拼接隐层
                        dtype=tf.float32,
                        scope="BILSTM" + str(idx))

                    # 从第三维拼接：[batch_size, time_step, hidden_size]
                    layer_hidden = tf.concat(outputs, 2)

        # 分割成前向和后向的输出
        outputs = tf.split(layer_hidden, num_or_size_splits=2, axis=-1)
        # [Batch, TimeStep, In_Hidden_Size]
        bilstm_layer = outputs[0] + outputs[1]

        # Attention
        with tf.name_scope("SoftAtt_layer"):
            self.output = TFSoftAttLayer(bilstm_layer, self.att_size).layer()

            # [Batch, In_Hidden_Size]
            return self.output
