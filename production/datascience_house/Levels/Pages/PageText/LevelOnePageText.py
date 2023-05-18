"""
Last modified: 18/05/2023
Written by Zhongjie Huang
"""
from production.datascience_house.Window import font


class LevelOnePageText:
    def __init__(self):
        # Introduction text to welcome players to the level 1
        self.introduction_textLine1 = font.render(
            "Welcome to Scorpio Interstellar. I am the messenger here.",
            True, (0, 0, 0))
        self.introduction_textLine2 = font.render(
            "We have been attacked by some interstellar disruptors who",
            True, (0, 0, 0))
        self.introduction_textLine3 = font.render(
            "spread viruses to disrupt the ecology of this interstellar system.", True, (0, 0, 0))
        self.introduction_textLine4 = font.render("If you can help us eliminate them, I would be very grateful.", True,
                                                  (0, 0, 0))
        self.introduction_textLine5 = font.render("Good luck!", True, (0, 0, 0))

        # Reminder text telling the player how to operate the aircraft
        self.reminder_textLine1 = font.render("Press up, down, left or right to move your plane.", True, (0, 0, 0))
        self.reminder_textLine2 = font.render("Press w to fire.", True, (0, 0, 0))

        # The text displayed after the player has destroyed all enemies in this level
        self.end_textLine1 = font.render("Wow, it's incredible that you were able to eliminate those monsters.",
                                         True,
                                         (0, 0, 0))
        self.end_textLine2 = font.render(
            "To thank you for your help, let me give you some crystals from our", True, (0, 0, 0))
        self.end_textLine3 = font.render(
            "interstellar system. They can make your spacecraft faster and also", True, (0, 0, 0))
        self.end_textLine4 = font.render("enhance your weapons.", True, (0, 0, 0))
        self.end_textLine5 = font.render("I wish you a pleasant journey.", True, (0, 0, 0))

        # The text instructing the player to leave the level
        self.exit_textLine1 = font.render("Well done! The exit of the interstellar has been opened.", True,
                                          (0, 0, 0))
        self.exit_textLine2 = font.render("Please proceed to the next interstellar destination.", True, (0, 0, 0))
