from flask import Flask, render_template, request
import gspread
from oauth2client.service_account import ServiceAccountCredentials

app = Flask(__name__)

# Set up Google Sheets credentials
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name('cred.json', scope)
gc = gspread.authorize(credentials)

# Open the Google Sheet
sheet = gc.open('o').sheet1  # Change to your sheet name

@app.route('/')
def popup():
    return render_template('popup.html')

@app.route('/submit', methods=['POST'])
def submit():
    # Process the submitted data
    data = request.form['data']
    sheet.append_row([data])
    return "data has beeb successfuly"

if __name__ == '__main__':
    app.run(debug=True)
