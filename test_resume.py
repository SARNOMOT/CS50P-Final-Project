import pytest
from unittest.mock import patch
from resume import Resume  
import os

@pytest.fixture
def resume():
    return Resume()

def test_get_personal_info(resume):
    inputs = iter(["John Doe", "john.doe@example.com", "1234567890"])
    with patch('builtins.input', lambda _: next(inputs)):
        resume.get_personal_info()

    assert resume.personal_info == {
        'name': 'John Doe',
        'email': 'john.doe@example.com',
        'phone': '1234567890'
    }

def test_get_education(resume):
    inputs = iter([
        "University of Python", "Computer Science", "2015-2019", "95",
        "no"
    ])
    with patch('builtins.input', lambda _: next(inputs)):
        resume.get_education()

    assert resume.education == [{
        'uni_name': 'University of Python',
        'uni_major': 'Computer Science',
        'uni_year': '2015-2019',
        'uni_grade': '95'
    }]

def test_get_experience(resume):
    inputs = iter([
        "Software Developer", "Developed Python applications.", "2019",
        "no"
    ])
    with patch('builtins.input', lambda _: next(inputs)):
        resume.get_experience()

    assert resume.experience == [{
        'exp_name': 'Software Developer',
        'exp_desc': 'Developed Python applications.',
        'exp_year': '2019'
    }]

def test_get_skills(resume):
    inputs = iter(["Python", "no"])
    with patch('builtins.input', lambda _: next(inputs)):
        resume.get_skills()

    assert resume.skills == ["Python"]

def test_generate_pdf(resume):
    resume.personal_info = {
        'name': 'John Doe',
        'email': 'john.doe@example.com',
        'phone': '1234567890'
    }
    resume.education = [{
        'uni_name': 'University of Python',
        'uni_major': 'Computer Science',
        'uni_year': '2015-2019',
        'uni_grade': '95'
    }]
    resume.experience = [{
        'exp_name': 'Software Developer',
        'exp_desc': 'Developed Python applications.',
        'exp_year': '2019'
    }]
    resume.skills = ["Python", "Data Analysis"]

    # Clean up generated file after test if it exists
    if os.path.exists("resume.pdf"):
        os.remove("resume.pdf")
