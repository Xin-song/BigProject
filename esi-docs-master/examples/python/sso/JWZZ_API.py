import requests
from esi_oauth_native_mylib import validate_eve_jwt
#%%
# The following four functions are for alliance ESIs
#%%
def JWZZ_alliances(sso_response):
    """List all aliances. Alliance/alliances
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
def JWZZ_alliances_info(sso_response,alliance_id):
    """Get Alliance information. Alliance/alliances/alliance_id
    Args:
        sso_response: A requests Response object gotten by calling the EVE
                      SSO /v2/oauth/token endpoint
        alliance_id: the id of alliances
    # ToDo check the type of the return
    Return: 
        dictioanry of alliance information: including creator_corporation_id(integer), creator_id(integer), date_founded(string)
        executor_corporation_id(integer), faction_id(integer), name(string),ticker(string,the short name of the alliance)
    """

    if sso_response.status_code == 200:
        data = sso_response.json()
        access_token = data["access_token"]

        aliances_path = ("https://esi.evetech.net/latest/alliances/{}/".format(alliance_id))

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
def JWZZ_alliances_corporations(sso_response,alliance_id):
    """List all current member corporations of an alliance. Alliance/alliances/{alliance_id}/corporations/
    Args:
        sso_response: A requests Response object gotten by calling the EVE
                      SSO /v2/oauth/token endpoint
        alliance_id: the id of alliances
    # ToDo check the type of the return
    Return: 
        	
        List of corporation IDs
    """

    if sso_response.status_code == 200:
        data = sso_response.json()
        access_token = data["access_token"]

        aliances_path = ("https://esi.evetech.net/latest/alliances/{}/"
                         "corperations/".format(alliance_id))

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
def JWZZ_alliances_icons(sso_response,alliance_id):
    """Get the icon urls for a alliance. Alliance/alliances/{alliance_id}/icons/
    Args:
        sso_response: A requests Response object gotten by calling the EVE
                      SSO /v2/oauth/token endpoint
        alliance_id: the id of alliances
    # ToDo check the type of the return
    Return: 
        	
        Icon URLs for the given alliance id and server: including two string, one is for 128x128, one is for 64x64
    """

    if sso_response.status_code == 200:
        data = sso_response.json()
        access_token = data["access_token"]

        aliances_path = ("https://esi.evetech.net/latest/alliances/{}/"
                         "icons/".format(alliance_id))

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
def JWZZ_alliances_icons(sso_response,alliance_id):
    """Get the icon urls for a alliance. Alliance/alliances/{alliance_id}/icons/
    Args:
        sso_response: A requests Response object gotten by calling the EVE
                      SSO /v2/oauth/token endpoint
        alliance_id: the id of alliances
    # ToDo check the type of the return
    Return: 
        	
        Icon URLs for the given alliance id and server: including two string, one is for 128x128, one is for 64x64
    """

    if sso_response.status_code == 200:
        data = sso_response.json()
        access_token = data["access_token"]

        aliances_path = ("https://esi.evetech.net/latest/alliances/{}/"
                         "icons/".format(alliance_id))

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
#The following six functions are for assets ESIs
#%%
def JWZZ_assets_characterassets(sso_response,character_id):
    """Requires the following scope: esi-assets.read_assets.v1
    Return a list of the characters assets
    characters/{character_id}/assets/
    Args:
        sso_response: A requests Response object gotten by calling the EVE
                      SSO /v2/oauth/token endpoint
        character_id: the id of character
    # ToDo check the type of the return
    Return: 
        	
        A flat list of the users assets
        max_items: 1000
        is_blueprint_copy,boolean
        is_singleton, boolean 是否是单件
        
    """

    if sso_response.status_code == 200:
        data = sso_response.json()
        access_token = data["access_token"]

        aliances_path = ("https://esi.evetech.net/latest/characters/{}/assets/".format(character_id))

        headers = {
            "Authorization": "Bearer {}".format(access_token)
        }

        res = requests.get(aliances_path, headers=headers)

        res.raise_for_status()

        data = res.json()
        print("The type of 'data' is {}".formate(type(data)))
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
def JWZZ_assets_characterassets_locations(sso_response,character_id):
    """Requires the following scope: esi-assets.read_assets.v1
    Return locations for a set of item ids, which you can get from character assets endpoint. Coordinates for items in hangars or stations are set to (0,0,0)
    /characters/{character_id}/assets/locations/
    Args:
        sso_response: A requests Response object gotten by calling the EVE
                      SSO /v2/oauth/token endpoint
        character_id: the id of character
    # ToDo check the type of the return
    Return: 
        item_id: integer
        position x,y,z numbers
    """

    if sso_response.status_code == 200:
        data = sso_response.json()
        access_token = data["access_token"]

        aliances_path = ("https://esi.evetech.net/latest/characters/{}/assets/locations/".format(character_id))

        headers = {
            "Authorization": "Bearer {}".format(access_token)
        }

        res = requests.get(aliances_path, headers=headers)

        res.raise_for_status()

        data = res.json()
        print("The type of 'data' is {}".formate(type(data)))
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
def JWZZ_assets_characterassets_names(sso_response,character_id):
    """Requires the following scope: esi-assets.read_assets.v1
    Return names for a set of item ids, which you can get from character assets endpoint. Typically used for items that can customize names, like containers or ships.
    /characters/{character_id}/assets/names/
    Args:
        sso_response: A requests Response object gotten by calling the EVE
                      SSO /v2/oauth/token endpoint
        character_id: the id of character
    # ToDo check the type of the return
    Return: 
        item_id integer
        name string
    """

    if sso_response.status_code == 200:
        data = sso_response.json()
        access_token = data["access_token"]

        aliances_path = ("https://esi.evetech.net/latest/characters/{}/assets/names/".format(character_id))

        headers = {
            "Authorization": "Bearer {}".format(access_token)
        }

        res = requests.get(aliances_path, headers=headers)

        res.raise_for_status()

        data = res.json()
        print("The type of 'data' is {}".formate(type(data)))
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
def JWZZ_assets_characterassets_names(sso_response,character_id):
    """Requires the following scope: esi-assets.read_assets.v1
    Return names for a set of item ids, which you can get from character assets endpoint. Typically used for items that can customize names, like containers or ships.
    /characters/{character_id}/assets/names/
    Args:
        sso_response: A requests Response object gotten by calling the EVE
                      SSO /v2/oauth/token endpoint
        character_id: the id of character
    # ToDo check the type of the return
    Return: 
        item_id integer
        name string
    """

    if sso_response.status_code == 200:
        data = sso_response.json()
        access_token = data["access_token"]

        alliances_path = ("https://esi.evetech.net/latest/characters/{}/assets/names/".format(character_id))

        headers = {
            "Authorization": "Bearer {}".format(access_token)
        }

        res = requests.get(alliances_path, headers=headers)

        res.raise_for_status()

        data = res.json()
        print("The type of 'data' is {}".formate(type(data)))
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
#%%
# Here are the functiosn get path for Alliance
def JWZZ_string_alliance_alliances():
    return "https://esi.evetech.net/latest/alliances/"
def JWZZ_string_alliance_allianceId(alliance_id):
    path = "https://esi.evetech.net/latest/alliances/{}/".format(alliance_id)
    return path
def JWZZ_string_alliance_corporations(alliance_id):
    path="https://esi.evetech.net/latest/alliances/{}/corporations/".format(alliance_id)
    return path
def JWZZ_string_alliance_icons(alliance_id):
    path="https://esi.evetech.net/latest/alliances/{}/icons/".format(alliance_id)
    return path
#%%
# Here are the functiosn get path for Assets
def JWZZ_string_char_assets(character_id):
    path="https://esi.evetech.net/latest/characters/{}/assets/".format(character_id)
    return path
def JWZZ_string_char_assets_locations(character_id):
    path="https://esi.evetech.net/latest/characters/{}/assets/locations/".format(character_id)
    return path
def JWZZ_string_char_assets_names(character_id):
    path="https://esi.evetech.net/latest/characters/{}/assets/names/".format(character_id)
    return path
def JWZZ_string_corp_assets(corporation_id):
    path="https://esi.evetech.net/latest/corporations/{}/assets/".format(corporation_id)
    return path
def JWZZ_string_corp_assets_locations(corporation_id):
    path="https://esi.evetech.net/latest/corporations/{}/assets/locations/".format(corporation_id)
    return path
def JWZZ_string_corp_assets_names(corporation_id):
    path="https://esi.evetech.net/latest/corporations/{}/assets/names/".format(corporation_id)
    return path
#%%
# Here are the functiosn get path for Bookmarks
def JWZZ_string_char_bookmarks(character_id):
    path="https://esi.evetech.net/latest/characters/{}/bookmarks/".format(character_id)
    return path
def JWZZ_string_char_bookmarks_folders(character_id):
    path="https://esi.evetech.net/latest/characters/{}/bookmarks/folders/".format(character_id)
    return path
def JWZZ_string_corp_bookmarks(corporation_id):
    path="https://esi.evetech.net/latest/corporations/{}/bookmarks/".format(corporation_id)
    return path
def JWZZ_string_corp_bookmarks_folders(corporation_id):
    path="https://esi.evetech.net/latest/corporations/{}/bookmarks/folders/".format(corporation_id)
    return path
#%%
# Here are the functiosn get path for Calendar
def JWZZ_string_char_calendar(character_id):
    path="https://esi.evetech.net/latest/characters/{}/calendar/".format(character_id)
    return path
def JWZZ_string_char_calendar_event(character_id,event_id):
    path="https://esi.evetech.net/latest/characters/{}/calendar/{}/".format(character_id,event_id)
    return path
'''
# Here should be an respnd to an event
# Todo
# Learn how to use this.
def JWZZ_string_char_calendar_event(character_id,event_id):
    path="https://esi.evetech.net/latest/characters/{}/calendar/{}/".format(character_id,event_id)
    return path
'''
def JWZZ_string_char_calendar_event_attendees(character_id,event_id):
    path="https://esi.evetech.net/latest/characters/{}/calendar/{}/attendees/".format(character_id,event_id)
    return path
#%%
# Here are the functiosn get path for Character
def JWZZ_string_char(character_id):
    path="https://esi.evetech.net/latest/characters/{}/".format(character_id)
    return path
def JWZZ_string_char_agents_research(character_id):
    path="https://esi.evetech.net/latest/characters/{}/agents_research/".format(character_id)
    return path
def JWZZ_string_char_blueprints(character_id):
    path="https://esi.evetech.net/latest/characters/{}/blueprints/".format(character_id)
    return path
def JWZZ_string_char_corporationhistory(character_id):
    path="https://esi.evetech.net/latest/characters/{}/corporationhistory/".format(character_id)
    return path
def JWZZ_string_char_cspa(character_id):
    # 这是个啥东西？
    # Todo
    # Post type
    path="https://esi.evetech.net/latest/characters/{}/cspa/".format(character_id)
    return path
def JWZZ_string_char_fatigue(character_id):
    path="https://esi.evetech.net/latest/characters/{}/fatigue/".format(character_id)
    return path
def JWZZ_string_char_medals(character_id):
    path="https://esi.evetech.net/latest/characters/{}/medals/".format(character_id)
    return path
def JWZZ_string_char_notifications(character_id):
    path="https://esi.evetech.net/latest/characters/{}/notifications/".format(character_id)
    return path
def JWZZ_string_char_notifications_contacts(character_id):
    path="https://esi.evetech.net/latest/characters/{}/notifications/contacts/".format(character_id)
    return path
def JWZZ_string_char_portrait(character_id):
    path="https://esi.evetech.net/latest/characters/{}/portrait/".format(character_id)
    return path