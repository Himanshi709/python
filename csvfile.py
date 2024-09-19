import pandas as pd

data ={
"Name" :["shipra","vidhi","nikita"],
"Age" :[20,22,19],
"City":["ghaziabad","delhi","noida"]

}
filepath=r"C:\Users\Lenovo\Desktop\pythonws\sample1.xlsx"
df= pd.DataFrame(data)
df.to_csv(filepath ) 
df = pd.read_csv(filepath)
print(df.head())