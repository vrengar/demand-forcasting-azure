from flask import Flask, request, render_template
import pandas as pd

app = Flask(__name__)

# Load the Excel file into a pandas DataFrame
df = pd.read_excel('data.xlsx')

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
            # Generate a downloadable Excel file with the filtered data
            filtered_df[['Column x']].to_excel('filtered_data.xlsx', index=False)
            
            # Return a message to the user
            return 'Filtered data has been generated as an Excel file.'
        else:
            return 'No data matching the specified conditions found.'
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
