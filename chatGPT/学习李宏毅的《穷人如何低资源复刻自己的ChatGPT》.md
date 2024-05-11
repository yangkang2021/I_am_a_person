# 学习李宏毅的《穷人如何低资源复刻自己的ChatGPT》
> 学习上周(23-04-21)李宏毅老师发布的最新课程[《穷人如何低资源复刻自己的ChatGPT》](https://speech.ee.ntu.edu.tw/~hylee/ml/2023-spring.php)
## 一. 学习笔记
1. 为什么需要复刻chatGPT？因为安全原因，要避免资料泄露。
	- openAI说：有可能会拿用户的对话数据来训练。
	- 要删除数据只能删除账号，不能选择其中一些删除。
2. 复刻chatGPT的方法：以chatGPT为师
	- 用chatGPT的答案来训练自己的模型。（参考论文Self-Instruct）
	- 让chatGPT帮你想更多问题
	- 让chatGPT帮你想更多任务
3. 复刻案例1：Alpaca-7B（草泥马）
	- 数据：用Self-Instruct让Text-advinci-003生成52k的对话数据。
	- 基础模型：LLaMa（羊驼）
4. 复刻案例2：vicuna-13B（小羊驼）
	- 数据：ShardGPT收集的与chatGPT对话的70k数据
	- 基础模型：LLaMa
	- 评估：让GPT-4打分
5. 复刻案例3：Dolly 2.0
	- LLaMa不能商用，Dolly可以
	- 用chatGPT的答案训练的模型不能商用，Dolly可以
	- 人工标注15k数据
6. 复刻案例对比
	- alpaca和vicuna成本已经极大的下降了。
	- 这些案例里面vicuna很强。
7. 其他方法
	- 把GPT-4看作人类来做强化学习。
	- Self-consistency和Self-improve让大模型自我进化。

## 二. 个人体会：
- 比起模型和算力，训练数据更加重要也更麻烦。
- 开源语言模型很多，但chatGPT/GPT4还是无敌的存在。
- 开源语言模型很多基于LLaMa微调训练。
- 数据安全，商用许可，数据来源许可，这些是重要的考虑点。 
- 特定场景可能不需要大语言模型，比如一个阅读理解任务就能解决基于已有知识文档的问答。