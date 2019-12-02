#%%
import pandas as pd
def split_csv(file_path:str,column:str):
    df = pd.read_csv(file_path)

#%%
    headlist=list(df.columns)
#%%

#%%
    mopaths=df[column].drop_duplicates(keep='first')

#%%
    mopathslist=list(mopaths.dropna())
#%%
#%%
    for n in mopathslist:
        print(type(n),n)


#%%
    for n in mopathslist:
        df[df['MOPATH2']==n].to_csv('temp/'+n+'.csv', header=headlist, index=False)
        df[df['MOPATH2']==n].head(5)

#%%
if __name__=="__main__":
    import sys
    filepaths=sys.argv[1]
    columns=sys.argv[2]
    split_csv(filepaths,columns)