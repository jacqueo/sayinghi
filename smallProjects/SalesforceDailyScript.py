# Master code to run on each new Salesforce data export. To be run at the end of each day.

"""Goal: provide a daily email to show
		(1) Which campaigns lead to newly created "Working Opporuntities" (and how many)
		(2) How many newly converted "Active Opportunties" and "Free Trials" did we create each day.
"""
# All imports
import pandas as pd
import numpy as np
import collections
import csv
import datetime as dt
import itertools
#import sendgrid, os


# Load daily Salesforce export
DailyExport = pd.read_csv('SalesforceTest3.csv')


# Set "Today" and "Yesterday" in Salesforce format
time = dt.datetime.today()
today = time.strftime("%-m/%-d/%y")
yesterday = (time - dt.timedelta(1)).strftime("%-m/%-d/%y")

# Array of indicies of new opportunties created today.
New_Opportunties = np.where(np.array((DailyExport['Created Date'] == '1/26/17')) == True) # change to 'today' for script.

# Turn array into list of indicies (unpack tuple)
NewOppsIndex = [x for xs in New_Opportunties for x in xs]

# Array of all new stages in DailyExport
ToStage = np.array(DailyExport['To Stage'])
FromStage = np.array(DailyExport['From Stage'])

# Various campaigns
Campaigns = DailyExport['Description']

# Campaign names of newly created opportunties today
DailyCampaigns = Campaigns[NewOppsIndex]

# Sum total of which campaigns lead to newly created "working opportunties".
CampaignData = collections.Counter(DailyCampaigns)

# Sum total of all newly created working opportunties
TotalNewOpportunties = sum(CampaignData.values())

#print(CampaignData)
week5one = CampaignData[0] # week5,1
week5two = CampaignData[1] # week5,2
week5three = CampaignData[2] # week5,3

# Track changes from 'Working' to 'Active' and 'Free Trial'
DailyConverts = (collections.Counter(ToStage[NewOppsIndex])) - (collections.Counter(FromStage[NewOppsIndex]))

def main():
    email_body =  ("Yesterday {}, there were {} new opportunities created; \n{} from Week5 Campaign 1, \n{} from Week5 Campaign 2, and... \n{} from Week5 Campaign 3."
        "\nWe also converted {} Working Opportunities into Active Opportunities and {} into Free Trials!"
    ).format(yesterday, TotalNewOpportunties, week5one, week5two, week5three, DailyConverts['Active Opportunity'], DailyConverts['Free Trial'])
    print(email_body)
main()

"""
    # sends an email to us with their email address
    sg = sendgrid.SendGridClient(os.environ['SENDGRID_USER_ID'], os.environ['SENDGRID_PASSWORD'])
    message = sendgrid.Mail()
    message.add_to('test' + ' ' + '1' + '<' + 'shahriver@ripplerecruiting.com' + '>')
    message.set_subject('Your day')
    message.set_html(email_body)
    message.set_from('Shahriver Hossain <shahriver@ripplerecruiting.com>')
    status, msg = sg.send(message)

main()
"""
