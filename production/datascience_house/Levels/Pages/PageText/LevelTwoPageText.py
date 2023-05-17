from production.datascience_house.Window import font


class LevelTwoPageText:
    def __init__(self):
        # 欢迎玩家来到第三关的介绍文字(玩家没有答题), 告诉玩家需要答题
        self.introduction1_textLine1 = font.render("Hello there! You've worked hard all the way!", True, (0, 0, 0))
        self.introduction1_textLine2 = font.render("I am a Libra constellation interstellar navigator.", True,
                                                   (0, 0, 0))
        self.introduction1_textLine3 = font.render("and in charge of navigating through this constellation.", True,
                                                   (0, 0, 0))
        self.introduction1_textLine4 = font.render("You need my permission to enter the Libra constellation.", True,
                                                   (0, 0, 0))
        self.introduction1_textLine5 = font.render("According to regulations, you need to answer a few questions.",
                                                   True,
                                                   (0, 0, 0))
        self.introduction1_textLine6 = font.render("Do you have the courage to accept the challenge?", True, (0, 0, 0))

        # 玩家选择答题后的提醒文字
        self.reminder1_textLine1 = font.render("You're so brave, I'm rooting for you!", True, (0, 0, 0))
        self.reminder1_textLine2 = font.render("There are 6 questions in total.", True, (0, 0, 0))
        self.reminder1_textLine3 = font.render("If you answer 70% correctly, you win! Good luck!", True, (0, 0, 0))

        # 玩家答题失败后的提醒文字
        self.reminder2_textLine1 = font.render("I'm sorry, but you didn't achieve a 70% accuracy rate,", True,
                                               (0, 0, 0))
        self.reminder2_textLine2 = font.render("so I cannot grant you access to our interstellar network.", True,
                                               (0, 0, 0))
        self.reminder2_textLine3 = font.render("Don't be discouraged, though.", True, (0, 0, 0))
        self.reminder2_textLine4 = font.render("You're welcome to come back and try again.", True, (0, 0, 0))

        # 玩家答题成功后的提醒文字
        self.reminder3_textLine1 = font.render("You have achieved a 70% accuracy rate, that's great!", True, (0, 0, 0))
        self.reminder3_textLine2 = font.render("Now I will grant you the passage to the Libra constellation", True,
                                               (0, 0, 0))
        self.reminder3_textLine3 = font.render("interstellar, and wish you a smooth journey.", True, (0, 0, 0))

        # 欢迎玩家来到第二关的介绍文字(玩家已经答题)
        self.introduction2_textLine1 = font.render("Welcome to the interstellar of Libra constellation.", True,
                                                   (0, 0, 0))
        self.introduction2_textLine2 = font.render(
            "It used to be a beautiful place, but since some interstellar raiders", True, (0, 0, 0))
        self.introduction2_textLine3 = font.render("came, they have destroyed the ecology here. I hope you can use ",
                                                   True,
                                                   (0, 0, 0))
        self.introduction2_textLine4 = font.render("your power to help us eliminate these annoying invaders.", True,
                                                   (0, 0, 0))
        self.introduction2_textLine5 = font.render("If you can do it, I would be very grateful. Good luck!", True,
                                                   (0, 0, 0))

        # 告诉玩家如何飞机性能的变化
        self.reminder4_textLine = font.render("You now have faster movement speed and stronger firepower.", True,
                                              (0, 0, 0))

        # 玩家消灭本关所有敌人后的提醒文字
        self.end_textLine1 = font.render("Thank you for helping us eliminate these monsters.", True, (0, 0, 0))
        self.end_textLine2 = font.render("You're really amazing! However, I still have a gift for you.", True,
                                         (0, 0, 0))
        self.end_textLine3 = font.render("Here's a crystal from our interstellar world. It can enable", True,
                                         (0, 0, 0))
        self.end_textLine4 = font.render("your spacecraft to shoot bullets that automatically track the enemy.", True,
                                         (0, 0, 0))
        self.end_textLine5 = font.render("I wish you a pleasant journey through the stars.", True, (0, 0, 0))

        # 指示玩家离开本关的提醒文字
        self.exit_textLine1 = font.render("Well done! The exit of the interstellar has been opened.", True, (0, 0, 0))
        self.exit_textLine2 = font.render("Please proceed to the next interstellar destination.", True, (0, 0, 0))
