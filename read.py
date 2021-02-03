#讀取檔案
#利用計數器執行每1000筆為一單位，讀取資料
data = []
count = 0
with open ('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0: #設定1000的餘數等於0
		   print(len(data))

print(data[0])
