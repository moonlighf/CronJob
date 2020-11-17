## epic_game
&#8195;主要是获取Epic游戏商城相关的定时任务

### [1.GetFreeEpicGames](https://github.com/moonlighf/CronJob/tree/main/epic_game)
&#8195;获取Epic的[每周免费游戏资讯](https://www.epicgames.com/store/en-US/free-games)，并实现游戏的自动领取入库 **（默认关闭，如果开启推荐用小号，防止垃圾游戏污染游戏库）**

![image](https://github.com/moonlighf/CronJob/tree/main/epic_game/images/epic.png)
#### Secrets设定参数解释
- IS_MOBILE_NOTICE：是否选用Bark统一推送（yes/no）
- BARK_API：自己的Bark的API地址
#### 更新日志
- 2020.11.13 更新实现Bark在手机端的推送
#### TODO
- [x] 实现免费游戏的信息的获取和推送（2020.11.13）
- [ ] 实现Epic的自动登录和游戏的自动领取