""" Python 3 native (desktop/mobile) OAuth 2.0 example.
This example can be run from the command line and will show you how the
OAuth 2.0 flow should be handled if you are a web based application.
Prerequisites:
    * Create an SSO application at developers.eveonline.com with the scope
      "esi-characters.read_blueprints.v1" and the callback URL
      "https://localhost/callback/". Note: never use localhost as a callback
      in released applications.
    * Have a Python 3 environment available to you (possibly by using a
      virtual environment: https://virtualenv.pypa.io/en/stable/).
    * Run pip install -r requirements.txt with this directory as your root.
"""
import base64
import hashlib
import secrets
import urllib
import requests

#%%
scope_list = ["esi-calendar.respond_calendar_events.v1","esi-calendar.read_calendar_events.v1"]
scopes = '+'.join(scope_list)
def print_auth_url(client_id, code_challenge=None):
    """Prints the URL to redirect users to.

    Args:
        client_id: The client ID of an EVE SSO application
        code_challenge: A PKCE code challenge
    """
    base_auth_url = "https://login.eveonline.com/v2/oauth/authorize/"
    params = {
        "response_type": "code",
        "redirect_uri": "https://localhost/callback/",
        "client_id": client_id,
        "scope": "publicData esi-calendar.respond_calendar_events.v1 esi-calendar.read_calendar_events.v1 esi-location.read_location.v1 esi-location.read_ship_type.v1 esi-mail.organize_mail.v1 esi-mail.read_mail.v1 esi-mail.send_mail.v1 esi-skills.read_skills.v1 esi-skills.read_skillqueue.v1 esi-wallet.read_character_wallet.v1 esi-wallet.read_corporation_wallet.v1 esi-search.search_structures.v1 esi-clones.read_clones.v1 esi-universe.read_structures.v1 esi-killmails.read_killmails.v1 esi-corporations.read_corporation_membership.v1 esi-assets.read_assets.v1 esi-planets.manage_planets.v1 esi-fleets.read_fleet.v1 esi-fleets.write_fleet.v1 esi-ui.write_waypoint.v1 esi-characters.write_contacts.v1 esi-fittings.read_fittings.v1 esi-fittings.write_fittings.v1 esi-markets.structure_markets.v1 esi-corporations.read_structures.v1 esi-characters.read_loyalty.v1 esi-characters.read_chat_channels.v1 esi-characters.read_standings.v1 esi-characters.read_agents_research.v1 esi-industry.read_character_jobs.v1 esi-markets.read_character_orders.v1 esi-characters.read_blueprints.v1 esi-location.read_online.v1 esi-contracts.read_character_contracts.v1 esi-clones.read_implants.v1 esi-killmails.read_corporation_killmails.v1 esi-corporations.track_members.v1 esi-wallet.read_corporation_wallets.v1 esi-characters.read_notifications.v1 esi-corporations.read_divisions.v1 esi-assets.read_corporation_assets.v1 esi-corporations.read_titles.v1 esi-corporations.read_blueprints.v1 esi-contracts.read_corporation_contracts.v1 esi-corporations.read_standings.v1 esi-corporations.read_starbases.v1 esi-markets.read_corporation_orders.v1 esi-industry.read_corporation_mining.v1 esi-planets.read_customs_offices.v1 esi-corporations.read_facilities.v1 esi-characters.read_titles.v1 esi-characters.read_fw_stats.v1 esi-corporations.read_fw_stats.v1 esi-characterstats.read.v1",
        "state": "unique-state"
    }

    if code_challenge:
        params.update({
            "code_challenge": code_challenge,
            "code_challenge_method": "S256"
        })

    string_params = urllib.parse.urlencode(params)
    full_auth_url = "{}?{}".format(base_auth_url, string_params)

    print("\nOpen the following link in your browser:\n\n {} \n\n Once you "
          "have logged in as a character you will get redirected to "
          "https://localhost/callback/.".format(full_auth_url))
#%%
def send_token_request(form_values, add_headers={}):
    """Sends a request for an authorization token to the EVE SSO.
    Args:
        form_values: A dict containing the form encoded values that should be
                     sent with the request
        add_headers: A dict containing additional headers to send
    Returns:
        requests.Response: A requests Response object
    """
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Host": "login.eveonline.com",
    }
    if add_headers:
        headers.update(add_headers)
    res = requests.post(
        "https://login.eveonline.com/v2/oauth/token",
        data=form_values,
        headers=headers,
    )
    print("Request sent to URL {} with headers {} and form values: "
          "{}\n".format(res.url, headers, form_values))
    res.raise_for_status()
    return res
#%%
def handle_sso_token_response(sso_response):
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

        print("\nSuccess! Here is the payload received from the EVE SSO: {}"
              "\nYou can use the access_token to make an authenticated "
              "request to {}".format(data, blueprint_path))

        headers = {
            "Authorization": "Bearer {}".format(access_token)
        }

        res = requests.get(blueprint_path, headers=headers)
        print("\nMade request to {} with headers: "
              "{}".format(blueprint_path, res.request.headers))
        res.raise_for_status()

        data = res.json()
        print("\n{} has {} blueprints".format(character_name, len(data)))
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
#%%
import sys
import requests
from jose import jwt
from jose.exceptions import ExpiredSignatureError, JWTError
SSO_META_DATA_URL = "https://login.eveonline.com/.well-known/oauth-authorization-server"
JWK_ALGORITHM = "RS256"
JWK_ISSUERS = ("login.eveonline.com", "https://login.eveonline.com")
JWK_AUDIENCE = "EVE Online"
def validate_eve_jwt(token: str) -> dict:
    """Validate a JWT access token retrieved from the EVE SSO.

    Args:
        token: A JWT access token originating from the EVE SSO
    Returns:
        The contents of the validated JWT access token if there are no errors
    """
    # fetch JWKs URL from meta data endpoint
    res = requests.get(SSO_META_DATA_URL)
    res.raise_for_status()
    data = res.json()
    try:
        jwks_uri = data["jwks_uri"]
    except KeyError:
        raise RuntimeError(
            f"Invalid data received from the SSO meta data endpoint: {data}"
        ) from None

    # fetch JWKs from endpoint
    res = requests.get(jwks_uri)
    res.raise_for_status()
    data = res.json()
    try:
        jwk_sets = data["keys"]
    except KeyError:
        raise RuntimeError(
            f"Invalid data received from the the jwks endpoint: {data}"
        ) from None

    # pick the JWK with the requested alogorithm
    jwk_set = [item for item in jwk_sets if item["alg"] == JWK_ALGORITHM].pop()

    # try to decode the token and validate it against expected values
    # will raise JWT exceptions if decoding fails or expected values do not match
    contents = jwt.decode(
        token=token,
        key=jwk_set,
        algorithms=jwk_set["alg"],
        issuer=JWK_ISSUERS,
        audience=JWK_AUDIENCE,
    )
    return contents
#%% Main program

# Generate the PKCE code challenge
random = base64.urlsafe_b64encode(secrets.token_bytes(32))
m = hashlib.sha256()
m.update(random)
d = m.digest()
code_challenge = base64.urlsafe_b64encode(d).decode().replace("=", "")

client_id = 'e58b08447d4f48618e0612e3276f45f7'

print_auth_url(client_id, code_challenge=code_challenge)

auth_code = input("Copy the \"code\" query parameter and enter it here: ")

code_verifier = random

form_values = {
    "grant_type": "authorization_code",
    "client_id": client_id,
    "code": auth_code,
    "code_verifier": code_verifier
}

res = send_token_request(form_values)

handle_sso_token_response(res)


