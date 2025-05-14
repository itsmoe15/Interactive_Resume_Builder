from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class User(UserMixin, db.Model):
    __tablename__ = 'user'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    
    # one-to-many: a user can own multiple CVs
    cvs = db.relationship('CV', back_populates='owner', cascade='all, delete-orphan')

class Style(db.Model):
    __tablename__ = 'style'
    
    id   = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    
    # one-to-many: a style can be used by many CVs
    cvs  = db.relationship('CV', back_populates='style')

class CV(db.Model):
    __tablename__ = 'cv'
    
    id                   = db.Column(db.Integer, primary_key=True, autoincrement=True)
    owner_id             = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), nullable=False)
    full_name            = db.Column(db.String(200), nullable=False)
    job_title            = db.Column(db.String(200), nullable=False)
    email                = db.Column(db.String(200), nullable=False)
    phone_number         = db.Column(db.String(100), nullable=False)
    address              = db.Column(db.String(300))
    professional_summary = db.Column(db.Text)
    skills               = db.Column(db.Text)  # comma-separated list
    style_id             = db.Column(db.Integer, db.ForeignKey('style.id'), nullable=False)
    
    owner = db.relationship('User', back_populates='cvs')
    style = db.relationship('Style', back_populates='cvs')
    work_experiences = db.relationship('WorkExperience', back_populates='cv', cascade='all, delete-orphan')
    educations       = db.relationship('Education',      back_populates='cv', cascade='all, delete-orphan')

class WorkExperience(db.Model):
    __tablename__ = 'work_experience'
    
    id          = db.Column(db.Integer, primary_key=True, autoincrement=True)
    cv_id       = db.Column(db.Integer, db.ForeignKey('cv.id', ondelete='CASCADE'), nullable=False)
    job_title   = db.Column(db.String(200), nullable=False)
    company     = db.Column(db.String(200), nullable=False)
    start_date  = db.Column(db.Date,   nullable=False)
    end_date    = db.Column(db.Date)
    is_current  = db.Column(db.Boolean, nullable=False, default=False)
    description = db.Column(db.Text)
    
    cv = db.relationship('CV', back_populates='work_experiences')

class Education(db.Model):
    __tablename__ = 'education'
    
    id                 = db.Column(db.Integer, primary_key=True, autoincrement=True)
    cv_id              = db.Column(db.Integer, db.ForeignKey('cv.id', ondelete='CASCADE'), nullable=False)
    degree_certificate = db.Column(db.String(200), nullable=False)
    institution        = db.Column(db.String(200), nullable=False)
    start_date         = db.Column(db.Date, nullable=False)
    end_date           = db.Column(db.Date)
    is_current         = db.Column(db.Boolean, nullable=False, default=False)
    description        = db.Column(db.Text)
    
    cv = db.relationship('CV', back_populates='educations')
