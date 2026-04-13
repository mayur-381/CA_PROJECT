from flask import Flask, render_template, send_from_directory, request, redirect, url_for, flash, session
'''
import numpy as np
import pandas as pd
import pyodbc
import pymssql
from pandas.tseries.offsets import DateOffset
import matplotlib.pyplot as plt
import os
'''
app = Flask(__name__)
app.secret_key = "your_secret_key"

# Routes
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/accounting-bookkeeping')
def accounting():
    return render_template('accounting-bookkeeping.html')

@app.route('/tax-preparation')
def tax_preparation():
    return render_template('tax-preparation.html')

@app.route('/audit')
def audit():
    return render_template('audit.html')

@app.route('/financial-analysis')
def financial_analysis():
    return render_template('financial-analysis.html')

@app.route('/payroll')
def payroll():
    return render_template('payroll.html')

@app.route('/finalisation')
def finalisation():
    return render_template('finalisation.html')

@app.route('/mis-reporting')
def mis_reporting():
    return render_template('mis-reporting.html')

@app.route('/financial-statements')
def financial_statements():
    return render_template('financial-statements.html')


@app.route('/contactus')
def contactus():
    return render_template('contactus.html')


# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
