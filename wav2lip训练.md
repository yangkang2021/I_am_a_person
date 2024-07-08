# wav2lip训练

## 训练数据组织
1. lrs2数据集格式
```
data_root (mvlrs_v1)
├── main, pretrain (we use only main folder in this work)
|	├── list of folders
|	│   ├── five-digit numbered video IDs ending with (.mp4)
```
2. lrs2预处理后用于训练的数据集格式
```
preprocessed_root (lrs2_preprocessed)
├── list of folders
|	├── Folders with five-digit numbered video IDs
|	│   ├── *.jpg
|	│   ├── audio.wav
```

## 在自己的数据集训练的指导思想：
1. 几分钟进行训练/微调，您可能无法获得良好的结果。
2. 在训练 Wav2Lip 之前，您必须为自己的数据集训练专家鉴别器。
3. 在大多数情况下，需要进行同步校正。
4. 视频要求25FPS。
5. 专家鉴别器的评估损失应降至 ~0.25，Wav2Lip 应降至 ~0.2

## 数据预处理和训练参考项目：
1. https://github.com/primepake/wav2lip_288x288
2. https://github.com/monk-after-90s/wav2lip_data_preprocess
3. https://github.com/nghiakvnvsd/wav2lip_data_preprocessing
4. https://github.com/zzj1111/Preprocessed-CMLR-Dataset-For-Wav2Lip

## 数据集
1. lrs2
   - https://aistudio.baidu.com/datasetoverview/2/1
   - https://aistudio.baidu.com/datasetdetail/228857
   - main: 48165个视频，2611592帧。
   - 160x160
2. CMLR
   - https://www.vipazoo.cn/CMLR.html 官网提供了百度网盘链接
   - https://pan.baidu.com/share/init?surl=bXj_LZy1wTInQE9ceJl7UA&pwd=1122
   - 480x360
3. AVSpeech
4. LRW1000:
   - https://pan.baidu.com/share/init?surl=XBT-5tAJxeIQ5UiEz8-9gQ&pwd=i9kp
5. GRID
    - https://spandh.dcs.shef.ac.uk//gridcorpus/
    - 直接能下载 
    - normal quality (360x288; ~1kbit/s) and high quality (720x576; ~6kbit/s).
1、HDTF https://pan.baidu.com/s/1UQ0I3L3FKxhA_PcS3YrL6w  提取码：elej
   - 1280x720
2、MEAD https://github.com/uniBruce/Mead
   - https://wywu.github.io/projects/MEAD/MEAD.html
   - 有百度网盘下载
   - 1920x1080
3、VOX https://pan.baidu.com/share/init?surl=wBL34jZRSMq4aJX-l3_pBw   提取码：xkfj
5. 汇总：
   - https://blog.csdn.net/u011570979/article/details/136928045
   - https://blog.csdn.net/lsb2002/article/details/135999742
   
## 优化方案
1. 高清人脸：192 x 288，256，288，Talking-Face-Generation
2. 超分：
   - coderformer
   - gfpgan
   - ResShift
3. 256项目
   - 人脸对齐
   - 声音平滑
   - 声音缩放
4. 人脸
   - https://github.com/instant-high/wav2lip-onnx-HQ
   - face-detection
   - face-alignment
   - face-parsing
   - face-enhancement
4. 参考项目
   - https://github.com/leeguandong/Wav2lipAll
   - IP_LAP：训练了一个mask解决方框问题
   - https://github.com/bjfrbjx/stream-wav2lip：头脸分离、嘴型替换、回补背景三个步骤分离
   - wav2lip-hq系列
     - https://github.com/Markfryazino/wav2lip-hq
     - https://github.com/GucciFlipFlops1917/wav2lip-hq-updated-ESRGAN
     - https://github.com/anothermartz/Easy-Wav2Lip
     - Easy-Wav2lip：
	  - Fast: 仅WAV2Lip
	  - Improved: WAV2Lip + 在嘴巴周围使用遮罩羽化，以去除脸部周围的边框
	  - Enhanced: WAV2Lip + 面部上的 mask + GFPGAN 放大 作者：SuperAI小夜 https://www.bilibili.com/read/cv34054452/ 出处：bilibili
   - wav2lip与sd结合
     - https://github.com/numz/wav2lip_uhq
     - https://github.com/numz/sd-wav2lip-uhq
     - https://github.com/yukyeongleee/Wav2Lip-HQ
    
