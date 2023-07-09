# IPL Chatbot

This project is an IPL (Indian Premier League) chatbot built using Google Dialogflow and Flask. It provides information and interacts with users regarding IPL match details, team information, match statistics, stadium details, and toss decisions.
## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)
## Demo Video
[IPL 2019 Chatbot](https://youtu.be/_dxrjlonAcI)
## Features

- **Match Details:** Users can inquire about specific match details by providing the date and city. The chatbot retrieves the match details, including the teams playing in the match.

- **Team Info:** Users can retrieve information about matches played between two specific teams. The chatbot provides the dates and cities where the matches were held.

- **Stadium:** Users can obtain information about matches held at a specific stadium. The chatbot returns the total number of matches played at the stadium along with the dates.

- **Toss Decision:** Users can inquire about the number of times a team won the toss and chose to bat or field in the IPL 2019.

## Technologies Used

- Google Dialogflow: For natural language processing and intent recognition.
- Flask: For building the backend web application.
- Pandas: For data manipulation and analysis.
- CSV: For reading the IPL match data from a CSV file.
- Python: The programming language used for the project.

## Usage

1. Install the required dependencies by running the following command: pip install flask pandas

2. Download a CSV file named 'IPL_Matches_Gravitas_AI_Problem_Statement_Data.csv' with the necessary IPL match data.

3. Uncomment and modify the lines `#df_filtered = df[df['season'] == 2019]` and `#df_filtered.to_csv('filtered_file.csv', index=False)` in the code to filter and save the required data to the 'filtered_file.csv' file.

4. Run the Flask application by executing the following command:  python app.py

5. Deploy the Flask application to a server or a local development environment.

6. Configure and integrate the Dialogflow chatbot with the deployed Flask application by setting up the webhook URL.

7. Interact with the chatbot by sending queries related to IPL match details, teams, stadiums, or toss decisions.

## Contributing

Contributions to the IPL chatbot project are welcome! If you would like to contribute, please follow these steps:

1. Fork the repository.

2. Create a new branch for your feature or bug fix.

3. Make the necessary changes and commit them.

4. Push the changes to your fork.

5. Submit a pull request describing the changes you've made.

## License

This project is licensed under the [MIT License](LICENSE).

## Contact

For any questions or suggestions regarding the IPL chatbot project, please reach out to:

- [Jasteg Singh](jastegsingh007@gmail.com)

---




