from user.models.test import Test
from user.models.client import Client
from user.models.testExecution import TestExecution
from user.models.testCase import TestCase
from user.models.testSuite import TestSuite
from user.models.user import User
from sqlalchemy.orm import aliased
from flask import jsonify
from datetime import datetime, timedelta

# def get_all_tests():
#     return TestExecution.query.order_by(TestExecution.id.desc()).limit(10)

def get_all_tests():
    all_tests = (TestExecution.query
                  .join(User, User.id == TestExecution.user_id)  # Join with User table based on user_id
                  .order_by(TestExecution.id.desc())
                  .limit(10)
                  .with_entities(TestExecution.id, TestExecution.test_ticket, TestExecution.test_description, User.first_name, User.last_name)  # Select desired columns
                  .all())
    
    return all_tests

# def get_aarp_tests():
#     aarp_tests = Test.query.filter(Test.test_ticket.like('AARP%')).order_by(Test.id.desc()).limit(10)
#     return aarp_tests


def get_aarp_tests():
    # Get the current time and adjust to the desired time range
    now = datetime.now()
    # Set the time to 4 PM today
    four_pm_today = now.replace(hour=16, minute=0, second=0, microsecond=0)
    
    # If the current time is before 4 PM, we need to adjust to the previous day
    if now < four_pm_today:
        four_pm_yesterday = (four_pm_today - timedelta(days=1))
    else:
        four_pm_yesterday = four_pm_today

    # Get the client_id for the client with the name 'AARP'
    client_id_subquery = Client.query.filter(Client.client_name.like('AARP')).with_entities(Client.id).scalar_subquery()

    # Perform a join between TestExecution and User to get the user name
    aarp_tests = (TestExecution.query
                  .join(User, User.id == TestExecution.user_id)  # Join with User table based on user_id
                  .filter(TestExecution.client_id == client_id_subquery)
                  .filter(TestExecution.updated_at >= four_pm_yesterday)  # Filter from 4 PM yesterday
                  .filter(TestExecution.updated_at < now)  # Filter up to 4 PM today
                  .order_by(TestExecution.id.desc())
                  .limit(10)
                  .with_entities(TestExecution.id, TestExecution.test_ticket, TestExecution.test_description, User.first_name, User.last_name)  # Select desired columns
                  .all())
    
    return aarp_tests


def get_all_test_cases():
    return TestCase.query.order_by(TestCase.id.asc())

def get_all_test_suites():
    return TestSuite.query.order_by(TestSuite.id.asc())
