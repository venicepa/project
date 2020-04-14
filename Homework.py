# coding=UTF-8
"""
串列生成一副有52張的撲克牌,洗牌以後 再發給四個玩家, 然後印出每個玩家手上的牌
"""
# 這代表從函式庫裡把 random 這個函式拿出來
# 然後把random這個函式裡面的 shuffle 這個東西拿出來使用
# shuffle 可以幹嘛？ 可以很簡單的把list裡面的成員排序直接打亂
from random import shuffle

# 先產生出一副52張 撲克牌 
# 花色先用 1234 依序代表 ♡ ♢ ♤ ♧
pokers1 = [ "1" + str(x) for x in range(1, 14)]
pokers2 = [ "2" + str(x) for x in range(1, 14)]
pokers3 = [ "3" + str(x) for x in range(1, 14)]
pokers4 = [ "4" + str(x) for x in range(1, 14)]
pokers = pokers1 + pokers2 + pokers3 + pokers4

#洗牌
shuffle(pokers)

player1 = []
player2 = []
player3 = []
player4 = []
players = [player1, player2, player3, player4]

# 發牌
for pocker in pokers:
    index = pokers.index(pocker) % 4
    if index == 1:
        player1.append(pocker)
    elif index == 2:
        player2.append(pocker)
    elif index == 3:
        player3.append(pocker)
    elif index == 0:
        player4.append(pocker)

#印出每個玩家手上的牌
for player in players:
    print("玩家" + str(players.index(player) + 1) + " : "),
    for card in player:
        
        if ( card[0] == str(1) ):
          print("♡" + card[1:]),
        elif ( card[0] == str(2) ):
          print("♢" + card[1:]),
        elif ( card[0] == str(3) ):
          print("♤" + card[1:]),
        elif ( card[0] == str(4) ):
          print("♧" + card[1:]),

        #這裡換行只是單純為了排版
        if (player.index(card) == 12):
          print("")
