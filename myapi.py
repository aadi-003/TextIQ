import requests
import urllib.parse
class API:
    def __init__(self):
        self.api_key = 'bcVzEVUestyWKfo1IZ3iPpgu8tIfZ7MJOXaSMY6g'


    def sentiment_analysis(self,text_to_analyze):

        encoded_text = urllib.parse.quote(text_to_analyze)
        api_url=f"https://api.api-ninjas.com/v1/sentiment?text={text_to_analyze}"

        # api_url = f"https://api-ninjas.com{encoded_text}"
        headers = {"X-Api-Key": self.api_key}

        try:
            response = requests.get(api_url, headers=headers)

            if response.status_code == requests.codes.ok:
                result = response.json()
                return result
                print("\n--- Success ---")
                # print(f"Sentiment: {result['sentiment']}")
                # print(f"Score:     {result['score']}")
            else:
                print(f"\nAPI Error {response.status_code}: {response.text}")

        except Exception as error:
            print(f"\nConnection Error: {error}")

    def language_analysis(self,text_to_analyze):
        pass

    def text_analysis(self,text1,text2):
        url = "https://api.api-ninjas.com/v1/textsimilarity"
        headers = {
            "X-Api-Key": self.api_key
        }

        params = {
            "text_1": text1,
            "text_2": text2
        }

        response = requests.post(
            url,
            headers=headers,
            json=params
        )

        if response.status_code == 200:
            result = response.json()
            return result
        else:
            return {
                "error": response.status_code,
                "message": response.text
            }
