from production.datascience_house.Window import font


class MainPageText:
    def __init__(self):
        # 欢迎玩家来到"数据科学房屋"(主页)的介绍文字
        self.introduction_textLine1 = font.render(
            "Welcome to the Data Science House. Begin your fantastic journey now!",
            True, (0, 0, 0))
        self.introduction_textLine2 = font.render(
            "Here, you will play the role of an interstellar traveler piloting a fighter jet,", True, (0, 0, 0))
        self.introduction_textLine3 = font.render(
            "exploring different galaxies and helping the intergalactic steward eliminate", True, (0, 0, 0))
        self.introduction_textLine4 = font.render("space destroyers.", True, (0, 0, 0))
        self.introduction_textLine5 = font.render("Begin your fantastic journey now!", True, (0, 0, 0))
