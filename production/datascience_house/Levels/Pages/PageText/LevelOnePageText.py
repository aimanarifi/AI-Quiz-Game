from production.datascience_house.Window import font


class LevelOnePageText:
    def __init__(self):
        # 欢迎玩家来到第一关的介绍文字
        self.introduction_textLine1 = font.render(
            "Welcome to Scorpio Interstellar. I am the messenger here. We have been",
            True, (0, 0, 0))
        self.introduction_textLine2 = font.render(
            "attacked by some interstellar disruptors who spread viruses to disrupt",
            True, (0, 0, 0))
        self.introduction_textLine3 = font.render(
            "the ecology of this interstellar system. If you can help us eliminate them,", True, (0, 0, 0))
        self.introduction_textLine4 = font.render(" I would be very grateful. Good luck!", True, (0, 0, 0))

        # 告诉玩家如何操作飞机的提醒文字
        self.reminder_textLine1 = font.render("Press up, down, left or right to move your plane.", True, (0, 0, 0))
        self.reminder_textLine2 = font.render("Press w to fire.", True, (0, 0, 0))

        # 玩家消灭本关所有敌人后显示的文字
        self.end_textLine1 = font.render("Wow, it's incredible that you were able to eliminate those monsters.",
                                               True,
                                               (0, 0, 0))
        self.end_textLine2 = font.render(
            "To thank you for your help, let me give you some crystals from our interstellar", True, (0, 0, 0))
        self.end_textLine3 = font.render(
            "system. They can make your spacecraft faster and also enhance your weapons.", True, (0, 0, 0))
        self.end_textLine4 = font.render("I wish you a pleasant journey.", True, (0, 0, 0))

        # 指示玩家离开本关的文字
        self.exit_textLine1 = font.render("Well done! The exit of the interstellar has been opened.", True,
                                               (0, 0, 0))
        self.exit_textLine2 = font.render("Please proceed to the next interstellar destination.", True, (0, 0, 0))
