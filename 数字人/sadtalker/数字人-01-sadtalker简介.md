# sadtalker简介

## 一. 学习计划
1. 小工蚁创始人课程
   - SadTalker数字人插件演示 Stable Diffusion生成视频 
   - SadTalker如何生成脸部表情 更自然视频？ 
   - 开源数字人项目SadTalker升级 v0.0.2版本功能介绍和演示 
   - SadTalker数字人助力企业短视频制作，提升品牌形象 
   - 如何让SadTalker数字人更自然？最佳实践参数详细讲解
   - 开源数字人SadTalker项目源代码解读
2. 把SadTalker和SadTalker-webui跑起来
3. 学习SadTalker的源码解读
4. 学习SadTalker的模型结构和训练方法
5. SadTalker的性能评测和优化
6. SadTalker的最佳实践

## 二. 跑起来
1. ![](.images/5056daeb.png)
2. 参数很重要：来自[best_practice.md](https://github.com/OpenTalker/SadTalker/blob/main/docs/best_practice.md)

| Name        | Configuration | default |   Explaination  | 
|:------------- |:------------- |:----- | :------------- |
| Enhance Mode | `--enhancer` | None | Using `gfpgan` or `RestoreFormer` to enhance the generated face via face restoration network 
| Background Enhancer | `--background_enhancer` | None | Using `realesrgan` to enhance the full video. 
| Still Mode   | ` --still` | False |  Using the same pose parameters as the original image, fewer head motion.
| Expressive Mode | `--expression_scale` | 1.0 | a larger value will make the expression motion stronger.
| save path | `--result_dir` |`./results` | The file will be save in the newer location.
| preprocess | `--preprocess` | `crop` | Run and produce the results in the croped input image. Other choices: `resize`, where the images will be resized to the specific resolution. `full` Run the full image animation, use with `--still` to get better results.
| ref Mode (eye) | `--ref_eyeblink` | None | A video path, where we borrow the eyeblink from this reference video to provide more natural eyebrow movement.
| ref Mode (pose) | `--ref_pose` | None | A video path, where we borrow the pose from the head reference video. 
| 3D Mode | `--face3dvis` | False | Need additional installation. More details to generate the 3d face can be founded [here](docs/face3d.md). 
| free-view Mode | `--input_yaw`,<br> `--input_pitch`,<br> `--input_roll` | None | Genearting novel view or free-view 4D talking head from a single image. More details can be founded [here](https://github.com/Winfredy/SadTalker#generating-4d-free-view-talking-examples-from-audio-and-a-single-image).





