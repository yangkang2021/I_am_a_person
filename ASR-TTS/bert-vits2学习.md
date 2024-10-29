# bert-vits2学习

## 一. 推理流程
1. get_text(text, "ZH", 模型超参数)
   - clean_text
      - text_normalize(text)
      - g2p(norm_text)
   - cleaned_text_to_sequence
   - get_bert
2. net_g.infer

## 二. bert-vits2资料
1. 官网：https://github.com/fishaudio/Bert-VITS2
2. 模型下载：
    - https://openi.pcl.ac.cn/Stardust_minus/Bert-VITS2/modelmanage/show_model
    - https://huggingface.co/OedoSoldier
3. web前端与Api：
   - https://v2.genshinvoice.top/
   - 调用示例：https://github.com/yakami129/VirtualWife/blob/main/domain-chatbot/apps/speech/tts/bert_vits2.py
4. onnx: https://github.com/huahuahuage/Bert-VITS2-Speech
5. 非官方扩展：
   - https://github.com/see2023/Bert-VITS2-ext

## 三. fish-speech
1. 官网：https://github.com/fishaudio/fish-speech
2. 网址：https://speech.fish.audio/
