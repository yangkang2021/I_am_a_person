# 移植Bert-vits2到C++

## 尺寸
get_bert ：Nx1024


## 分句
```
根据文本进行按句子切分成三级列表
text_split_to_sentence
```

## 预处理
```
__text_to_model_inputs // return phones, tones, language_id, zh_bert, jp_bert, en_bert
    get_text
        norm_text, phone, tone, word2ph = clean_text(text, language)
        # print(norm_text, phone, tone, word2ph)
        # 将phone, tone, language转化为对应id表示
        phone, tone, language = cleaned_text_to_sequence(phone, tone, language)
        bert_ori: np.float32 = get_bert(norm_text, word2ph, language_str) 
            input_feed = __structure_onnx_inputs
                tokenized_tokens = tokenizer(text)
            __run_onnx
            __get_phone_level_feature
```
## vits2的参数        
```
seq=phones,
tone=tones,
language_id=language_id,
bert_zh=zh_bert,
bert_jp=jp_bert,
bert_en=en_bert,
speaker_id=speaker_id,
seed=seed,
seq_noise_scale=noise_scale,
sdp_noise_scale=noise_scale_w,
length_scale=length_scale,
sdp_ratio=sdp_ratio,
emotion=emotion,
```
self.models.emb_g.run   speaker_id->1x256             
self.models.enc.run
```
"x": seq,
"t": tone,
"language": language_id,
"bert_0": bert_zh,
"bert_1": bert_jp,
"bert_2": bert_en,
"g": g,
```
self.models.sdp.run
```
"x": x, "x_mask": x_mask, "zin": zinput.astype(np.float32), "g": g
```
self.models.dp.run
```
"x": x, "x_mask": x_mask, "g": g
```
self.models.flow.run
```
"z_p": z_p.astype(np.float32),
"y_mask": y_mask.astype(np.float32),
"g": g,
```
self.models.dec.run
```
"z_in": z, "g": g
```




## G2P
文本处理clean_text：
1. text_normalize：替换所有阿拉伯数字转为中文，同时将中文符号替换为英文符号
2. g2p：将文本转换成拼音
    - phone:拼音的声母、韵母
    - tone:声调 1 2 3 4 5
    - word2ph:如果只有韵母，返回1，如果有声母韵母，返回2
3. g2p的流程：
    - 将文本按照标点符号切分成列表
    - 处理每个词：
        - jieba的分词
        - jieba的分词后处理
4. CPPG2P
    - https://github.com/mohamad-hasan-sohan-ajini/CPPG2P
    - https://github.com/NaruseMioShirakana/MoeVoiceStudio
    - https://github.com/NaruseMioShirakana/TextCleaner

---
## jieba
1. https://github.com/fxsjy/jieba
2. cppjieba
    - https://github.com/yanyiwu/cppjieba
    - https://github.com/sweetorange2022/jiebacpp_ok


## pinyin
1. https://github.com/mozillazg/python-pinyin
2. cpppinyin
    - https://github.com/search?q=%E6%B1%89%E5%AD%97%E8%BD%AC%E6%8B%BC%E9%9F%B3+language%3AC%2B%2B&type=repositories&l=C%2B%2B&s=updated&o=desc
    - https://github.com/ESiangChioa/pinyinc
    - https://github.com/Shellbye/hanzi2pinyin 参考python-pinyin
    - https://github.com/flyhouzi/chinese-to-pinyin
    - https://github.com/maplefan/Chinese2Pinyin 没有声调
## tokenizer
1. 原始：BertTokenizer/DebertaV2TokenizerFast/DebertaV2TokenizerFast
2. cpptokenizer
    - https://github.com/mlc-ai/tokenizers-cpp
    - https://github.com/Peter-Chou/transformer_cpp_tokenizers
    - https://github.com/Sorrow321/huggingface_tokenizer_cpp
    - https://github.com/huggingface/tokenizers

---
## c++调用python
1. windows
    - https://github.com/ShenghaoZhou/cpp_call_python_wrapper 通过pybind11
    - https://github.com/RaphaeleL/PyCpp_Wrapper 通过libpython
    - https://github.com/miyanyan/callpython 通过pybind11
    - https://github.com/kivy 
2. android
    - https://github.com/yan12125/python3-android
    - https://github.com/kivy/python-for-android
    - https://github.com/joaoventura/pybridge
    - https://github.com/chaquo/chaquopy