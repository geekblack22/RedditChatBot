import voice_db as db

comment_bodys = db.get_comment_bodys()
# comment_ids = db.get_comment_ids()
comment_parent_ids = db.get_comment_parent_ids()
print("Num Comments: ",len(comment_bodys))
parents = []
children = []
conversation_count = 0
count = 0
curr_count = 0
curr_count = int(open("tracking.txt","r").read())
file_interval = 20000
def in_black_list(parent):
    black_list = ["r\\","[","]","https"]
    invalid = False
    for black in black_list:
        if black in parent:
            invalid = True
            break
    return invalid
for i in range(curr_count,len(comment_bodys)):
    # training_file = open("training.txt","a",encoding="utf8")
    # child_file = open("cat.to","a",encoding="utf8")
    count = i
    try:
        if comment_parent_ids[i] == comment_parent_ids[i]:
           
            # if curr_count > count and curr_count != 0:
            #     print("SKIPED: ",count)
            #     continue
            
            parent = db.get_submission( comment_parent_ids[i])
            if parent != None:
                if parent.selftext != "[removed]" and parent.selftext != None:
                    if parent.selftext.strip() == "" :
                        continue
                    # print(parent.selftext.split())   
                    with open(r"data\training_convo_interval_"+str(int(conversation_count/file_interval))+"_database_Start_"+str(curr_count)+".txt","a",encoding="utf8") as f:
                        f.write("PROMT"+'\n')
                        f.write(" ".join(parent.selftext.split()).replace('\\',"") + '\n')
                       
                else:
                    # print(parent.title.split())   
                    if (parent.title.strip() == "" and parent.title != None)  :
                        continue


                    with open(r"data\training_convo_interval_"+str(int(conversation_count/file_interval))+"_database_Start_"+str(curr_count)+".txt","a",encoding="utf8") as f:
                        f.write("PROMT"+'\n')
                        f.write(" ".join(parent.title.split()).replace('\\',"")+'\n')
                        
            
            else:    
                parent = db.get_comment(comment_parent_ids[i])
                if parent == None or parent.body == "" or comment_bodys[i].strip() == "" :
                    print("ERROR NO RESPONSE TO: ",comment_bodys[i])
                    continue
                with open(r"data\training_convo_interval_"+str(int(conversation_count/file_interval))+"_database_Start_"+str(curr_count)+".txt","a",encoding="utf8") as f:
                    f.write("PROMT"+'\n')
                    f.write(" ".join(parent.body.split()).replace('\\',"")+'\n')
                    
           
            with open(r"data\training_convo_interval_"+str(int(conversation_count/file_interval))+"_database_Start_"+str(curr_count)+".txt","a",encoding="utf8") as f:
                f.write("RESPONSE"+'\n')
                f.write(" ".join(comment_bodys[i].split()).replace('\\',"") +'\n')
            print("Conversations: ",conversation_count)
            conversation_count+=1
    except Exception as e:
        with open("tracking.txt","w",encoding="utf8") as f:
                f.write(str(count)) 
        break
with open("tracking.txt","w",encoding="utf8") as f:
                f.write(str(count))
# parent_file = open("cat.from","a",encoding="utf8")
# child_file = open("cat.to","a",encoding="utf8")
# with parent_file as f:
#     for parent in parents:
#         f.write(parent+'\n')
# with child_file as f:
#     for child in children:
#         f.write(child+'\n')
# parent_file.close()
# child_file.close()
