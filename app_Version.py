from flask import Flask, render_template, send_file, redirect, url_for, request
from analyzer import generate_population, analyze_traits, generate_graphs, save_csv
import os

app = Flask(__name__)

# In-memory population dataset
population = generate_population()
graphs = generate_graphs(population)
summary = analyze_traits(population)

@app.route('/')
def index():
    global population, graphs, summary
    return render_template('index.html', summary=summary, graphs=graphs, population=population, loading=False)

@app.route('/reload')
def reload_population():
    global population, graphs, summary
    population = generate_population()
    summary = analyze_traits(population)
    graphs = generate_graphs(population)
    return redirect(url_for('index'))

@app.route('/download_csv')
def download_csv():
    global population
    save_csv(population)
    return send_file('dataset.csv', as_attachment=True)

@app.route('/loading')
def loading():
    # Fake loading page before showing results
    return render_template('index.html', loading=True)

@app.route('/about')
def about():
    contributors = ["Rithika (rithirs)", "Member2", "Member3", "Member4", "Member5"]
    return render_template('about.html', contributors=contributors)

if __name__ == '__main__':
    app.run(debug=True)
