# 实战Scrapy加Splash爬取js加载网站(天眼查)

## 目标
- 获取某个企业在天眼查上展示的文本信息

## 环境
- python3.6
- docker and splash
- scrapy

## 原理
- splash集成webkit,then具有处理js的能力。并且使用Twisted框架实现，故与scrapy结合很好(`都是异步非阻塞`)，哪怕是分布式扩展方面。利用html解析库beautiful4进行解析出结构化数据、

## 过程
- 使用Docker运行Splash服务
    - [install docker](https://docs.docker.com/v17.12/)
    - [install splash and start it](http://splash.readthedocs.io/en/latest/install.html)
        ```
            $ docker pull scrapinghub/splash
            $ docker run -p 5023:5023 -p 8050:8050 -p 8051:8051 scrapinghub/splash #可以访问 http://localhost:8050/
            $ docker-machine ip default # 还得运行splash的IP地址，端口默认为8050,这个地址:端口在配置文件setting.py里会使用到。
        ```

- 安装scrapy，其他第三方库, 推荐使用virtualenv虚拟环境
    - `pip3 install -r requirements.txt`

- 开始爬取
    - `scrapy crawl tianyancha_spider -s LOG_FILE=scrapy.log`
