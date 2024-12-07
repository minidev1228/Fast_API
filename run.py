import requests

url = 'http://127.0.0.1:8000'

data = {
    "user_id": "user3",
    "username": "testuser",
    "password_hash": "hashedpassword",
    "email": "testuser@example.com",
    "first_name": "Test",
    "last_name": "User",
    "role": "user",
    "profile_picture": "http://example.com/profile.jpg",
    "bio": "This is a test user",
    "created_at": "2024-12-01T00:00:00",
    "updated_at": "2024-12-01T00:00:00"
}

response = requests.post("http://127.0.0.1:8000/user", json=data)  # create new user
# response = requests.get("http://127.0.0.1:8000/user/user3") # get user by user's id
# response = requests.get("http://127.0.0.1:8000/user/all")  # get all users
# response = requests.delete("http://127.0.0.1:8000/user/user1")  # delete user by user's id



# Print the response content
print(response.status_code)  # HTTP status code
print(response.json())        # Parsed JSON response