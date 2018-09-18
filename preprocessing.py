import pandas as pd
import numpy as np
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import LabelEncoder
df = pd.read_csv("watchers.csv",names = ["project_id","user_id","timestamp"],nrows = 25000) 

pro_lst = np.array(list(set(df['project_id'])))
temp = []
for i in pro_lst:	
	temp.append(np.where(df['project_id'] == i))
	
usr_ids = []
for i in temp:
	u = []
	for j in i:
		usr_ids.append(df['user_id'].values[j]) 

temp.clear()

for i in range(0,len(usr_ids)):
	if len(usr_ids[i])>=10:
		temp.append(usr_ids[i])

usr_ids.clear()
for i in temp:
	usr_ids.append(i)
# print(usr_ids)
temp.clear()

s = set(usr_ids[0])
# print(s)
for i in range(1,len(usr_ids)):
	k = set(usr_ids[i])
	# print(k)
	s = s.union(set(k))

s = list(s)
# label_encoder = LabelEncoder()
# integer_encoded = label_encoder.fit_transform(s)
# # print(integer_encoded)
# onehot_encoder = OneHotEncoder(sparse=False)
# integer_encoded = integer_encoded.reshape(len(integer_encoded), 1)
# onehot_encoded = onehot_encoder.fit_transform(integer_encoded)
# print(onehot_encoded[0])
# print(onehot_encoded[1])