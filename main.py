#Remote Control with Alpay 10/04/21

class Remote():

    def __init__(self, tv_Power = "Off", tv_Sound = 0, channel_list = ["BBC"], channel = "BBC", deleted_channel = 0):

        self.tv_Power = tv_Power
        self.tv_Sound = tv_Sound
        self.channel = channel
        self.channel_list = channel_list
        self.deleted_channel = deleted_channel

    def tv_status_on(self, seson):

        self.tv_Power = seson

        if(self.tv_Power == "On"):

            print("TV is switched on.")

    def tv_status_off(self, sesoff):

        self.tv_Power = sesoff

        if(self.tv_Power == "Off"):

            print("TV is switched off.")

    def tv_Soundd(self):

        sound_status = input("Do you want to change the level of Volume? Click > or <")

        if(sound_status == ">"):

            if (self.tv_Sound == 15):

                print("TV sound is at its highest level which is 15")

            else:

                self.tv_Sound = self.tv_Sound + 1

                print("TV sound = {}".format(self.tv_Sound))

        elif (sound_status == "<"):

            if (self.tv_Sound == 0):

                print("TV sound is at its lowest level")

            else:

                self.tv_Sound = self.tv_Sound - 1
                print("TV sound = {}".format(self.tv_Sound))

    def add_channel_to_list(self):

        self.channel = input("A new channel name:")

        print("New channel added.")

        self.channel_list.append(self.channel)

        print(self.channel_list)

    def delete_channel_to_list(self):

        self.deleted_channel = input("Name the channel you would like to delete.")

        i = 0

        for element in self.channel_list:

            if(self.deleted_channel == self.channel_list[i]):

                self.channel_list[i].pop
                print("{} named channel just removed from channel list.".format(self.deleted_channel))
                print("New Channel List is:{}".format(self.channel_list))

            i = i + 1

newly_class = Remote()

print("If you would like to switch on/off TV, Click 3 Text = On / Off")
print("If you would like to level up/down the volume, Click 2 Text = > / <")
print("If you would like to add a new channel, Click 1 Text = Channel Name")
print("If you want to end the programme, Click 4 ")

while True:

    answer = input("Which function would you like to start with? :")

    if(answer == "1"):

        print("Do you want to add a new channel?")
        newly_class.add_channel_to_list()

    elif(answer == "2"):

        print("Do you want to change the volume?")
        newly_class.tv_Soundd()

    elif(answer == "3"):

        yanit = input("Do you want to switch on/off TV?")

        if(yanit == "On"):

            newly_class.tv_status_on(yanit)

        elif(yanit == "Off"):

            newly_class.tv_status_off(yanit)

    elif (answer == "4"):

        print("Programme is turned off.")
        break







