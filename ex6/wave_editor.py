import wave_helper
import math
import os
import copy

CHOOSE = "Please choose:"
CHANGE = "1 - Change wav file"
UNITE = "2 - Unit two wav files"
COMPOSE = "3 - Compose melody in format suitable for wav file"
EXIT = "4 - Exit"
BACKWARDS = "1 - Backward"
SPEED_UP = "2 - Speed up"
SLOW_DOWN = "3 - Slow down"
VOL_UP = "4 - Volume up"
VOL_DOWN = "5 - Volume down"
LOW_PASS_FILTER = "6 - Low pass filter"
INVALID_FILE = "The file is invalid"
INVALID_CHOICE = "Invalid choice, please choose again"
DUMMY_FRAME_RATE = 999  # used when passing an empty audio data, no real usage
AUDIO_SAVE = "1 - Save audio"
AUDIO_CHANGE = "2 - Change audio"
INVALID_SAVE = "Unable to save"
INVALID_NUM_OF_FILES = "Number of files invalid"
MAX_VOL = 32767
MIN_VOL = -32768
CHANGE_VALUE = 1.2
SAMPLES_PER_TIME = 125
COMPOSING_SAMPLE_RATE = 2000
NOTE_TO_FREQUENCY = {"A": 440, "B": 494, "C": 523, "D": 587, "E": 659,
                     "F": 698, "G": 784}


def menu():
    """"a function that presents to user the main menu"""
    stop = False
    while not stop:
        print(CHOOSE + "\n" + CHANGE + "\n" + UNITE + "\n" + COMPOSE + "\n" +
              EXIT + "\n")
        user_choice = input()  # the user chooses what to do with wav file
        if user_choice == "1":
            change_wav_file(DUMMY_FRAME_RATE, [])  # this input means we
            #  should read the data from file specified by the user(first time
            #  reaching this menu)
        elif user_choice == "2":
            unite_files()
        elif user_choice == "3":
            compose_melody()
        elif user_choice == "4":  # exit the program
            stop = True
        else:  # user's choice is invalid
            print(INVALID_CHOICE)  # and start loop again



def change_wav_file(input_frame_rate, input_audio_data):
    """a function that presents to user the change wave file menu"""
    if input_audio_data:  # not the first time changing audio
        frame_rate = input_frame_rate
        audio_data = input_audio_data
    else:  # first time seeing this menu
        while True:
            print("Please write the name of the file you would like to read:")
            file = input()
            loaded_file = wave_helper.load_wave(file)
            if loaded_file == -1:
                print(INVALID_FILE)  # and start loop again
            else:
                frame_rate, audio_data = loaded_file
                break  # file is valid, we can get out of the loop

    choice_valid = False
    while not choice_valid:
        print(CHOOSE + "\n" + BACKWARDS + "\n" + SPEED_UP + "\n" + SLOW_DOWN +
              "\n" + VOL_UP + "\n" + VOL_DOWN + "\n" + LOW_PASS_FILTER)
        user_choice = input()  # user chooses the change he would like to make
        if user_choice == "1":
            choice_valid = True
            changed_audio = backwards_audio(audio_data)
        elif user_choice == "2":
            choice_valid = True
            changed_audio = speed_up_audio(audio_data)
        elif user_choice == "3":
            choice_valid = True
            changed_audio = slow_down_audio(audio_data)
        elif user_choice == "4":
            choice_valid = True
            changed_audio = volume_up(audio_data)
        elif user_choice == "5":
            choice_valid = True
            changed_audio = volume_down(audio_data)
        elif user_choice == "6":
            choice_valid = True
            changed_audio = low_pass_filter(audio_data)
        else:
            print(INVALID_CHOICE)  # and start loop again

    transition_menu(frame_rate, changed_audio)


def backwards_audio(audio_data):
    """a function that gets list of audio data and returns the list
    backwards"""
    new_audio_data = copy.deepcopy(audio_data)
    new_audio_data.reverse()  # reversing the list
    return new_audio_data


def speed_up_audio(audio_data):
    """a function that gets list of audio data and speeds up the audio 2 times
    more"""
    new_audio_data =[]
    for i in range(0, len(audio_data), 2):  # traversing list and skipping
        # even indices
        new_audio_data.append(audio_data[i])
    return new_audio_data


def slow_down_audio(audio_data):
    """a function that gets list of audio data and slows down the audio 2
    times more"""
    new_audio_data = copy.deepcopy(audio_data)
    i=0
    while i < (len(new_audio_data)-1):
        left = int((new_audio_data[i][0]+new_audio_data[i+1][0])/ 2)
        right = int((new_audio_data[i][1] + new_audio_data[i+1][1])/2)
        new_audio_data.insert(i+1, [left, right])
        i += 2  # make sure we reach next wanted index
    return new_audio_data


def multiply_pair(i):
    """a helper function that gets list of two int values and multiplies
    each one by 1.2"""
    left = int(i[0] * CHANGE_VALUE)
    right = int(i[1] * CHANGE_VALUE)
    #  these next lines make sure the range will be between max volume,
    # and min volume
    if left < MIN_VOL:
        left = MIN_VOL
    elif left > MAX_VOL:
        left = MAX_VOL
    if right < MIN_VOL:
        right = MIN_VOL
    elif right > MAX_VOL:
        right = MAX_VOL
    return left, right


def volume_up(audio_data):
    """a function that gets list of audio data and turns the volume up"""
    new_audio_data = []
    for i in audio_data:
        left, right = multiply_pair(i)
        new_audio_data.append([left, right])
    return new_audio_data


def volume_down(audio_data):
    """a function that gets list of audio data and turns the volume down"""
    new_audio_data = []
    for i in audio_data:
        left = int(i[0] / CHANGE_VALUE)
        right = int(i[1] / CHANGE_VALUE)
        new_audio_data.append([left, right])
    return new_audio_data


def low_pass_filter(audio_data):
    """a function that gets list of data audio and returns a low pass filter
     data audio list"""
    if len(audio_data) < 2:  # low pass filter not possible
        return audio_data
    else:
        new_audio_data = []
        # these next two lines take care of first index
        left = int((audio_data[0][0] + audio_data[1][0]) / 2)
        right = int((audio_data[0][1] + audio_data[1][1]) / 2)
        new_audio_data.append([left, right])
        for i in range(1, (len(audio_data) - 1)):
            left = int((audio_data[i - 1][0] + audio_data[i][0] +
                        audio_data[i + 1][0]) / 3)
            right = int((audio_data[i - 1][1] + audio_data[i][1] +
                        audio_data[i + 1][1]) / 3)
            new_audio_data.append([left, right])
        # these next two lines take care of last index
        left = int((audio_data[-2][0] + audio_data[-1][0]) / 2)
        right = int((audio_data[-2][1] + audio_data[-1][1]) / 2)
        new_audio_data.append([left, right])
        return new_audio_data


def unite_files():
    """a function that presents to user unite files menu"""
    while True:
        print("Please write the names of the two files you would like to"
              " unite: ")
        two_files = input()
        lst_files = two_files.split()
        if len(lst_files) != 2:
            print(INVALID_NUM_OF_FILES)
            continue  # start the loop again
        file1 = lst_files[0]  # means the user wrote 2 file names, as needed
        file2 = lst_files[1]
        loaded_file1 = wave_helper.load_wave(file1)
        loaded_file2 = wave_helper.load_wave(file2)
        if loaded_file1 == -1:
            print("File 1 - " + INVALID_FILE)
            continue  # ask for 2 file names again
        if loaded_file2 == -1:
            print("File 2 - " + INVALID_FILE)
            continue
        break  # every user's input was valid
    united_frame_rate, united_audio_data = \
        union_audio_files(loaded_file1[0], loaded_file1[1],
                          loaded_file2[0], loaded_file2[1])

    transition_menu(united_frame_rate, united_audio_data)


def gcd(x, y):
    """a function that gets two int numbers and calculates their gcd"""
    while y > 0:
        x, y = y, x % y
    return x


def update_according_to_rate(x, y, audio_data):
    """a function that updates audio data so that from each x indices it
    takes first y samples """
    new_audio_data = []
    i = 0
    while i < len(audio_data):
        for j in range(y):
            if i < len(audio_data):
                new_audio_data.append(audio_data[i])
                i += 1
        i += (x-y)
    return new_audio_data


def average_of_two_lists(audio_data1, audio_data2):
    """a function that creates new audio list, created by averages of two
    given audio lists"""
    i = 0
    new_audio_data = []
    for i in range(len(audio_data2)):
        left = int((audio_data1[i][0] + audio_data2[i][0]) / 2)
        right = int((audio_data1[i][1] + audio_data2[i][1]) / 2)
        new_audio_data.append([left, right])
    new_audio_data.extend(audio_data1[i + 1:])  # adds to new list extra
    # indices from the longer list
    return new_audio_data


def unite_audio_lists(audio_data1, audio_data2):
    """a function that unites two audio data lists"""
    new_audio_data = []
    if len(audio_data1) >= len(audio_data2):
        new_audio_data = average_of_two_lists(audio_data1, audio_data2)
    elif len(audio_data2) > len(audio_data1):
        new_audio_data = average_of_two_lists(audio_data2, audio_data1)
    return new_audio_data


def union_audio_files(frame_rate1, audio_data1, frame_rate2, audio_data2):
    """a function that unites two audio files"""
    new_audio_data1 = copy.deepcopy(audio_data1)
    new_audio_data2 = copy.deepcopy(audio_data2)
    frame_rate = frame_rate1
    gc = gcd(frame_rate1, frame_rate2)
    if frame_rate1 > frame_rate2:
        new_audio_data1 = update_audio(audio_data1, frame_rate1,
                                       frame_rate2, gc)
        frame_rate = frame_rate2
    elif frame_rate2 > frame_rate1:
        new_audio_data2 = update_audio(audio_data2, frame_rate2,
                                       frame_rate1, gc)
        frame_rate = frame_rate1
    united_audio_data = unite_audio_lists(new_audio_data1, new_audio_data2)
    return frame_rate, united_audio_data


def update_audio(audio_data, frame_rate1, frame_rate2, gc):
    """a function that updates audio data so it will fit the frame rate of
    united audio file"""
    x = int(frame_rate1 / gc)  # out of every x in audio_data
    y = int(frame_rate2 / gc)  # we will take first y's
    new_audio_data = update_according_to_rate(x, y, audio_data)
    return new_audio_data


def compose_melody():
    """a function that presents to user compose melody menu"""
    while True:
        print("Please write name of file with composing instructions: ")
        composing_file = input()
        if not os.path.isfile(composing_file):
            print(INVALID_FILE)
        else:
            break
    composition(composing_file)


def transition_menu(frame_rate, audio_data):
    """a function that presents to user the transition menu"""
    valid_choice = False
    while not valid_choice:
        print(CHOOSE + "\n" + AUDIO_SAVE + "\n" + AUDIO_CHANGE)
        user_choice = input()
        if user_choice == "1":  # save audio
            while True:
                print("Please write name of file in which you would like to"
                      " save audio")
                filename = input()
                if wave_helper.save_wave(frame_rate, audio_data,
                                         filename) == -1:
                    print(INVALID_SAVE)
                else:
                    valid_choice = True
                    break  # from inner loop, (and afterwards from outer loop,
                    #  since valid_choice is True) and going back to main menu
        elif user_choice == "2":  # change audio
            change_wav_file(frame_rate, audio_data)
            valid_choice = True
        else:
            print(INVALID_CHOICE)  # start outer loop again


def composition(composing_file):
    """a function that gets text file with composition instructions and
     creates audio data"""
    f = open(composing_file, 'r').read()
    instructions_lst = f.strip().split()  # removing \n and spaces
    audio_data = list()
    i = 0
    while i < len(instructions_lst):
        # this next line adds each note data audio to general audio data
        audio_data.extend(add_note_to_audio_data(instructions_lst[i],
                                                 int(instructions_lst[i+1])))
        i += 2
    transition_menu(COMPOSING_SAMPLE_RATE, audio_data)


def add_note_to_audio_data(note, time):
    """a function that gets a note (or Q for quiet) and playing time
    (time is in 1/16 seconds), and returns audio data for this note"""
    audio_data = list()
    num_samples = time*SAMPLES_PER_TIME  # number of samples in the note's
    #  audio data
    if note == "Q":  # quiet
        for i in range(num_samples):
            audio_data.append([0, 0])
    else:
        samples_per_cycle = COMPOSING_SAMPLE_RATE / (NOTE_TO_FREQUENCY[note])
        for i in range(num_samples):
            val = int(MAX_VOL * math.sin(math.pi*2*(i/samples_per_cycle)))
            audio_data.append([val, val])
    return audio_data


if __name__ == '__main__':
    menu()