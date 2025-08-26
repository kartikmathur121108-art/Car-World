from flask import Flask, render_template, request
import time
import pandas as pd

app = Flask(__name__)

df = pd.read_csv("data/cars.csv")

@app.route('/')
def index():
    page = int(request.args.get('oage', 1))
    per_page = 20
    total = len(df)
    start = (page - 1) * per_page
    end = start + per_page
    cars = df.iloc[start:end].to_dict(orient='records')
    return render_template('index.html', cars=cars, page=page, total_pages=(total// per_page) +(1 if total % per_page else 0))