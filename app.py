from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    source_text = request.form.get('source_text', '').strip()
    translation = source_text[::-1]  # Example logic: Reverse the source text
    return render_template('result.html', source_text=source_text, translation=translation)

if __name__ == '__main__':
    app.run(debug=True)
