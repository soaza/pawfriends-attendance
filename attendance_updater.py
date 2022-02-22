import csv
from random import randint
import pandas as pd
from datetime import date


def main():

   tracking_list = []
   
   CSV_PATH = "BFF tracking sheet.csv"
   
   with open(CSV_PATH) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        line_count += 1

        if line_count >=1 :
            name,num_visits,last_visit,include = row
            if include:
                new_person_obj = {"index":line_count - 2,"name":name,"num_visits": num_visits if num_visits else 0,"last_visit":last_visit,"random_tiebreaker":randint(0, 10)}
                tracking_list.append(new_person_obj)
                


    # Sort ascending by num_visits
    tracking_list.sort(key=lambda x: (x["num_visits"],x["random_tiebreaker"]))
    
    # Get 5 members
    shortlisted_members = []
    for member in tracking_list[0:5]:
        shortlisted_members.append((member["name"],member["index"]))
    
    print("Shortlisted:",shortlisted_members)
    # reading the csv file
    df = pd.read_csv(CSV_PATH)
        
    for member in shortlisted_members:
        index = member[1]
        df.loc[index,'Last Visit'] = date.today()
        df.loc[index,'Number of Visits'] += 1
        
        
    
    # writing into the file
    df.to_csv(CSV_PATH, index=False)
    
    print(f'Processed {line_count} lines.')

if __name__ == "__main__":
    main()