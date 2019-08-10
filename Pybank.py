# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 02:19:38 2019

@author: ai3ca
"""
import pandas as pd 
filepath = "budget_data.csv"
budget_df = pd.read_csv(filepath, encoding = "UTF-8")

month = len(budget_df["Date"].unique())
total_pf = budget_df['Profit/Losses'].sum()
avg_change = total_pf / month

greatest_increase = budget_df['Profit/Losses'].max()
greatest_decrease = budget_df['Profit/Losses'].min()

greatest_increase_date=budget_df.loc[budget_df['Profit/Losses']==greatest_increase,"Date"]
greatest_decrease_date=budget_df.loc[budget_df['Profit/Losses']==greatest_decrease,"Date"]


print("Financial Analysis")
print("----------------------------------")
print("Total Months: " + str(month))
print("Total: " +"$"+ str(total_pf))
print("Average Change: " +"$"+str(avg_change))
print("Greatest Increase in Profits: " +str(greatest_increase_date)+
      "("+"$"+str(greatest_increase)+")" )
print("Greatest Decrease in Profits: " +str(greatest_decrease_date)+
      "("+"$"+str(greatest_decrease)+")" )


with open('Result.txt', 'w') as text:


    text.write("Financial Analysis"+ "\n")
    text.write("-------------------------------------------\n")
    text.write("Total Months: " + str(month) + "\n")
    text.write("Total Profits: " + "$" + str(total_pf) +"\n")
    text.write("Average Change: " + '$' + str(int(avg_change)) + "\n")
    text.write("Greatest Increase in Profits: " +str(greatest_increase_date)+ " ($" + str(greatest_increase) + ")\n")
    text.write("Greatest Decrease in Profits: "  + str(greatest_decrease_date)+" ($" + str(greatest_decrease) + ")\n")
