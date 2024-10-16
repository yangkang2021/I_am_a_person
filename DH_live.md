# DINet与DH_live

## DINet
1. 原理
   - 看论文
   - https://blog.csdn.net/jiaoyangwm/article/details/136570638
   - 对图像特征进行仿射变化，得到与音频同步的嘴部图像特征，然后解码得到
2. 训练
   - ![](.images/1b96e981.png)
3. 代码结构
   - 推理输入：crop_frame, ref_img(随机选择), deepspeech(音频特征)
   - 第一阶段训练frame：net_g(DINet网络)，net_dI（Discriminator网络），net_vgg（Vgg19网络无需训练）
   - 第二阶段训练clip: 多了一个net_dV（Discriminator网络）
3. 总结
   - deepspeech模型479MB，DeepSpeech的V0.1版本 
   - 并没有给出同步模型的训练代码，参考wav2lip的同步专家模型：https://github.com/MRzzm/DINet/issues/56

## DINet_optimized
1. 代码:https://github.com/Elsaam2y/DINet_optimized
2. 优化
   - 移除了DeepSpeech，用wav2vec来提取特征。
   - 训练一个轻量级模型实现从wav2vec特征到DeepSpeech特征的映射
   - 增强了图像特征提取

## DH_live
> 作者的原话，我的翻译
1. 模型介绍：
   - Simply put, it is forcibly splitting the neural rendering algorithm into two parts. Simplify the audio_decoder and proceed with a simplified DiNet model. 
      > 简单地说，就是强行将神经渲染算法分成两部分。 简化的audio_decoder模型和简化的DiNet模型。
   - Audio_decoder is distilled from a more powerful model and outputs detailed changes in mouth shape. Add 3D rotation and manually construct a single-layer face UV map. 
      > Audio_decoder是从更强大的模型中提炼出来的，并输出嘴形的详细变化。 添加三维旋转信息，并手动构建单层人脸UV贴图。
   - DiNet acts as a decoder to generate the final face.
      > DiNet充当解码器来生成最终的人脸。
2. 关于没提供训练代码，怎么训练：
   - For DiNet, you can refer to the training and dataset construction steps in the code to complete your own training. 
     > 对于DiNet，您可以参考代码中的训练和数据集构建步骤来完成自己的训练。
   - For audio encoder, you need to find a satisfactory digital human model or commercial product that produces sufficient video as distilled material.
     > 对于音频编码器，您需要找到一个令人满意的数字人模型或商业产品，以产生足够的视频作为蒸馏材料。 
   - I have verified that using the generated stable data, a lightweight LSTM algorithm is enough to achieve good performance.
     > 我已经验证过，使用生成的稳定数据，轻量级的LSTM算法足以实现良好的性能。
   - Note: Do not only use mouth keypoints as the output of LSTM, better feature representation must be used, for example, I used PCA algorithm to extract pixel-level changes of the mouth.
     > 注意：不要只使用嘴巴关键点作为LSTM的输出，必须使用更好的特征表示，例如，我使用PCA算法来提取嘴巴的像素级变化。

2. 从其他数字人模型蒸馏出音频模型： 从声音fbank特征，直接生成15x30的嘴巴图像特征。
2. 用去掉了音频特征DINet模型生成最终的嘴部图，然后像拷贝回原图。 
1. 三个模型：
    - audio.pkl：2.59MB, 从音频直接得到，15x30的嘴巴图像
    - pca.pkl：8.54k，PCA算法用来提取嘴巴的像素级变化
    - render.pth
1. DINet + [LiveSpeechPortraits](https://github.com/YuanxunLu/LiveSpeechPortraits)
2. 把deepspeech换成了简单的LSTM
3. 音频编码，从其他成熟的商业化模型蒸馏得到一个简单的LSTM模型。 wenet?
4. 推理
   - imgs
   - keypoint_rotate.pkl
   - 
5. 训练数据准备：
   - train_video_list
     - img：model_name/image/*.png
     - keypoint：model_name/keypoint_rotate.pkl
     - face_mask：model_name/face_mat_mask20240722.pkl
     - 

## LiveSpeechPortraits
1. 用了wenet?
2. 没说怎么训练，有人复现
   - https://github.com/vicdxxx/LiveSpeechPortraits
   - 

## IP_LAP