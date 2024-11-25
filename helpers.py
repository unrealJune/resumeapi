class Job:
    def __init__(self, id, title, company, location, timerange, bullets:list):
        self.title = title
        self.id = id
        self.company = company
        self.location = location
        self.timerange = timerange
        self.bullets = bullets

    def serialize(self):
        return {
            'id': self.id,
            'title': self.title,
            'company': self.company,
            'location': self.location,
            'timerange': self.timerange,
            'bullets': [bullet.serialize() for bullet in self.bullets]
        }

class Bullet:
    def __init__(self, text:str, subbullets:list):
        self.text = text,
        self.subbullets = subbullets

    #to json
    def serialize(self):
        return {
            'text': self.text,
            'subbullets': [subbullet.serialize() for subbullet in self.subbullets]
        }