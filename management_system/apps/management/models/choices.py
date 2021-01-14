from enum import Enum


class Base(Enum):
    """ Base enum for choices """

    @classmethod
    def choices(cls):
        return tuple((i.name, i.value) for i in cls)


class EnglishLevel(Base):
    NO = 'No'
    A1 = 'A1'
    A2 = 'A2'
    B1 = 'B1'
    B2 = 'B2'
    C1 = 'C1'
    C2 = 'C2'


class PositionStatus(Base):
    ACTIVE = "Active"
    SECURED = "Secured"


class OpportunityPriority(Base):
    LOW = "Low"
    MEDIUM = "Medium"
    HIGH = "High"


class Sex(Base):
    MALE = "Male"
    FEMALE = "Female"
