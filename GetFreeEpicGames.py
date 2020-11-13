# -*- coding: utf-8 -*-#
# -------------------------------------------------------------------------------
# Name         :  GetFreeEpicGames
# Description  :  免费获取epic每周的免费游戏
# Author       :  skymoon9406@gmail.com
# Date         :  2020/11/13
# -------------------------------------------------------------------------------
# --------------------------------设置工作路径------------------------------------#
import sys
import os

CURRENT_PATH = os.path.split(os.path.realpath(__file__))[0]
PARENT_PATH = os.path.dirname(CURRENT_PATH)
sys.path.append(CURRENT_PATH)
sys.path.append(PARENT_PATH)
# --------------------------------导入模块和包------------------------------------#
import requests


# noinspection PyBroadException
class GetFreeEpicGames:
    def __init__(self):
        pass

    @staticmethod
    def connect_to_url(url):
        headers = {
            "referer": "https://www.epicgames.com/",
            "user-agent":  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) "
                           "Chrome/86.0.4240.111 Safari/537.36"
        }
        try:
            res = requests.get(url)
            return res.text
        except Exception:
            pass

    def get_free_game_info(self):
        free_games_url = "https://store-site-backend-static.ak.epicgames.com/" \
                         "freeGamesPromotions?locale=zh-CN&country=CN&allowCountries=CN"
        print(self.connect_to_url(free_games_url))

    def run_task(self):
        self.get_free_game_info()


if __name__ == '__main__':
    GetFreeEpicGames().run_task()
