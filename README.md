# 招商银行财经新闻分析
![](https://raw.githubusercontent.com/Roc-J/zhaoshang_economic_news/master/photos/title.png)
## 赛题背景  

[赛题连接](https://www.nowcoder.com/activity/2018cmbchina/bigdata/2)

财经新闻作为重要却海量的投资数据，无时无刻不在影响着投资者们的投资决策，为了更好地提示客户当下新闻事件对应的投资机会和投资风险，本课以研发“历史事件连连看”为目的，旨在根据当前新闻内容从历史事件中搜索出相似新闻报道，后期可以结合事件与行情，辅助客户采取相应投资策略。  
该赛题是让参赛者为每一条测试集数据寻找其最相似的TOP 20条新闻（不包含测试新闻本身），我们会根据参赛者提交的结果和实际的数据进行对比，采用mAP值作为评价指标。

* baseline.py  
使用TF-IDF算法进行文本相似度分析
* baseline_2.py  
去停用词，使用TF-IDF算法进行文本相似度分析

>说明：请对照一下第一列提交的情况，因为去停用词后出的相似度有差异，第一列好像有几个不是提交文档的id，请注意，并且感觉去停用词效果没那么好！

运行时间大约在1到2个小时，结果在0.09+上，但是去停用词感觉结果差一点，希望大家能发挥聪明才智完善。

# 结果
![](https://raw.githubusercontent.com/Roc-J/zhaoshang_economic_news/master/photos/results.png)


# 有同学反应，目前不开放
