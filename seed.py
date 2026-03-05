import requests

URL = "http://localhost:8000/matches/"

payload = {
  "script": "暗流涌动 (Trouble Brewing)",
  "storyteller": "Test STM",
  "winning_team": "good",
  "password": "botc",
  "players": [
    {
      "player_id": 1,
      "character": "Imp",
      "initial_alignment": "bad",
      "final_alignment": "bad",
      "survived": False
    },
    {
      "player_id": 2,
      "character": "Poisoner",
      "initial_alignment": "bad",
      "final_alignment": "bad",
      "survived": True
    },
    {
      "player_id": 3,
      "character": "Investigator",
      "initial_alignment": "good",
      "final_alignment": "good",
      "survived": False
    },
    {
      "player_id": 4,
      "character": "Empath",
      "initial_alignment": "good",
      "final_alignment": "good",
      "survived": True
    },
    {
      "player_id": 5,
      "character": "Slayer",
      "initial_alignment": "good",
      "final_alignment": "good",
      "survived": True
    }
  ]
}

# 先创建玩家
players = ["Alice", "Bob", "Charlie", "David", "Eve"]
for p in players:
    requests.post("http://localhost:8000/players/", json={"name": p})

# 插入 1 场对局
res = requests.post(URL, json=payload)
print(res.status_code, res.text)
