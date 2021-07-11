import requests
import pytest

class Test_callapi:
    def test_api(self):
#Get Requests
        parameter= {"page": 2}
        get_response= requests.get("https://reqres.in/api/users", params= parameter, timeout=2)
        print(get_response)
        response_code= get_response.status_code
        assert response_code==200, "Response Code doesn't match"
        json= get_response.json()
        print(json)




