import os
import pytest
import json
from src.multiple_choice_logger import MultipleChoiceLogger

@pytest.fixture
def temp_log_file(tmp_path):
    """Create a temporary log file for testing."""
    return str(tmp_path / 'test_responses.json')

def test_log_response(temp_log_file):
    """Test logging a basic response."""
    logger = MultipleChoiceLogger(temp_log_file)
    
    response = logger.log_response(
        question="What is the capital of France?", 
        choices=["Paris", "London", "Berlin"], 
        user_response="Paris",
        user_id="user1"
    )
    
    # Check returned response details
    assert response['question'] == "What is the capital of France?"
    assert response['choices'] == ["Paris", "London", "Berlin"]
    assert response['user_response'] == "Paris"
    assert response['user_id'] == "user1"
    
    # Verify file was created and contains the response
    with open(temp_log_file, 'r') as f:
        logged_responses = json.load(f)
    
    assert len(logged_responses) == 1
    assert logged_responses[0] == response

def test_invalid_response(temp_log_file):
    """Test logging an invalid response raises an error."""
    logger = MultipleChoiceLogger(temp_log_file)
    
    with pytest.raises(ValueError, match="Response 'Madrid' is not in the list of choices"):
        logger.log_response(
            question="What is the capital of France?", 
            choices=["Paris", "London", "Berlin"], 
            user_response="Madrid"
        )

def test_empty_question(temp_log_file):
    """Test logging with an empty question raises an error."""
    logger = MultipleChoiceLogger(temp_log_file)
    
    with pytest.raises(ValueError, match="Question cannot be empty"):
        logger.log_response(
            question="", 
            choices=["Paris", "London", "Berlin"], 
            user_response="Paris"
        )

def test_empty_choices(temp_log_file):
    """Test logging with empty choices raises an error."""
    logger = MultipleChoiceLogger(temp_log_file)
    
    with pytest.raises(ValueError, match="Choices list cannot be empty"):
        logger.log_response(
            question="What is the capital?", 
            choices=[], 
            user_response="Paris"
        )

def test_multiple_responses(temp_log_file):
    """Test logging multiple responses."""
    logger = MultipleChoiceLogger(temp_log_file)
    
    # Log multiple responses
    logger.log_response(
        question="Favorite color?", 
        choices=["Red", "Blue", "Green"], 
        user_response="Blue",
        user_id="user1"
    )
    
    logger.log_response(
        question="Favorite color?", 
        choices=["Red", "Blue", "Green"], 
        user_response="Green",
        user_id="user2"
    )
    
    # Verify both responses are logged
    with open(temp_log_file, 'r') as f:
        logged_responses = json.load(f)
    
    assert len(logged_responses) == 2
    assert logged_responses[0]['user_response'] == "Blue"
    assert logged_responses[1]['user_response'] == "Green"

def test_get_user_responses(temp_log_file):
    """Test retrieving responses for a specific user."""
    logger = MultipleChoiceLogger(temp_log_file)
    
    # Log responses for multiple users
    logger.log_response(
        question="Favorite fruit?", 
        choices=["Apple", "Banana", "Orange"], 
        user_response="Apple",
        user_id="user1"
    )
    
    logger.log_response(
        question="Favorite fruit?", 
        choices=["Apple", "Banana", "Orange"], 
        user_response="Banana",
        user_id="user2"
    )
    
    logger.log_response(
        question="Favorite fruit?", 
        choices=["Apple", "Banana", "Orange"], 
        user_response="Orange",
        user_id="user1"
    )
    
    # Retrieve and check user1's responses
    user1_responses = logger.get_user_responses("user1")
    assert len(user1_responses) == 2
    assert {resp['user_response'] for resp in user1_responses} == {"Apple", "Orange"}
    
    # Retrieve and check user2's responses
    user2_responses = logger.get_user_responses("user2")
    assert len(user2_responses) == 1
    assert user2_responses[0]['user_response'] == "Banana"

def test_get_all_responses(temp_log_file):
    """Test retrieving all responses."""
    logger = MultipleChoiceLogger(temp_log_file)
    
    # Log multiple responses
    logger.log_response(
        question="Favorite season?", 
        choices=["Spring", "Summer", "Autumn", "Winter"], 
        user_response="Summer",
        user_id="user1"
    )
    
    logger.log_response(
        question="Favorite season?", 
        choices=["Spring", "Summer", "Autumn", "Winter"], 
        user_response="Winter",
        user_id="user2"
    )
    
    # Retrieve all responses
    all_responses = logger.get_user_responses()
    assert len(all_responses) == 2
    assert {resp['user_response'] for resp in all_responses} == {"Summer", "Winter"}