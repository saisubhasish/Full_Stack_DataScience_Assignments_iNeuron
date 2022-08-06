df = pd.read_excel('D:/FSDS-iNeuron/3.Resource/dataFSDS/Attribute DataSet.xlsx', sheet_name = 'Sai', header= None, names= ['a', 'b', 'c', 'd'])
df1 = pd.read_csv('D:/FSDS-iNeuron/3.Resource/dataFSDS/haberman.csv', header= None, names=['age', "patient's year of operation", 'Number of positive', 'Survival Status'])
df2 = pd.read_csv('D:/FSDS-iNeuron/3.Resource/dataFSDS/haberman(1).csv', sep='@')  # online json viewer
pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/Smarket.csv')
a = pd.read_html('https://www.basketball-reference.com/leagues/NBA_2015_totals.html')
df.to_csv('D:/FSDS-iNeuron/3.Resource/dataFSDS/AttributeDataset.csv', sep='#')
