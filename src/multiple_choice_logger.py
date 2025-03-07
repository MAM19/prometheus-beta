import json
import os
from typing import List, Dict, Any, Optional

class MultipleChoiceLogger:
    """
    A class to log and manage user responses to multiple-choice questions.
    
    The logger supports:
    - Logging individual responses
    - Storing responses to a JSON file
    - Retrieving logged responses
    - Handling various input validations
    """
    
    def __init__(self, log_file: str = 'responses.json'):
        """
        Initialize the MultipleChoiceLogger.
        
        :param log_file: Path to the JSON file for storing responses (default: 'responses.json')
        """
        self.log_file = log_file
        # Ensure the directory exists
        os.makedirs(os.path.dirname(log_file) or '.', exist_ok=True)
    
    def log_response(self, 
                     question: str, 
                     choices: List[str], 
                     user_response: str, 
                     user_id: Optional[str] = None) -> Dict[str, Any]:
        """
        Log a user's response to a multiple-choice question.
        
        :param question: The text of the multiple-choice question
        :param choices: List of possible answer choices
        :param user_response: The user's selected response
        :param user_id: Optional unique identifier for the user
        :return: A dictionary containing the logged response details
        :raises ValueError: If the response is not in the list of choices
        """
        # Validate inputs
        if not question:
            raise ValueError("Question cannot be empty")
        
        if not choices:
            raise ValueError("Choices list cannot be empty")
        
        if user_response not in choices:
            raise ValueError(f"Response '{user_response}' is not in the list of choices: {choices}")
        
        # Create response entry
        response_entry = {
            'question': question,
            'choices': choices,
            'user_response': user_response,
            'user_id': user_id
        }
        
        # Read existing responses
        responses = self._read_responses()
        
        # Add new response
        responses.append(response_entry)
        
        # Write updated responses
        self._write_responses(responses)
        
        return response_entry
    
    def _read_responses(self) -> List[Dict[str, Any]]:
        """
        Read existing responses from the log file.
        
        :return: List of logged responses
        """
        try:
            with open(self.log_file, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []
        except json.JSONDecodeError:
            # Handle empty or corrupted file
            return []
    
    def _write_responses(self, responses: List[Dict[str, Any]]):
        """
        Write responses to the log file.
        
        :param responses: List of response entries to write
        """
        with open(self.log_file, 'w') as f:
            json.dump(responses, f, indent=2)
    
    def get_user_responses(self, user_id: Optional[str] = None) -> List[Dict[str, Any]]:
        """
        Retrieve responses, optionally filtered by user ID.
        
        :param user_id: Optional user ID to filter responses
        :return: List of responses matching the user ID (or all responses if no ID provided)
        """
        responses = self._read_responses()
        
        if user_id is not None:
            return [resp for resp in responses if resp.get('user_id') == user_id]
        
        return responses