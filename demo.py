import requests
import time
# from quickstart import start,create_message,send_message
# service = start()
# message = create_message('me','bsureshjnv@gmail.com','chegg','Found question')
data = {'clientId':'CHGG','email':'darshanpriya0@gmail.com','password':'Trivial!123'}
url = 'https://www.chegg.com/auth/_ajax/auth/v1/login?clientId=CHGG'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
           'Host':'www.chegg.com',
           'DNT':'1'}
s = requests.Session()
#s.get(url='https://www.chegg.com/my/expertqa',headers=headers)
#page = s.get(url='https://www.chegg.com/auth?action=login',headers=headers)
# print(page.headers)
# print(page.cookies)
page1 = s.post(url=url,data=data,headers=headers)
#print(page1.text)
#page2 = s.get('https://www.chegg.com/my/expertqa',headers=headers)
#print(page2.text)
page3 = s.get('http://www.chegg.com/homework-help/expertquestion',headers=headers)
z = str(page3.text)
i = 200
skipurl = 'https://www.chegg.com/study/_ajax/expertquestion'# type post request
skip_data={'questionId':3434,'skipTime':'543','skipReason':'InsufficientKnowledge','skipSource':'skipGetNextQuestion','questionSkipSource':'d'}
while(i>0):
    #time.sleep(15)
    i=i-1
    z = str(s.get('https://www.chegg.com/homework-help/expertquestion',headers=headers).text)
    print('page is ')
    print(z)
    if 'Time remaining to complete the answer' in z:
        print('answering question')
        time.sleep(600)
    elif 'Skip & Get next question' in z:
        time.sleep(20)
        print('question going to be skipped')
        z = str(s.get('http://www.chegg.com/homework-help/expertquestion',headers=headers).text)
        if 'Time remaining to complete the answer' in z:
            print('question answering')
            time.sleep(600)
        else:
            index = z.find('data-qid') + 10
            end_index = index + 7
            qid = z[index:end_index + 1]
            skip_data['questionId']=qid
            s.post(url= skipurl,data=skip_data,headers=headers)
            print('skipped question')
    else:
        print('elsesss')
        time.sleep(10)








# while(i>0):
#     time.sleep(10)
#     i=i-1
#     if "Skip & Get next question" in z:
#         print("found question")
#         send_message(service,'me',message)
#         time.sleep(600)
#         page3 = s.get('http://www.chegg.com/homework-help/expertquestion', headers=headers)
#         z = str(page3.text)
#     else:
#         page3 = s.get('http://www.chegg.com/homework-help/expertquestion', headers=headers)
#         z = str(page3.text)
