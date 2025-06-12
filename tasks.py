'''File for invoking tasks'''
import subprocess
from invoke import task

@task
def pytest(c, o):
    '''run pytestt with or without arguments'''
    if o == 'ios':
        subprocess.call(['pytest', '-m ios', '--junit-xml=logs/junit.xml'])
    elif o == 'android':
        subprocess.call(['pytest', '-m android', '--junit-xml=logs/junit.xml'])
    else:
        subprocess.call(['pytest'])

@task
def homescreen(c):
    '''home screen tests'''
    subprocess.call(['pytest', '-m homescreen', '--junit-xml=logs/junit.xml', '-v'])

@task
def echobox(c):
    '''echo box tests'''
    subprocess.call(['pytest', '-m echobox', '--junit-xml=logs/junit.xml', '-v'])
