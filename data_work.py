# import the required libs

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# pull in the existing csv file

main_df = pd.read_csv("combined_data_output.csv", low_memory=False)

# list all the columns of all the entire data set
def list_all_columns():
    for title in main_df.columns:
        print(title)

# list_all_columns()

# pull in specific fields for analisis and viewing
select_fields = main_df[[
    'candidate_name',
    'contribution_receipt_amount',
    'party',
    'contribution_receipt_date',
    'contributor_zip',
    'contributor_id',
    'transaction_id'
]]

# convert recipt date to date time object from pandas
select_fields['contribution_receipt_date'] = pd.to_datetime(select_fields['contribution_receipt_date'], errors='coerce')

select_fields['month'] = select_fields['contribution_receipt_date'].dt.to_period('M')


# extract a smple of either all or the selection of fields for analisis
# the function takes in all or select and a given numer of entries
def sample_data(size,num):
    if size == 'all':
        data = main_df.sample(int(num))
        print(data)
        return data
    elif size == "select":
        data = select_fields.sample(int(num))
        print(data)
        return data

#sample_data('sample',5)

def df_info(df):
    data_info = df.info()

    print(data_info)

def df_overview(df):

    print('\tData Overview')

    # describe the data
    stats_data = df.describe(include=[object])

    print(stats_data)

    disc_data = df.describe(include=[np.number])

    print(disc_data)

#sample_data('all',5).info()

def aggr_cand_month():

    grouped_data = select_fields.groupby(['candidate_name','month'])['contribution_receipt_amount'].sum().unstack()
    grouped_data.T.plot(kind='line', marker='o', figsize=(10,6))
    plt.title('Total Contributions by Month for Each Candidate')
    plt.xlabel('Month')
    plt.ylabel('Total Contributions')
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.legend(title='Candidate Name')
    plt.tight_layout()
    plt.savefig('plt1.png')
    #plt.show()
    
#aggr_cand_month()

def avg_cand_don_sorted():
    grouped_avg = select_fields.groupby(['candidate_name','month'])['contribution_receipt_amount'].mean().reset_index()
    grouped_avg_sorted = grouped_avg.sort_values(by=['candidate_name','contribution_receipt_amount'], ascending=[True, False])
    pivot_table = grouped_avg_sorted.pivot(index='month', columns='candidate_name', values='contribution_receipt_amount')
    pivot_table.plot(kind='line', figsize=(10,6))
    
    plt.title('Mean Contributions by Month for Each Candidate')
    plt.xlabel('Month')
    plt.ylabel('Total Contributions')
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.legend(title='Month and Year')
    plt.tight_layout()
    plt.savefig('plt2.png')
    #plt.show()
#avg_cand_don_sorted()


def avg_cand_don():
    grouped_avg = select_fields.groupby(['candidate_name','month'])['contribution_receipt_amount'].mean().reset_index()

    plt.figure(figsize=(10,6))
    sns.barplot(data=grouped_avg, x='month', y='contribution_receipt_amount', hue='candidate_name')

    plt.title('Mean Contributions by Month for Each Candidate')
    plt.xlabel('Month')
    plt.ylabel('Average Contributions')
    plt.grid(True, axis='y')
    plt.xticks(rotation=45)
    plt.legend(title='Month and Year')
    plt.tight_layout()
    plt.savefig('plt3.png')
    #plt.show()

#avg_cand_don()

def scatter_plot():
    donor_count = select_fields.groupby(['candidate_name','month'])['transaction_id'].nunique().reset_index(name='num_donors')
    amount_raised = select_fields.groupby(['candidate_name','month'])['contribution_receipt_amount'].sum().reset_index(name='total_raised')
    merged_df = pd.merge(donor_count, amount_raised, on=['candidate_name', 'month'])
    
    plt.figure(figsize=(8,6))
    sns.scatterplot(data=merged_df, x='num_donors', y='total_raised', hue='candidate_name', style='candidate_name')
    plt.title('Scatter Plot of Number of Doners vs. Total Raised Per Month')
    plt.xlabel('Number of Donors in a Month')
    plt.ylabel('Amount Raised')
    plt.savefig('plt5.png')
    #plt.show()
    
#scatter_plot()

def raised_overall_bar():
    raised = select_fields.groupby('candidate_name')['contribution_receipt_amount'].sum().reset_index()
    raised.columns = ['candidate_name', 'total_raised']
    raised = raised.sort_values(by='total_raised', ascending=False)

    sns.barplot(data=raised, x='candidate_name', y='total_raised', hue='candidate_name')
    #raised.plot(kind='bar', )

    plt.title('Totals Raised by Candidate')
    plt.ylabel('Total Raised in Millions')
    plt.xlabel('Candidate Name')
    plt.setp(plt.xticks(rotation=15))
    plt.savefig('plt6.png')
    #plt.show()

#raised_overall_bar()

def raised_monthly():
    monthly = select_fields.groupby('month')['contribution_receipt_amount'].sum()
    print(monthly)
    plt.figure(figsize=(8,6))
    monthly.plot(kind='bar', figsize=(8,6), legend=None)
    plt.xticks(rotation=45)
    plt.ylabel('Total Raised by Month')
    plt.title('Monthly Totals Raised for All Candidates')
    plt.savefig('plt7.png')
    #plt.show()
#raised_monthly()

def num_donations():
    donations = select_fields.groupby('candidate_name')['transaction_id'].count()
    donations = donations.sort_values(ascending=False)
    donations = donations.head()
    print(donations)
    donations.plot(kind='barh', figsize=(8,6))
    plt.title('Individual Donations by Candidate')
    plt.xlabel('Total Individual Donations')
    plt.ylabel('')
    plt.yticks(rotation=45)
    plt.savefig('plt8.png')
    #plt.show()
    
num_donations()