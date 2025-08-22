club = {"Music Club":{(100 , "Rachel"), (101 , "Pheobe")}, "Dance Club" : {(200, "Joy"),  (201, "Chandler")} , "Sports Club":{(300, "Rose"), (301, "Gunther")}}
print(club)


#Add a new club with members

club["Arts Club"] = {(400, "Miya"), (401 , "Maya")}
print(club)

#Add/remove students from clubs

club["Dance Club"].remove((200, "Joy"))
print("AFTER REMOVED A STUDENT FROM CLUB",club)


club["Dance Club"].add((203, "Emma"))
print("AFTER ADD STUDENT FROM CLUB",club)