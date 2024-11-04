# I_am_a_person
实时互动GPT数字人

## 零. 数据预处理
1. 视频分段
   - TransNetV2：最好的镜头分割模型
1. 人脸人体检测识别
   - insightface + buffalo_l：人脸检测、识别、对齐、人脸属性。
   - https://github.com/1adrianb/face-alignment：里面有人脸检测和对齐。 wav2lip用的这个
   - yolov8n-face：wav2lip-256用的这个
   - openface
2. 分割与抠图Matting 
   - face-parsing
   - DeepLabV3
   - https://github.com/PeterL1n/RobustVideoMatting
   - 最强AI一键抠图，BiRefNet V2
   - SAM2
   - https://github.com/ZHKKKe/MODNet
2. 表情识别
   - 基于图像的：
     - https://github.com/WiseGeorge/Fast-Facial-Emotion-Monitoring-FFEM-Package
   - 基于文本的：gpt

## 一. 数字人形象生成与定制
1. [视频生成](视频生成/视频生成.md)
2. [换脸](faceSwap/换脸.md)
1. https://github.com/modelscope/facechain.git
1. AI绘图（stableDiffusion）
   - [AI绘图系列](stableDiffusion/README.md)
   - [AI绘画的应用方向](stableDiffusion/AI绘画的应用方向.md)
   - sd，mj，flux，即梦

## 二. 数字人输入--语音识别
1. [AI语音-01-概述](ASR-TTS/AI语音-01-概述.md)
1. [k2语音识别.md](1.语音识别/k2语音识别.md)
2. whisper
3. funasr+Paraformer:https://github.com/modelscope/FunASR
4. SenseVoice：https://github.com/FunAudioLLM/SenseVoice
5. wenet

## 三. 数字人大脑--大语言模型
1. 角色扮演模型
   - Index-1.9B-Character ：https://github.com/bilibili/Index-1.9B
   - Character-LLM：https://github.com/choosewhatulike/trainable-agents
2. 小模型
   - miniCPM
   - MiniCPM-V
   - Phi-3-v
   - gemna2b

## 四. 数字人讲话唱歌--语音合成
1. tts
   - vits，vits2
   - [bert-vits2](bert-vits2学习.md)
   - gpt-sovits
   - fish-speech
   - CosyVoice： https://github.com/FunAudioLLM/CosyVoice
   - F5
   - maskgct牛逼：https://maskgct.github.io/,https://github.com/open-mmlab/Amphion/tree/main/models/tts/maskgct
   - Matcha-TTS
2. 唱歌tts(singing voice conversion)：
   - so-vits-svc
   - NeuCoSVC
3. 聊天tts
   - ChatTTS： https://github.com/2noise/ChatTTS
4. 其他
   - XTTS
   - openvoice与MeloTTS
   - https://github.com/PaddlePaddle/PaddleSpeech
   - 支持超过 7000 种语言的文本转语音模型ToucanTTS

## 五. 数字人驱动
1. [真人数字人项目](数字人/README.md)
3. [动捕](动作与动捕/README.md)
1. 虚拟数字人
   - [虚幻引擎MetaHuman数字人](ue/README.md)
   - [ue和unity数字人.md](ue/ue和unity数字人.md)
2. 三维重建数字人
   - [学习NeRF(新视角合成)](https://gitee.com/yangkang2022/nerf-learn)
   - 3D高斯gaussian-splatting
   - 苹果联合德国马普所推出的，基于高斯函数的3D数字人合成工具HUGS
   - https://machinelearning.apple.com/research/hugs
   - 训练45秒，渲染300+FPS！MVSGaussian：高效泛化的混合Gaussian
   - 超越AnimateAnyone！Meta提出全身3D虚拟人ExAvatar,可由简短视频建模转化为3D数字形象

## 六. 部署
1. [梅尔普算法及其python和c++实现](梅尔普算法及其python和c++实现.md)

## 七. 其他
1. [参考项目](参考项目.md)
