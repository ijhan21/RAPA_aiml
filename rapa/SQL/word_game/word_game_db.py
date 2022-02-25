import random
import time
import pyglet # py sound for linux, pip install pyglet 설치
import sqlite3
from datetime import datetime
words = []                                   # 영어 단어 리스트(1000개 로드)
game_cnt = 1                                 # 게임 시도 횟수
corr_cnt = 0                                 # 정답 개수
# DB생성 #auto commit : 실행하면 db에 바로 반영
conn = sqlite3.connect("wordgameDB.db", isolation_level=None)
# 커서객체 생성
cur = conn.cursor()
# DB Table 만들기
# id 자동증가 : autoincrement
# 정답수 : corr_cnt
# 걸린시간 : record txt
# 저장한시간
cur.execute("create table if not exists wordgame(id integer primary key autoincrement, \
    corr_cnt integer not null, record text not null, regdate text not null)")
with open('./data/word.txt', 'r') as f:  # 문제 txt 파일 로드
    for c in f:
        words.append(c.strip())
print(words)                                 # 단어 리스트 확인
input("Ready? Press Enter Key!")             # Enter Game Start!sq
start = time.time()                          # Start Time
while game_cnt <= 5:                         # 5회 반복
    random.shuffle(words)                    # List shuffle!
    que_word = random.choice(words)                 # List -> words random extract!
    print()
    print("*Question # {}".format(game_cnt))
    print(que_word)                                 # 문제 출력
    input_word = input()                              # 타이핑 입력
    print()
    if str(que_word).strip() == str(input_word).strip():     # 입력 확인(공백제거)
        good_sound = pyglet.resource.media(                  # 정답 소리 재생
            'assets/good.wav',
        )
        good_sound.play()
        print("Pass!")
        corr_cnt += 1                         # 정답 개수 카운트
    else:
        bad_sound = pyglet.resource.media(              # 오답 소리 재생
            'assets/bad.wav',
        )
        bad_sound.play()
        print("Wrong!")
    game_cnt += 1                                   # 다음 문제 전환
time.sleep(0.2)  # 단위 : sec, 마지막 문제 소리 재생을 위해 시간 지연
end = time.time()                            # End Time
exe_time = end - start                             # 총 게임 시간
exe_time = format(exe_time, ".3f")                       # 소수 셋째 자리 출력(시간)
if corr_cnt >= 3:                             # 3개 이상 합격
    print("결과 : 합격")
else:
    print("불합격")

#################################################
# 기록 DB 삽입
sql = "INSERT INTO wordgame('corr_cnt','record','regdate') values (%s,'%s','%s');"%(corr_cnt, str(exe_time), datetime.now())
# print(sql)
cur.execute(sql)
conn.commit()
conn.close()
#################################################33
# 수행 시간 출력
print("게임 시간 :", exe_time, "초", "정답 개수 : {}".format(corr_cnt))
# 시작지점
if __name__ == '__main__':
    pass