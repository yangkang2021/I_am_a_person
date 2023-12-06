# bert-vits2学习


## 一. 推理流程
1. get_text(text, "ZH", 模型超参数)
   - clean_text
      - text_normalize(text)
      - g2p(norm_text)
   - cleaned_text_to_sequence
   - get_bert
2. net_g.infer


