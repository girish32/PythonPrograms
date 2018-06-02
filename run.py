import pandas as pd
df = pd.read_csv("op.txt",names=["date","period"]+list(range(1,13)),index_col=[0,1])
df = df.stack().reset_index().rename(columns={"level_2":"hour",0:"Load (MW)"})
df.index = pd.to_datetime(df.apply(lambda x: "{date} {hour}:00 {period}".format(**x),axis=1))
df.drop(["date", "hour", "period"], axis=1, inplace=True)
print(df)