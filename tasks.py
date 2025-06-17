'''File for invoking tasks'''
import subprocess
from invoke import task

@task
def pytest(c):
    '''run pytestt with or without arguments'''
    subprocess.call(['pytest', '--junit-xml=logs/junit.xml', '-v'])

@task
def homescreen(c):
    '''home screen tests'''
    subprocess.call(['pytest', '-m homescreen', '--junit-xml=logs/junit.xml', '-v'])

@task
def echobox(c):
    '''echo box tests'''
    subprocess.call(['pytest', '-m echobox', '--junit-xml=logs/junit.xml', '-v'])
