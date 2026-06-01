import fakeredis, json, os, threading

PERSIST_FILE = 'redis_data.json'
_save_lock = threading.Lock()

class PersistentFakeRedis:
    def __init__(self, persist_file=PERSIST_FILE):
        self._server = fakeredis.FakeServer()
        self._r = fakeredis.FakeRedis(server=self._server, decode_responses=True)
        self._persist_file = persist_file
        self._load()

    def _load(self):
        if os.path.exists(self._persist_file):
            try:
                with open(self._persist_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                for key, value in data.get('strings', {}).items():
                    self._r.set(key, value)
                for key, members in data.get('sets', {}).items():
                    if members:
                        self._r.sadd(key, *members)
                print(f'[redis] Loaded {len(data.get("strings",{}))} strings, {len(data.get("sets",{}))} sets')
            except Exception as e:
                print(f'[redis] Load failed: {e}')

    def _save(self):
        with _save_lock:
            try:
                strings, sets = {}, {}
                for key in self._r.keys('*'):
                    t = self._r.type(key)
                    if t == 'string' and self._r.ttl(key) == -1:
                        strings[key] = self._r.get(key)
                    elif t == 'set':
                        sets[key] = list(self._r.smembers(key))
                with open(self._persist_file, 'w', encoding='utf-8') as f:
                    json.dump({'strings': strings, 'sets': sets}, f, ensure_ascii=False)
            except Exception as e:
                print(f'[redis] Save failed: {e}')

    def set(self, key, value, ex=None, **kw):
        result = self._r.set(key, value, ex=ex, **kw)
        if ex is None:
            threading.Thread(target=self._save, daemon=True).start()
        return result

    def get(self, key): return self._r.get(key)
    def exists(self, *k): return self._r.exists(*k)
    def ttl(self, key): return self._r.ttl(key)
    def type(self, key): return self._r.type(key)
    def keys(self, p='*'): return self._r.keys(p)
    def smembers(self, key): return self._r.smembers(key)
    def sismember(self, key, val): return self._r.sismember(key, val)
    def incr(self, key): r=self._r.incr(key); threading.Thread(target=self._save,daemon=True).start(); return r
    def incrby(self, key, n): r=self._r.incrby(key,n); threading.Thread(target=self._save,daemon=True).start(); return r

    def delete(self, *keys):
        result = self._r.delete(*keys)
        threading.Thread(target=self._save, daemon=True).start()
        return result

    def sadd(self, key, *values):
        result = self._r.sadd(key, *values)
        threading.Thread(target=self._save, daemon=True).start()
        return result

    def srem(self, key, *values):
        result = self._r.srem(key, *values)
        threading.Thread(target=self._save, daemon=True).start()
        return result

    def __getattr__(self, name):
        return getattr(self._r, name)

r = PersistentFakeRedis()
