import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('no_of_facories_in_public_and_private_sector.csv')
df = df.set_index('Year')
df = df[['Public Sector - Total  (cols.  4-10)','Private Sector - Total (Col. 12-20)']]

idf = pd.read_csv('export_import_tradebalance_2012_13_dec_crore_1.csv')
idf['Year'] = idf['Year'].apply(lambda x : x[:-3])
idf = idf.set_index('Year')
idf = idf.ix['2000':'2010']
idf = idf[['Exports (including re-exports)','Imports']]

plt.figure()
plt.suptitle("Yearly Change in Import and Export with respect to No. Public and Private Sector Factories")
ax = plt.subplot(211)
plt.plot(df['Private Sector - Total (Col. 12-20)'], c='b',label='Private Sector')
plt.plot(df['Public Sector - Total  (cols.  4-10)'], c='r', label='Public Sector')
plt.xlabel('Years')
plt.ylabel('No. of Factories')
plt.xticks([2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010])
l = plt.legend(handlelength=0,handletextpad=0,frameon=False)
for line,text in zip(l.get_lines(), l.get_texts()):
	text.set_color(line.get_color())
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

ax1 = plt.subplot(212)
plt.plot(idf['Imports'], c='y',label='Imports')
plt.plot(idf['Exports (including re-exports)'],c='g', label='Exports')
plt.xlabel('Years')
plt.ylabel('Rs. (In Crore)')

plt.xticks([2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010])
ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)
l = plt.legend(handlelength=0,handletextpad=0,frameon=False)

for line,text in zip(l.get_lines(), l.get_texts()):
	text.set_color(line.get_color())
for item in l.legendHandles:
	item.set_visible(False)
plt.show()