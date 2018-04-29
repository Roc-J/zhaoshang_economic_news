# -*- coding: utf-8 -*-
# Roc-J

import jieba
import pandas as pd
from gensim import corpora, models, similarities

def train_text():
    # 训练文本数据
    all_doc = []
    datas = pd.read_csv("train_data.csv")
    titles = datas['title']
    for title in titles:
        all_doc.append(title)

    # 对目标文档进行分词
    all_doc_list = []
    for doc in all_doc:
        doc_list = [word for word in jieba.cut(doc)]
        all_doc_list.append(doc_list)


    # 测试文档进行分词
    test_doc = []
    test_datas = pd.read_csv("test_data.csv")
    test_titles = test_datas["title"]
    for title in test_titles:
        test_doc.append(title)
    test_doc_list = []
    for doc in test_doc:
        doc_list = [word for word in jieba.cut(doc)]
        test_doc_list.append(doc_list)

    # 制作语料库
    dictionary = corpora.Dictionary(all_doc_list)
    dictionary.keys()
    dictionary.token2id
    corpus = [dictionary.doc2bow(doc) for doc in all_doc_list]
    tfidf = models.TfidfModel(corpus)
    results = []
    for doc_test_list in test_doc_list:
        doc_test_vec = dictionary.doc2bow(doc_test_list)
        index = similarities.SparseMatrixSimilarity(tfidf[corpus], num_features=len(dictionary.keys()))
        sim = index[tfidf[doc_test_vec]]
        similiar_sorted = sorted(enumerate(sim), key=lambda item: -item[1])[:21]
        indexs = [str(item[0]+1) for item in similiar_sorted]
        results.append(" ".join(indexs))

    with open("results.txt", "w") as f:
        for item in results:
            item = item.strip().split()
            for i in range(1, 21):
                f.write(item[0] + "\t" + item[i] + "\n")

if __name__ == "__main__":
    train_text()
    with open("results.txt", "r") as f, open("submisson.txt", "w") as wf:
        datas = f.readlines()
        for data in datas:
            data = data.strip().split("\t")
            wf.write(data[0] + "\t" + data[1] + "\n")

