## CronJob
&#8195;主要是一些自用的有趣的定时任务，部署在github action

### [1.GetFreeEpicGames](https://github.com/moonlighf/CronJob/tree/main/epic_game)
&#8195;获取Epic的每周免费游戏资讯，并实现游戏的自动领取入库 **（默认关闭，如果开启推荐用小号，防止垃圾游戏污染游戏库）**
#### Secrets设定参数解释
- IS_MOBILE_NOTICE：是否选用Bark统一推送（yes/no）
- BARK_API：自己的Bark的API地址
#### 更新日志
- 2020.11.13 更新实现Bark在手机端的推送
#### TODO
- [] 实现Epic的自动登录和游戏的自动领取