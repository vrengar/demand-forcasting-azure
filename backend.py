from flask import Flask, request, render_template, send_file
import pandas as pd

app = Flask(__name__)

# Load the CSV file into a pandas DataFrame
df = pd.read_csv('data.csv')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Retrieve user inputs from the form
        column_a = int(request.form['column_a'])
        column_b = request.form['column_b']
        column_c = request.form['column_c']
        
        # Perform the filtering based on the conditions
        filtered_df = df[(df['ColumnA'] % 2 == 0) & (df['ColumnB'] == column_b) & (df['ColumnC'].isin([column_c, 'Dallas', 'Austin']))]
        
        if not filtered_df.empty:
            # Generate a downloadable CSV file with the filtered data
            filtered_df[['Column x']].to_csv('filtered_data.csv', index=False)
            
            # Send the file as an attachment in email
            # Replace the placeholders with your email configuration
            send_email('recipient@example.com', 'Filtered Data', 'Please find the attached file.', 'filtered_data.csv')
            
            # Return a message to the user
            return 'Filtered data has been sent to your email.'
        else:
            return 'No data matching the specified conditions found.'
    
    return render_template('index.html')

def send_email(recipient, subject, body, attachment_path):
    # Add your email sending logic here
    # You can use libraries like smtplib or third-party services like SendGrid to send the email
    pass

if __name__ == '__main__':
    app.run()
