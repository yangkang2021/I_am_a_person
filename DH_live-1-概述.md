# DH_live

## 一. 理论指导
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
     
## 相关项目
1. DINet 
2. [LiveSpeechPortraits](https://github.com/YuanxunLu/LiveSpeechPortraits)
    - 用了wenet?
    - 没说怎么训练，有人复现 https://github.com/vicdxxx/LiveSpeechPortraits