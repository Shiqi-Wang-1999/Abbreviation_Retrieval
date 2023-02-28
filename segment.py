"""
分词器，包括 ['char', 'jieba', 'hanlp']三种
"""
import json
import os
from log import Logger
log = Logger().logger


class Segmentor(object):
    """分词工具"""

    def __init__(self, stopwords_filepath, isrmstopwords: bool = True, type: str = 'jieba'):
        '''type：分词器类型 ['char', 'jieba', 'hanlp']'''
        '''isrmstopwords：是否去停用词'''
        self.type = type
        self.isrmstopwords = isrmstopwords
        self.stopwords_filepath = stopwords_filepath
        self.stopwords=self.get_stopwords(self.stopwords_filepath)
        # 验证分词器是否安装完整
        if self.type not in ['char', 'jieba', 'hanlp']:
            raise ValueError(
                'cutter error, please use one of the {char, jieba,hanlp}')
        if self.type == 'jieba':
            try:
                import jieba
            except ModuleNotFoundError:
                raise ModuleNotFoundError(
                    "please install jieba, `$ pip install jieba`")

        elif self.type == 'hanlp':
            try:
                import pyhanlp
            except ModuleNotFoundError:
                raise ModuleNotFoundError(
                    "please install pyhanlp, `$ pip install pyhanlp`")

    def segment(self, sentence: str = None):
        word_tag_list = []
        if self.type == 'jieba':
            import jieba.posseg as pseg
            result = pseg.cut(sentence)
            for w in result:
                word_tag_list.append(w.word)
        if self.type == 'hanlp':
            import pyhanlp
            for w in pyhanlp.HanLP.segment(sentence):
                word_tag_list.append(w.word)
        if self.type == 'char':
            word_tag_list = list(sentence)
        if self.isrmstopwords:
            word_tag_list = self.rm_stop_word(word_tag_list, self.stopwords)
        return word_tag_list

    def get_stopwords(self, stopwords_file):
        stopWords = []
        if os.path.exists(stopwords_file):
            # 读取下载的停用词表，并保存在列表中
            with open(stopwords_file, "r", encoding='UTF-8') as f:
                stopWords = f.read().split("\n")
        return stopWords

    def rm_stop_word(self, wordList, stopWords):
        # 去除停用词
        wordList = [word for word in wordList if word not in stopWords]
        return wordList


if __name__ == '__main__':
    seg1 = Segmentor(type="jieba", isrmstopwords=True,
                     stopwords_filepath='model\stopWord.json')
    word_tag_list_1 = seg1.segment("北京大学")
    print(word_tag_list_1)
