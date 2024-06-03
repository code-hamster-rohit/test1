from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/changeDatabase', methods=['POST'])
def changeDatabase():
    data = request.get_json()
    try:
        df = pd.read_csv('/tmp/newDatabase.csv')
    except:
        df = pd.DataFrame(columns=['number'])
        df.to_csv('/tmp/newDatabase.csv', index=False)
    df = pd.read_csv('/tmp/newDatabase.csv')
    new_index = len(df.index)
    df.loc[new_index] = [data['value']]
    df.to_csv('/tmp/newDatabase.csv', index=False)
    return {'value': data['value']}

if __name__ == '__main__':
    app.run()