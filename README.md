# Deeplearning手脚架

```wensong
这是一个快速搭建NLP、CV、推荐等DL方向的手脚架，包括基本的分类、回归、聚类、序列标注、双塔等常见模型的简洁实现。
```

![Python版本](https://img.shields.io/badge/Python-2.7|3.7-blue) ![Tensorflow版本](https://img.shields.io/badge/Tensorflow-1.5.0|2.1.0-blue) ![https://img.shields.io/badge/pytorch-1.3.1%7C1.4.0-blue](https://img.shields.io/badge/pytorch-1.3.1|1.4.0-blue) ![](https://img.shields.io/badge/MacOS-10.15.4-blue)



## 目录说明

```python
.
├── LICENSE
├── README.md
├── add_comments.py
├── add_comments_to_tree.sh
├── ci.sh
├── corpus                                            # 语料
│   ├── README.md
│   └── nlp
│       ├── chinese
│       └── english
│           ├── rt-polarity.neg
│           └── rt-polarity.pos
├── demos                                             # 执行
│   ├── README.md
│   ├── __init__.py
│   ├── executes                                  # 执行内核
│   │   ├── __init__.py
│   │   ├── executor.py                       # 执行器
│   │   ├── graph_processor.py                # 构图处理器
│   │   ├── init_processor.py                 # 参数处理器
│   │   ├── pre_processor.py                  # 语料处理器
│   │   ├── session_processor.py              # 会话处理器
│   ├── nlp_classifier.py                         # nlp分类器
│   ├── run_nlp_classifier.sh
│   └── test.py
├── layers                                            # 高级层
│   ├── __init__.py
│   ├── tf_base_layer.py
│   ├── tf_bilstm_att_layer.py
│   ├── tf_classifier_layer.py
│   ├── tf_embedding_layer.py
│   ├── tf_soft_att_layer.py
│   ├── tf_textcnn_layer.py
├── models                                            # 模型层
│   ├── README.md
│   ├── __init__.py
│   ├── cv
│   │   └── README.md
│   ├── nlp
│   │   ├── __init__.py
│   │   ├── classification
│   │   │   ├── __init__.py
│   │   │   ├── tf_base_classifier.py
│   │   │   ├── tf_bilstmatt_classifier.py
│   │   │   ├── tf_textcnn_classifier.py
│   │   ├── cluster
│   │   │   └── __init__.py
│   │   ├── seq2seq
│   │   │   └── __init__.py
│   │   ├── sequence_labeling
│   │   │   └── __init__.py
│   │   └── similarity
│   │       ├── README.md
│   │       └── __init__.py
│   └── tmp
│       ├── base_classifier.py
│       ├── bilstm_attention.py
│       ├── data_helpers.py
│       ├── test.py
│       └── text_cnn.py
├── run.sh                                            # 执行入口
├── save_models                                       # 模型保存地址
│   ├── 1589251118
│   │   └── checkpoints
│   └── 1589251301
│       └── checkpoints
└── utils
├── README.md
├── __init__.py
├── tf_utils.py                                       # 工具类
```

## 说明文档

*   [已实现NLP模型文档](https://github.com/snowhws/deeplearning/tree/master/models)
*   [Graph与Session的关系：适合构建复杂组合模型](https://www.jianshu.com/p/b636de7c251a)

## License

[Apache License 2.0](LICENSE)

