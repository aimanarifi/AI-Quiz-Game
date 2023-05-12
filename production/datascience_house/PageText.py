"""
Last modified: 03/05/2023
Written by Zhongjie Huang

这个类定义了游戏的四个页面(主页, 第一关, 第二关和第三关)中所有要展示的文字
"""
import pygame

text_box_position_x = 290
text_box_position_y = 270
text_color = (0, 0, 0)
font = pygame.font.Font(None, 35)


class TextMainPage:
    def __init__(self):
        # 欢迎玩家来到"数据科学房屋"(主页)的介绍文字
        self.welcome_textLine1 = font.render("Welcome to the Data Science House. Begin your fantastic journey now!",
                                             True, text_color)
        self.welcome_textLine2 = font.render(
            "Here, you will play the role of an interstellar traveler piloting a fighter jet,", True, text_color)
        self.welcome_textLine3 = font.render(
            "exploring different galaxies and helping the intergalactic steward eliminate", True, text_color)
        self.welcome_textLine4 = font.render("space destroyers.", True, text_color)
        self.welcome_textLine5 = font.render("Begin your fantastic journey now!", True, text_color)


class TextLevelOnePage:
    def __init__(self):
        # 欢迎玩家来到第一关的介绍文字
        self.welcome_textLine1 = font.render("Welcome to Scorpio Interstellar. I am the messenger here. We have been",
                                             True, text_color)
        self.welcome_textLine2 = font.render("attacked by some interstellar disruptors who spread viruses to disrupt",
                                             True, text_color)
        self.welcome_textLine3 = font.render(
            "the ecology of this interstellar system. If you can help us eliminate them,", True, text_color)
        self.welcome_textLine4 = font.render(" I would be very grateful. Good luck!", True, text_color)

        self.instruction_textLine1 = font.render("Press up, down, left or right to move your plane.", True, text_color)
        self.instruction_textLine2 = font.render("Press w to fire.", True, text_color)

        # 告诉玩家如何操作飞机的提醒文字
        self.end_textLine1 = font.render("Wow, it's incredible that you were able to eliminate those monsters.", True,
                                         text_color)
        self.end_textLine2 = font.render(
            "To thank you for your help, let me give you some crystals from our interstellar", True, text_color)

        # 玩家消灭本关所有敌人后的提醒文字
        self.end_textLine3 = font.render("system. They can make your spacecraft faster and also enhance your weapons.",
                                         True, text_color)
        self.end_textLine4 = font.render("I wish you a pleasant journey.", True, text_color)

        # 指示玩家离开本关的提醒文字
        self.exit_textLine1 = font.render("Well done! The exit of the interstellar has been opened.", True, text_color)
        self.exit_textLine2 = font.render("Please proceed to the next interstellar destination.", True, text_color)


class TextLevelTwoPage:
    def __init__(self):
        # 欢迎玩家来到第三关的介绍文字(玩家没有答题), 告诉玩家需要答题
        self.welcome1_textLine1 = font.render("Hello there! You've worked hard all the way!", True, text_color)
        self.welcome1_textLine2 = font.render("I am a Libra constellation interstellar navigator.", True, text_color)
        self.welcome1_textLine3 = font.render("and in charge of navigating through this constellation.", True,
                                              text_color)
        self.welcome1_textLine4 = font.render("You need my permission to enter the Libra constellation.", True,
                                              text_color)
        self.welcome1_textLine5 = font.render("According to regulations, you need to answer a few questions.", True,
                                              text_color)
        self.welcome1_textLine6 = font.render("Do you have the courage to accept the challenge?", True, text_color)

        # 玩家选择答题后的提醒文字
        self.introduction1_textLine1 = font.render("You're so brave, I'm rooting for you!", True, text_color)
        self.introduction1_textLine2 = font.render("There are 6 questions in total.", True, text_color)
        self.introduction1_textLine3 = font.render("If you answer 70% correctly, you win! Good luck!", True, text_color)

        # 玩家答题失败后的提醒文字
        self.introduction2_textLine1 = font.render("I'm sorry, but you didn't achieve a 70% accuracy rate,", True,
                                                   text_color)
        self.introduction2_textLine2 = font.render("so I cannot grant you access to our interstellar network.", True,
                                                   text_color)
        self.introduction2_textLine3 = font.render("Don't be discouraged, though.", True, text_color)
        self.introduction2_textLine4 = font.render("You're welcome to come back and try again.", True, text_color)

        # 玩家答题成功后的提现文字
        self.welcome2_textLine1 = font.render("You have achieved a 70% accuracy rate, that's great!", True, text_color)
        self.welcome2_textLine2 = font.render("Now I will grant you the passage to the Libra constellation", True,
                                              text_color)
        self.welcome2_textLine3 = font.render("interstellar, and wish you a smooth journey.", True, text_color)

        # 欢迎玩家来到第二关的欢迎文字(玩家已经答题)
        self.welcome3_textLine1 = font.render("Welcome to the interstellar of Libra constellation.", True, text_color)
        self.welcome3_textLine2 = font.render("It used to be a beautiful place, but since some interstellar raiders",
                                              True, text_color)
        self.welcome3_textLine3 = font.render("came, they have destroyed the ecology here. I hope you can use ", True,
                                              text_color)
        self.welcome3_textLine4 = font.render("your power to help us eliminate these annoying invaders.", True,
                                              text_color)
        self.welcome3_textLine5 = font.render("If you can do it, I would be very grateful. Good luck!", True,
                                              text_color)

        # 告诉玩家如何飞机性能的变化
        self.instruction_textLine = font.render("You now have faster movement speed and stronger firepower.", True,
                                                text_color)

        # 玩家消灭本关所有敌人后的提醒文字
        self.end_textLine1 = font.render("Thank you for helping us eliminate these monsters.", True, text_color)
        self.end_textLine2 = font.render("You're really amazing! However, I still have a gift for you.", True,
                                         text_color)
        self.end_textLine3 = font.render("Here's a crystal from our interstellar world. It can enable", True,
                                         text_color)
        self.end_textLine4 = font.render("your spacecraft to shoot bullets that automatically track the enemy.", True,
                                         text_color)
        self.end_textLine5 = font.render("I wish you a pleasant journey through the stars.", True, text_color)

        # 指示玩家离开本关的提醒文字
        self.exit_textLine1 = font.render("Well done! The exit of the interstellar has been opened.", True, text_color)
        self.exit_textLine2 = font.render("Please proceed to the next interstellar destination.", True, text_color)


class TextLevelThreePage:
    def __init__(self):
        # 欢迎玩家来到第三关的介绍文字(玩家没有答题), 告诉玩家需要答题
        self.welcome1_textLine1 = font.render("Hello, this is the messenger from the Pisces interstellar region.", True,
                                              text_color)
        self.welcome1_textLine2 = font.render(
            "You are about to enter our territory, and according to our communication records,", True, text_color)
        self.welcome1_textLine3 = font.render(
            "you do not have the permission to enter. However, since you have managed to", True, text_color)
        self.welcome1_textLine4 = font.render("reach this point, I assume you are aware of the rules.", True,
                                              text_color)
        self.welcome1_textLine5 = font.render("Would you like to take on the challenge?", True, text_color)

        # 玩家选择答题后的提醒文字
        self.introduction1_textLine1 = font.render("You are indeed very brave. Let's begin then.", True, text_color)
        self.introduction1_textLine2 = font.render("There are a total of 9 questions here. Good luck!", True,
                                                   text_color)

        # 玩家答题失败后的提醒文字
        self.introduction2_textLine1 = font.render("I'm sorry, but you did not meet the requirements,", True,
                                                   text_color)
        self.introduction2_textLine2 = font.render("so I cannot grant you access. Please feel free to come", True,
                                                   text_color)
        self.introduction2_textLine3 = font.render("back and challenge again in the future.", True, text_color)

        # 玩家答题成功后的提现文字
        self.welcome_afterQuestionAnswered_textLine1 = font.render("Congratulations, you have passed the test.", True,
                                                                   text_color)
        self.welcome_afterQuestionAnswered_textLine2 = font.render(
            "Now, let me grant you the permission to enter our interstellar",
            True, text_color)
        self.welcome_afterQuestionAnswered_textLine3 = font.render(
            "region. However, I must warn you that the monsters in our region", True, text_color)
        self.welcome_afterQuestionAnswered_textLine4 = font.render("are quite formidable.", True,
                                                                   text_color)
        self.welcome_afterQuestionAnswered_textLine5 = font.render(
            "I wish you good luck and smooth sailing on your journey.", True, text_color)

        # 欢迎玩家来到第三关的欢迎文字(玩家已经答题)
        self.welcome3_textLine1 = font.render("Welcome to the Pisces interstellar region.", True, text_color)
        self.welcome3_textLine2 = font.render(
            "This was one of the first places to be invaded by the interstellar destroyers.", True, text_color)
        self.welcome3_textLine3 = font.render(
            "Those destroyers have evolved and become stronger here, and we have not been able to eliminate them.",
            True, text_color)
        self.welcome3_textLine4 = font.render(
            "If you can help us defeat them, you will become a hero of our interstellar region.", True, text_color)
        self.welcome3_textLine5 = font.render("Good luck to you!", True, text_color)

        # 告诉玩家如何飞机性能的变化
        self.instruction_textLine1 = font.render(
            "Your spacecraft can now shoot bullets that automatically track the enemy.", True, text_color)
        self.instruction_textLine2 = font.render("Press the R key to fire them.", True, text_color)

        # 玩家消灭本关所有敌人后的提醒文字
        self.end_textLine1 = font.render("Wow, you have eliminated all those destroyers.", True, text_color)
        self.end_textLine2 = font.render("That's incredible! You have truly become a hero of the interstellar region.",
                                         True, text_color)
        self.end_textLine3 = font.render("Congratulations on your achievement!", True, text_color)

        # 指示玩家离开本关的提醒文字
        self.exit_textLine1 = font.render("Well done! The exit of the interstellar has been opened.", True, text_color)
        self.exit_textLine2 = font.render("Please proceed to the final destination.", True, text_color)
