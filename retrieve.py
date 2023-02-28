"""
倒排表
"""
from segment import Segmentor
def creat_retrieve(text_token_list):
    '''
       生成倒排表
    '''
    inverted_list = {}
    for index,sentence in enumerate(text_token_list):
        ### 你需要完成的代码
        if type(sentence)==list:
            for word in sentence:
                if word not in inverted_list:
                    inverted_list[word] = [index]
                else:
                    inverted_list[word].append(index) 
    return inverted_list

def get_retrieve_result(sentence,invertedList,segment:Segmentor):
    '''
        输入一个句子sentence，根据倒排表进行快速检索，返回与该句子较相近的一些候选问题的index
        候选问题由包含该句子中任一单词或包含与该句子中任一单词意思相近的单词的问题索引组成
    '''
    text_token_list =segment.segment(sentence)
    candidate = set()
    for word in text_token_list:
        if word in invertedList:
            candidate = candidate | set(invertedList[word])
    return candidate
