import matplotlib.pyplot as plt
  
counties = []
cases = []
  
f = open('umdCounty.txt','r')
for row in f:
    row = row.split(' ')
    counties.append(row[0])
    cases.append(float(int(row[0])))
  
plt.bar(counties, cases, color = 'g', label = 'File Data')
  
plt.xlabel('County', fontsize = 12)
plt.ylabel('Case Number', fontsize = 12)
  
plt.title('Cases per County', fontsize = 20)
plt.legend()
plt.show()