import speech_recognition as sr  
import time
from gtts import gTTS
import os
ch=1
scoreH=0
scoreM=0
check=0
loop_check=0
round1=0
l1=['ा','ी','ू','ौ','ै','ो']
                                                                
try:
    while(ch==1):
        loop_check=+1
        check=0with sr.Microphone() as source:                                                                       
            print("Speak:")                                                                                   
            audio = sr.Recognizer().listen(source)
            print("time over")
        print("You said " + sr.Recognizer().recognize_google(audio, language='hi-IN'))
        
        a=sr.Recognizer().recognize_google(audio, language='hi-IN')
        
        if(round1>0):
            if songtext[-1] in l1:
                if songtext[-2]!=a[0]:
                    print('y')
                    print(songtext[-2])
                    print(a[0])
                    print('you are cheating')
                    check=1
                    scoreM=scoreM+1
                    a=songtext        else:
                if songtext[-1]!=a[0]:
                    print('x')
                    print(songtext[-1])
                    print(a[0])
                    print('you are cheating')
                    check=1
                    scoreM=scoreM+1
                    a=songtext
                    
        
        if a[-1] in l1:
            mytext = 'चलिए में' + a[-2]+'ा' + 'शब्द से गाती हूँ,'q="C:\\LENOVO\\Desktop\\Project_Antakshari\\Database\\"+a[-2]+"\\1.txt"
                
            
        else:
            mytext = 'चलिए में' + a[-1]+'ा' + 'शब्द से गाती हूँ,'
            q="C:\\LENOVO\\Desktop\\Project_Antakshari\\Database\\"+a[-1]+"\\1.txt"try:
            my_file=open(q,encoding="utf8")
            
        except:
            mytext = 'में हार मानती हूँ, आप ही इस शब्द से गायॆ'
            print(mytext)
            scoreH=scoreH+1
            if(check==1):
                print('scoreH ='+str(scoreH))
                print( 'scoreM ='+str(scoreM))
                break
            time.sleep(2)
            continue
        
        songtext=my_file.read()language = 'hi'myobj = gTTS(text=mytext, lang=language, slow=False)
        myobj.save("welcome.mp3")
        os.system("welcome.mp3")
        
        myobj = gTTS(text=songtext, lang=language, slow=False)
        myobj.save("welcome1.mp3")
        os.system("welcome1.mp3")
        
        round1+=1time.sleep(6)
        
        hertext1='क्या आप इस खेल को आगे बढ़ाना चाहते ह, हा के लिए 1 दबाये और ना के लिए 0'
        
        myobj = gTTS(text=hertext1, lang=language, slow=False)
        myobj.save("welcome2.mp3")
        os.system("welcome2.mp3")
        
        ch=int(input(""))
        if(ch==0):
            print('scoreH ='+str(scoreH))
            print( 'scoreM ='+str(scoreM))
            break
        
        hertext2='चलिए आप'+songtext[-2]+'शब्द से गायॆ'
        myobj = gTTS(text=hertext2, lang=language, slow=False)
        myobj.save("welcome3.mp3")
        os.system("welcome3.mp3")
        
        time.sleep(2)
        
    
except sr.UnknownValueError:
    print("Could not understand audio")
except sr.RequestError as e:
    print("Could not request results; {0}".format(e))
    
    
    #some comment
