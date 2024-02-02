from flask import Flask,request,render_template,flash
import subprocess

app = Flask(__name__)
@app.route('/')
def index():
    return "index<br><a href='/wol'>Wake On Lan</wol>"
@app.route('/wol' , methods=['GET','POST'])
def wol():
     if request.method == 'POST' :
        macaddress = request.form['Macaddress']
        ipaddress = request.form['Ipaddress']
     return render_template('wol.html')
     command = "wakeonlan " , macaddress , "| ping " , Ipaddress
     result = subprocess.check_output(["/bin/bash", "-c", command])
     message = ("命令执行成功！")
     message = ("输出结果为:\n", result)
     if result.returncode == 0:
        message = f"<h1 class='{text-align: center;color:green}'>Wake up successfully!</h1><br><h5 class='text-align: center;'>your machine {macaddress} is waking up.</h5><br><h6>bash:</h6>" , result.stdout
        print("waking up")
     else:
        message = "<h1 class='{text-align: center;color:red}'> Command or your Mac address wrong! </h1><br><h4>Format:</h4><code>XX:XX:XX:XX:XX:XX</code>"
     flash(message)
     if __name__ == '__main__':
        app.run(debug=True)
~                                                                                                                                
~                                                                                                                                
~                                 
