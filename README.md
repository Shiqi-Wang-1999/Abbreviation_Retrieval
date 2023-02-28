# 说明文档
## 环境准备
- 语言：python3 
- 依赖包：requirements.txt  
- 依赖包安装方法：pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/
## 程序说明
* model\sgns.zhihu.word 词向量
* model\stopWord.json 停用词
* model\token_vector.bin 字向量
* embedding.py 构建句子向量的方法
* load_data.py 数据读取与生成
* segment.py  分词工具
* sim_matcher.py 相似度匹配方法
* retrieve.py 倒排表方法
* main.py 匹配主方法
* api.py  接口
# 程序使用
* 主方法使用：命令行:python main.py 或 编辑器运行
* 接口使用：命令行：python api.py 或 编辑器运行
* 接口访问页面：http:ip:port/docs,如http://192.168.7.245:5555/docs

