from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/extract', methods=['POST'])
def extract_emails():
    text = request.form.get('text')
    
    import re
    email_pattern = r'\S+@\S+'
    extracted_emails = re.findall(email_pattern, text)

    return render_template('result.html', emails=extracted_emails)

if __name__ == '__main__':
    app.run(debug=True)
