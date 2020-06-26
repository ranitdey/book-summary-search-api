# Search API


Search API service allows to search through summaries.The core functionality of the search is built only with language functionality without any search related libraries. The wrapper API is written with flask.


# Search Algorithms
There are two search algorithms available in the library. The first one calculates similarity ratio using Levenshtein distance and the second one uses partial ratio calculated using substring match and Levenshtein distance.
Before applying any of these algorithms the data gets preprocessed and also gets converted into Inverted Index. This helps to reduce the search space.
# How to run?
Make sure you have python3 installed in your system. Steps:
- Clone the project
- Create an virtual environnment with python3
- Go to project root
- install dependencies
```sh
pip install -r requirements.txt
```
- Run the API
```sh
python api/manage.py run
```
- The above command will start the server in :
```sh
http://127.0.0.1:5000
```
# How to run tests?
- Run the below commands to run API tests and core search tests:
```sh
 pytest api/test 
 pytest core_search/test/search_tests.py
```
# API
##### POST  /api/v1/search
Example request payload:    
  ```javascript
{
        "queries": ["in your l","is your problems","I should do"],
        "size": 2
    }
  ```
  
  Example response:
```javascript
{
    "results": [
        [
            {
                "summary": "The Book in Three Sentences: A book of 73 photos by master landscape photographer Christopher Burkett.",
                "id": 22,
                "query": "in your l",
                "author": "Christopher Burkett"
            },
            {
                "summary": "The Book in Three Sentences: A book of 68 photos by master landscape photographer Christopher Burkett.",
                "id": 41,
                "query": "in your l",
                "author": "Christopher Burkett"
            }
        ],
        [
            {
                "summary": "The Book in Three Sentences: Seek out new ideas and try new things. When trying something new, do it on a scale where failure is survivable. Seek out feedback and learn from your mistakes as you go along.",
                "id": 4,
                "query": "is your problems",
                "author": "Tim Harford"
            },
            {
                "summary": "The Book in Three Sentences: Before you pay your expenses, take your profit first. Run your business based on what you can afford to do today, not what you hope to be able to afford someday. When profit comes first, it is the focus, and it is never forgotten.",
                "id": 39,
                "query": "is your problems",
                "author": "Mike Michalowicz"
            }
        ],
        [
            {
                "summary": "The Book in Three Sentences: Seek out new ideas and try new things. When trying something new, do it on a scale where failure is survivable. Seek out feedback and learn from your mistakes as you go along.",
                "id": 4,
                "query": "I should do",
                "author": "Tim Harford"
            },
            {
                "summary": "The Book in Three Sentences: Everyone has a truth that they need to live and share. For the author, that truth was committing to the daily practice of repeating the phrase “I love myself.” When you love yourself, life loves you back.",
                "id": 26,
                "query": "I should do",
                "author": "Kamal Ravikant"
            }
        ]
    ]
}

  ```
  