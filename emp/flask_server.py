from flask import Flask
import voting
app = Flask(__name__)

@app.route('/voting',methods=['POST'])
def votings():
	data=request
	return "Hello World!"

if __name__ == "__main__":
    app.run()    