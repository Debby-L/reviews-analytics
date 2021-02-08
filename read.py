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

print('檔案讀取完了, 總共有', len(data), '筆資料')

sum_len = 0
for d in data: #從清單中調出每筆資料的長度
    sum_len = sum_len + len(d) #加總全部資料長度
print ('留言的平均長度為', sum_len/len(data)) #已知共有1000000筆資料

new = []
for d in data: #篩選資料
	if len(d) < 100: #建立條件
		new.append(d) #鍵入新的清單
print('一共有', len(new), '筆留言長度小於100')
print(new[0])
print(new[1])