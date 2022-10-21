import voice_db as db

comments = db.get_comments()
parents = []
children = []
conversation_count = 0

for comment in comments:
    parent_file = open("cat.from","a",encoding="utf8")
    child_file = open("cat.to","a",encoding="utf8")
    if comment.parentId == comment.parentId:
       
        
        parent = db.get_submission( comment.parentId)
        if parent != None:
            if parent.selftext != "[removed]" and parent.selftext != None:
                if parent.selftext.strip() == "":
                    continue
                # print(parent.selftext.split())   
                with parent_file as f:
               
                    f.write(" ".join(parent.selftext.split()) + '\n')
            else:
                # print(parent.title.split())   
                if parent.title.strip() == "" and parent.title != None:
                    continue


                with parent_file as f:

                    f.write(" ".join(parent.title.split())+'\n')
        
        else:    
            parent = db.get_comment(comment.parentId)
            if parent == None or parent.body == "" or comment.body.strip() == "" :
                print("ERROR NO RESPONSE TO: ",comment.body)
                continue
            with parent_file as f:   
                f.write(" ".join(parent.body.split())+'\n')
        conversation_count+=1
        with child_file as f:
            f.write(" ".join(comment.body.split())+'\n')
        print("Conversations: ",conversation_count)

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
