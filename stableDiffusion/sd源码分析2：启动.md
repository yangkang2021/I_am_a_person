# sd源码分析2：启动
> webui.bat/webui.sh --> launch.py --> webui.py --> modules/ui.py

## 一. 启动命令
1. 普通启动
```
./webui.sh 或者 ./webui.bat
```
2. 启动后台运行
```
nohup ./webui.sh --server-name=0.0.0.0 --share --theme dark --api &  > ./nohup.out 2&>1
```
3. 跳过环境配置，直接python启动
```
C:\Users\MoMing\Desktop\sd-webui-aki\sd-webui-aki-v4\py310\python.exe C:\Users\MoMing\Desktop\sd-webui-aki\sd-webui-aki-v4\launch.py --theme dark --xformers --api --autolaunch
```
记得把根python加入到path：
```
os.environ['PATH'] = 'C:/Anaconda3;C:/Anaconda3/Library/mingw-w64/bin;C:/Anaconda3/Library/usr/bin;C:/Anaconda3/Library/bin;C:/Anaconda3/Scripts;C:/Anaconda3/bin;C:/Anaconda3/condabin;' + os.environ['PATH']
```

## 二. 启动过程

1. webui.bat：创建venv虚拟环境，然后启动launch.py并传递所有参数。
2. launch.py：
   - pip安装依赖 + git下载代码
   - 启动webui.py的webui或者api_only
3. webui.py
   - webui.webui()
      - initialize：加载：扩展、模型等等
      - 启动gradio：
      - ```
        shared.demo = modules.ui.create_ui()
        app, local_url, share_url = shared.demo.launch(...)
        wait_on_server(shared.demo)
        ```
4. modules/ui.py：进入ui界面
