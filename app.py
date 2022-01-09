import numpy as np
import pandas as pd
import pickle
from flask import Flask,request,jsonify,render_template
app=Flask(__name__)

model1=pickle.load(open('model.pkl','rb'))
@app.route('/')
#render_template('index.html')
def home():
	return render_template('index.html')
@app.route('/sub',methods=['POST'])
def predict():
	
	if request.method=="POST":
		age=int(request.form["age"])
		sex=request.form["sex"]
		cp=int(request.form["cp"])
		restbp=int(request.form["rest Bp"])
		chol=int(request.form["chol"])
		fbs=int(request.form["fbs"])
		restecg=int(request.form["restecg"])
		hb=int(request.form["hb"])
		exang=int(request.form["exang"])
		op=float(request.form["op"])
		slope=int(request.form["slope"])
		ca=int(request.form["ca"])
		thal=int(request.form["thal"])
		sex1=2
		if (sex=="Male"):
			sex1=1
		else:
			sex1=0
		ns=model1.predict([[age,sex1,cp,restbp,chol,fbs,restecg,hb,exang,op,slope,ca,thal]])
	if (ns==[0]):
		s="Negative"
		return render_template("sub.html",n=s,age=age,sex=sex,cp=cp,restbp=restbp,chol=chol,fbs=fbs,restecg=restecg,hb=hb,exang=exang,op=op,slope=slope,ca=ca,thal=thal)
	else:
		s="Positive"
		return render_template("sub.html",n=s,age=age,sex=sex,cp=cp,restbp=restbp,chol=chol,fbs=fbs,restecg=restecg,hb=hb,exang=exang,op=op,slope=slope,ca=ca,thal=thal)
if __name__=='__main__':
	app.run(debug=True)