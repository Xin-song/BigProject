import requests
from esi_oauth_native_mylib import validate_eve_jwt


# %%
# The following four functions are for alliance ESIs
# %%
def handle_sso_token_response(sso_response):
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


# %%
# The following six functions are for assets ESIs
# %%
def JWZZ_assets_characterassets(sso_response, character_id):
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


# %%
def JWZZ_assets_characterassets_locations(sso_response, character_id):
    """Requires the following scope: esi-assets.read_assets.v1
    Return locations for a set of item ids, which you can get from character assets endpoint.
    Coordinates for items in hangars or stations are set to (0,0,0)
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


# %%
def JWZZ_assets_characterassets_names(sso_response, character_id):
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

# %%
# Here are the functiosn get path for Alliance
def JWZZ_s_alliance_alliances():
    return "https://esi.evetech.net/latest/alliances/"


def JWZZ_s_alliance_allianceId(alliance_id):
    path = "https://esi.evetech.net/latest/alliances/{}/".format(alliance_id)
    return path


def JWZZ_s_alliance_corporations(alliance_id):
    path = "https://esi.evetech.net/latest/alliances/{}/corporations/".format(alliance_id)
    return path


def JWZZ_s_alliance_icons(alliance_id):
    path = "https://esi.evetech.net/latest/alliances/{}/icons/".format(alliance_id)
    return path


# %%
# Here are the functiosn get path for Assets
def JWZZ_s_char_assets(character_id):
    path = "https://esi.evetech.net/latest/characters/{}/assets/".format(character_id)
    return path


def JWZZ_s_char_assets_locations(character_id):
    path = "https://esi.evetech.net/latest/characters/{}/assets/locations/".format(character_id)
    return path


def JWZZ_s_char_assets_names(character_id):
    path = "https://esi.evetech.net/latest/characters/{}/assets/names/".format(character_id)
    return path


def JWZZ_s_corp_assets(corporation_id):
    path = "https://esi.evetech.net/latest/corporations/{}/assets/".format(corporation_id)
    return path


def JWZZ_s_corp_assets_locations(corporation_id):
    path = "https://esi.evetech.net/latest/corporations/{}/assets/locations/".format(corporation_id)
    return path


def JWZZ_s_corp_assets_names(corporation_id):
    path = "https://esi.evetech.net/latest/corporations/{}/assets/names/".format(corporation_id)
    return path


# %%
# Here are the functiosn get path for Bookmarks
def JWZZ_s_char_bookmarks(character_id):
    path = "https://esi.evetech.net/latest/characters/{}/bookmarks/".format(character_id)
    return path


def JWZZ_s_char_bookmarks_folders(character_id):
    path = "https://esi.evetech.net/latest/characters/{}/bookmarks/folders/".format(character_id)
    return path


def JWZZ_s_corp_bookmarks(corporation_id):
    path = "https://esi.evetech.net/latest/corporations/{}/bookmarks/".format(corporation_id)
    return path


def JWZZ_s_corp_bookmarks_folders(corporation_id):
    path = "https://esi.evetech.net/latest/corporations/{}/bookmarks/folders/".format(corporation_id)
    return path


# %%
# Here are the functiosn get path for Calendar
def JWZZ_s_char_calendar(character_id):
    path = "https://esi.evetech.net/latest/characters/{}/calendar/".format(character_id)
    return path


def JWZZ_s_char_calendar_event(character_id, event_id):
    path = "https://esi.evetech.net/latest/characters/{}/calendar/{}/".format(character_id, event_id)
    return path


'''
# Here should be an respnd to an event
# Todo
# Learn how to use this.
def JWZZ_s_char_calendar_event(character_id,event_id):
    path="https://esi.evetech.net/latest/characters/{}/calendar/{}/".format(character_id,event_id)
    return path
'''


def JWZZ_s_char_calendar_event_attendees(character_id, event_id):
    path = "https://esi.evetech.net/latest/characters/{}/calendar/{}/attendees/".format(character_id, event_id)
    return path


# %%
# Here are the functiosn get path for Character
def JWZZ_s_char(character_id):
    path = "https://esi.evetech.net/latest/characters/{}/".format(character_id)
    return path


def JWZZ_s_char_agents_research(character_id):
    path = "https://esi.evetech.net/latest/characters/{}/agents_research/".format(character_id)
    return path


def JWZZ_s_char_blueprints(character_id):
    path = "https://esi.evetech.net/latest/characters/{}/blueprints/".format(character_id)
    return path


def JWZZ_s_char_corporationhistory(character_id):
    path = "https://esi.evetech.net/latest/characters/{}/corporationhistory/".format(character_id)
    return path


def JWZZ_s_char_cspa(character_id):
    # 这是个啥东西？
    # Todo
    # Post type
    path = "https://esi.evetech.net/latest/characters/{}/cspa/".format(character_id)
    return path


def JWZZ_s_char_fatigue(character_id):
    path = "https://esi.evetech.net/latest/characters/{}/fatigue/".format(character_id)
    return path


def JWZZ_s_char_medals(character_id):
    path = "https://esi.evetech.net/latest/characters/{}/medals/".format(character_id)
    return path


def JWZZ_s_char_notifications(character_id):
    path = "https://esi.evetech.net/latest/characters/{}/notifications/".format(character_id)
    return path


def JWZZ_s_char_notifications_contacts(character_id):
    path = "https://esi.evetech.net/latest/characters/{}/notifications/contacts/".format(character_id)
    return path


def JWZZ_s_char_portrait(character_id):
    path = "https://esi.evetech.net/latest/characters/{}/portrait/".format(character_id)
    return path


def JWZZ_s_char_roles(character_id):
    path = "https://esi.evetech.net/latest/characters/{}/roles/".format(character_id)
    return path


def JWZZ_s_char_standings(character_id):
    path = "https://esi.evetech.net/latest/characters/{}/standings/".format(character_id)
    return path


def JWZZ_s_char_titles(character_id):
    path = "https://esi.evetech.net/latest/characters/{}/titles/".format(character_id)
    return path


def JWZZ_s_char_affiliation():
    # Bulk lookup of character IDs to corporation, alliance and faction
    # 批量查找角色的公司，联盟，种族，需要输入
    # Todo
    # Post type
    path = "https://esi.evetech.net/latest/characters/affiliation/"
    return path


# %%
# Here are the functiosn get path for Clones
def JWZZ_s_char_clones(character_id):
    path = "https://esi.evetech.net/latest/characters/{}/clones/".format(character_id)
    return path


def JWZZ_s_char_implants(character_id):
    path = "https://esi.evetech.net/latest/characters/{}/implants/".format(character_id)
    return path


# %%
# Here are the functiosn get path for Contacts
def JWZZ_s_alli_contacts(alliance_id):
    path = "https://esi.evetech.net/latest/alliances/{}/contacts/".format(alliance_id)
    return path


def JWZZ_s_alli_contacts_labels(alliance_id):
    path = "https://esi.evetech.net/latest/alliances/{}/contacts/labels/".format(alliance_id)
    return path


def JWZZ_s_char_contacts(character_id):
    path = "https://esi.evetech.net/latest/characters/{}/contacts/".format(character_id)
    return path


def JWZZ_s_char_contacts_labels(character_id):
    path = "https://esi.evetech.net/latest/characters/{}/contacts/labels/".format(character_id)
    return path


def JWZZ_s_corp_contacts(corporation_id):
    path = "https://esi.evetech.net/latest/corporations/{}/contacts/".format(corporation_id)
    return path


def JWZZ_s_corp_contacts_labels(corporation_id):
    path = "https://esi.evetech.net/latest/corporations/{}/contacts/labels/".format(corporation_id)
    return path


# There are three more ESIs with 'Post', 'Put' and 'Delete' attribute, they are not added here.
# 还有三个，post，put，delete暂不添加

# %%
# Here are the functiosn get path for Contracts
def JWZZ_s_char_contracts(character_id):
    path = "https://esi.evetech.net/latest/characters/{}/contracts/".format(character_id)
    return path


def JWZZ_s_char_contracts_bid(character_id, contract_id):
    path = "https://esi.evetech.net/latest/characters/{}/contracts/{}/bids/".format(character_id, contract_id)
    return path


def JWZZ_s_char_contracts_items(character_id, contract_id):
    path = "https://esi.evetech.net/latest/characters/{}/contracts/{}/items/".format(character_id, contract_id)
    return path


def JWZZ_s_publ_contracts(region_id):
    path = "https://esi.evetech.net/latest/contracts/public/{}/".format(region_id)
    return path


def JWZZ_s_publ_contracts_bid(contract_id):
    path = "https://esi.evetech.net/latest/contracts/public/bids/{}/".format(contract_id)
    return path


def JWZZ_s_publ_contracts_items(contract_id):
    path = "https://esi.evetech.net/latest/contracts/public/items/{}/".format(contract_id)
    return path


def JWZZ_s_corp_contracts(corporation_id):
    path = "https://esi.evetech.net/latest/corporations/{}/contracts/".format(corporation_id)
    return path


def JWZZ_s_corp_contracts_bid(corporation_id, contract_id):
    path = "https://esi.evetech.net/latest/corporations/{}/contracts/{}/bids/".format(corporation_id, contract_id)
    return path


def JWZZ_s_corp_contracts_items(corporation_id, contract_id):
    path = "https://esi.evetech.net/latest/corporations/{}/contracts/{}/items/".format(corporation_id, contract_id)
    return path


# %%
# Here are the functiosn get path for Corporations
def JWZZ_s_corp(corporation_id):
    path = "https://esi.evetech.net/latest/corporations/{}/".format(corporation_id)
    return path


def JWZZ_s_corp_alliancehistory(corporation_id):
    path = "https://esi.evetech.net/latest/corporations/{}/alliancehistory/".format(corporation_id)
    return path


def JWZZ_s_corp_blueprints(corporation_id):
    path = "https://esi.evetech.net/latest/corporations/{}/blueprints/".format(corporation_id)
    return path


def JWZZ_s_corp_containers_logs(corporation_id):
    path = "https://esi.evetech.net/latest/corporations/{}/containers/logs/".format(corporation_id)
    return path


def JWZZ_s_corp_divisions(corporation_id):
    path = "https://esi.evetech.net/latest/corporations/{}/divisions/".format(corporation_id)
    return path


def JWZZ_s_corp_facilities(corporation_id):
    path = "https://esi.evetech.net/latest/corporations/{}/facilities/".format(corporation_id)
    return path


def JWZZ_s_corp_icons(corporation_id):
    path = "https://esi.evetech.net/latest/corporations/{}/icons/".format(corporation_id)
    return path


def JWZZ_s_corp_medals(corporation_id):
    path = "https://esi.evetech.net/latest/corporations/{}/medals/".format(corporation_id)
    return path


def JWZZ_s_corp_medals_issued(corporation_id):
    path = "https://esi.evetech.net/latest/corporations/{}/medals/issued/".format(corporation_id)
    return path


def JWZZ_s_corp_members(corporation_id):
    path = "https://esi.evetech.net/latest/corporations/{}/members/".format(corporation_id)
    return path


def JWZZ_s_corp_members_limit(corporation_id):
    path = "https://esi.evetech.net/latest/corporations/{}/members/limit/".format(corporation_id)
    return path


def JWZZ_s_corp_membertracking(corporation_id):
    path = "https://esi.evetech.net/latest/corporations/{}/membertracking/".format(corporation_id)
    return path


def JWZZ_s_corp_roles(corporation_id):
    path = "https://esi.evetech.net/latest/corporations/{}/roles/".format(corporation_id)
    return path


def JWZZ_s_corp_roles_history(corporation_id):
    path = "https://esi.evetech.net/latest/corporations/{}/roles/history/".format(corporation_id)
    return path


def JWZZ_s_corp_shareholders(corporation_id):
    path = "https://esi.evetech.net/latest/corporations/{}/shareholders/".format(corporation_id)
    return path


def JWZZ_s_corp_standings(corporation_id):
    path = "https://esi.evetech.net/latest/corporations/{}/standings/".format(corporation_id)
    return path


def JWZZ_s_corp_starbases(corporation_id):
    path = "https://esi.evetech.net/latest/corporations/{}/starbases/".format(corporation_id)
    return path


def JWZZ_s_corp_starbases_settings(corporation_id, starbase_id):
    path = "https://esi.evetech.net/latest/corporations/{}/starbases/{}/".format(corporation_id, starbase_id)
    return path


def JWZZ_s_corp_structures(corporation_id):
    path = "https://esi.evetech.net/latest/corporations/{}/structures/".format(corporation_id)
    return path


def JWZZ_s_corp_titles(corporation_id):
    path = "https://esi.evetech.net/latest/corporations/{}/titles/".format(corporation_id)
    return path


def JWZZ_s_corp_npccorps():
    path = "https://esi.evetech.net/latest/corporations/npccorps/".format()
    return path


# %%
# Here are the functiosn get path for Dogma
def JWZZ_s_dogma_attributes():
    path = "https://esi.evetech.net/latest/dogma/attributes/".format()
    return path


def JWZZ_s_dogma_attributes_info(attribute_id):
    path = "https://esi.evetech.net/latest/dogma/attributes/{}/".format(attribute_id)
    return path


def JWZZ_s_dogma_dynamic_items(type_id, item_id):
    path = "https://esi.evetech.net/latest/dogma/dynamic/items/{}/{}/".format(type_id, item_id)
    return path


def JWZZ_s_dogma_effects_info(effect_id):
    path = "https://esi.evetech.net/latest/dogma/effects/{}/".format(effect_id)
    return path

# %%
# Here are the functiosn get path for Faction Warfare
def JWZZ_s_faction_war_ch_stats(character_id):
    path = "https://esi.evetech.net/latest/characters/{}/fw/stats/".format(character_id)
    return path

def JWZZ_s_faction_war_corp_stats(corporation_id):
    path = "https://esi.evetech.net/latest/corporations/{}/fw/stats/".format(corporation_id)
    return path

def JWZZ_s_faction_war_leaderboards():
    path = "https://esi.evetech.net/latest/fw/leaderboards/".format()
    return path

def JWZZ_s_faction_war_leaderboards_chars():
    path = "https://esi.evetech.net/latest/fw/leaderboards/characters/".format()
    return path

def JWZZ_s_faction_war_leaderboards_corps():
    path = "https://esi.evetech.net/latest/fw/leaderboards/corporations/".format()
    return path

def JWZZ_s_faction_war_stats():
    path = "https://esi.evetech.net/latest/fw/stats/".format()
    return path

def JWZZ_s_faction_war_systems():
    path = "https://esi.evetech.net/latest/fw/systems/".format()
    return path

def JWZZ_s_faction_war_wars():
    path = "https://esi.evetech.net/latest/fw/wars/".format()
    return path


# %%
# Here are the functiosn get path for Fittings

def JWZZ_s_fittings(character_id):
    path = "https://esi.evetech.net/latest/characters/{}/fittings/".format(character_id)
    return path

# The other two are Post and Delete
# ToDo
# Add them if needed

# %%
# Here are the functiosn get path for Fleets

#Todo
# There are 4 Put, 3 Post, 3 Delete Esis in this section
# Add them if needed.

def JWZZ_s_fleet_char(character_id):
    path = "https://esi.evetech.net/latest/characters/{}/fleet/".format(character_id)
    return path

def JWZZ_s_fleet(fleet_id):
    path = "https://esi.evetech.net/latest/fleets/{}/".format(fleet_id)
    return path

def JWZZ_s_fleet_members(fleet_id):
    path = "https://esi.evetech.net/latest/fleets/{}/members/".format(fleet_id)
    return path

def JWZZ_s_fleet_wings(fleet_id):
    path = "https://esi.evetech.net/latest/fleets/{}/wings/".format(fleet_id)
    return path

# %%
# Here are the functiosn get path for Incursions

def JWZZ_s_incursions():
    path = "https://esi.evetech.net/latest/incursions/".format()
    return path

# %%
# Here are the functiosn get path for Industry

def JWZZ_s_industry_char_jobs(character_id):
    path = "https://esi.evetech.net/latest/characters/{}/industry/jobs/".format(character_id)
    return path

def JWZZ_s_industry_char_mining(character_id):
    path = "https://esi.evetech.net/latest/characters/{}/mining/".format(character_id)
    return path

def JWZZ_s_industry_corp_mining_extractions(corporation_id):
    path = "https://esi.evetech.net/latest/corporation/{}/mining/extractions/".format(corporation_id)
    return path

def JWZZ_s_industry_corp_mining_observers(corporation_id):
    path = "https://esi.evetech.net/latest/corporation/{}/mining/observers/".format(corporation_id)
    return path

def JWZZ_s_industry_corp_mining_observers_record(corporation_id,observer_id):
    path = "https://esi.evetech.net/latest/corporation/{}/mining/observers/{}/".format(corporation_id,observer_id)
    return path

def JWZZ_s_industry_corp_jobs(corporation_id):
    path = "https://esi.evetech.net/latest/corporations/{}/industry/jobs/".format(corporation_id)
    return path

def JWZZ_s_industry_facilities():
    path = "https://esi.evetech.net/latest/industry/facilities/".format()
    return path

def JWZZ_s_industry_systems():
    path = "https://esi.evetech.net/latest/industry/systems/".format()
    return path

# %%
# Here are the functiosn get path for Insurance

def JWZZ_s_insurance():
    path = "https://esi.evetech.net/latest/insurance/prices/".format()
    return path

# %%
# Here are the functiosn get path for Killmails

def JWZZ_s_kill_char(character_id):
    path = "https://esi.evetech.net/latest/characters/{}/killmails/recent/".format(character_id)
    return path

def JWZZ_s_kill_corp(corporation_id):
    path = "https://esi.evetech.net/latest/corporations/{}/killmails/recent/".format(corporation_id)
    return path

def JWZZ_s_kill_mail(killmail_id,killmail_hash):
    path = "https://esi.evetech.net/latest/killmails/{}/{}/".format(killmail_id,killmail_hash)
    return path

# %%
# Here are the functiosn get path for Locations

def JWZZ_s_loc_char(character_id):
    path = "https://esi.evetech.net/latest/characters/{}/location/".format(character_id)
    return path

def JWZZ_s_loc_char_online(character_id):
    path = "https://esi.evetech.net/latest/characters/{}/online/".format(character_id)
    return path

def JWZZ_s_loc_char_ship(character_id):
    path = "https://esi.evetech.net/latest/characters/{}/ship/".format(character_id)
    return path

# %%
# Here are the functiosn get path for Loyalty

def JWZZ_s_loy_char(character_id):
    path = "https://esi.evetech.net/latest/characters/{}/loyalty/points/".format(character_id)
    return path

def JWZZ_s_loy_offers(corporation_id):
    path = "https://esi.evetech.net/latest/loyalty/stores/{}/offers/".format(corporation_id)
    return path

# %%
# Here are the functiosn get path for Mail

#Todo
# There are 1 Put, 2 Post, 2 Delete Esis in this section
# Add them if needed.

def JWZZ_s_mail_char(character_id):
    path = "https://esi.evetech.net/latest/characters/{}/mail/".format(character_id)
    return path

def JWZZ_s_mail_char_content(character_id,mail_id):
    path = "https://esi.evetech.net/latest/characters/{}/mail/{}/".format(character_id,mail_id)
    return path

def JWZZ_s_mail_char_labels(character_id):
    path = "https://esi.evetech.net/latest/characters/{}/mail/labels/".format(character_id)
    return path

def JWZZ_s_mail_char_lists(character_id):
    path = "https://esi.evetech.net/latest/characters/{}/mail/lists/".format(character_id)
    return path

# %%
# Here are the functiosn get path for Market

def JWZZ_s_mkt_char_orders(character_id):
    path = "https://esi.evetech.net/latest/characters/{}/orders/".format(character_id)
    return path

def JWZZ_s_mkt_char_orders_history(character_id):
    path = "https://esi.evetech.net/latest/characters/{}/orders/history/".format(character_id)
    return path

def JWZZ_s_mkt_corp_orders(corporation_id):
    path = "https://esi.evetech.net/latest/corporations/{}/orders/".format(corporation_id)
    return path

def JWZZ_s_mkt_corp_orders_history(corporation_id):
    path = "https://esi.evetech.net/latest/corporations/{}/orders/history/".format(corporation_id)
    return path

def JWZZ_s_mkt_regi_history(region_id):
    path = "https://esi.evetech.net/latest/markets/{}/history/".format(region_id)
    return path

def JWZZ_s_mkt_regi_orders(region_id):
    path = "https://esi.evetech.net/latest/markets/{}/orders/".format(region_id)
    return path

def JWZZ_s_mkt_regi_types(region_id):
    path = "https://esi.evetech.net/latest/markets/{}/types/".format(region_id)
    return path

def JWZZ_s_mkt_groups():
    path = "https://esi.evetech.net/latest/markets/groups/".format()
    return path

def JWZZ_s_mkt_groups_info(market_group_id):
    path = "https://esi.evetech.net/latest/markets/groups/{}/".format(market_group_id)
    return path

def JWZZ_s_mkt_prices():
    path = "https://esi.evetech.net/latest/markets/prices/".format()
    return path

def JWZZ_s_mkt_stru(structure_id):
    path = "https://esi.evetech.net/latest/markets/structures/{}/".format(structure_id)
    return path

# %%
# Here are the functiosn get path for Opportunities
# 不会真有人调用这几个ESI吧？

def JWZZ_s_oppo_char(character_id):
    path = "https://esi.evetech.net/latest/characters/{}/opportunities/".format(character_id)
    return path

def JWZZ_s_oppo_groups():
    path = "https://esi.evetech.net/latest/opportunities/groups/".format()
    return path

def JWZZ_s_oppo_groups_info(group_id):
    path = "https://esi.evetech.net/latest/opportunities/groups/{}/".format(group_id)
    return path

def JWZZ_s_oppo_groups_tasks():
    path = "https://esi.evetech.net/latest/opportunities/tasks/".format()
    return path

def JWZZ_s_oppo_groups_task(task_id):
    path = "https://esi.evetech.net/latest/opportunities/tasks/{}/".format(task_id)
    return path

# %%
# Here are the functiosn get path for Planetary Interaction

def JWZZ_s_PI_char(character_id):
    path = "https://esi.evetech.net/latest/characters/{}/planets/".format(character_id)
    return path

def JWZZ_s_PI_char_planet(character_id,planet_id):
    path = "https://esi.evetech.net/latest/characters/{}/planets/{}/".format(character_id,planet_id)
    return path

def JWZZ_s_PI_corp_offices(corporation_id):
    path = "https://esi.evetech.net/latest/corporations/{}/customs_offices/".format(corporation_id)
    return path

def JWZZ_s_PI_schematic(schematic_id):
    path = "https://esi.evetech.net/latest/universe/schematics/{}/".format(schematic_id)
    return path

# %%
# Here are the functiosn get path for Routes

def JWZZ_s_routes(origin,destination):
    path = "https://esi.evetech.net/latest/route/{}/{}/".format(origin,destination)
    return path

# %%
# Here are the functiosn get path for Search

def JWZZ_s_search(character_id):
    path = "https://esi.evetech.net/latest/characters/{}/search/".format(character_id)
    return path

# %%
# Here are the functiosn get path for Skills

def JWZZ_s_skill_char_attri(character_id):
    path = "https://esi.evetech.net/latest/characters/{}/attributes/".format(character_id)
    return path

def JWZZ_s_skill_char_queue(character_id):
    path = "https://esi.evetech.net/latest/characters/{}/skillqueue/".format(character_id)
    return path

def JWZZ_s_skill_char_skills(character_id):
    path = "https://esi.evetech.net/latest/characters/{}/skills/".format(character_id)
    return path

# %%
# Here are the functiosn get path for Sovereignity

def JWZZ_s_sovereignty_campaigns():
    path = "https://esi.evetech.net/latest/sovereignty/campaigns/".format()
    return path

def JWZZ_s_sovereignty_map():
    path = "https://esi.evetech.net/latest/sovereignty/map/".format()
    return path

def JWZZ_s_sovereignty_structures():
    path = "https://esi.evetech.net/latest/sovereignty/structures/".format()
    return path

# %%
# Here are the functiosn get path for Status

def JWZZ_s_status():
    path = "https://esi.evetech.net/latest/status/".format()
    return path

# %%
# Here are the functiosn get path for Universe

# Todo There are two post ESIs

def JWZZ_s_uni_ancestries():
    path = "https://esi.evetech.net/latest/universe/ancestries/".format()
    return path

def JWZZ_s_uni_asteroid_belts(asteroid_belt_id):
    path = "https://esi.evetech.net/latest/universe/asteroid_belts/{}/".format(asteroid_belt_id)
    return path

def JWZZ_s_uni_bloodlines():
    path = "https://esi.evetech.net/latest/universe/bloodlines/".format()
    return path

def JWZZ_s_uni_categories_info(category_id):
    path = "https://esi.evetech.net/latest/universe/categories/{}/".format(category_id)
    return path

def JWZZ_s_uni_constellations():
    path = "https://esi.evetech.net/latest/universe/constellations/".format()
    return path

def JWZZ_s_uni_constellations_info(constellation_id):
    path = "https://esi.evetech.net/latest/universe/constellations/{}/".format(constellation_id)
    return path

def JWZZ_s_uni_factions():
    path = "https://esi.evetech.net/latest/universe/factions/".format()
    return path

def JWZZ_s_uni_graphics():
    path = "https://esi.evetech.net/latest/universe/graphics/".format()
    return path

def JWZZ_s_uni_graphics_info(graphic_id):
    path = "https://esi.evetech.net/latest/universe/graphics/{}/".format(graphic_id)
    return path

def JWZZ_s_uni_groups():
    path = "https://esi.evetech.net/latest/universe/groups/".format()
    return path

def JWZZ_s_uni_groups_info(group_id):
    path = "https://esi.evetech.net/latest/universe/groups/{}/".format(group_id)
    return path

def JWZZ_s_uni_moons(moon_id):
    path = "https://esi.evetech.net/latest/universe/moons/{}/".format(moon_id)
    return path

def JWZZ_s_uni_planets_info(planet_id):
    path = "https://esi.evetech.net/latest/universe/planets/{}/".format(planet_id)
    return path

def JWZZ_s_uni_races():
    path = "https://esi.evetech.net/latest/universe/races/".format()
    return path

def JWZZ_s_uni_regions():
    path = "https://esi.evetech.net/latest/universe/regions/".format()
    return path

def JWZZ_s_uni_regions_info(region_id):
    path = "https://esi.evetech.net/latest/universe/regions/{}/".format(region_id)
    return path

def JWZZ_s_uni_stargates_info(stargate_id):
    path = "https://esi.evetech.net/latest/universe/stargates/{}/".format(stargate_id)
    return path

def JWZZ_s_uni_stars_info(star_id):
    path = "https://esi.evetech.net/latest/universe/stars/{}/".format(star_id)
    return path

def JWZZ_s_uni_stations_info(station_id):
    path = "https://esi.evetech.net/latest/universe/stations/{}/".format(station_id)
    return path

def JWZZ_s_uni_structures():
    path = "https://esi.evetech.net/latest/universe/structures/".format()
    return path

def JWZZ_s_uni_structures_info(structure_id):
    path = "https://esi.evetech.net/latest/universe/structures/{}/".format(structure_id)
    return path

def JWZZ_s_uni_system_jumps():
    path = "https://esi.evetech.net/latest/universe/system_jumps/".format()
    return path

def JWZZ_s_uni_system_kills():
    path = "https://esi.evetech.net/latest/universe/system_kills/".format()
    return path

def JWZZ_s_uni_systems():
    path = "https://esi.evetech.net/latest/universe/systems/".format()
    return path

def JWZZ_s_uni_systems_info(system_id):
    path = "https://esi.evetech.net/latest/universe/systems/{}/".format(system_id)
    return path

def JWZZ_s_uni_types():
    path = "https://esi.evetech.net/latest/universe/types/".format()
    return path

def JWZZ_s_uni_types_info(type_id):
    path = "https://esi.evetech.net/latest/universe/types/{}/".format(type_id)
    return path

# %%
# Here are the functiosn get path for User Interface

# Todo
# All are post esis

# %%
# Here are the functiosn get path for Wallet

def JWZZ_s_wallet_char(character_id):
    path = "https://esi.evetech.net/latest/characters/{}/wallet/".format(character_id)
    return path

def JWZZ_s_wallet_char_journal(character_id):
    path = "https://esi.evetech.net/latest/characters/{}/wallet/journal/".format(character_id)
    return path

def JWZZ_s_wallet_char_transactions(character_id):
    path = "https://esi.evetech.net/latest/characters/{}/wallet/transactions/".format(character_id)
    return path

def JWZZ_s_wallet_corp(corporation_id):
    path = "https://esi.evetech.net/latest/corporations/{}/wallet/".format(corporation_id)
    return path

def JWZZ_s_wallet_corp_journal(corporation_id,division):
    path = "https://esi.evetech.net/latest/corporations/{}/wallet/{}/journal/".format(corporation_id,division)
    return path

def JWZZ_s_wallet_corp_transactions(corporation_id,division):
    path = "https://esi.evetech.net/latest/corporations/{}/wallet/{}/transactions/".format(corporation_id,division)
    return path

# %%
# Here are the functiosn get path for Wars

def JWZZ_s_war():
    path = "https://esi.evetech.net/latest/wars/".format()
    return path

def JWZZ_s_war_info(war_id):
    path = "https://esi.evetech.net/latest/wars/{}/".format(war_id)
    return path

def JWZZ_s_war_killmails(war_id):
    path = "https://esi.evetech.net/latest/wars/{}/killmails/".format(war_id)
    return path






























