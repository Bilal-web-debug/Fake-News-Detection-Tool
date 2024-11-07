import pickle
from flask import Flask, render_template, request

# Load the trained model and vectorizer
model = pickle.load(open('fake_news_model.pkl', 'rb'))
vectorizer = pickle.load(open('vectorizer.pkl', 'rb'))

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        news = request.form['news']
        data = vectorizer.transform([news])
        prediction = model.predict(data)[0]
        
        if prediction == 1:
            result = 'Real News'
        else:
            result = 'Fake News'
        
        return render_template('result.html', prediction=result)

if __name__ == '__main__':
    app.run(debug=True)
