from behave import *
from behave import given, when, then
from main import counting

@given('I have 3 numbers: {A}, {B},{C}')
def step(context, A, B, C):
    context.a=A
    context.b = B
    context.c = C
@when('I count diskriminant and korni')
def step(context):
    context.result = counting(int(context.a),int(context.b),int(context.c))

@then('I expect to get result = {result}')
def step(context, result):
    assert str(context.result) == result