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
import sendgrid, os


# Load daily Salesforce export
DailyExport = pd.read_csv('SalesforceFeb9.csv')

# Set "Today" and "Yesterday" in Salesforce format
time = dt.datetime.today()
today = time.strftime("%-m/%-d/%y")
yesterday = (time - dt.timedelta(1)).strftime("%-m/%-d/%y")

# Array of indicies of new opportunties created today.
# Changing 'Created Date' to 'Last Modified'
New_Opportunties = np.where(np.array((DailyExport['Created Date'] == yesterday)) == True) # change to 'today' for script.
New_Opportunty_Edits = np.where(np.array((DailyExport['Last Modified'] == yesterday)) == True) # to track opportunties edited each day.

# Turn array into list of indicies (unpack tuple)
NewOppsIndex = [x for xs in New_Opportunties for x in xs]
NewOppsEditIndex = [x for xs in New_Opportunty_Edits for x in xs]

# Array of all new stages in DailyExport
ToStage = np.array(DailyExport['To Stage'])
FromStage = np.array(DailyExport['From Stage'])

# Various campaigns
Campaigns = DailyExport['Description']

# Campaign names of newly created opportunties today
DailyCampaigns = Campaigns[NewOppsIndex]
DailyCampaignEdits = Campaigns[NewOppsEditIndex]

# Sum total of which campaigns lead to newly created "working opportunties".
CampaignData = collections.Counter(DailyCampaigns)
CampaignDataEdits = collections.Counter(DailyCampaignEdits)

# Sum total of all newly created working opportunties
# Needs to be two seperate funtions (this is total changes to opportunties)
# We need a counter for accounts created "today" >> Created Date
TotalNewOpportunties = sum(CampaignData.values())
TotalNewOppsEdits = sum(CampaignDataEdits.values())

# Track changes from 'Working' to 'Active' and 'Free Trial'
# Problem: will not count instances where Opp A goes from Working to Active, and Opp B goes from Active to Free Trial, because it subtracts the "From Active" (of Opp B) from the "To Active" (of Opp A)
DailyConverts = (collections.Counter(ToStage[NewOppsIndex])) #- (collections.Counter(FromStage[NewOppsIndex]))
DailyConvertsEdits = (collections.Counter(ToStage[NewOppsEditIndex]))

# Avoid duplicate new opportunity entries when edits are made same day
DailyNames = DailyExport['Opportunity Name'][NewOppsIndex] # all daily created names
DailyEditedNames = DailyExport['Opportunity Name'][NewOppsEditIndex] # all daily edited opps names
UniqueOpps = [] # allows only one unique entry 
for x in DailyNames:
    if x not in UniqueOpps:
        UniqueOpps.append(x)

# Total new entries for the day
TotalUnique = len(UniqueOpps)

# Avoid duplicate entries for stage changes (active -> free trial, free trial -> closed) for same day.
UO = collections.Counter(UniqueOpps)
print(UO)
DN = collections.Counter(DailyEditedNames)
print(DN)
TotalEdits = len((DN - UO).keys())
print(TotalEdits)
Edits = (DN - UO) # if Edits is 0, then go with DN. Hardcode tomorrow.
if len(Edits) == 0:
    Edits = DN
print(Edits)

# isolating campaign name for unique updates/edits
camp = []
for i in DN:
    camp.append(DailyExport[DailyExport['Opportunity Name'] == i].index.tolist())
print(camp)
newcamp = []
for i in camp:
    newcamp.append(i[-1])
print(newcamp)
CampaignsToday = collections.Counter([DailyExport['Description'][i] for i in newcamp])
WhichCampaigns = collections.Counter([ToStage[i] for i in newcamp])

print(CampaignsToday)

W5C1 = CampaignsToday['W5C1'] # week5,1
W5C2 = CampaignsToday['W5C2']
W5C3 = CampaignsToday['W5C3']
W5C4 = CampaignsToday['W5C4']
WeWo = CampaignsToday['WeWo']


def main():
    email_body =  ("Yesterday {}, there were {} new opportunities created, and {} account updates."
        "<br>Here's were those new opportunies came from:"
        " <br>{} from W5C1, <br>{} from W5C2, <br>{} from W5C3, <br>{} from W5C4 and... <br>{} from WeWo."
        "<br>All in all, we converted {} Accounts into Active Opportunities, {} into Free Trials, and {} into Verbal Commitments!"
    ).format(yesterday, TotalUnique, TotalEdits, W5C1, W5C2, W5C3, W5C4, WeWo, WhichCampaigns['Active Opportunity'], WhichCampaigns['Free Trial'], WhichCampaigns['Verbal Commitment'])
    print(email_body)

    emails = ['jake@ripplerecruiting.com', 'dan@ripplerecruiting.com', 'alejandro@ripplerecruiting.com', 'brandon@ripplerecruiting.com']
    for email in emails:
    	# sends an email to us with their email address
        sg = sendgrid.SendGridClient(os.environ['SENDGRID_USER_ID'], os.environ['SENDGRID_PASSWORD'])
        message = sendgrid.Mail()
        message.add_to('<' + email + '>')
        message.set_subject('Your day')
        message.set_html(email_body)
        message.set_from('Jake OConnor <jake@ripplerecruiting.com>')
        status, msg = sg.send(message)

main()
