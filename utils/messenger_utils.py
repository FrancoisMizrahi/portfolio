import streamlit as st
import pandas as pd
import datetime
import json
import re

from functools import partial


def repair_json(file_name):
    escapes = partial(re.compile(rb'\\u00([\da-f]{2})').sub,lambda m: bytes.fromhex(m[1].decode()),)
    with open(file_name, 'rb') as binary_data:
        repaired = escapes(binary_data.read())
    parsed_json = json.loads(repaired)
    return parsed_json

def get_messenger_data():
    parsed_json = repair_json("data/messenger/message_ano.json")
    return parsed_json


def get_participant_message_counts(parsed_json):
    participants = {}
    for i in parsed_json['messages']:
        if i["sender_name"] in participants.keys():
            participants[i["sender_name"]]["messages_count"] += 1
            if 'reactions' in i.keys():
                participants[i["sender_name"]]["reaction_count"] += len(i["reactions"])
        else:
            participants[i["sender_name"]] = {"messages_count": 0, "reaction_count": 0}
    
    df = pd.DataFrame.from_dict(participants, orient='index').reset_index()
    df['reaction_rate'] = df['reaction_count']/ df['messages_count']
    return df


def get_participant_full_df(parsed_json):
    messages = {}
    for i in parsed_json['messages']:
        messages[i['timestamp_ms']] = {"sender_name": i['sender_name'],
                                    "timestamp": datetime.datetime.fromtimestamp(int(i['timestamp_ms'])/1000),
                                    "year": datetime.datetime.fromtimestamp(int(i['timestamp_ms'])/1000).year,
                                    "month": datetime.datetime.fromtimestamp(int(i['timestamp_ms'])/1000).month,
                                    "day": datetime.datetime.fromtimestamp(int(i['timestamp_ms'])/1000).day,
                                    "day_week": datetime.datetime.fromtimestamp(int(i['timestamp_ms'])/1000).weekday(),
                                    "time": f"{datetime.datetime.fromtimestamp(int(i['timestamp_ms'])/1000).hour}:{datetime.datetime.fromtimestamp(int(i['timestamp_ms'])/1000).minute}:00.000"
                                    }
        if 'content' in i.keys():
            messages[i['timestamp_ms']]["content"] = i['content']
            
        if 'reactions' in i.keys():
            messages[i['timestamp_ms']]["reactions"] = i['reactions']
            messages[i['timestamp_ms']]["reactions_count"] = len(i['reactions'])
            

    return pd.DataFrame.from_dict(messages, orient='index').reset_index()