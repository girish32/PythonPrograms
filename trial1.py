import urllib3
import pandas as pd

url='http://oasis.pjm.com/doc/projload.txt'
filename='pjmload.xls'
connection_pool = urllib3.PoolManager()
resp = connection_pool.request('GET',url )
f = open(filename, 'wb')
f.write(resp.data)
f.close()
resp.release_conn()

with open(filename, "r") as filehandle:
    file_content = filehandle.readlines()

processedlist = []

date = ""

store_it = 0

for eachline in file_content:

    if "RTO COMBINED HOUR ENDING INTEGRATED FORECAST LOAD MW" in eachline:
        store_it = 1
        print "RTO COMBINED HOUR ENDING INTEGRATED FORECAST LOAD MW"
        print ""

    if "PSE&G/MIDATL HOUR ENDING INTEGRATED FORECAST LOAD MW" in eachline:
        store_it = 0
        # print "not storing"

    if store_it == 1:

        if " am " in eachline or " pm " in eachline:
            tmp_list = []
            tmp_list = eachline.split()
            if tmp_list[1] == "am":
                date = tmp_list[0]
                tmp_list.remove("am")
            else:
                tmp_list
                #tmp_list.insert(0, date)
                tmp_list.remove("pm")
            # print tmp_list
            goodline = ",".join(tmp_list)
            processedlist.append(goodline)

with open("op.txt","w") as f:
    for eachline in processedlist:
        print eachline
        f.write(eachline+ '\n')
f.close()

df = pd.read_csv("op.txt",names=["date","period"]+list(range(1,13)),index_col=[0,1])
df = df.stack().reset_index().rename(columns={"level_2":"hour",0:"OK"})
df.index = pd.to_datetime(df.apply(lambda x: "{date} {hour}:00 {period}".format(**x),axis=1))
df.drop(["date", "hour", "period"], axis=1, inplace=True)
print(df)
df.to_csv('out.csv')
