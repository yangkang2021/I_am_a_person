# bert-vits2与melo-tts学习

## 一. bert-vits2从训练到推理
1. 版本选择
2. 训练
3. 推理：分割，mix，auto，融合文本，跨语言推理。
4. 原理：
	- bert的意义

## 二. melo-tts从训练到推理
1. 训练: 底模不支持中英混合

## 三. K2推理

## 四. melo-tts与bert-vits2的差异
1. 为什么快？ 优化了什么？
	- 速度基本相当，只是bert-tts的dec的ups模型，偶尔很慢。
	```
   	melo-infer: 我要杀你们，已经早都杀了，如果我乔峰要去拿一样东西，无论是皇宫里或者千军万马之中，都易如反掌。 0.2 0.6 0.8 1.0
	melo-tts emb time: 0
	melo-tts enc time: 29
	melo-tts sdp+dp time: 18
	melo-tts numpy time: 6
	melo-tts flow time: 378
	melo-tts dec time: 3594
	melo-tts infer time: cpu 4027
	
	bert-infer: 我要杀你们，已经早都杀了，如果我乔峰要去拿一样东西，无论是皇宫里或者千军万马之中，都易如反掌。 0.2 0.6 0.8 1
	bert-tts emb time: 0
	bert-tts enc time: 45
	bert-tts sdp+dp time: 25
	bert-tts numpy time: 4
	bert-tts flow time: 403
	bert-tts dec time: 3884
	bert-tts infer time: cpu 4362
	bert-infer: 我要杀你们，已经早都杀了，如果我乔峰要去拿一样东西，无论是皇宫里或者千军万马之中，都易如反掌。 0.2 0.6 0.8 1
	bert-tts emb time: 0
	bert-tts enc time: 47
	bert-tts sdp+dp time: 25
	bert-tts numpy time: 5
	bert-tts flow time: 445
	bert-tts dec time: 9067
	bert-tts infer time: cpu 9590
	```
2. 怎么支持中英文混合的speaker的？
	- 他把中文和英文的符号symbols、声调、bert合并到一起了吗？


