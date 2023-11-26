from flask import Flask,render_template,request


app=Flask(__name__)

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
        time=1000
    elif(speed=='Medium'):
        time=1500
    elif(speed=='Slow'):
        time=2000
    result=check(number)
    if result[0]:
        return render_template('home.html',info=result[-1],times=times,number=number)
    elif times > 150:
        return render_template('home.html',info="MAXIMUM 150 SMS ONLY",times=times,number=number)
    else:
        return render_template('home.html',times=times,number1=number,speed=time)
    
    
if __name__=='__main__':
    app.run(debug=True,host='192.168.0.108')