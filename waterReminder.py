import send_sms
import time
from datetime import datetime

def hourChecker():
    return datetime.now().hour

def send_reminder(body):
    sub = 'Water Reminder'
    recipient = "5555555555@msg.telus.com" #change this to the desired email

    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    sent = False
    while not sent:
        try:
            send_sms.email_alert(sub, body, recipient)
            print('sent reminder to {} at {}'.format(recipient, str(current_time)))
            sent = True
        except:
            time.sleep(60)


def main():
    hoursDone = []
    messages = {'9' : 'good morning you should get a glass of water',
                '11' : 'hey happy late morning its time for a cuppa',
                '13' : 'its around 1pm that means wadda time',
                '15' : 'howdy good afternoon its water chuggin hour',
                '17' : 'hey almost dinner perfect time for a glass of water',
                '19' : 'BREAKING NEWS: get wadda',
                '21' : 'i love youu and you should get a cup of water before bed'}

    
    while 1:
        currentHour = hourChecker()
        if currentHour == 0:
            hoursDone.clear()

        if str(currentHour) in messages.keys():    
            if currentHour not in hoursDone:
                send_reminder(messages[str(currentHour)])
                hoursDone.append(currentHour)

        time.sleep(60)
        
        

if __name__ == '__main__':
    main()

        
