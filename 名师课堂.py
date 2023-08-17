import requests
import time
import json

list =[]

request_data = {
    "clientSource": "web",
    "clockVideoId": "",
    "startTime": 1692101239303,
    "timePoint": 0,
    "duration": "",
    "learnSource": 1,
    "learnType": "1",
    "courseId": "",
    "fileSizeAtPath": "",
    "clientVersion": "1.0",
    "token": "",
    "uid": "",
    "teacherId": "",
    "enterType": "integral"
}

for i in list:
  timePoint = 0
  duration = 10
  a =0
  print("当前课程名称%s"%i["courseName"])
  while True:

    if(timePoint>60):
      a+=1
      timePoint = i["duration"]
      duration = i["duration"]
      if(a==3):break


    courseId = i["courseId"]
    request_data["timePoint"] = timePoint
    request_data["duration"] = duration
    request_data["courseId"] = courseId
    url = "https://api.mingshiclass.com/shixun/submitStudyRecord1.0"
    response = requests.post(url, json=request_data)
    timePoint += 20
    duration += 20
    print(request_data)
    print(json.loads(response.text)['data']['resultStr'])

    time.sleep(10)