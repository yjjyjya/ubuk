# *提示词 prompt*

- 语法
    
    - 推荐使用英语
    
    - 不同的提示词用逗号 `,` 隔开
    
    - 同一关键词混合多要素时用 `|`，例如 `red|blue hair`
    
    - 赋予提示词权重，例如 `(1girl:1.1),(long hair:1.21)`
    
    - 渐变
        
        - `a girl with long [white:yellow:16] hair`，迭代前16步为白发，之后提示词变为黄色头发
        
        - `a girl with long [white:yellow:0.5] hair`，总的迭代步数的前一半为白发，之后提示词变为黄色头发
    
    - 交替使用中括号中的提示词，例如 `[cow|horse|cat|dog] in a field`

> 逗号前后允许有 **空格** 或者 **换行**  

- 建议
    
    - 用换行将不同类的词分开，方便随时调整  
        ```
        画质词
        (masterpiece:1.331), best quality,
        描述词
        (1girl:1.1),(long hair:1.21)
        ```
    
    - 关键词控制在 75个（100个）以内
    
    - 越关键的词，越往前放
    
    - 相似的同类，放在一起
    
    - 只写必要的关键词


# *反向提示词 Negative prompt*

用文字描述你不想在图像中出现的东西  
AI 大致做法就是  
1、对图片进行去噪处理，使其看起来更像你的提示词  
2、对图片进行去噪处理，使其看起来更像你的反向提示词（无条件条件）  
3、观察这两者之间的差异，并利用它来产生一组对噪声图片的改变  
4、尝试将最终结果移向前者而远离后者  
5、一个相对比较通用的负面提示词设置  
```
lowres,bad anatomy,bad hands,text,error,missing fingers,extra digit,fewer digits,cropped,worst quality,low quality,normal quality,jpeg artifacts,signature,watermark,username,blurry,bad feet,
```


# *提示词编写 tips*

- 前摇  
    ```
    masterpiece,best quality,official art,extremely detailed CG unity 8k,wallpaper,highly detailed,illustration
    ```

- 人物  
    人设、身体、服装、饰品等等  

- 背景  
    时间、天气、季节、建筑、场地等等  

B 站搜索 **元素宝典**，有参考案例  


# *其他基础*

| 名词 | 文件名 | 路径 | 备注 |
| --- | --- | --- | --- |
| 大模型或者底模型 | ckpt | `D:\stable-diffusion-new\models\Stable-diffusion` |  |
| embeddings | pt | `D:\stable-diffusion-new\embeddings` | 可以识别某个特定的角色 |
| Hypernetwork | pt | `D:\stable-diffusion-new\models\hypernetworks` | 指定画风 |
| DreamBooth | | |
| LoRA |  | 存放路径 <br> 1、使用插件 <br> `D:\stable-diffusion-new\extensions\sd-webui-addtional-networks\models\lora`<br>2、不使用插件 <br> `D:\stable-diffusion-new\models\lora`| 一般用于角色训练 |

- 插件安装  
    github上下载后手动安装，插件存放目录 `D:\stable-diffusion-new\extensions\`


# *模型训练*

https://www.bilibili.com/video/BV1ss4y1s7ta/?spm_id_from=333.999.0.0&vd_source=f17bac2fc1c6cdda2557b1601f2c6413  

步骤  
1、复制训练图片，在 stable-diffusion 根目录下创建新的文件夹 train 用于存放训练图片。例如我现在有几十张的梵高大师画作的图片，然后创建目录 `D:\stable-diffusion-new\train\fangao`，接着在该目录下再创建文件夹 `\fangao_in` 和 `\fangao_out`，再把图片都粘贴到 `\fangao_in` 目录下  
2、执行图像预处理。注意勾选使用 deepbooru 生成文字说明  
3、创建 Dreambooth 模型，生成的文件在 `D:\stable-diffusion-new\models\dreambooth` 下  


# *参考资料*

https://www.tjsky.net/tutorial/488  
https://blog.csdn.net/m0_37857300/article/details/127445588  
https://www.imgtp.com/  