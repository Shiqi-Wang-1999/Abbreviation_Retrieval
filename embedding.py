
"""
将文本向量化
"""
import numpy as np
import gensim
from bert_embedding import BertEmbedding
import mxnet
import logging
logging.basicConfig(
    format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)


class Embedding(object):

    def __init__(self, embedding_path, isbert: bool = False):
        self.embedding_path = embedding_path
        self.isbert = isbert
        if not self.isbert:
            # 基于word2vec的词向量
            self.model = gensim.models.KeyedVectors.load_word2vec_format(
                self.embedding_path, binary=False)
    '''获取词向量'''

    def get_wordvector(self, word):  # 获取词向量
        try:
            return self.model[word]
        except:
            return np.zeros(self.model['你'].shape[0])

    '''构建句子向量,句子向量等于字符向量求平均'''

    def creat_sentence_vec(self, word_list):
        if self.isbert:
            # 基于bert的句子向量
            text = "".join(word_list)
            # 预训练语言模型bert向量
            bert_embedding = self.bert_embedding([text])
            bert_train = np.array([np.mean(np.array(one[1]), axis=0)
                                  for one in bert_embedding], dtype=float)
            sentence_vec = bert_train[0]
        else:
            sentence_vec = np.array([self.get_wordvector(c)
                                     for c in word_list]).sum(axis=0) / (len(word_list))

        return sentence_vec

    def bert_embedding(self, textlist):
        ctx = mxnet.cpu(0)
        # 导入gpu版本的bert embedding预训练的模型。
        # 若没有gpu，则ctx可使用其默认值cpu(0)。但使用cpu会使程序运行的时间变得非常慢
        # 若之前没有下载过bert embedding预训练的模型，执行此句时会花费一些时间来下载预训练的模型
        embedding = BertEmbedding(ctx=ctx)
        bert_embedding = embedding(textlist)
        return bert_embedding


if __name__ == '__main__':
    # 测试向量
    word2vector_embedding_path = 'model/sgns.zhihu.word'
    embedding = Embedding(word2vector_embedding_path)
    print(embedding.get_wordvector("你好"))
    ctx = mxnet.cpu(0)
    embedding = BertEmbedding(ctx=ctx)
    bert_embedding = embedding(["你好"])
    vec = np.array([np.mean(np.array(one[1]), axis=0)
                    for one in bert_embedding], dtype=float)
    print(vec)
