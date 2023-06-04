import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

df = pd.read_csv('data/dataset.csv')

df.drop(['Symptom_7','Symptom_8','Symptom_9','Symptom_10','Symptom_11','Symptom_12','Symptom_13','Symptom_14','Symptom_15','Symptom_16','Symptom_17'],axis=1,inplace=True)

#Remove Hyphen
for col in df.columns:
    df[col]= df[col].str.replace('_',' ')

cols = df.columns

data = df[cols].values.flatten()

reshaped = pd.Series(data)
reshaped = reshaped.str.strip()
reshaped = reshaped.values.reshape(df.shape)

df = pd.DataFrame(reshaped, columns = df.columns)

df.fillna(0,inplace=True)

df_s = pd.read_csv('data/Symptom-severity.csv')

# Remove Hyphen
df_s['Symptom']=df_s['Symptom'].str.replace('_',' ')

a= np.array(df_s['weight'])

vals = df.values
symptoms = df_s['Symptom'].unique()

for i in range(len(symptoms)):
    vals[vals == symptoms[i]] = df_s[df_s['Symptom'] == symptoms[i]]['weight'].values[0]
    
newdf = pd.DataFrame(vals, columns=cols)

newdf = newdf.replace('dischromic  patches', 0)
newdf = newdf.replace('spotting  urination',0)
newdf = newdf.replace('foul smell of urine',0)

X = newdf.drop(['Disease'],axis=1)
y = newdf['Disease']

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size = 0.2,stratify=y,random_state=0)

clf_rfc = RandomForestClassifier(n_estimators=700,random_state=0,n_jobs=-1,verbose=4)
clf_rfc.fit(X_train,y_train)


#Prediction function
def predict(s1,s2,s3,s4='vomiting',s5='vomiting',s6='vomiting'):
    l = [s1,s2,s3,s4,s5,s6]
    
    x= np.array(df_s['Symptom'])
    y= np.array(df_s['weight'])
    for i in range(len(l)):
        for j in range(len(x)):
            if l[i]==x[j]:
                l[i]=y[j]
    res = [l]
    pred = clf_rfc.predict(res)
    return pred[0]

df_prec = pd.read_csv('data/symptom_precaution.csv')

def precaution(d):
    df_new_prec = df_prec.loc[df_prec['Disease'] == d]
    return df_new_prec.iat[0,1], df_new_prec.iat[0,2], df_new_prec.iat[0,3], df_new_prec.iat[0,4]

def symptomsList():
    return symptoms.tolist()