from app import create_app,db
from app.models import *

app =create_app('default')

if __name__=="__main__":
    #app.run(debug=True)
    app.run(host="127.0.0.1",port=8000,debug=True)