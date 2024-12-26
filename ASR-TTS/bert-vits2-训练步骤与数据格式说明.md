# bert-vits2-训练步骤与数据格式说明

## 一. 训练和推理步骤
1. 启动数据预处理WebUI.bat, 在web界面上面操作5步
    - 第一步：生成配置文件, 完成后手动改configs/config.json的speaker列表
    - 第二步：预处理音频文件
    - 第三步：预处理标签文件
    - 第四步：生成 BERT 特征文件
    - 第五步：生成 CLAP 特征文件（我跳过了）
2. 启动训练.bat
3. 启动tensorboard.bat
4. 启动WebUI.bat

## 二. 数据格式
1. 原始的数据只有raw和esd.list
2. 其他都是生成的

## 三. 关于两个配置文件
1. config.json：模型的配置
    - 由预处理webui生成
2. config.yml：整个项目各个模块的配置
    - 手动从default_config.yml拷贝到configs/config.yml并修改
