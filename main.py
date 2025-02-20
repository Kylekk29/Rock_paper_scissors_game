import cv2  #For the image capture and put text on the image
import mediapipe as mp  #For the image hand processing
import time #For calculate the FPS
import random #For the computer to get a random choice
mphands = mp.solutions.hands #Set this variable to use the internal function of the mediapipe package
hands = mphands.Hands(min_detection_confidence=0.05, max_num_hands=1)
mpdraw = mp.solutions.drawing_utils
handLmsStyle = mpdraw.DrawingSpec(color=(0,0,255),thickness=3)#The style of the hand's 21 landmarks
handConStyle = mpdraw.DrawingSpec(color=(0,255,0),thickness=1)#The style of the connections of those 21 landmarks
cap = cv2.VideoCapture(1)#Let the variable cap to be the video capture function of opencv
def get_hand__point_position(frame):
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)#Convert the BGR to RGB for processing
    result = hands.process(frame_rgb)#process the image(frame)
    return result
def get_fps(frame, imagewidth):
    global current_time
    global pervious_time
    current_time = time.time()
    fps = 1/(current_time-pervious_time)#Calculate the FPS by using the difference of time between each run of while loop of programe
    pervious_time = time.time()#Reset the pervious time to the current time for the next run
    #show the FPS
    cv2.putText(frame, f'FPS:{int(fps)}', (imagewidth-150,50), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0,0,255), 1)
def draw_hand_utils(frame, result):
    if result.multi_hand_landmarks:
        for handlankmark in result.multi_hand_landmarks:
            mpdraw.draw_landmarks(frame, handlankmark, mphands.HAND_CONNECTIONS, handLmsStyle, handConStyle)
            #Draw the landmarks of the image frame by using the handlankmark data.
            #Use the internal function to draw the conection of 21 landmarks and the style set on line9,10
            #All command said respectively
            for i, eachlandmark in enumerate(handlankmark.landmark):
                xpos = int(eachlandmark.x * imagewidth)#The absolute x axis of the i landmarks
                ypos = int(eachlandmark.y * imageheight)#The absolute y axis of the i landmarks
                cv2.putText(frame, str(i), (xpos - 25, ypos + 5), cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 0.5, (0, 0, 0), 1)
                #Show the number of hand landmarks near the hand landmarks location
                if i == 4 or i == 8 or i == 12 or i == 16 or i == 20:
                    cv2.circle(frame, (xpos, ypos), 7, (0, 255, 255), cv2.FILLED)
                #Highlight the main detect point by adding a yellow circle above it
            handsign = getHandMove(handlankmark) 
            #Because need the all 21 data so need to run in this intention for the variable that store the 21 point data
            return handsign
def getHandMove(handlankmark):
    eachlandmark = handlankmark.landmark
    #The eachlandmarks here is a ratio of x y axis but enough for determine the handsign
    #The three conditions to determine the type of handsign by comparing the y asis of the required handlandmarks
    if all([eachlandmark[i].y< eachlandmark[i+3].y for i in range(9, 20, 4)]):
        handsign = 'rock'
    elif eachlandmark[13].y < eachlandmark[16].y and eachlandmark[17].y < eachlandmark[20].y:
        handsign = 'scissors'
    elif eachlandmark[4].y < eachlandmark[0].y and eachlandmark[8].y < eachlandmark[0].y: 
        handsign = 'paper'
    else:
        handsign = 'Error'
    return handsign #Return the handsign to the main function
def computer_random_choice():#Use a random package function to get a random choice of the computer
    choice_list = ['rock', 'paper', 'scissors']
    computer_choice_int = random.randint(0, 2)
    computer_choice = choice_list[computer_choice_int]
    return computer_choice
def player_win_loss(computer_choice, handsign):#The all conditions to determine the result of the player
    #3 is error, 2 is tied, 1 is win, 0 is lose
    if handsign == 'Error':
        player_result = 3
    elif computer_choice == 'rock' and handsign == 'paper':
        player_result = 1
    elif computer_choice == 'paper' and handsign == 'scissors':
        player_result = 1
    elif computer_choice == 'scissors' and handsign == 'rock':
        player_result = 1
    elif handsign == 'rock' and computer_choice == 'paper':
        player_result = 0
    elif handsign == 'paper' and computer_choice == 'scissors':
        player_result = 0
    elif handsign == 'scissors' and computer_choice == 'rock':
        player_result = 0
    elif handsign == computer_choice:
        player_result =2
    else:
        player_result = 3        
    return player_result
def result_status_and_data_count():#Change the result of the player to the str type and calculate the statistics
    global strresult_statistics_status 
    global win_round
    global total_round
    if player_result == 3:
        return "Error"
    else:
        strresult_statistics_status = True
        total_round +=1
        if player_result == 0:
            return "You lose "
        elif player_result == 2:
            return 'It is a tied'
        elif player_result == 1:
            win_round +=1
            return 'You win'
    
def put_result(result_player_str):
    if strresult_statistics_status == True: #If the calculation of the statistics is started
        cv2.putText(frame, f'Computer choice: {computer_choice}', (10,50), cv2.FONT_HERSHEY_COMPLEX, 1, (0,255,255), 1)
        if result_player_str != 0 :
            cv2.putText(frame, result_player_str, (10,80), cv2.FONT_HERSHEY_COMPLEX, 1, (0,255,255), 1)
        cv2.putText(frame, f"Your chocie: {handsign}", (10,110), cv2.FONT_HERSHEY_COMPLEX,1, (0,255,255), 1)
        win_percent = (win_round/total_round)*100#Cal the win percent
        win_percent = round(win_percent,2)
        loss_round = total_round-win_round
        cv2.putText(frame, f'Your win percent is {win_percent}%', (10,140), cv2.FONT_HERSHEY_COMPLEX,1, (0,255,0), 1)
        cv2.putText(frame, f"Your statistics: {total_round} rounds, {win_round} wins, {loss_round} losses", (10,170), cv2.FONT_HERSHEY_COMPLEX, 0.7, (0,255,0), 1)
def put_rule():#Show how to quit and start
    cv2.putText(frame, 'Press d to play', (10,200), cv2.FONT_HERSHEY_COMPLEX, 1, (0,255,255), 1)
    cv2.putText(frame, 'Press q to quit', (10,230), cv2.FONT_HERSHEY_COMPLEX, 1, (0,255,255), 0)
strresult_statistics_status=False #Set the status of the game to Fasle
total_score=0 #For calculate the statistics in function put_result
total_round=0 #For calculate the statistics in function put_result
win_round=0 #For calculate the statistics in function put_result
pervious_time = 0 #Calculate the FPS by using the difference of time between each run of while loop of programe
current_time = 0
result_player_str = 0 #Initials the str type of result of player need to show
while(True):
    #get hand sign start
    handsign = 0 #Initials the handsign result after the processing of 
    ret, frame = cap.read()  #ret is test is image is read, the frame store the image
    framewidth = 1280#The width of frame to br resized
    frameheight = 720#The height of frame to be resized
    frame = cv2.resize(frame, (framewidth, frameheight)) #resize the frame to the setted value 
    frame = cv2.flip(frame, 1)#Flip the image(laterally invert)for better user experience 
    imageheight = frame.shape[0]#The image height after the image basic processing
    imagewidth = frame.shape[1]#The image width after the image basic processing
    if not ret:#Test weather image is read
        print('Error')
        break
    result_hand_pos_point = get_hand__point_position(frame)#Give the frame to the function and 
    #return the result after the process
    handsign = draw_hand_utils(frame, result_hand_pos_point)
    #print(handsign)
    get_fps(frame, imagewidth)#Show the FPS on the image
    if cv2.waitKey(1) & 0xFF == ord('q'):#press q to quit
        break
    if  cv2.waitKey(20) & 0xFF == ord('d'):#press d to play the game
        computer_choice = computer_random_choice()#Get the computer choice
        player_result = player_win_loss(computer_choice, handsign)#Get the player result
        result_player_str = result_status_and_data_count()#Get the player result in str type and calculate the statistics
    
    put_result(result_player_str)#Show the result on the image
    put_rule()#Show info
    cv2.imshow('paper scissors rock', frame)#Display the image of the game's frame
    
cap.release()
cv2.destroyAllWindows()
