import csv
from random import randint


def main():

   tracking_list = []
   with open('BFF tracking sheet.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            line_count += 1
        else:
            name,num_visits,last_visit,include = row
            if include:
                new_person_obj = {"name":name,"num_visits": num_visits if num_visits else 0,"last_visit":last_visit,"random_tiebreaker":randint(0, 10)}
                tracking_list.append(new_person_obj)
                


    # Sort ascending by num_visits
    tracking_list.sort(key=lambda x: (x["num_visits"],x["random_tiebreaker"]))
    
    # Get 5 members
    shortlisted_members = []
    for member in tracking_list[0:5]:
        shortlisted_members.append(member["name"])
    
    print(shortlisted_members)

    print(f'Processed {line_count} lines.')

if __name__ == "__main__":
    main()