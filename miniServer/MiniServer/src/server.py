from flask import Flask, request, render_template, jsonify
import pypyodbc 
import random 
import ldap
import socket, pickle

app = Flask(__name__)

userid = ""

@app.route("/")
def login():
    return render_template('Login.html', msg=False)

@app.route("/MainBoard")
def MainBoard():
    return render_template('MainBoard.html', msg=False)

#connect.simple_bind_s('uid=admin,ou=system', 'secret')

@app.route("/ProcessLogin", methods=['POST'])
def processLogin():
    
    try:
        userid=request.form["userid"]
        pwd=request.form["pwd"]
        print(userid, pwd)
        connect = ldap.initialize('ldap://localhost:10389', bytes_mode=False)
        connect.set_option(ldap.OPT_REFERRALS, 0)
        connect.simple_bind_s(userid, pwd)
    except ldap.INVALID_CREDENTIALS:
        print("Your username or password is incorrect.")
        return render_template('Login.html', msg=True)
    except ldap.LDAPError as e:
        if type(e.message) == dict and e.message.has_key('desc'):
            print(e.message['desc'])
        else: 
            return render_template('Login.html', msg=False)
    return render_template('MainBoard.html')

@app.route("/TerminateClientProcessListing")
def TerminateClientProcessListing():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
   
    s.sendall(b'TerminateClientProcessListing')
    
    data = s.recv(1024*1024)
    
    processInfoList = pickle.loads(data)
    
    return render_template('TerminateClientProcessListing.html', processInfoList=processInfoList)


@app.route("/TerminateClientProcess")
def TerminateClientProcess():
    pid = request.args.get('pid')
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
   
    s.sendall(('TerminateClientProcessPID'+str(pid)).encode())
    
    data = s.recv(1024*1024)
    
    result = pickle.loads(data)
    
    print("TerminateClientProcess Result ", result)
    return render_template('TerminateClientProcess.html', result=result)

@app.route("/DownloadUnZipNodeJS")
def DownloadUnZipNodeJS():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
   
    s.sendall(b'DownloadNodeJS')
    
    data = s.recv(1024*1024)
    
    result = pickle.loads(data)     
    
    
    return render_template('DownloadUnZipNodeJS.html', result=result)


@app.route("/ContentManagementInstalled")
def contentManagement():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
   
    s.sendall(b'ContentManagementInstalled')
    
    data = s.recv(1024*1024)
    
    installed = pickle.loads(data)
    
    
    return render_template('ContentManagementInstalled.html', installed=installed)


@app.route("/ContentManagementNotInstalled")
def ContentManagementNotInstalled():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
   
    s.sendall(b'ContentManagementNotInstalled')
    
    data = s.recv(1024*1024)
    
    notinstalled = pickle.loads(data)
    
    s.close()
    return render_template('ContentManagementNotInstalled.html', notinstalled=notinstalled)

@app.route("/HealthMonitoring")
def healthMonitoring():
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
   
    s.sendall(b'GetDeviceInfo')
    
    data = s.recv(1024*1024)
    
    deviceInfo = pickle.loads(data)

    s.close()
    return render_template('HealthMonitoring.html', deviceInfo=deviceInfo)





import socket
HOST = '127.0.0.1'  
PORT = 9999        





if __name__ == "__main__":
    app.run()
    
    