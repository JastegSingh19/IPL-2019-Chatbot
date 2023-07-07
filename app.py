from flask import Flask,request,jsonify
import csv
from datetime import datetime
import pandas as pd
df = pd.read_csv('filtered_file.csv')
app=Flask(__name__)
@app.route('/',methods=['POST'])
def index():
    data=request.get_json()
    action = data.get('queryResult').get('intent').get('displayName')
    subaction=data.get('queryResult').get('action')
    if action=='Match Details':
        date=data.get('queryResult').get('parameters').get('date-time')
        city=data.get('queryResult').get('parameters').get('geo-city')
        date=date[2:10]
        print(date)
        date_object = datetime.strptime(date, "%y-%m-%d")
        new_date_string = date_object.strftime("%d/%m/%y")
        print(new_date_string)
        team1='';team2=''
        with open('filtered_file.csv','r') as file:
            csv_reader=csv.reader(file)
            for row in csv_reader:
                if(new_date_string==row[3] and city==row[2]):
                    team1=row[4]
                    team2=row[5]
        if(team1=='' and team2==''):
            response={
                'fulfillmentText': "No match was played in this date and city"
            }
        else:
            response = {
                'fulfillmentText': "The match was played between {} and {}. Do you want to know more about this match?".format(team1, team2)
            }
    elif subaction=='MatchDetails.MatchDetails-yes':
        date = data.get('queryResult').get('outputContexts')[1].get('parameters').get('date-time')
        city = data.get('queryResult').get('outputContexts')[1].get('parameters').get('geo-city')
        date = date[2:10]
        date_object = datetime.strptime(date, "%y-%m-%d")
        new_date_string = date_object.strftime("%d/%m/%y")
        print(new_date_string)
        tosswin='';tosdecide='';winner='';venue='';win_by_runs='';win_by_wickets='';mom='';
        with open('filtered_file.csv','r') as file:
            csv_reader=csv.reader(file)
            for row in csv_reader:
                if(new_date_string==row[3] and city==row[2]):
                    tosswin=row[6]
                    tosdecide=row[7]
                    venue=row[14]
                    winner=row[10]
                    win_by_runs=row[11]
                    win_by_wickets=row[12]
                    mom=row[13]
        response={
            'fulfillmentText':"{} won the toss and decided to {}. The match was held at {}. {} team won by {} runs and {} wickets. The man of the match was given to {}. Do you want to know more about umpires of the match ".format(tosswin,tosdecide,venue,winner,win_by_runs,win_by_wickets,mom)
        }
    if subaction=='MatchDetails.MatchDetails-yes.MatchDetailsinfo-yes-yes':
        date = data.get('queryResult').get('outputContexts')[1].get('parameters').get('date-time')
        city = data.get('queryResult').get('outputContexts')[1].get('parameters').get('geo-city')
        date = date[2:10]
        date_object = datetime.strptime(date, "%y-%m-%d")
        new_date_string = date_object.strftime("%d/%m/%y")
        umpire1 = ''; umpire2 = ''
        with open('filtered_file.csv', 'r') as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                if (new_date_string == row[3] and city == row[2]):
                    umpire1=row[15]
                    umpire2=row[16]
        response={
            'fulfillmentText': "The first umpire of the match was {} and the second umpire was {}".format(umpire1,umpire2)
        }
    if action=='Team Info':
        team1=data.get('queryResult').get('parameters').get('Teams')[0]
        team2 = data.get('queryResult').get('parameters').get('Teams')[1]
        date=[];city=[]
        with open('filtered_file.csv', 'r') as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                if (team1 == row[4] and team2 == row[5]) or (team1 == row[5] and team2 == row[4]):
                    date.append(row[3])
                    city.append(row[2])
        if len(date) > 0:
            res = f"Matches between {team1} and {team2} were played on the following dates:\n"
            for i in range(len(date)):
                res += f"-Date: {date[i]}, City: {city[i]}\n"
        else:
            res = f"No matches found between {team1} and {team2}."
        print(res)

        response = {
            'fulfillmentText': res
        }
    if action=='Stadium':
        stadium=data.get('queryResult').get('parameters').get('Stadiums')
        print(stadium)
        date=[]
        with open('filtered_file.csv', 'r') as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                if stadium==row[14]:
                    date.append(row[3])
                    city=row[2]
        if len(date) >0:
            res=f"Total {len(date)} matches were played at {stadium}, {city}.The dates were:-"
            for i in range(len(date)-1):
                res+=f"{date[i]},"
            res+=f"{date[i]}. Want to know more about just search for city and date to get the particular match information."
        else:
            res=f"No match was held at {stadium}"
        response={
            'fulfillmentText': res
        }
    if action=='Toss Decision':
        team=data.get('queryResult').get('parameters').get('teams')
        toss=data.get('queryResult').get('parameters').get('Toss_Dec')
        count=0
        with open('filtered_file.csv', 'r') as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                if team==row[6] and toss==row[7]:
                    count=count+1
        response={
            'fulfillmentText':"{} had won the toss and decided to {} {} times in the IPL 2019.".format(team,toss,count)
        }




    return jsonify(response)

if __name__=="__main__":
    #df_filtered = df[df['season'] == 2019]
    #df_filtered.to_csv('filtered_file.csv', index=False)

    app.run(debug=True,port=5001)