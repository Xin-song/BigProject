import requests
from esi_oauth_native_mylib import validate_eve_jwt
#%%
#%%
def JWZZ_aliances(sso_response):
    """List all aliances.
    Args:
        sso_response: A requests Response object gotten by calling the EVE
                      SSO /v2/oauth/token endpoint
    Return:
        list of alliances
    """

    if sso_response.status_code == 200:
        data = sso_response.json()
        access_token = data["access_token"]

        aliances_path = ("https://esi.evetech.net/latest/alliances")

        headers = {
            "Authorization": "Bearer {}".format(access_token)
        }

        res = requests.get(aliances_path, headers=headers)

        res.raise_for_status()

        data = res.json()

        return data
    else:

        print("\nSent request with url: {} \nbody: {} \nheaders: {}".format(
            sso_response.request.url,
            sso_response.request.body,
            sso_response.request.headers
        ))
        print("\nSSO response code is: {}".format(sso_response.status_code))
        print("\nSSO response JSON is: {}".format(sso_response.json()))
        return None
#%%


#%%
def JWZZ_aliances(sso_response):
    """Get Alliance information.
    Args:
        sso_response: A requests Response object gotten by calling the EVE
                      SSO /v2/oauth/token endpoint
    """

    if sso_response.status_code == 200:
        data = sso_response.json()
        access_token = data["access_token"]

        aliances_path = ("https://esi.evetech.net/latest/alliances")

        headers = {
            "Authorization": "Bearer {}".format(access_token)
        }

        res = requests.get(aliances_path, headers=headers)

        res.raise_for_status()

        data = res.json()

        return data
    else:

        print("\nSent request with url: {} \nbody: {} \nheaders: {}".format(
            sso_response.request.url,
            sso_response.request.body,
            sso_response.request.headers
        ))
        print("\nSSO response code is: {}".format(sso_response.status_code))
        print("\nSSO response JSON is: {}".format(sso_response.json()))
        return None


#%%
def JWZZ_blueprints(sso_response):
    """Handles the authorization code response from the EVE SSO.
    Args:
        sso_response: A requests Response object gotten by calling the EVE
                      SSO /v2/oauth/token endpoint
    """

    if sso_response.status_code == 200:
        data = sso_response.json()
        access_token = data["access_token"]

        print("\nVerifying access token JWT...")

        jwt = validate_eve_jwt(access_token)
        character_id = jwt["sub"].split(":")[2]
        character_name = jwt["name"]
        blueprint_path = ("https://esi.evetech.net/latest/characters/{}/"
                          "blueprints/".format(character_id))

        headers = {
            "Authorization": "Bearer {}".format(access_token)
        }

        res = requests.get(blueprint_path, headers=headers)
        print("\nMade request to {} with headers: "
              "{}".format(blueprint_path, res.request.headers))
        res.raise_for_status()

        data = res.json()
        print("\n{} has {} blueprints".format(character_name, len(data)))
        return data
    else:
        print("\nSomething went wrong! Re read the comment at the top of this "
              "file and make sure you completed all the prerequisites then "
              "try again. Here's some debug info to help you out:")
        print("\nSent request with url: {} \nbody: {} \nheaders: {}".format(
            sso_response.request.url,
            sso_response.request.body,
            sso_response.request.headers
        ))
        print("\nSSO response code is: {}".format(sso_response.status_code))
        print("\nSSO response JSON is: {}".format(sso_response.json()))
        return None