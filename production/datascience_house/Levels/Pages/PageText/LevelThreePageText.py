from production.datascience_house.Window import font


class LevelThreePageText:
    def __init__(self):
        # 欢迎玩家来到第三关的介绍文字(玩家没有答题), 告诉玩家需要答题
        self.introduction1_textLine1 = font.render("Hello, this is the messenger from the Pisces interstellar region.",
                                                   True,
                                                   (0, 0, 0))
        self.introduction1_textLine2 = font.render(
            "You are about to enter our territory, and according to our ", True, (0, 0, 0))
        self.introduction1_textLine3 = font.render(
            "communication records, you do not have the permission to enter.", True, (0, 0, 0))
        self.introduction1_textLine4 = font.render("However, since you have managed to reach this point,", True,
                                                   (0, 0, 0))
        self.introduction1_textLine5 = font.render(
            "I assume you are aware of the rules.", True,
            (0, 0, 0))
        self.introduction1_textLine6 = font.render("Would you like to take on the challenge?", True, (0, 0, 0))

        # 玩家选择答题后的提醒文字
        self.reminder1_textLine1 = font.render("You are indeed very brave. Let's begin then.", True, (0, 0, 0))
        self.reminder1_textLine2 = font.render("There are a total of 9 questions here.", True,
                                               (0, 0, 0))
        self.reminder1_textLine3 = font.render("Good luck!", True,
                                               (0, 0, 0))

        # 玩家答题失败后的提醒文字
        self.reminder2_textLine1 = font.render("I'm sorry, but you did not meet the requirements,", True,
                                                   (0, 0, 0))
        self.reminder2_textLine2 = font.render("so I cannot grant you access. Please feel free to", True,
                                                   (0, 0, 0))
        self.reminder2_textLine3 = font.render("come back and challenge again in the future.", True, (0, 0, 0))

        # 玩家答题成功后的提醒文字
        self.reminder3_textLine1 = font.render("Congratulations, you have passed the test.", True,
                                               (0, 0, 0))
        self.reminder3_textLine2 = font.render(
            "Now, let me grant you the permission to enter our interstellar",
            True, (0, 0, 0))
        self.reminder3_textLine3 = font.render(
            "region. However, I must warn you that the monsters in our", True, (0, 0, 0))
        self.reminder3_textLine4 = font.render("region are quite formidable.", True,
                                               (0, 0, 0))
        self.reminder3_textLine5 = font.render(
            "Good luck!", True, (0, 0, 0))

        # 欢迎玩家来到第三关的介绍文字(玩家已经答题)
        self.introduction2_textLine1 = font.render("Welcome to the Pisces interstellar region.", True, (0, 0, 0))
        self.introduction2_textLine2 = font.render("This was one of the first places to be invaded by the ", True,
                                                   (0, 0, 0))
        self.introduction2_textLine3 = font.render("interstellar destroyers.", True, (0, 0, 0))
        self.introduction2_textLine4 = font.render("Those destroyers have evolved and become stronger here,", True,
                                                   (0, 0, 0))
        self.introduction2_textLine5 = font.render("and we have not been able to eliminate them.", True, (0, 0, 0))
        self.introduction2_textLine6 = font.render("If you can help us defeat them, you will become a hero ", True,
                                                   (0, 0, 0))
        self.introduction2_textLine7 = font.render("of our interstellar region.", True, (0, 0, 0))
        self.introduction2_textLine8 = font.render("Good luck to you!", True, (0, 0, 0))

        # 告诉玩家如何飞机性能的变化
        self.reminder4_textLine1 = font.render(
            "Your spacecraft can now shoot bullets that automatically track the enemy.", True, (0, 0, 0))
        self.reminder4_textLine2 = font.render("Press the R key to fire them.", True, (0, 0, 0))

        # 玩家消灭本关所有敌人后的提醒文字
        self.end_textLine1 = font.render("Wow, you have eliminated all those destroyers.", True, (0, 0, 0))
        self.end_textLine2 = font.render("That's incredible! You have truly become a hero",
                                         True, (0, 0, 0))
        self.end_textLine3 = font.render("of the interstellar region.",
                                         True, (0, 0, 0))
        self.end_textLine4 = font.render("Congratulations on your achievement!", True, (0, 0, 0))

        # 指示玩家离开本关的提醒文字
        self.exit_textLine1 = font.render("Well done! The exit of the interstellar has been opened.", True, (0, 0, 0))
        self.exit_textLine2 = font.render("Please proceed to finish your journey.", True, (0, 0, 0))
