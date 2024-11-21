class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self) -> None:
        """
        Initializes
        """
        self.__status = False
        self.__muted = False
        self.__volume = self.MIN_VOLUME
        self.__channel = self.MIN_CHANNEL
        self.__store = 0
    def power(self) -> None:
        """
        Turn power on and off
        """
        self.__status = not self.__status

    def mute(self) -> None:
        """
        Mutes and Unmutes
        """
        if self.__status:
            self.__muted = not self.__muted
            if self.__muted:
                self.__store = self.__volume
                self.__volume = self.MIN_VOLUME

    def channel_up(self) -> None:
        """
        Channel Up Button
        Wraps to low channels
        """
        if self.__status:
            if self.__channel == self.MAX_CHANNEL:
                self.__channel = self.MIN_CHANNEL
            else:
                self.__channel += 1

    def channel_down(self) -> None:
        """
        Channel Down Button
        Wraps to high channels
        """
        if self.__status:
            if self.__channel == self.MIN_CHANNEL:
                self.__channel = self.MAX_CHANNEL
            else:
                self.__channel -= 1

    def volume_up(self) -> None:
        """
        Volume Up Button
        Max at 2
        """
        if self.__status:
            if self.__muted:
                self.__muted = False
                self.__volume = self.__store
                if self.__volume < self.MAX_VOLUME:
                    self.__volume += 1
            if self.__volume < self.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self) -> None:
        """
        Volume Down Button
        Min at 2
        """
        if self.__status:
            if self.__muted:
                self.__muted = False
                self.__volume = self.__store
            if self.__volume > self.MIN_VOLUME:
                self.__volume -= 1

    def __str__(self):

        power_status = "True" if self.__status else "False"
        return f"Power: {power_status}, Channel: {self.__channel}, Volume: {self.__volume}"
