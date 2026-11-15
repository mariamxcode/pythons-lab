def phone_option():
    phone_option_menu =""" 
                       Options
                        1.Memory in use
                        2.Type of view
                        3.Memory status
                        0. to go back
                    """
    while True:
        option_choice = int(input(phone_option_menu))
        match option_choice:
            case 1:
                print("This is Memory in use")
            case 2:
                print("This is Type of View")
            case 3:
                print("This is Memory Status")
            case 0: 
                return
        if option_choice == 0:
            False
def phone_book():
    phone_book_menu ="""
        1.Search
        2.Service Nos
        3.Add name
        4.Erase
        5.Edit
        6.Copy
        7.Assign Tone
        8.Send b'card
        9.Options
        10.Speech dials
        11.Voice tags
        0.Go back
    """
    while True:
        phone_choice = int(input(phone_book_menu))
        match phone_choice:
            case 1:
               print("You are now searching the phone book")
            case 2:
               print("This is Service No ")
            case 3:
               print("This is Add Name")
            case 4:
               print("This Erase Name")
            case 5:
               print("This Edit Name")
            case 6:
               print("This Copy Name")
            case 7:
               print("This Assign Tone")
            case 8:
               print("This Send b'card")
            case 9:
                phone_option()
            case 10:
               print("This is Speed dials")
            case 11:
               print("This is Voice tags")
            case 0:
                return
        if phone_choice == 0:
            False
def messages():
    message_menu ="""
    
        1. Write messages 
        2. Inbox 
        3. Outbox 
        4. Picture messages 
        5. Templates 
        6. Smileys 
        7. Message settings
        8. Info service 
        9. Voice mailbox number 
        10. Service command editor
        0.Go Back
        
    """
    while True:
        message_choice = int(input(message_menu))
        match message_choice:
            case 1:
               print("You are now Writing message")
            case 2:
               print("Checking Inbox.")
            case 3:
               print("Seeing your Outlook")
            case 4:
               print("Picture Message")
            case 5:
               print("This a template")
            case 6:
               print("This is Smiley")
            case 7:
                setting_menu =""" 
                        1.Set 1
                        2.Common
                        0.Go back
                        
                    """
                while True:
                    setting_choice = int(input(setting_menu))
                    match setting_choice:
                        case 1:
                            set_1_menu =""" 
                            1.Message center number
                            2.Message sent as
                            3.Message validity  
                            0. Go back
                        """
                            while True:
                                 set_1_choice = int(input(set_1_menu))
                                 match set_1_choice:
                                    case 1:
                                       print("Message center number")
                                    case 2:
                                       print("Message sent as")
                                    case 3:
                                       print("Message validity")
                                    case 0:
                                        break
                                 if set_1_choice == 0: 
                                    False
                        case 2:
                            common_menu =""" 
                                1.Delivery Report
                                2.Reply via same center
                                3.Character Support 
                                0. Go back
                            """
                            while True:
                                 common_choice = int(input(common_menu))
                                 match common_choice:
                                    case 1:
                                       print("Delivery Report")
                                    case 2:
                                       print("Reply via same center")
                                    case 3:
                                       print("Character Support")
                                    case 0:
                                        break
                                 if common_choice== 0:
                                    False
                        case 0:
                            break
                if  setting_choice == 0:
                    False
                
            case 8:
               print("Info Service")
            case 9:
               print("Voice mailbox number")
            case 10:
               print("Service command editor")
            case 0:
                break
        if message_choice == 0:
            False
                        
def chat():
    print("Chat")
    
                
def call_register():
    call_menu ="""
    
        1. Missed Call 
        2. Received Call
        3. Dialed numbers
        4. Erase Recent Call List 
        5. Show call duration
        6. Show call cost
        7. Call cost setting
        8. Prepaid credit
        0.Go Back
        
    """ 
    while True:
        call_choice = int(input(call_menu))
        match call_choice:
            case 1:
               print("Missed Call")
            case 2:
               print("Received Calls")
            case 3:
               print("Dialed Numbers")
            case 4:
               print("Erase Recent Call List")
            case 5:
                duration_menu="""
                1.Last call duration
                2.All call duration
                3.Received calls' duration
                4.Dialed calls' duration
                5.Clear timer
                0.Go back
                """
                while True:
                    duration_choice = int(input(duration_menu))
                    match duration_choice:
                        case 1:
                            print("Last call duration")
                        case 2:
                           print("All call duration")
                        case 3:
                           print("Received calls' duration")
                        case 4:
                           print("Dialed calls' duration")
                        case 5:
                           print("Clear timer")
                        case 0:
                            break
                    if duration_choice == 0:
                        False
            case 6:
                call_cost_menu="""
                    1.Last call cost
                    2.All calls' cost
                    3.Clear counters
                    0.Go back
                """
                while True:
                    call_cost_choice = int(input(call_cost_menu))
                    match call_cost_choice :
                        case 1:
                           print("Last call cost")
                        case 2:
                           print("All calls' cost")
                        case 3:
                           print("Clear counters")
                        case 0:
                            break
                    if call_cost_choic == 0:
                        False
            case 7:
               print("Call cost setting")
            case 8:
               print("Prepaid credit")
            case 0:
                break
        if call_choice == 0:
            False
                    
            
                            
                
def tones():
    tone_menu ="""
    
        1. Ringing Tone
        2. Ringing Volume
        3. Incoming call alert
        4. Message alert tone
        5. Keypad tones
        6. Warning tones
        7. Vibrating alert
        8. Screen saver
        0.Go Back
        
    """
    while True:
        tone_choice = int(input(tone_menu))
        match tone_choice:
            case 1:
               print("Ringing Tone")
            case 2:
               print("Ringing Volume")
            case 3:
               print("Incoming call alert")
            case 4:
               print("Message alert tone")
            case 5:
               print("Keypad tones")
            case 6:
               print("Warning tones")
            case 7:
               print("Vibrating alert")
            case 8:
               print("Screen saver")
            case 0:
                break
        if tone_choice == 0:
            False
    
def setting():
    setting_menu="""
                1.Call Settings
                2.Phone Settings
                3.Security Settings
                4.Restore Factory Settings
                0.Go back
                """
    while True:
        setting_choice = int(input(setting_menu))
        match setting_choice:
            case 1:
                call_settings_menu="""
                    1.Automatic redial
                    2.Speed dialing
                    3.Call Waiting options
                    4.Own number sending
                    5.Phone line in use
                    6.Automatic Answer
                    0.Go back
                    """
                while True:
                    call_settings_choice = int(input(call_settings_menu))
                    match call_settings_choice:
                        case 1:
                            print("Automatic redial")
                        case 2:
                           print("Speed dialing")
                        case 3:
                            print("Call Waiting options")
                        case 4:
                           print("Own number sending")
                        case 5:
                           print("Phone line in use")
                        case 6:
                           print("Automatic Answer")
                        case 0:
                            break
                    if call_settings_choice == 0:
                        False
            case 2:
                phone_settings_menu="""
                    1.Language
                    2.Cell Info display
                    3.Welcome note
                    4.Network selection
                    5.Confirm SIM service action
                    0.Go back
                    """
                while True:
                    phone_settings_choice = int(input(phone_settings_menu))
                    match call_settings_choice:
                        case 1:
                            print("Language")
                        case 2:
                           print("Call Info display")
                        case 3:
                            print("Welcome note")
                        case 4:
                           print("Network selection")
                        case 5:
                           print("Confirm SIM service action")
                        case 0:
                            break
                    if phone_settings_choice == 0:
                        False
            case 3:
                security_settings_menu="""
                    1.PIN code request
                    2.Call barring service
                    3.Fixed dialing
                    4.Closed user group
                    5.Security level
                    6.Change access codes
                    0.Go back
                    """
                while True:
                    security_settings_choice = int(input(security_settings_menu))
                    match security_settings_choice:
                        case 1:
                            print("PIN code request")
                        case 2:
                           print("Call barring service")
                        case 3:
                            print("Fixed dialing")
                        case 4:
                           print("Closed user group")
                        case 5:
                           print("Security level")
                        case 6:
                           print("Change access codes")
                        case 0:
                            break
                    if security_settings_choice == 0:
                        False
                
            case 4:
                print("Restore Factory Settings")
                
        if setting_choice == 0:
            False
        
def call_divert():
    print("Diverting call")
    
def music():
    music_menu="""
        1.Music Player
        2.Radio
        3.Recorder
        4.Track list
        0.Go back
                        
            """
    while True:
        music_choice = int(input(music_menu))
        match music_choice:
            case 1:
                print("Music Player")
            case 2:
                print("Radio")
            case 3:
                print("Recorder")
            case 4:
                print("Track list")
            case 0:
                break
        if music_choice == 0:
            False

def games():
  print("Games .....")
def calculator():
    print("Calculator....")
def remainder():
    print("Reminder...")
def clock():
    clock_menu="""
        1.Alarm Clock
        2.Clock Setting
        3.Date setting
        4.Stop Watch
        5.Countdown timer
        6.Auto update of date and time
        0.Go back           
            """
    while True:
        clock_choice = int(input(clock_menu))
        match clock_choice:
            case 1:
                print("Alarm Clock")
            case 2:
                print("Clock Setting")
            case 3:
                print("Date setting")
            case 4:
                print("Stop Watch")
            case 5:
                print("Countdown timer")
            case 6:
                print("Auto update of date and time")
            case 0:
                break
        if clock_choice == 0:
            False
def profile():
    print("Profiles...")
def service():
    print("Service...")
def sim_service():
    print("SIM Services....")
    
def access_menu(choice = " "):
    nokia_menu ="""
        Welcome to Nokia
        1.Phone Book
        2.Messages
        3.Chats
        4.Call register
        5.Tones
        6.Setting
        7.Call divert
        8.Music
        9.Games
        10.Calculator
        11.Reminder
        12.Clock
        13.Profiles
        14.Services
        15.SIM services
        0.Go back
        Select an option:
    """
    while True:
        menu_choice = int(input(nokia_menu))
        match menu_choice :
            case 1: 
               phone_book()
            case 2:
                messages()
            case 3:
                chat()
            case 4:
                call_register()
            case 5:
                tones()
            case 6:
                setting()
            case 7:
                call_divert()
            case 8:
                music()
            case 9:
                games()
            case 10:
                calculator()
            case 11:
                remainder()
            case 12:
                clock()
            case 13:
                profile()
            case 14:
                service()
            case 15:
                sim_service()
            case 0:
                return
        if menu_choice  == 0:
             False
choice = input("Enter space to enter menu:  ")
access_menu(choice)
