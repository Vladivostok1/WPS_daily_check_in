import json, os, time
import requests
import notify
sids = [
#     "V02StVuaNcoKrZ3BuvJQ1FcFS_xnG2k00af250d4002664c02f",
#     "V02SWIvKWYijG6Rggo4m0xvDKj1m7ew00a8e26d3002508b828",
#     "V02Sr3nJ9IicoHWfeyQLiXgvrRpje6E00a240b890023270f97",
#     "V02SBsNOf4sJZNFo4jOHdgHg7-2Tn1s00a338776000b669579",
#     "V02S2oI49T-Jp0_zJKZ5U38dIUSIl8Q00aa679530026780e96",
#     "V02ShotJqqiWyubCX0VWTlcbgcHqtSQ00a45564e002678124c",
#     "V02SFiqdXRGnH5oAV2FmDDulZyGDL3M00a61660c0026781be1",
#     "V02S7tldy5ltYcikCzJ8PJQDSy_ElEs00a327c3c0026782526",
#     "V02SPoOluAnWda0dTBYTXpdetS97tyI00a16135e002684bb5c",
#     "V02Sb8gxW2inr6IDYrdHK_ywJnayd6s00ab7472b0026849b17",
#     "V02SwV15KQ_8n6brU98_2kLnnFUDUOw00adf3fda0026934a7f",
#     "V02SC1mOHS0RiUBxeoA8NTliH2h2NGc00a803c35002693584d"
    "V02StVuaNcoKrZ3BuvJQ1FcFS_xnG2k00af250d4002664c02f",
    "V02SWIvKWYijG6Rggo4m0xvDKj1m7ew00a8e26d3002508b828",
    "V02Sr3nJ9IicoHWfeyQLiXgvrRpje6E00a240b890023270f97",
    "V02SBsNOf4sJZNFo4jOHdgHg7-2Tn1s00a338776000b669579",
    "V02S2oI49T-Jp0_zJKZ5U38dIUSIl8Q00aa679530026780e96",
    "V02ShotJqqiWyubCX0VWTlcbgcHqtSQ00a45564e002678124c",
    "V02SFiqdXRGnH5oAV2FmDDulZyGDL3M00a61660c0026781be1",
    "V02S7tldy5ltYcikCzJ8PJQDSy_ElEs00a327c3c0026782526",
    "V02SPoOluAnWda0dTBYTXpdetS97tyI00a16135e002684bb5c",
    "V02Sb8gxW2inr6IDYrdHK_ywJnayd6s00ab7472b0026849b17",
    "V02SwV15KQ_8n6brU98_2kLnnFUDUOw00adf3fda0026934a7f",
    "V02S8fWiw86zsFg1oE5p4hCHAR6GPE000a4e69e2002508b828"

]
mk = 0

def request_re(sid, invite_userid, rep = 30):
    invite_url = 'http://zt.wps.cn/2018/clock_in/api/invite'
    r = requests.post(invite_url, headers={'sid': sid}, data={ 'invite_userid': invite_userid, "client_code": "040ce6c23213494c8de9653e0074YX30", "client": "alipay" } )
    js = json.loads(r.content)
    if js['msg'] == 'tryLater' and rep > 0:
        rep -= 1
        time.sleep(10)
        r = request_re(sid, invite_userid, rep)
    return r
    
invite_userid = os.getenv('USER_ID')
for j in sids:
    try:
        r = request_re(j, invite_userid)
        js = json.loads(r.content)
        if js['result'] == 'ok':
            mk += 1
    except:pass
            
print('成功邀请%d位好友'%(mk))   

PUSH_KEY = os.getenv('PUSH_KEY')
if PUSH_KEY:
    data = {
        'text':'WPS邀请好友任务：成功邀请到%d位好友'%(mk),
        'desp':'成功邀请%d位好友'%(mk)
    }
    print(data)
    notify.post_push(PUSH_KEY,data['desp'],data['text'])
