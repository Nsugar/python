alines =  []
for aline_number in range(30):
    new_aline = {'color':'green','point':5,'speed':'slow'}
    alines.append(new_aline)
for aline in alines[:5]:
    print(aline)
print(len(alines))