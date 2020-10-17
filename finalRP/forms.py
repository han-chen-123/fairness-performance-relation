from flask_wtf import FlaskForm
from wtforms.fields import StringField, IntegerField, SubmitField, RadioField, SelectField, TextField, DateField
from wtforms.validators import DataRequired, InputRequired
from wtforms.validators import DataRequired
import random
import mysql.connector
from mysql.connector import Error

class Consent(FlaskForm):
    participant_name = TextField('', validators = [DataRequired()])
    researcher_name = TextField('', validators = [DataRequired()])
    response = RadioField('', choices=[('Agree','I agree to the above terms and conditions'),('Disagree','I disagree to the above terms and conditions')], validators=[DataRequired()])
    # date = DateField('')
    submit10 = SubmitField('Next')

class HomePage(FlaskForm):
    age = SelectField('Please Enter your age:', choices=[(str(i),i) for i in range(18,70)],validators=[DataRequired()])
    gender = RadioField('Please select your gender:', choices=[('male','Male'),('female','Female')],validators=[DataRequired()])
    education = RadioField('Please select your edcuation degree:', choices=[('high school','High School'),('bachelors','Bachelors'),('masters','Masters'),('phd','PhD')],validators=[DataRequired()])
    submit1 = SubmitField('Next')

class FirstQuestion(FlaskForm):

    q1 = RadioField('',choices=[('Strongly Disagree','Strongly Disagree'),('Disagree','Disagree'),('Neither Agree nor Disagree','Neither Agree nor Disagree'),('Agree','Agree'),('Strongly Agree','Strongly Agree')], validators=[DataRequired()])
    q2 = RadioField('',choices=[('Strongly Disagree','Strongly Disagree'),('Disagree','Disagree'),('Neither Agree nor Disagree','Neither Agree nor Disagree'),('Agree','Agree'),('Strongly Agree','Strongly Agree')], validators=[DataRequired()])
    q3 = RadioField('',choices=[('Strongly Disagree','Strongly Disagree'),('Disagree','Disagree'),('Neither Agree nor Disagree','Neither Agree nor Disagree'),('Agree','Agree'),('Strongly Agree','Strongly Agree')], validators=[DataRequired()])
    q4 = RadioField('',choices=[('Strongly Disagree','Strongly Disagree'),('Disagree','Disagree'),('Neither Agree nor Disagree','Neither Agree nor Disagree'),('Agree','Agree'),('Strongly Agree','Strongly Agree')], validators=[DataRequired()])
    q5 = RadioField('',choices=[('Strongly Disagree','Strongly Disagree'),('Disagree','Disagree'),('Neither Agree nor Disagree','Neither Agree nor Disagree'),('Agree','Agree'),('Strongly Agree','Strongly Agree')], validators=[DataRequired()])
    q6 = RadioField('',choices=[('Strongly Disagree','Strongly Disagree'),('Disagree','Disagree'),('Neither Agree nor Disagree','Neither Agree nor Disagree'),('Agree','Agree'),('Strongly Agree','Strongly Agree')], validators=[DataRequired()])
    q7 = RadioField('',choices=[('Satisfication','Satisfication'),('Neither statisfication nor Dissatisfaction','Neither statisfication nor Dissatisfaction'),('Dissatisfaction','Dissatisfaction')], validators=[DataRequired()])
    q8 = RadioField('',choices=[('Machine selection and human selection match very well','Machine selection and human selection match very well'),('ARA did not consider the total amount of applicant','ARA did not consider the total amount of applicant'),('little difference is allowed','little difference is allowed'),('Bias may affect the result','Bias may affect the result'),('I dont know','I dont know')], validators=[DataRequired()])

    submit2 = SubmitField('Next')
    submit12 = SubmitField('Next')

class SecondQuestion(FlaskForm):

    q1 = RadioField('',choices=[('Strongly Disagree','Strongly Disagree'),('Disagree','Disagree'),('Neither Agree nor Disagree','Neither Agree nor Disagree'),('Agree','Agree'),('Strongly Agree','Strongly Agree')], validators=[DataRequired()])
    q2 = RadioField('',choices=[('Strongly Disagree','Strongly Disagree'),('Disagree','Disagree'),('Neither Agree nor Disagree','Neither Agree nor Disagree'),('Agree','Agree'),('Strongly Agree','Strongly Agree')], validators=[DataRequired()])
    q3 = RadioField('',choices=[('Strongly Disagree','Strongly Disagree'),('Disagree','Disagree'),('Neither Agree nor Disagree','Neither Agree nor Disagree'),('Agree','Agree'),('Strongly Agree','Strongly Agree')], validators=[DataRequired()])
    q4 = RadioField('',choices=[('Strongly Disagree','Strongly Disagree'),('Disagree','Disagree'),('Neither Agree nor Disagree','Neither Agree nor Disagree'),('Agree','Agree'),('Strongly Agree','Strongly Agree')], validators=[DataRequired()])
    q5 = RadioField('',choices=[('Strongly Disagree','Strongly Disagree'),('Disagree','Disagree'),('Neither Agree nor Disagree','Neither Agree nor Disagree'),('Agree','Agree'),('Strongly Agree','Strongly Agree')], validators=[DataRequired()])
    q6 = RadioField('',choices=[('Strongly Disagree','Strongly Disagree'),('Disagree','Disagree'),('Neither Agree nor Disagree','Neither Agree nor Disagree'),('Agree','Agree'),('Strongly Agree','Strongly Agree')], validators=[DataRequired()])
    q7 = RadioField('',choices=[('Satisfication','Satisfication'),('Neither statisfication nor Dissatisfaction','Neither statisfication nor Dissatisfaction'),('Dissatisfaction','Dissatisfaction')], validators=[DataRequired()])
    q8 = RadioField('',choices=[('Machine selection and human selection match very well','Machine selection and human selection match very well'),('ARA did not consider the total amount of applicant','ARA did not consider the total amount of applicant'),('little difference is allowed','little difference is allowed'),('Bias may affect the result','Bias may affect the result'),('I dont know','I dont know')], validators=[DataRequired()])
    submit3 = SubmitField('Next')
    submit12 = SubmitField('Next')

class ChartFig(FlaskForm):
    q1 = RadioField('',choices=[('applicant','applicant'),('recruiter','recruiter')], validators=[DataRequired()])
    q2 = RadioField('',choices=[('Satisfication','Satisfication'),(' Neither statisfication nor Dissatisfaction',' Neither statisfication nor Dissatisfaction'),('Dissatisfaction','Dissatisfaction')], validators=[DataRequired()])
    q3 = RadioField('',choices=[('Machine selection and human selection match very well','Machine selection and human selection match very well'),('ARA did not consider the total amount of applicant','ARA did not consider the total amount of applicant'),('little difference is allowed','little difference is allowed'),('Bias may affect the result','Bias may affect the result'),('I dont know','I dont know')], validators=[DataRequired()])

    submit9 = SubmitField('Next')
    submit11 = SubmitField('Next')

    submit13 = SubmitField('Next')


class ThirdQuestion(FlaskForm):

    q1 = RadioField('',choices=[('Strongly Disagree','Strongly Disagree'),('Disagree','Disagree'),('Neither Agree nor Disagree','Neither Agree nor Disagree'),('Agree','Agree'),('Strongly Agree','Strongly Agree')], validators=[DataRequired()])
    q2 = RadioField('',choices=[('Strongly Disagree','Strongly Disagree'),('Disagree','Disagree'),('Neither Agree nor Disagree','Neither Agree nor Disagree'),('Agree','Agree'),('Strongly Agree','Strongly Agree')], validators=[DataRequired()])
    q3 = RadioField('',choices=[('Strongly Disagree','Strongly Disagree'),('Disagree','Disagree'),('Neither Agree nor Disagree','Neither Agree nor Disagree'),('Agree','Agree'),('Strongly Agree','Strongly Agree')], validators=[DataRequired()])
    q4 = RadioField('',choices=[('Strongly Disagree','Strongly Disagree'),('Disagree','Disagree'),('Neither Agree nor Disagree','Neither Agree nor Disagree'),('Agree','Agree'),('Strongly Agree','Strongly Agree')], validators=[DataRequired()])
    q5 = RadioField('',choices=[('Strongly Disagree','Strongly Disagree'),('Disagree','Disagree'),('Neither Agree nor Disagree','Neither Agree nor Disagree'),('Agree','Agree'),('Strongly Agree','Strongly Agree')], validators=[DataRequired()])
    q6 = RadioField('',choices=[('Strongly Disagree','Strongly Disagree'),('Disagree','Disagree'),('Neither Agree nor Disagree','Neither Agree nor Disagree'),('Agree','Agree'),('Strongly Agree','Strongly Agree')], validators=[DataRequired()])
    q7 = RadioField('',choices=[('Satisfication','Satisfication'),('Neither statisfication nor Dissatisfaction','Neither statisfication nor Dissatisfaction'),('Dissatisfaction','Dissatisfaction')], validators=[DataRequired()])
    q8 = RadioField('',choices=[('Machine selection and human selection match very well','Machine selection and human selection match very well'),('ARA did not consider the total amount of applicant','ARA did not consider the total amount of applicant'),('little difference is allowed','little difference is allowed'),('Bias may affect the result','Bias may affect the result'),('I dont know','I dont know')], validators=[DataRequired()])

    submit4 = SubmitField('Next')

class FourthQuestion(FlaskForm):
    q1 = RadioField('',choices=[('Strongly Disagree','Strongly Disagree'),('Disagree','Disagree'),('Neither Agree nor Disagree','Neither Agree nor Disagree'),('Agree','Agree'),('Strongly Agree','Strongly Agree')], validators=[DataRequired()])
    q2 = RadioField('',choices=[('Strongly Disagree','Strongly Disagree'),('Disagree','Disagree'),('Neither Agree nor Disagree','Neither Agree nor Disagree'),('Agree','Agree'),('Strongly Agree','Strongly Agree')], validators=[DataRequired()])
    q3 = RadioField('',choices=[('Strongly Disagree','Strongly Disagree'),('Disagree','Disagree'),('Neither Agree nor Disagree','Neither Agree nor Disagree'),('Agree','Agree'),('Strongly Agree','Strongly Agree')], validators=[DataRequired()])
    q4 = RadioField('',choices=[('Strongly Disagree','Strongly Disagree'),('Disagree','Disagree'),('Neither Agree nor Disagree','Neither Agree nor Disagree'),('Agree','Agree'),('Strongly Agree','Strongly Agree')], validators=[DataRequired()])
    q5 = RadioField('',choices=[('Strongly Disagree','Strongly Disagree'),('Disagree','Disagree'),('Neither Agree nor Disagree','Neither Agree nor Disagree'),('Agree','Agree'),('Strongly Agree','Strongly Agree')], validators=[DataRequired()])
    q6 = RadioField('',choices=[('Strongly Disagree','Strongly Disagree'),('Disagree','Disagree'),('Neither Agree nor Disagree','Neither Agree nor Disagree'),('Agree','Agree'),('Strongly Agree','Strongly Agree')], validators=[DataRequired()])
    q7 = RadioField('',choices=[('Satisfication','Satisfication'),('Neither statisfication nor Dissatisfaction','Neither statisfication nor Dissatisfaction'),('Dissatisfaction','Dissatisfaction')], validators=[DataRequired()])
    q8 = RadioField('',choices=[('Machine selection and human selection match very well','Machine selection and human selection match very well'),('ARA did not consider the total amount of applicant','ARA did not consider the total amount of applicant'),('little difference is allowed','little difference is allowed'),('Bias may affect the result','Bias may affect the result'),('I dont know','I dont know')], validators=[DataRequired()])

    submit5 = SubmitField('Next')


class FifthQuestion(FlaskForm):


    q1 = RadioField('',choices=[('Strongly Disagree','Strongly Disagree'),('Disagree','Disagree'),('Neither Agree nor Disagree','Neither Agree nor Disagree'),('Agree','Agree'),('Strongly Agree','Strongly Agree')], validators=[DataRequired()])
    q2 = RadioField('',choices=[('Strongly Disagree','Strongly Disagree'),('Disagree','Disagree'),('Neither Agree nor Disagree','Neither Agree nor Disagree'),('Agree','Agree'),('Strongly Agree','Strongly Agree')], validators=[DataRequired()])
    q3 = RadioField('',choices=[('Strongly Disagree','Strongly Disagree'),('Disagree','Disagree'),('Neither Agree nor Disagree','Neither Agree nor Disagree'),('Agree','Agree'),('Strongly Agree','Strongly Agree')], validators=[DataRequired()])
    q4 = RadioField('',choices=[('Strongly Disagree','Strongly Disagree'),('Disagree','Disagree'),('Neither Agree nor Disagree','Neither Agree nor Disagree'),('Agree','Agree'),('Strongly Agree','Strongly Agree')], validators=[DataRequired()])
    q5 = RadioField('',choices=[('Strongly Disagree','Strongly Disagree'),('Disagree','Disagree'),('Neither Agree nor Disagree','Neither Agree nor Disagree'),('Agree','Agree'),('Strongly Agree','Strongly Agree')], validators=[DataRequired()])
    q6 = RadioField('',choices=[('Strongly Disagree','Strongly Disagree'),('Disagree','Disagree'),('Neither Agree nor Disagree','Neither Agree nor Disagree'),('Agree','Agree'),('Strongly Agree','Strongly Agree')], validators=[DataRequired()])
    q7 = RadioField('',choices=[('Satisfication','Satisfication'),('Neither statisfication nor Dissatisfaction','Neither statisfication nor Dissatisfaction'),('Dissatisfaction','Dissatisfaction')], validators=[DataRequired()])
    q8 = RadioField('',choices=[('Machine selection and human selection match very well','Machine selection and human selection match very well'),('ARA did not consider the total amount of applicant','ARA did not consider the total amount of applicant'),('little difference is allowed','little difference is allowed'),('Bias may affect the result','Bias may affect the result'),('I dont know','I dont know')], validators=[DataRequired()])
    submit6 = SubmitField('Next')


class SixthQuestion(FlaskForm):


    q1 = RadioField('',choices=[('Strongly Disagree','Strongly Disagree'),('Disagree','Disagree'),('Neither Agree nor Disagree','Neither Agree nor Disagree'),('Agree','Agree'),('Strongly Agree','Strongly Agree')], validators=[DataRequired()])
    q2 = RadioField('',choices=[('Strongly Disagree','Strongly Disagree'),('Disagree','Disagree'),('Neither Agree nor Disagree','Neither Agree nor Disagree'),('Agree','Agree'),('Strongly Agree','Strongly Agree')], validators=[DataRequired()])
    q3 = RadioField('',choices=[('Strongly Disagree','Strongly Disagree'),('Disagree','Disagree'),('Neither Agree nor Disagree','Neither Agree nor Disagree'),('Agree','Agree'),('Strongly Agree','Strongly Agree')], validators=[DataRequired()])
    q4 = RadioField('',choices=[('Strongly Disagree','Strongly Disagree'),('Disagree','Disagree'),('Neither Agree nor Disagree','Neither Agree nor Disagree'),('Agree','Agree'),('Strongly Agree','Strongly Agree')], validators=[DataRequired()])
    q5 = RadioField('',choices=[('Strongly Disagree','Strongly Disagree'),('Disagree','Disagree'),('Neither Agree nor Disagree','Neither Agree nor Disagree'),('Agree','Agree'),('Strongly Agree','Strongly Agree')], validators=[DataRequired()])
    q6 = RadioField('',choices=[('Strongly Disagree','Strongly Disagree'),('Disagree','Disagree'),('Neither Agree nor Disagree','Neither Agree nor Disagree'),('Agree','Agree'),('Strongly Agree','Strongly Agree')], validators=[DataRequired()])
    q7 = RadioField('',choices=[('Satisfication','Satisfication'),('Neither statisfication nor Dissatisfaction','Neither statisfication nor Dissatisfaction'),('Dissatisfaction','Dissatisfaction')], validators=[DataRequired()])
    q8 = RadioField('',choices=[('Machine selection and human selection match very well','Machine selection and human selection match very well'),('ARA did not consider the total amount of applicant','ARA did not consider the total amount of applicant'),('little difference is allowed','little difference is allowed'),('Bias may affect the result','Bias may affect the result'),('I dont know','I dont know')], validators=[DataRequired()])
    submit7 = SubmitField('Next')


class SeventhQuestion(FlaskForm):


    q1 = RadioField('',choices=[('Strongly Disagree','Strongly Disagree'),('Disagree','Disagree'),('Neither Agree nor Disagree','Neither Agree nor Disagree'),('Agree','Agree'),('Strongly Agree','Strongly Agree')], validators=[DataRequired()])
    q2 = RadioField('',choices=[('Strongly Disagree','Strongly Disagree'),('Disagree','Disagree'),('Neither Agree nor Disagree','Neither Agree nor Disagree'),('Agree','Agree'),('Strongly Agree','Strongly Agree')], validators=[DataRequired()])
    q3 = RadioField('',choices=[('Strongly Disagree','Strongly Disagree'),('Disagree','Disagree'),('Neither Agree nor Disagree','Neither Agree nor Disagree'),('Agree','Agree'),('Strongly Agree','Strongly Agree')], validators=[DataRequired()])
    q4 = RadioField('',choices=[('Strongly Disagree','Strongly Disagree'),('Disagree','Disagree'),('Neither Agree nor Disagree','Neither Agree nor Disagree'),('Agree','Agree'),('Strongly Agree','Strongly Agree')], validators=[DataRequired()])
    q5 = RadioField('',choices=[('Strongly Disagree','Strongly Disagree'),('Disagree','Disagree'),('Neither Agree nor Disagree','Neither Agree nor Disagree'),('Agree','Agree'),('Strongly Agree','Strongly Agree')], validators=[DataRequired()])
    q6 = RadioField('',choices=[('Strongly Disagree','Strongly Disagree'),('Disagree','Disagree'),('Neither Agree nor Disagree','Neither Agree nor Disagree'),('Agree','Agree'),('Strongly Agree','Strongly Agree')], validators=[DataRequired()])
    q7 = RadioField('',choices=[('Satisfication','Satisfication'),('Neither statisfication nor Dissatisfaction','Neither statisfication nor Dissatisfaction'),('Dissatisfaction','Dissatisfaction')], validators=[DataRequired()])
    q8 = RadioField('',choices=[('Machine selection and human selection match very well','Machine selection and human selection match very well'),('ARA did not consider the total amount of applicant','ARA did not consider the total amount of applicant'),('little difference is allowed','little difference is allowed'),('Bias may affect the result','Bias may affect the result'),('I dont know','I dont know')], validators=[DataRequired()])
    submit8 = SubmitField('Next')


class EightQuestion(FlaskForm):

    q1 = RadioField('',choices=[('Strongly Disagree','Strongly Disagree'),('Disagree','Disagree'),('Neither Agree nor Disagree','Neither Agree nor Disagree'),('Agree','Agree'),('Strongly Agree','Strongly Agree')], validators=[DataRequired()])
    q2 = RadioField('',choices=[('Strongly Disagree','Strongly Disagree'),('Disagree','Disagree'),('Neither Agree nor Disagree','Neither Agree nor Disagree'),('Agree','Agree'),('Strongly Agree','Strongly Agree')], validators=[DataRequired()])
    q3 = RadioField('',choices=[('Strongly Disagree','Strongly Disagree'),('Disagree','Disagree'),('Neither Agree nor Disagree','Neither Agree nor Disagree'),('Agree','Agree'),('Strongly Agree','Strongly Agree')], validators=[DataRequired()])
    q4 = RadioField('',choices=[('Strongly Disagree','Strongly Disagree'),('Disagree','Disagree'),('Neither Agree nor Disagree','Neither Agree nor Disagree'),('Agree','Agree'),('Strongly Agree','Strongly Agree')], validators=[DataRequired()])
    q5 = RadioField('',choices=[('Strongly Disagree','Strongly Disagree'),('Disagree','Disagree'),('Neither Agree nor Disagree','Neither Agree nor Disagree'),('Agree','Agree'),('Strongly Agree','Strongly Agree')], validators=[DataRequired()])
    q6 = RadioField('',choices=[('Strongly Disagree','Strongly Disagree'),('Disagree','Disagree'),('Neither Agree nor Disagree','Neither Agree nor Disagree'),('Agree','Agree'),('Strongly Agree','Strongly Agree')], validators=[DataRequired()])
    q7 = RadioField('',choices=[('Satisfication','Satisfication'),('Neither statisfication nor Dissatisfaction','Neither statisfication nor Dissatisfaction'),('Dissatisfaction','Dissatisfaction')], validators=[DataRequired()])
    q8 = RadioField('',choices=[('Machine selection and human selection match very well','Machine selection and human selection match very well'),('ARA did not consider the total amount of applicant','ARA did not consider the total amount of applicant'),('little difference is allowed','little difference is allowed'),('Bias may affect the result','Bias may affect the result'),('I dont know','I dont know')], validators=[DataRequired()])
    submit15 = SubmitField('Next')


class NineQuestion(FlaskForm):

    q1 = RadioField('',choices=[('Strongly Disagree','Strongly Disagree'),('Disagree','Disagree'),('Neither Agree nor Disagree','Neither Agree nor Disagree'),('Agree','Agree'),('Strongly Agree','Strongly Agree')], validators=[DataRequired()])
    q2 = RadioField('',choices=[('Strongly Disagree','Strongly Disagree'),('Disagree','Disagree'),('Neither Agree nor Disagree','Neither Agree nor Disagree'),('Agree','Agree'),('Strongly Agree','Strongly Agree')], validators=[DataRequired()])
    q3 = RadioField('',choices=[('Strongly Disagree','Strongly Disagree'),('Disagree','Disagree'),('Neither Agree nor Disagree','Neither Agree nor Disagree'),('Agree','Agree'),('Strongly Agree','Strongly Agree')], validators=[DataRequired()])
    q4 = RadioField('',choices=[('Strongly Disagree','Strongly Disagree'),('Disagree','Disagree'),('Neither Agree nor Disagree','Neither Agree nor Disagree'),('Agree','Agree'),('Strongly Agree','Strongly Agree')], validators=[DataRequired()])
    q5 = RadioField('',choices=[('Strongly Disagree','Strongly Disagree'),('Disagree','Disagree'),('Neither Agree nor Disagree','Neither Agree nor Disagree'),('Agree','Agree'),('Strongly Agree','Strongly Agree')], validators=[DataRequired()])
    q6 = RadioField('',choices=[('Strongly Disagree','Strongly Disagree'),('Disagree','Disagree'),('Neither Agree nor Disagree','Neither Agree nor Disagree'),('Agree','Agree'),('Strongly Agree','Strongly Agree')], validators=[DataRequired()])
    q7 = RadioField('',choices=[('Satisfication','Satisfication'),('Neither statisfication nor Dissatisfaction','Neither statisfication nor Dissatisfaction'),('Dissatisfaction','Dissatisfaction')], validators=[DataRequired()])
    q8 = RadioField('',choices=[('Machine selection and human selection match very well','Machine selection and human selection match very well'),('ARA did not consider the total amount of applicant','ARA did not consider the total amount of applicant'),('little difference is allowed','little difference is allowed'),('Bias may affect the result','Bias may affect the result'),('I dont know','I dont know')], validators=[DataRequired()])
    submit16 = SubmitField('Next')


class TenQuestion(FlaskForm):

    q1 = RadioField('',choices=[('Strongly Disagree','Strongly Disagree'),('Disagree','Disagree'),('Neither Agree nor Disagree','Neither Agree nor Disagree'),('Agree','Agree'),('Strongly Agree','Strongly Agree')], validators=[DataRequired()])
    q2 = RadioField('',choices=[('Strongly Disagree','Strongly Disagree'),('Disagree','Disagree'),('Neither Agree nor Disagree','Neither Agree nor Disagree'),('Agree','Agree'),('Strongly Agree','Strongly Agree')], validators=[DataRequired()])
    q3 = RadioField('',choices=[('Strongly Disagree','Strongly Disagree'),('Disagree','Disagree'),('Neither Agree nor Disagree','Neither Agree nor Disagree'),('Agree','Agree'),('Strongly Agree','Strongly Agree')], validators=[DataRequired()])
    q4 = RadioField('',choices=[('Strongly Disagree','Strongly Disagree'),('Disagree','Disagree'),('Neither Agree nor Disagree','Neither Agree nor Disagree'),('Agree','Agree'),('Strongly Agree','Strongly Agree')], validators=[DataRequired()])
    q5 = RadioField('',choices=[('Strongly Disagree','Strongly Disagree'),('Disagree','Disagree'),('Neither Agree nor Disagree','Neither Agree nor Disagree'),('Agree','Agree'),('Strongly Agree','Strongly Agree')], validators=[DataRequired()])
    q6 = RadioField('',choices=[('Strongly Disagree','Strongly Disagree'),('Disagree','Disagree'),('Neither Agree nor Disagree','Neither Agree nor Disagree'),('Agree','Agree'),('Strongly Agree','Strongly Agree')], validators=[DataRequired()])
    q7 = RadioField('',choices=[('Satisfication','Satisfication'),('Neither statisfication nor Dissatisfaction','Neither statisfication nor Dissatisfaction'),('Dissatisfaction','Dissatisfaction')], validators=[DataRequired()])
    q8 = RadioField('',choices=[('Machine selection and human selection match very well','Machine selection and human selection match very well'),('ARA did not consider the total amount of applicant','ARA did not consider the total amount of applicant'),('little difference is allowed','little difference is allowed'),('Bias may affect the result','Bias may affect the result'),('I dont know','I dont know')], validators=[DataRequired()])
    submit17 = SubmitField('Next')


class EleventQuestion(FlaskForm):

    q1 = RadioField('',choices=[('Strongly Disagree','Strongly Disagree'),('Disagree','Disagree'),('Neither Agree nor Disagree','Neither Agree nor Disagree'),('Agree','Agree'),('Strongly Agree','Strongly Agree')], validators=[DataRequired()])
    q2 = RadioField('',choices=[('Strongly Disagree','Strongly Disagree'),('Disagree','Disagree'),('Neither Agree nor Disagree','Neither Agree nor Disagree'),('Agree','Agree'),('Strongly Agree','Strongly Agree')], validators=[DataRequired()])
    q3 = RadioField('',choices=[('Strongly Disagree','Strongly Disagree'),('Disagree','Disagree'),('Neither Agree nor Disagree','Neither Agree nor Disagree'),('Agree','Agree'),('Strongly Agree','Strongly Agree')], validators=[DataRequired()])
    q4 = RadioField('',choices=[('Strongly Disagree','Strongly Disagree'),('Disagree','Disagree'),('Neither Agree nor Disagree','Neither Agree nor Disagree'),('Agree','Agree'),('Strongly Agree','Strongly Agree')], validators=[DataRequired()])
    q5 = RadioField('',choices=[('Strongly Disagree','Strongly Disagree'),('Disagree','Disagree'),('Neither Agree nor Disagree','Neither Agree nor Disagree'),('Agree','Agree'),('Strongly Agree','Strongly Agree')], validators=[DataRequired()])
    q6 = RadioField('',choices=[('Strongly Disagree','Strongly Disagree'),('Disagree','Disagree'),('Neither Agree nor Disagree','Neither Agree nor Disagree'),('Agree','Agree'),('Strongly Agree','Strongly Agree')], validators=[DataRequired()])
    q7 = RadioField('',choices=[('Satisfication','Satisfication'),('Neither statisfication nor Dissatisfaction','Neither statisfication nor Dissatisfaction'),('Dissatisfaction','Dissatisfaction')], validators=[DataRequired()])
    q8 = RadioField('',choices=[('Machine selection and human selection match very well','Machine selection and human selection match very well'),('ARA did not consider the total amount of applicant','ARA did not consider the total amount of applicant'),('little difference is allowed','little difference is allowed'),('Bias may affect the result','Bias may affect the result'),('I dont know','I dont know')], validators=[DataRequired()])
    submit18 = SubmitField('Next')



class SampleQuestion(FlaskForm):

    q2 = RadioField('', choices=[('applicant', 'applicant'), ('recruiter', 'recruiter')], validators=[DataRequired()])

    submit12 = SubmitField('Next')

