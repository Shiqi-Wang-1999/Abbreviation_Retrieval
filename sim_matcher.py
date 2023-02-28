"""
基于向量空间模型的的短文本相似度匹配
"""
from segment import Segmentor
from embedding import Embedding
import numpy as np
import os
from retrieve import creat_retrieve,get_retrieve_result


class SimMatcher:
    def __init__(self, embedding: Embedding, seg: Segmentor):
        self.embedding = embedding
        self.segmentor = seg
    '''基于余弦相似度计算句子之间的相似度'''

    def similarity_cosine(self, word_list1, word_list2):
        # 构建句子向量
        vector1 = self.embedding.creat_sentence_vec(word_list1)
        vector2 = self.embedding.creat_sentence_vec(word_list2)
        cos1 = np.sum(vector1*vector2)
        cos21 = np.sqrt(sum(vector1**2))
        cos22 = np.sqrt(sum(vector2 ** 2))
        if cos21 * cos22 > 0:
            similarity = cos1 / float(cos21 * cos22)
        else:
            similarity = 0.0
        return similarity
    '''计算句子相似度'''

    def distance(self, text1, text2):  # 相似性计算主函数
        word_list1 = self.segmentor.segment(text1)
        word_list2 = self.segmentor.segment(text2)
        return self.similarity_cosine(word_list1, word_list2)

    '''基于相似度的匹配主函数,返回top_K相似度结果'''

    def matcher(self, text, text_list, top_k: int = 3):
        sim = np.array([self.distance(text, t) for t in text_list])
        if len(text_list)<=0:
            out = {"max": 0.0, "other_top": []}
            return out
        if len(text_list)< top_k:
            top_k=len(text_list)
        top_max_text = text_list[np.argsort(sim)[-1]]
        # 取相似度度最大的
        max_sim = {"name": top_max_text, "sim": '%.5f' % np.max(sim)}
        # 取其他top_相似度
        top_k_index = np.argsort(sim)[len(sim) - top_k:len(sim) - 1]
        second = []
        for index in top_k_index:
            sim_dic = {"name": text_list[index],
                       "sim": '%.5f' % sim[index]}
            second.append(sim_dic)
        out = {"max": max_sim, "other_top": second}
        return out
