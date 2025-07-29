import requests


def header(token):
    headers =  {
    "accept": "*/*",
    "accept-language": "en-US,en;q=0.9,ko-KR;q=0.8,ko;q=0.7",
    "authorization": token,
    "content-type": "application/json",
    "priority": "u=1, i",
    "sec-ch-ua": "\"Not)A;Brand\";v=\"8\", \"Chromium\";v=\"138\", \"Google Chrome\";v=\"138\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"macOS\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "x-context-properties": "eyJsb2NhdGlvbiI6ImNoYXRfaW5wdXQifQ==",
    "x-debug-options": "bugReporterEnabled",
    "x-discord-locale": "ko",
    "x-discord-timezone": "Asia/Seoul",
    "x-super-properties": "eyJvcyI6Ik1hYyBPUyBYIiwiYnJvd3NlciI6IkNocm9tZSIsImRldmljZSI6IiIsInN5c3RlbV9sb2NhbGUiOiJlbi1VUyIsImhhc19jbGllbnRfbW9kcyI6ZmFsc2UsImJyb3dzZXJfdXNlcl9hZ2VudCI6Ik1vemlsbGEvNS4wIChNYWNpbnRvc2g7IEludGVsIE1hYyBPUyBYIDEwXzE1XzcpIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIENocm9tZS8xMzguMC4wLjAgU2FmYXJpLzUzNy4zNiIsImJyb3dzZXJfdmVyc2lvbiI6IjEzOC4wLjAuMCIsIm9zX3ZlcnNpb24iOiIxMC4xNS43IiwicmVmZXJyZXIiOiIiLCJyZWZlcnJpbmdfZG9tYWluIjoiIiwicmVmZXJyZXJfY3VycmVudCI6IiIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6IiIsInJlbGVhc2VfY2hhbm5lbCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjQyMzk2MywiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbCwiY2xpZW50X2xhdW5jaF9pZCI6ImFlYTAzNDJmLWYxMjItNDUyZC1hMjUzLTZkY2ExN2RhZmU4ZCIsImxhdW5jaF9zaWduYXR1cmUiOiJkYzM4NGE4YS1lMjAwLTQyNmQtODIwOC02MTJjYzYxODkwYTQiLCJjbGllbnRfYXBwX3N0YXRlIjoiZm9jdXNlZCIsImNsaWVudF9oZWFydGJlYXRfc2Vzc2lvbl9pZCI6IjYwNmM2NDY5LThjNDctNDgwZS05ZDg1LTdkZjMzMjVjMzA4NiJ9"}
    return headers

def isEditmsg(channel_id,msg_id,token,msg):
    headers = header(token)
    body = {
        "mobile_network_type":"unknown",
        "content":msg,
        "nonce":msg_id,
        "tts":"false",
        "flags":0
        }
    r = requests.post(f"https://discord.com/api/v9/channels/{channel_id}/messages",json=body,headers=headers)

    if r.status_code == 200:
        return {"status":"success"}
    else:
        return {"status":'fail'}

def main():
    msg = input("수정할 메세지를 입력 해 주세요 > ")
    msg_id = int(input("메세지 아이디를 입력 해 주세요 > "))
    channel_id = int(input("수정 할 메세지가 있는 채널 아이디를 적어주세요 > "))
    token = input("디스코드 토큰을 적어주세요 > ")
    if len(msg_id) > 19 or len(channel_id) > 19:
        return input("메세지 id 또는 채널 id의 길이는 19자 입니다.")
    edit = isEditmsg(channel_id,msg_id,token,msg)

    if edit["status"] == "success":
        print("메세지 수정 성공\nhttps://partynextdoor.xyz/")
    else:
        print("메세지 수정 실패\nhttps://partynextdoor.xyz/")

if __name__ == "__main__":
    main()

