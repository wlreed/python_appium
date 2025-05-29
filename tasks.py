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
def ios(c):
    '''run ios suite of tests'''
    subprocess.call(['pytest', '-m ios', '--junit-xml=logs/junit.xml', '-v'])

@task
def android(c):
    '''run android suite of tests'''
    subprocess.call(['pytest', '-m android', '--junit-xml=logs/junit.xml', '-v'])

@task
def test(c):
    '''test process'''
    subprocess.call(['pytest', '-m test', '--junit-xml=logs/junit.xml', '-v'])

@task
def configed(c):
    '''configed tests'''
    subprocess.call(['pytest', '-m configed', '--junit-xml=logs/junit.xml', '-v'])
