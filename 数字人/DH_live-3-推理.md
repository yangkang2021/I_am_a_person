# DH_live推理

## 一. 推理
1. 三个模型：
    - audio.pkl：2.59MB, 从音频直接得到，15x30的嘴巴图像
    - pca.pkl：8.54k，PCA算法用来提取嘴巴的像素级变化
    - render.pth：37.75MB, 渲染模型

## 二. 数据准备：data_preparation.py
1. 从mp4 --生成--> circle.mp4 + keypoint_rotate.pkl
2. circle.mp4: 正序+逆序的视频
3. keypoint_rotate.pkl：ExtractFromVideo提取关键点信息
   - 用mediapipe检测人脸，并做质量检测。
   - 把人脸剪裁出来
   - 用mediapipe做人脸mesh网格剪裁，得到478点的三维信息。
   - pts_3d = pts_3d = np.zeros([totalFrames, 478, 3])写入文件

## 三. 推理过程：demo.py
> 两个模型，两个步骤
1. 两个模型
   - AudioModel().loadModel("checkpoint/audio.pkl")
   - RenderModel().loadModel("checkpoint/render.pth")
2. 两步
   - mouth_frame = audioModel.interface_wav(wavpath)
   - frame = renderModel.interface(mouth_frame)

## 四. 音频模型
1. pca.pkl
   - 一个7 x 1350的数据， 7x15x30x3
   - 前六个数据，左右半边相加取均值
2. talkingface.models.audio2bs_lstm.Audio2Feature
3. 计算fbank = knf.OnlineFbank(opts)
4. 调用模型bs_array, hn, cn = self.__net(input, h0, c0)
5. 乘上pca后reshape成图像

## 五. 渲染模型
1. talkingface.models.DINet import DINet_five_Ref as DINet
2. reset_charactor
   - prepare_video_data
   - 取出需要的141个点，main_keypoints_index
   - 做一个平滑smooth_array
   - 选5个参考帧：根据嘴巴开合程度，选取开合最大的那一半
   - video_pts_process: 先根据pts_array_origin计算出旋转矩阵、去除旋转后的人脸关键点、面部mask
   - __mouth_coords_array
3. interface
   - generate_input_pixels
   - net.interface(source_tensor, source_prompt_tensor)

```
dh-live-audio:
in1--input.shape: torch.Size([1, 1838, 80])
in2--h0.shape: torch.Size([2, 1, 192])
in3--c0.shape: torch.Size([2, 1, 192])
out1--bs_array.shape: torch.Size([1, 919, 6])
out2--hn.shape: torch.Size([2, 1, 192])
out3--cn.shape: torch.Size([2, 1, 192])

dh-live-render:
in1--source_tensor.shape: torch.Size([1, 3, 256, 256])
in2--source_prompt_tensor.shape: torch.Size([1, 3, 256, 256])
in3--self.ref_tensor: torch.Size([1, 30, 256, 256])
out1--fake_out.shape: torch.Size([1, 3, 256, 256])

```

## 六. 模型结构
1. Audio2Feature
   - 输入fbank
   - downsample
   - LSTM
   - fc
   - 输出要乘以pca
2. DINet_five_Ref
   - 输入ref_image ：ref_in_conv + appearance_conv_list[0] 得到ref_in_feature
   - source_img ：source_in_conv  得到source_in_feature
   - source_in_feature + ref_in_feature ：
     - trans_conv，
     - global_avg2d，
     - adaAT，
     - appearance_conv_list[1]
     - 得到 out_conv
   

把deepspeech换成了简单的LSTM,音频编码，从其他成熟的商业化模型蒸馏得到一个简单的LSTM模型。 wenet?
3. 从其他数字人模型蒸馏出音频模型： 从声音fbank特征，直接生成15x30的嘴巴图像特征。
2. 用去掉了音频特征DINet模型生成最终的嘴部图，然后像拷贝回原图。 

   
4. 推理
   - imgs
   - keypoint_rotate.pkl
