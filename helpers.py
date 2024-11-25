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

class Resume:
    def __init__(self, name, contact, about, education, skills:list, jobs:list):
        self.name = name
        self.contact = contact
        self.about = about
        self.education = education
        self.skills = skills
        self.jobs = jobs
    
    def serialize(self):
        return {
            'name': self.name,
            'contact': self.contact.serialize(),
            'about': self.about,
            'education': self.education.serialize(),
            'skills': [skill.serialize() for skill in self.skills],
            'jobs': [job.serialize() for job in self.jobs]
        }
    
class Contact:
    def __init__(self, email, location, webLink1, webLink2):
        self.email = email
        self.location = location
        self.webLink1 = webLink1
        self.webLink2 = webLink2

    
    def serialize(self):
        return {
            'email': self.email,
            'location': self.location,
            'webLink1': self.webLink1,
            'webLink2': self.webLink2
        }

class Coursework:
    def __init__(self, headline, courses):
        self.headline = headline
        self.courses = courses

    def serialize(self):
        return {
            'headline': self.headline,
            'courses': [course.serialize() for course in self.courses]
        }

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