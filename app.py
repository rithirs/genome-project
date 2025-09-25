from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def index():
    # This will list all files in your repo directory
    files = os.listdir(os.path.dirname(__file__))
    # You can pass this list to your template
    return render_template('index.html', files=files)

if __name__ == '__main__':
    app.run(debug=True)

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
