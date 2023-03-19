import swagger_client
from swagger_client.rest import ApiException
from swagger_client import Configuration

api = swagger_client.CharacterApi()
api.api_client.set_default_header('User-Agent', 'my-test-agent') # Set a relevant user agent so we know which software is actually using ESI
api.api_client.host = "https://esi.tech.ccp.is"
Configuration().access_token = "{access token}" # fill in your access token here
try:
    response = api.get_characters_character_id_standings({character id}) # fill in the character id here
    print(response)
except ApiException as e:
    print("Exception when calling CharacterApi->get_characters_character_id_standings: %s\n" % e)