import time
import progressbar


#讀取檔案
#利用計數器執行每1000筆為一單位，讀取資料
data = []
count = 0
bar = progressbar.ProgressBar(max_value=1000000) 
with open ('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		bar.update(count)
		

print('檔案讀取完了, 總共有', len(data), '筆資料')

print(data[0]) #print out the first one data

sum_len = 0
for d in data: #從清單中調出每筆資料的長度
    sum_len = sum_len + len(d) #加總全部資料長度
print ('留言的平均長度為', sum_len/len(data)) #已知共有1000000筆資料

new = []
for d in data: #篩選資料
	if len(d) < 100: #建立條件"設定留言長度小於100"
		new.append(d) #將找出的留言建立成為新的清單
print('一共有', len(new), '筆留言長度小於100') #印出有幾筆
print(new[0]) #挑選新清單其中第一項
print(new[1]) #挑選新清單其中第二項

good = [] 
for d in data:
	if 'good' in d:#從資料篩選出含有'good'的留言
	   good.append(d)
print('一共有', len(good), '筆留言提到good')

#快寫法
good = [d for d in data if 'good' in d] 
# 開頭d =good.append(d), d = 留言
# d 可以變換成任何數字/布林值, 留言被1取代

bad = ['bad' in d for d in data]
#每一筆留言中包含'bad' 顯示"true or false"
#基礎寫法：
#bad = []
#for d in data:
	#bad.append('bad' in d)


#文字計數
#加入計時 import time-->加入模組
start_time = time.time() #設定查詢資料起始時間
wc = {} #word count
for d in data: #d=留言
	words = d.split(' ') #分割每個字，split本身預設值就是空白鍵，不寫也沒關係，而且可以避免'空字串'被算進次數
	for word in words: #讀取每一個字
		if word in wc: 
			wc[word] += 1 #查找wc字典中的word並計算
		else:
			wc[word] = 1 #新增新字進字典

#將資料格式化，建立word=key, wc=value
for word in wc:
	if wc[word] > 1000000:
		print(word, wc[word])

print(len(wc)) #字典的長度
end_time = time.time() #設定查詢資料結束時間
print('花了', end_time - start_time, 'second') #計算時計花時間


while True:
	word = input('請問你想查甚麼字:')
	if word == 'q':
		break
	if word in wc:
		print(word, '出現過的次數為: ', wc[word])
	else:
		print('這個字沒有出現過喔!')
print('感謝使用本查詢功能')

