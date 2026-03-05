from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import relationship
import datetime
from database import Base

class Player(Base):
    __tablename__ = "players"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    
    matches = relationship("MatchPlayer", back_populates="player")

class Match(Base):
    __tablename__ = "matches"
    
    id = Column(Integer, primary_key=True, index=True)
    date = Column(DateTime, default=datetime.datetime.utcnow)
    script = Column(String)  # 游玩剧本（如：暗流涌动）
    storyteller = Column(String)  # 说书人名称
    winning_team = Column(String)  # 获胜阵营 "good" 或 "bad"
    
    players = relationship("MatchPlayer", back_populates="match")

class MatchPlayer(Base):
    __tablename__ = "match_players"
    
    id = Column(Integer, primary_key=True, index=True)
    match_id = Column(Integer, ForeignKey("matches.id"))
    player_id = Column(Integer, ForeignKey("players.id"))
    
    character = Column(String)  # 角色名称
    initial_alignment = Column(String)  # 初始阵营 "good" 或 "bad"
    final_alignment = Column(String)    # 最终阵营 "good" 或 "bad"
    survived = Column(Boolean, default=False) # 是否存活
    
    match = relationship("Match", back_populates="players")
    player = relationship("Player", back_populates="matches")
