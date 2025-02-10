from sqlalchemy import create_engine, event
import pymysql
import pandas as pd
from sqlalchemy.orm import declarative_base


# engine = create_engine(
#     "mysql+pymysql://{user}:{pw}@localhost:3306/{db}"
#     .format(user="root",
#             pw="nikhil",
#             db="careers")
# )

engine = create_engine('mysql+pymysql://root:nikhil@localhost:3306/careers')


# data in dataframe
jobs_df = pd.read_sql('SELECT * FROM jobs', engine) #read the entire table
JOBS = []
for i in range(len(jobs_df)):
    JOBS.append(jobs_df.loc[i].to_dict())





# engine = create_engine("sqlite:///careers.db")

# connection = engine.connect()
# results = connection.execute('SELECT * FROM jobs').fetchall()
#
# for result in results:
#     print(result)