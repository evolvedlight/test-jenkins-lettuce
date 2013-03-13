# -*- coding: utf-8 -*-
from lettuce import step

@step(u'Given I have the following students in my database:')
def given_i_have_the_following_students_in_my_database(step):
    pass
@step(u'When I bill names starting with "([^"]*)"')
def when_i_bill_names_starting_with_group1(step, group1):
    pass
@step(u'Then I see those billed students:')
def then_i_see_those_billed_students(step):
    pass
@step(u'And those that werent:')
def and_those_that_weren_t(step):
    pass
