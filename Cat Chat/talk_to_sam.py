import gpt_2_simple as gpt2
import speech_recognition as sr
import pyttsx3
sess = gpt2.start_tf_sess()
gpt2.load_gpt2(sess,model_name='124M')
def get_user_input():
    source = sr.Recognizer()
    with sr.Microphone() as input:
        print("Start Talking")
        # source.adjust_for_ambient_noise(input)
        user_audio = source.listen(input,phrase_time_limit=10)
        print("Shut Up")
    return source.recognize_sphinx(user_audio)

while True:
    try:
        # user_input =get_user_input()'
        user_input = input("User Prompt: ")
        tot_user_input = "PROMT\n"+ user_input+"\nRESPONSE\n"
        print("USER INPUT: ",user_input)
        response_len = len(user_input)
        if response_len >= 10 and response_len < 20:
            response_len *=1.2
        response = gpt2.generate(sess,return_as_list=True,model_name='124M',include_prefix=False,prefix=  tot_user_input,length=int(response_len))[0]
        response = response.replace("PROMT","").replace("RESPONSE","").replace("\n"," ").replace('\r', " ")
        questions =["Who","What","Where","How","Should","Are you","Do you"]
        check_question = [q for q in questions if q.lower() in user_input.lower()] 
        if len(check_question) > 0:
            response = response.replace(user_input,"")
        print(response)
        engine = pyttsx3.init()
        engine.say(response)
        engine.runAndWait()
    except:
        print("Wainting fror User Input")