""" Test data that corresponds to Alumni Events service & its endpoints"""

Data = {
    'myEvents': {
              "fixtures": {"headers": {'HBS_PERSON_ID': '75279', 'Accept': 'application/json'},
                       "endpoint": "allMyEvents",
                       },
              "tc001": {
                       },
              "tc002": {
                       "endpoint": "allMyEvents",
                       },
              "tc003": {"headers": {'HBS_PERSON_ID': '75279', 'Accept': 'application/xml'},
                       "endpoint": "allMyEvents",
                       },
              "tc004": {
                       },
            }
       }