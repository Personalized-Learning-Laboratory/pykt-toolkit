import pandas as pd
from .utils import sta_infos, write_txt

USER_ID = "user_id"
SKILL_ID = "skill_id"
KEYS = [USER_ID, SKILL_ID]

def read_data_from_csv(read_file, write_file):
    with open(read_file, "r") as f:
        data = f.readlines()[1:]
    user_data = {}
    for line in data:
        uid, submit_time, qid, skill_id, correct, duration = line.strip().split(",")
        if uid not in user_data:
            user_data[uid] = {
                "skill_id": [skill_id],
                "correct": [correct],
                "duration": [duration],
                "submit_time": [submit_time],
                "qid": [qid]
            }
        else:
            user_data[uid]["skill_id"].append(skill_id)
            user_data[uid]["correct"].append(correct)
            user_data[uid]["duration"].append(duration)
            user_data[uid]["submit_time"].append(submit_time)
            user_data[uid]["qid"].append(qid)
    file_content = []
    for uid in user_data:
        userdata = []
        userdata.append([uid, str(len(user_data[uid]['skill_id']))])
        userdata.append(user_data[uid]["qid"])
        userdata.append(user_data[uid]["skill_id"])
        userdata.append(user_data[uid]["correct"])
        userdata.append(user_data[uid]["submit_time"])
        userdata.append(user_data[uid]["duration"])
        #userdata.append(f"{uid},{len(user_data[uid]['skill_id'])}")
        #userdata.append(",".join(user_data[uid]["qid"]))
        #userdata.append(",".join(user_data[uid]["skill_id"]) + "\n")
        #userdata.append(",".join(user_data[uid]["correct"]) + "\n")
        #userdata.append(",".join(user_data[uid]["submit_time"]) + "\n")
        #userdata.append(",".join(user_data[uid]["duration"]) + "\n")
        file_content.append(userdata)
    #with open(write_file, "w") as f:
    #    for userinfo in file_content:
    #        f.write("\n".join(userinfo))
    write_txt(write_file, file_content)
    print("\n[DONE]")

    return

