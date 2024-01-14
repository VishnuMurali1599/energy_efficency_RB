from flask import Flask,request,render_template
from src.pipeline.predict_pipeline import CustomData,PredictPipeline

application=Flask(__name__)

app=application

## Route for a home page

@app.route('/')
def index():
    return render_template('index.html') 

@app.route('/predictdata',methods=['GET','POST'])
def predict_datapoint():
    if request.method=='GET':
        return render_template('home.html')
    else:
        data=CustomData(
            X1=request.form.get('X1'),
            X2=request.form.get('X2'),
            X3=request.form.get('X3'),
            X4=request.form.get('X4'),
            X5=request.form.get('X5'),
            X6=request.form.get('X6'),
            X7=request.form.get('X7'),
            X8=request.form.get('X8')

        )
        pred_df=data.get_data_as_data_frame()
        print(pred_df)
        print("Before Prediction")

        predict_pipeline=PredictPipeline()
        print("Mid Prediction")
        results=predict_pipeline.predict(pred_df)
        print("after Prediction")
        return render_template('home.html',results=results[0])
    

if __name__=="__main__":
    app.run(host="0.0.0.0",port=8080)        