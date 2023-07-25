import pandas as pd
import http.client

url = 'https://mtp.indianrailways.gov.in/view_section.jsp?lang=0&id=0,2,630,658'

try:
    df_list = pd.read_html(url)
    df = df_list[5]  # Assuming the DataFrame you want to save is at index 5.
    print(df)
    
    # Save the DataFrame to a JSON file.
    df.to_json('railway_data.json', orient='records')
    print("Data saved to JSON file successfully.")
    
except http.client.IncompleteRead as e:
    print(f"IncompleteRead error: {e}")
    # Optionally, you can retry the request or take other actions to handle the error.
except Exception as e:
    print(f"An error occurred: {e}")
