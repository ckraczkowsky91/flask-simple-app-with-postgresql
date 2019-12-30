from flask import Flask, render_template
from . import simpleApp

@simpleApp.route('/')
def index():
    return render_template('index.html')

@simpleApp.route('/input')
def input():
    return render_template('input.html')
