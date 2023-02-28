
import os
from segment import Segmentor
from embedding import Embedding
from sim_matcher import SimMatcher
from retrieve import creat_retrieve,get_retrieve_result

"""以下设置为全局变量"""
#匹配数据
match_data_file = '高校名称.txt'
text_list=[]
if os.path.exists(match_data_file):
    # 读取高校名称进行匹配
    with open(match_data_file, "r", encoding='UTF-8') as f:
        text_list = f.read().split("\n")
#停用词路径
stopwords_filepath = 'model\stopWord.json'
#词向量路径
word_embedding_path = 'model/sgns.zhihu.word'
word_embedding = Embedding(word_embedding_path)
#字向量路径
token_embedding_path = 'model/token_vector.bin'
token_embedding = Embedding(token_embedding_path, isbert=False)
#bert向量
bert_embedding = Embedding(None, isbert=True)

def main_match(text,segment_type,isbert,isrmstopwords):
    """程序主方法"""
    #创建分词器
    segment=Segmentor(type=segment_type, isrmstopwords=isrmstopwords,stopwords_filepath=stopwords_filepath)
    embedding=None
    #构建向量
    if segment_type=='char':
        if not isbert:
            embedding=token_embedding
        else:
            embedding=bert_embedding
    else:
        embedding=word_embedding
    #生成倒排表
    text_token_list=[segment.segment(text) for text in text_list]
    inverted_list=creat_retrieve(text_token_list)
    #获取候选对比项
    candidate_index=get_retrieve_result(text,inverted_list,segment)
    candidate_list=[text_list[i] for i in candidate_index]
    #相似度匹配
    simer = SimMatcher(embedding=embedding, seg=segment)
    return simer.matcher(text, candidate_list)

if __name__ == '__main__':
    text = '中央财大'
    print(main_match(text,'jieba',False,True))
    print(main_match(text,'hanlp',False,True))
    print(main_match(text,'char',False,True)) #效果较好
    print(main_match(text,'char',True,True))#没有GPU会很慢
    