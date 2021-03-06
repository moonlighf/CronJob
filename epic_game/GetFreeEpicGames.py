# -*- coding: utf-8 -*-#
# -------------------------------------------------------------------------------
# Name         :  GetFreeEpicGames
# Description  :  免费获取epic每周的免费游戏
# Author       :  skymoon9406@gmail.com
# Date         :  2020/11/13
# -------------------------------------------------------------------------------
# --------------------------------设置工作路径------------------------------------#
import os
import sys

CURRENT_PATH = os.path.split(os.path.realpath(__file__))[0]
PARENT_PATH = os.path.dirname(CURRENT_PATH)
sys.path.append(CURRENT_PATH)
sys.path.append(PARENT_PATH)
# --------------------------------导入模块和包------------------------------------#
import json
import requests
from retrying import retry
from datetime import datetime, timedelta


# noinspection PyBroadException
class GetFreeEpicGames:
    def __init__(self):
        self.games_info = {}

    @staticmethod
    def convert_time_to_cn_time(old_time):
        standard_old_time = old_time.replace("T", " ").replace("Z", "").replace(".000", "")
        standard_cn_time = (datetime.strptime(standard_old_time, "%Y-%m-%d %H:%M:%S") + timedelta(hours=20)).strftime(
            "%Y.%m.%d %H:%M")
        return standard_cn_time

    @retry(stop_max_attempt_number=3, wait_random_min=3000, wait_random_max=4000)
    def connect_to_url(self, url):
        headers = {
            "referer": "https://www.epicgames.com/",
            "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/86.0.4240.111 Safari/537.36"
        }
        res = requests.get(url, headers=headers)
        if res.status_code == 200 and len(res.text) > 200:
            return res.text
        else:
            raise ConnectionError

    def parse_and_get_game_name(self, res_text):
        try:
            json_data = json.loads(res_text)
        except json.decoder.JSONDecodeError:
            print("----------获取免费游戏名称错误----------")
            sys.exit(-1)
        # 解析
        games = json_data["data"]["Catalog"]["searchStore"]["elements"]
        print("----------开始获取最近的免费游戏名称----------")
        for game in games:
            game_tile = game["title"]
            # 区分正在限免和非正在限免
            promotional_games = game["promotions"]["promotionalOffers"]
            if len(promotional_games) == 0:
                game_start_time = game["promotions"]["upcomingPromotionalOffers"][0]["promotionalOffers"][0][
                    "startDate"]
                game_end_time = game["promotions"]["upcomingPromotionalOffers"][0]["promotionalOffers"][0]["endDate"]
            else:
                game_start_time = game["promotions"]["promotionalOffers"][0]["promotionalOffers"][0]["startDate"]
                game_end_time = game["promotions"]["promotionalOffers"][0]["promotionalOffers"][0]["endDate"]
            # 时间处理为CN时间
            start_cn_time = self.convert_time_to_cn_time(game_start_time)
            end_cn_time = self.convert_time_to_cn_time(game_end_time)
            self.games_info[game_tile] = {
                "start_time": start_cn_time,
                "end_time": end_cn_time
            }
            print('【{}】\n【游戏开始领取时间】{}\n【游戏结束领取时间】{}\n'.format(game_tile, start_cn_time, end_cn_time))

    def get_free_game_info(self):
        free_games_url = "https://store-site-backend-static.ak.epicgames.com/" \
                         "freeGamesPromotions?locale=zh-CN&country=CN&allowCountries=CN"
        try:
            all_free_game_res_text = self.connect_to_url(free_games_url)
            self.parse_and_get_game_name(all_free_game_res_text)
        except ConnectionError:
            pass

    def bark_notice(self, bark_api):
        notice_text = bark_api + '❤EPIC本周免费游戏领取:/'
        for game_title, game_info in self.games_info.items():
            notice_text = notice_text + '☎【{}】\n\t开始时间：{}\n\t结束时间：{}\n'.format(
                game_title, game_info["start_time"], game_info["end_time"])
        # 去掉最后一个多余的\n
        notice_text = notice_text[:-1] + '?url=https://www.epicgames.com/store/zh-CN/free-games'
        requests.get(notice_text)

    def run_task(self, is_bark_notice, bark_api):
        # 获取免费游戏信息
        self.get_free_game_info()
        # 用户推送信息
        if is_bark_notice == "yes":
            print("----------本次启用Bark推送----------")
            self.bark_notice(bark_api)


if __name__ == '__main__':
    # _is_bark_notice = 'yes'
    # _bark_api = ""
    _is_bark_notice = os.environ["IS_MOBILE_NOTICE"]
    _bark_api = os.environ["BARK_API"]
    GetFreeEpicGames().run_task(_is_bark_notice, _bark_api)
