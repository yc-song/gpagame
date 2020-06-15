'''
🎉이번학기도 어김없이 돌아온 고팸배 학점내기
(버전: 3)
°목적: 고팸 인간들의 학점 평균을 맞춰라!
°갠톡으로 예상학점/자기학점(해당자만) 저에게 보내세요.
°기한은 7/1 저녁 6시까지.
°조건: 예상평균과 실제평균의 차가 1을 초과하면 실격!
°상품-♡♡여러분의 후원 부탁드려요♡♡
1등:
2등:
3등:
꼴지:
'''
import pandas as pd
df = pd.read_csv('db.csv', encoding='utf-8') #csv 불러옴
dev=[] #편차 저장을 위한 list
present=[]
# estimated[df["이름"]]=float(df["예상학점"])
# real[df["이름"]]=float(df["자기학점"])

a=0
r=0
M=len(df['name'])
for value in df['own']:
    if float(value)>0:
        a+=value
    else:
        M-=1
average=a/M #학점 평균 산출
print("이번 학기 학점 평균은 {}입니다.".format(average))

for value in df['est']:
    dev.append(float(abs(average-value))) #예상학점 대비 편차 계산

df["dev"]=dev
u=0
for i,j in zip(df['name'],df['dev']): #편차 1 넘으면 실격
    if j>=1:
        df=df.drop(u)
        print("실격자가 발생했습니다. 실격자는 {}입니다.".format(i))
    u+=1
N=len(df['name'])
while len(present)<3: #선물 리스트 정리
    present.append("1등 상품입니다")
    present.append("2등 상품입니다")
    present.append("3등 상품입니다")
    break
while 3<=len(present)<=N:
    present.append("없습니다")
    if len(present)==N-1:
        present.append("꼴찌 상품입니다")
        break

df=df.sort_values(by="dev",axis=0,ascending=True) #편차로 서열 정리
df["present"]=present
for i,j,k in zip(df['name'],df["dev"],df["present"]): #최종 결과 출력
    r+=1
    print("{}등은 {}, 편차는 {}입니다. 선물은 {}.".format(r,i,round(j,3),k))

