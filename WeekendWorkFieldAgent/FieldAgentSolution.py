import phonenumbers, os, re, logging, datetime, matplotlib
from email_validator import validate_email, EmailNotValidError
import pandas as pd

def is_valid_date(filename):
    try:
        date = filename.split("_")[2]
        date = date.split(".")[0]
        year = int(date[:4])
        month = int(date[4:6])
        day = int(date[6:])
        datetime.datetime(int(year), int(month), int(day)) #if error is thrown date is invalid
        return True
    except:
        return False

def sort_files(files):
    regex = "^(NYL_FieldAgent_)[0-9]{8}(\.csv)$" # File starts with NYL_FieldAgent_ and ends with .csv with only the 8 letters changing 
    filtered = list(filter(lambda f: re.match(regex, f) and is_valid_date(f), files))
    filtered.sort()
    sorted = filtered[::-1] # Sorted ascending so reverses to get descending
    return sorted

if __name__ == '__main__':
    logpath = 'Files/fa_logfile.log'
    logging.basicConfig(filename=logpath, format='%(asctime)s: [%(levelname)s]: %(message)s', datefmt="%H:%M", level=logging.DEBUG)

    with open(logpath, 'r+') as f:
        f.truncate(0)
    logging.info('Logfile was cleared')

    files = os.listdir('Files')
    fa_files = sort_files(files)

    try:
        df = pd.read_csv('Files/' + fa_files[0])
        logging.info(f"File {fa_files[0]} selected as most recent file")
    except:
        logging.error("No files found in directory to process")
        exit(0)
    
    try:
        prev_df = pd.read_csv('Files/' + fa_files[1])
        diff = abs(df.shape[0] - prev_df.shape[0])

        if diff > 500:
            logging.error(f'Line count difference between {fa_files[0]} and {fa_files[1]} was greater than 500 lines')
            exit(0)
        logging.info(f'Difference in line counts between {fa_files[0]} and {fa_files[1]} was {diff}')
    except:
        logging.info(f"No other files in directory to compare {fa_files[0]} with")
    
    f = open("Files/NYL.lst", "r")
    for x in f:
        if x == fa_files[0] + '\n':
            logging.error(f'File {fa_files[0]} has already been processed')
            f.close()
            exit()
    f.close()

    f = open("Files/NYL.lst", "a")
    f.write(fa_files[0] + '\n')
    f.close()

    df = df.rename(columns = {"Agent Writing Contract Start Date (Carrier appointment start date)":"Agent Writing Contract Start Date"})
    df = df.rename(columns = {"Agent Writing Contract Status (actually active and cancelled\'s should come in two different files)":"Agent Writing Contract Status"})
    try:
        df.to_csv(path_or_buf="Files/" + fa_files[0], index=False)
    except:
        print(f'Could not write to {fa_files[0]}. File may be open')
        logging.error(f'Failed to write to {fa_files[0]}')
        exit(0)

    row_num = 2
    states_lst = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA", 
          "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", 
          "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", 
          "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", 
          "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]

    for index, row in df.iterrows():
        num = row["Agent Phone Number"]
        email = row["Agent Email Address"]
        state = row["Agent State"]

        #Check phone number
        try:
            parsed_num = phonenumbers.parse("+1" + num, None)
            if not phonenumbers.is_valid_number(parsed_num):
                logging.info(f'Invalid number {num} in row {row_num}')
        except:
            logging.info(f'No agent phone number in row {row_num}')

        #Check email
        try:
            validate_email(email)
        except EmailNotValidError as e:
            logging.info(f'Invalid email {email} in row {row_num}')

        #Check state
        if not state in states_lst:
            logging.info(f'Invalid state {state} in row {row_num}')
        row_num += 1

    logging.info(f'File finished processing')
    # Dataframe with headers as index and data as rows
    df_index = df.set_index(list(df.columns))
    print(df_index)

    # Dataframe grouped by Agency State
    by_state = df.groupby('Agency State').count()
    print(by_state)
    
    #Dateframe showing Agent First and Last Name, State Date, and When agent became A20
    df_slice = df[["Agent First Name", "Agent Last Name", "Agent Writing Contract Start Date", "Date when an agent became A2O"]]
    print(df_slice)

    df_index.hist()
    by_state.hist()