from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class Audition(Base):
    __tablename__ = 'auditions'

    id = Column(Integer, primary_key=True)
    actor = Column(String)
    location = Column(String)
    phone = Column(Integer)
    hired = Column(Boolean, default=False)
    role_id = Column(Integer, ForeignKey('roles.id'))

    # Audition.role returns an instance of role associated with this audition
    role = relationship('Role', back_populates='auditions')

    def call_back(self):
        """Changes the hired attribute to True."""
        self.hired = True

    def __repr__(self):
        return f'<Audition actor={self.actor} hired={self.hired}>'


class Role(Base):
    __tablename__ = 'roles'

    id = Column(Integer, primary_key=True)
    character_name = Column(String)

    # Role.auditions returns all auditions associated with this role
    auditions = relationship('Audition', back_populates='role')

    def actors(self):
        """Returns a list of names from the actors associated with this role."""
        return [a.actor for a in self.auditions]

    def locations(self):
        """Returns a list of locations from the auditions associated with this role."""
        return [a.location for a in self.auditions]

    def lead(self):
        """Returns the first instance of the audition hired for this role."""
        hired_list = [a for a in self.auditions if a.hired]
        if hired_list:
            return hired_list[0]
        return 'no actor has been hired for this role'

    def understudy(self):
        """Returns the second instance of the audition hired for this role."""
        hired_list = [a for a in self.auditions if a.hired]
        if len(hired_list) > 1:
            return hired_list[1]
        return 'no actor has been hired for understudy for this role'

    def __repr__(self):
        return f'<Role character_name={self.character_name}>'