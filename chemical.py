class Chemical:
    def __init__(self, cas_number, name, banned, classification, melting_point, boiling_point, flashpoint, storage_temp):
        self.cas_number = cas_number
        self.name = name
        self.banned = banned
        self.classification = classification
        self.melting_point = melting_point
        self.boiling_point = boiling_point
        self.flashpoint = flashpoint
        self.storage_temp = storage_temp
