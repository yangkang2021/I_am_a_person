# DINet分析

## DINet
1. 原理
   - 看论文
   - https://blog.csdn.net/jiaoyangwm/article/details/136570638
   - 对图像特征进行仿射变化，得到与音频同步的嘴部图像特征，然后解码得到
2. 训练
   - ![](.images/34fadc07.png)
   - ![](.images/1b96e981.png)
3. 代码结构
   - 推理输入：crop_frame, ref_img(随机选择), deepspeech(音频特征)
   - 第一阶段训练frame：net_g(DINet网络)，net_dI（Discriminator网络），net_vgg（Vgg19网络无需训练）
   - 第二阶段训练clip: 多了一个net_dV（Discriminator网络）
3. 总结
   - deepspeech模型479MB，DeepSpeech的V0.1版本 
   - 并没有给出同步模型的训练代码，参考wav2lip的同步专家模型：https://github.com/MRzzm/DINet/issues/56
