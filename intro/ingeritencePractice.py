class Record:
    def __init__(self, artist: str, title: str) -> None:
        self.artist = artist
        self.title = title
        
    def __str__(self) -> str:
        return f"{self.title} ({self.artist})"
    
class RecordShelf(Record):
    def __init__(self) -> None:
        self.__records = []
        
    def add(self, record: Record):
        self.__records.append(record)
        
    def __iter__(self):
        self.n = 0
        return self
    
    def __next__(self):
        if self.n < len(self.__records):
            self.n += 1
            return self.__records[self.n-1]
        else:
            raise StopIteration
        
        
r1 = Record("Beatles", "Revorver")
r2 = Record("Led Zeplin", "IV")
r3 = Record("U2", "Rattle and Hum")

shelf = RecordShelf()
shelf.add(r1)
shelf.add(r2)
shelf.add(r3)

for rec in shelf:
    print(rec)