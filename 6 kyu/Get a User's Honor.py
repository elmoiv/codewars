def get_honor(un):
    return json.loads(requests.get('https://www.codewars.com/api/v1/users/'+un).content)["honor"]
