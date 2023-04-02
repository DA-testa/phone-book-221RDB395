# python

def _hash_func(self, s):
    ans = 0
    for c in reversed(s):
        ans = (ans * self._multiplier + ord(c)) % self._prime
     return ans % self.bucket_count
def add(self, string):
    hashed = self._hash_func(string)
    bucket = self.buckts[hashed]
    if string not in bucket:
        self.buckets[hashed] = [string] + bucket
        
def delete(self, string):
    hashed = self._hash_func(string)
    bucket = self.buckts[hashed]
    for i in range(len(bucket)):
        if bucket[i] == string:
            bucket.pop(i)
            break

def find(self, string):
    hashed = self._hash_func(string)
    if string in self.buckets[hashed]:
        return "yes"
    return "no"
