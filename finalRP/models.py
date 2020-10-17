
from forms import  HomePage, FirstQuestion, SecondQuestion, ChartFig, ThirdQuestion, FourthQuestion, FifthQuestion, SixthQuestion, SeventhQuestion, SampleQuestion, EightQuestion, NineQuestion, TenQuestion, EleventQuestion, Consent
from flask import render_template, redirect, url_for, session, flash, Flask, request
import numpy as np
import mysql.connector
from mysql.connector import Error
import time
import sys
import datetime
import random

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'
app.permanent_session_lifetime = datetime.timedelta(days=365)

choice_dict = {
    "applicant": "applicant",
    "recruiter": "recruiter",
    "Satisfication": 1,
    " Neither statisfication nor Dissatisfaction": 2,
    "Dissatisfaction": 3,
    "Strongly Disagree": 1,
    "Disagree": 2,
    "Neither Agree nor Disagree": 3,
    "Agree": 4,
    "Strongly Agree": 5,
    "Machine selection and human selection match very well": 1,
    "ARA did not consider the total amount of applicant": 2,
    "little difference is allowed": 3,
    "Bias may affect the result": 4,
    "I dont know": 5,
}

############################################

        # VIEWS WITH FORMS

#########################################


@app.route('/', methods=['GET', 'POST'])
def consent_form():
    session['index'] = 0
    form10 = Consent()
    if form10.validate_on_submit():
        session['participant_name'] = form10.participant_name.data
        session['researcher_name'] = form10.researcher_name.data
        session['response'] = form10.response.data
        t = datetime.datetime.now().date()
        session['date'] = t.strftime('%m/%d/%Y')
        return redirect(url_for('user_info'))
    return render_template('consent.html', form10=form10)

@app.route('/home', methods=['GET', 'POST'])
def user_info():
    form = HomePage()
    if form.validate_on_submit():
        session['Age'] = form.age.data
        session['Gender'] = form.gender.data
        session['Education'] = form.education.data

        return redirect(url_for('sample_fig'))
    return render_template('home.html',form=form)

@app.route('/test_simulation', methods=['GET', 'POST'])
def sample_fig():
    form11 = ChartFig()
    applicants = [10,7,5,4]
    if form11.submit11.data:
        return redirect(url_for('sample_question'))
    return render_template('sample_fig.html', form11=form11, applicants=applicants)


@app.route('/test_question', methods=['GET', 'POST'])
def sample_question():
    form12 = SampleQuestion()
    if form12.validate_on_submit():
        session['q2'] = request.form['q2']
        return redirect(url_for('preread'))
    return render_template('sample_question.html',form12=form12)


@app.route('/preread', methods=['GET', 'POST'])
def preread():
    form13 = ChartFig()
    if form13.submit13.data:
        connection = mysql.connector.connect(host='localhost',
                                             database='common',
                                             user='root',
                                             password='19930720Ch')
        cursor = connection.cursor()
        mySql_insert_query = """replace INTO qa (Participant_Name, Researcher_Name, response, Date, Age, Gender, Education, Role)
                                VALUES (%s, %s, %s, %s, %s, %s, %s, %s) """

        recordTuple = (session['participant_name'], session['researcher_name'], session['response'], session['date'], session['Age'], session['Gender'], session['Education'], session['q2'])
        cursor.execute(mySql_insert_query, recordTuple)
        connection.commit()
        cursor.close()
        connection.close()

        return redirect(url_for('chart_fig'))
    return render_template('preread.html',form13=form13)


@app.route('/simulation', methods=['GET', 'POST'])
def chart_fig():
    form9 = ChartFig()
    now = datetime.datetime.now()
    session['Start_Time'] = now.strftime('%H:%M:%S')
    tasks = [
        [10,5,10,5,'performance90'],
        [10,6,8,4,'performance90'],[10,8,5,3,'performance90'],[10,5,5,1,'performance90'],
        [10,6,10,2,'performance90'],[10,3,10,8,'performance90'],[10,8,5,1,'performance90'],[10,9,10,2,'performance90'],
        [10,1,10,9,'performance90'],[10,1,10,10,'performance90'],[10,10,10,0,'performance90'],
        [10, 5, 10, 5, 'performance80'], [10, 6, 8, 4, 'performance80'], [10, 8, 5, 3, 'performance80'],
        [10, 5, 5, 1, 'performance80'], [10, 6, 10, 2, 'performance80'], [10, 3, 10, 8, 'performance80'],
        [10, 8, 5, 1, 'performance80'], [10, 9, 10, 2, 'performance80'], [10, 1, 10, 9, 'performance80'],
        [10, 1, 10, 10, 'performance80'], [10, 10, 10, 0, 'performance80'],
        
        [10, 5, 10, 5, 'performance70'], [10, 6, 8, 4, 'performance70'], [10, 8, 5, 3, 'performance70'],
        [10, 5, 5, 1, 'performance70'], [10, 6, 10, 2, 'performance70'], [10, 3, 10, 8, 'performance70'],
        [10, 8, 5, 1, 'performance70'], [10, 9, 10, 2, 'performance70'], [10, 1, 10, 9, 'performance70'],
        [10, 1, 10, 10, 'performance70'], [10, 10, 10, 0, 'performance70'],
        
        [10, 5, 10, 5, 'performance60'], [10, 6, 8, 4, 'performance60'], [10, 8, 5, 3, 'performance60'],
        [10, 5, 5, 1, 'performance60'], [10, 6, 10, 2, 'performance60'], [10, 3, 10, 8, 'performance60'],
        [10, 8, 5, 1, 'performance60'], [10, 9, 10, 2, 'performance60'], [10, 1, 10, 9, 'performance60'],
        [10, 1, 10, 10, 'performance60'], [10, 10, 10, 0, 'performance60'],
        
        [10, 5, 10, 5, 'performance50'], [10, 6, 8, 4, 'performance50'], [10, 8, 5, 3, 'performance50'],
        [10, 5, 5, 1, 'performance50'], [10, 6, 10, 2, 'performance50'], [10, 3, 10, 8, 'performance50'],
        [10, 8, 5, 1, 'performance50'], [10, 9, 10, 2, 'performance50'], [10, 1, 10, 9, 'performance50'],
        [10, 1, 10, 10, 'performance50'], [10, 10, 10, 0, 'performance50'],


             ]
    applicants = tasks[session['index']]
    session['applicants'] = applicants
    if form9.validate_on_submit():

        session['a2'] = form9.q2.data
        session['a3'] = form9.q3.data

        connection = mysql.connector.connect(host='localhost',
                                             database='common',
                                             user='root',
                                             password='19930720Ch')
        cursor = connection.cursor()
        mySql_insert_query = """update qa set `%s` = %s where participant_name = %s"""

        recordTuple = (role, str(choice_dict[session['q2']]) , session['participant_name'])
        cursor.execute(mySql_insert_query, recordTuple)
        connection.commit()
        cursor.close()
        connection.close()


    if form9.submit9.data:
        return redirect(url_for('first_answer'))
    return render_template('simulation.html', form9=form9, applicants=applicants)



@app.route('/Q1', methods=['GET', 'POST'])
def first_answer():
    now = datetime.datetime.now()
    session['End_Time'] = now.strftime('%H:%M:%S')
    form2 = FirstQuestion()
    if form2.validate_on_submit():
        session['A1'] = form2.q1.data
        session['A2'] = form2.q2.data
        session['A3'] = form2.q3.data
        session['A4'] = form2.q4.data
        session['A5'] = form2.q5.data
        session['A6'] = form2.q6.data
        session['A7'] = form2.q7.data
        session['A8'] = form2.q8.data
        connection = mysql.connector.connect(host='localhost',
                                             database='common',
                                             user='root',
                                             password='19930720Ch')
        cursor = connection.cursor()
        mySql_insert_query = """update qa set `%s` = %s where participant_name = %s"""

        recordTuple = (int(session['index'])+1, str(choice_dict[session['A1']])+str(choice_dict[session['A2']])+str(choice_dict[session['A3']])+str(choice_dict[session['A4']])+str(choice_dict[session['A5']])+str(choice_dict[session['A6']])+str(choice_dict[session['A7']])+str(choice_dict[session['A8']]),session['participant_name'])
        cursor.execute(mySql_insert_query, recordTuple)
        connection.commit()
        cursor.close()
        connection.close()
        if session['index'] == 55:
            url = 'thankyou'
        else:
            url = 'chart_fig'
        session['index'] = session['index'] + 1
        return redirect(url_for(url))
    return render_template('Q1.html',form2=form2)





@app.route('/Q2', methods=['GET', 'POST'])
def second_answer():
    form3 = SecondQuestion()
    if form3.validate_on_submit():
        session['A1'] = form3.q1.data
        session['A2'] = form3.q2.data
        session['A3'] = form3.q3.data
        session['A4'] = form3.q4.data
        session['A5'] = form3.q5.data
        session['A6'] = form3.q6.data
        session['A7'] = form3.q7.data
        session['A8'] = form3.q8.data
        return redirect(url_for('third_answer'))
    return render_template('Q2.html',form3=form3)



@app.route('/Q3', methods=['GET', 'POST'])
def third_answer():
    form4 = ThirdQuestion()
    if form4.validate_on_submit():
        session['A1'] = form4.q1.data
        session['A2'] = form4.q2.data
        session['A3'] = form4.q3.data
        session['A4'] = form4.q4.data
        session['A5'] = form4.q5.data
        session['A6'] = form4.q6.data
        session['A7'] = form4.q7.data
        session['A8'] = form4.q8.data
        return redirect(url_for('fourth_answer'))
    return render_template('Q3.html',form4=form4)



@app.route('/Q4', methods=['GET', 'POST'])
def fourth_answer():
    form5 = FourthQuestion()
    if form5.validate_on_submit():
        session['A1'] = form5.q1.data
        session['A2'] = form5.q2.data
        session['A3'] = form5.q3.data
        session['A4'] = form5.q4.data
        session['A5'] = form5.q5.data
        session['A6'] = form5.q6.data
        session['A7'] = form5.q7.data
        session['A8'] = form5.q8.data
        return redirect(url_for('fifth_answer'))
    return render_template('Q4.html',form5=form5)



@app.route('/Q5', methods=['GET', 'POST'])
def fifth_answer():
    form6 = FifthQuestion()
    if form6.validate_on_submit():
        session['A1'] = form6.q1.data
        session['A2'] = form6.q2.data
        session['A3'] = form6.q3.data
        session['A4'] = form6.q4.data
        session['A5'] = form6.q5.data
        session['A6'] = form6.q6.data
        session['A7'] = form6.q7.data
        session['A8'] = form6.q8.data
        return redirect(url_for('sixth_answer'))
    return render_template('Q5.html',form6=form6)



@app.route('/Q6', methods=['GET', 'POST'])
def sixth_answer():
    form7 = SixthQuestion()
    if form7.validate_on_submit():
        session['A1'] = form7.q1.data
        session['A2'] = form7.q2.data
        session['A3'] = form7.q3.data
        session['A4'] = form7.q4.data
        session['A5'] = form7.q5.data
        session['A6'] = form7.q6.data
        session['A7'] = form7.q7.data
        session['A8'] = form7.q8.data
        return redirect(url_for('seventh_answer'))
    return render_template('Q6.html',form7=form7)


@app.route('/Q7', methods=['GET', 'POST'])
def seventh_answer():
    form8 = SeventhQuestion()
    if form8.validate_on_submit():
        session['A1'] = form8.q1.data
        session['A2'] = form8.q2.data
        session['A3'] = form8.q3.data
        session['A4'] = form8.q4.data
        session['A5'] = form8.q5.data
        session['A6'] = form8.q6.data
        session['A7'] = form8.q7.data
        session['A8'] = form8.q8.data
        return redirect(url_for('Eight_answer'))
    return render_template('Q7.html',form8=form8)


@app.route('/Q8', methods=['GET', 'POST'])
def Eight_answer():
    form15 = EightQuestion()
    if form15.validate_on_submit():
        session['A1'] = form15.q1.data
        session['A2'] = form15.q2.data
        session['A3'] = form15.q3.data
        session['A4'] = form15.q4.data
        session['A5'] = form15.q5.data
        session['A6'] = form15.q6.data
        session['A7'] = form15.q7.data
        session['A8'] = form15.q8.data
        return redirect(url_for('Nine_answer'))
    return render_template('Q8.html',form15=form15)



@app.route('/Q9', methods=['GET', 'POST'])
def Nine_answer():
    form16 = NineQuestion()
    if form16.validate_on_submit():
        session['A1'] = form16.q1.data
        session['A2'] = form16.q2.data
        session['A3'] = form16.q3.data
        session['A4'] = form16.q4.data
        session['A5'] = form16.q5.data
        session['A6'] = form16.q6.data
        session['A7'] = form16.q7.data
        session['A8'] = form16.q8.data
        return redirect(url_for('Ten_answer'))
    return render_template('Q9.html',form16=form16)



@app.route('/Q10', methods=['GET', 'POST'])
def Ten_answer():
    form17 = TenQuestion()
    if form17.validate_on_submit():
        session['A1'] = form17.q1.data
        session['A2'] = form17.q2.data
        session['A3'] = form17.q3.data
        session['A4'] = form17.q4.data
        session['A5'] = form17.q5.data
        session['A6'] = form17.q6.data
        session['A7'] = form17.q7.data
        session['A8'] = form17.q8.data
        return redirect(url_for('Elevent_answer'))
    return render_template('Q10.html',form17=form17)


@app.route('/Q11', methods=['GET', 'POST'])
def Elevent_answer():
    form18 = EleventQuestion()
    if form18.validate_on_submit():
        session['A1'] = form18.q1.data
        session['A2'] = form18.q2.data
        session['A3'] = form18.q3.data
        session['A4'] = form18.q4.data
        session['A5'] = form18.q5.data
        session['A6'] = form18.q6.data
        session['A7'] = form18.q7.data
        session['A8'] = form18.q8.data
        return redirect(url_for(url))
    return render_template('Q11.html',form18=form18)



@app.route('/thankyou', methods=['GET', 'POST'])
def thankyou():
    return render_template('thankyou.html')




if __name__ == '__main__':
    app.run(debug=True)
