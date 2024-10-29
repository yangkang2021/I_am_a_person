# 梅尔普算法及其python和c++实现

MFCC特征

## 算法流程
1. preemphasis 预加重算法：防止预期噪声（ protect against anticipated noise）
    - lfilter 线性滤波器
2. melspectrogram
    - stft ：短时傅里叶变换
    - melfilter：计算梅尔普的偏置basis
    - spectrogram：计算频谱图
    - dot：乘起来得到结果
3. amp_to_db：将mel频谱转换到db
4. normalize：正规化

## 学习
https://zhuanlan.zhihu.com/p/493160516
https://www.zhihu.com/column/c_1493292986553659393