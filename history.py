from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from googletrans import Translator
import threading

app = Flask(__name__)
CORS(app)

# Initialize Translator
translator = Translator()

# Array to store queries
queries_array = []
lock = threading.Lock()

def translate_to_english(text):
    translated_text = translator.translate(text, dest='en').text
    return translated_text

def save_to_file():
    global queries_array
    global lock
    
    with lock:
        queries_to_save = queries_array[:]
        queries_array.clear()

    with open('user_queries.txt', 'a') as f:
        for query, lang in queries_to_save:
            # Translate to English if not already in English
            if lang != 'en':
                query = translate_to_english(query)
            f.write(query + '\n')

def start_save_timer():
    threading.Timer(20.0, save_to_file).start()

@app.route('/save_to_file', methods=['POST'])
@cross_origin()
def add_to_file():
    global queries_array
    data = request.json
    query = data.get('data', '')
    lang = data.get('selected_language', 'en')

    with lock:
        # Convert query to string if it's a list
        if isinstance(query, list):
            query = ' '.join(query)
        
        # Check if query is already in English
        if lang == 'en':
            queries_array.append((query, lang))
        else:
            # Translate to English
            query_en = translate_to_english(query)
            queries_array.append((query_en, lang))

    start_save_timer()
    return jsonify({'message': 'Query added to save list!'})

if __name__ == '__main__':
    app.run(debug=True, port=5001)


# from flask import Flask, request, jsonify
# from flask_cors import CORS, cross_origin
# from googletrans import Translator
# import threading
# import time

# app = Flask(__name__)
# CORS(app)

# # Initialize Translator
# translator = Translator()

# # Array to store queries
# queries_array = []
# lock = threading.Lock()

# def translate_to_english(text):
#     translated_text = translator.translate(text, dest='en').text
#     return translated_text


# def save_to_file():
#     global queries_array
#     global lock
    
#     with lock:
#         queries_to_save = queries_array[:]
#         queries_array.clear()

#     translated_queries = []
#     for query, lang in queries_to_save:
#         # Translate to English if not already in English
#         if lang != 'en':
#             query = translate_to_english(query)
#         translated_queries.append(query)


#     with open('user_queries.txt', 'a') as f:
#         for query in translated_queries:
#             f.write(query + '\n')

# def start_save_timer():
#     threading.Timer(10.0, save_to_file).start()

# @app.route('/save_to_file', methods=['POST'])
# @cross_origin()
# def add_to_file():
#     global queries_array
#     data = request.json
#     query = data.get('data', '')
#     lang = data.get('selected_language', 'en')

#     with lock:
#         queries_array.append((query, lang))

#     start_save_timer()
#     return jsonify({'message': 'Query added to save list!'})

# if __name__ == '__main__':
#     app.run(debug=True, port=5001)


# from flask import Flask, request, jsonify
# from flask_cors import CORS, cross_origin
# from googletrans import Translator
# import threading

# app = Flask(__name__)
# CORS(app)

# # Initialize Translator
# translator = Translator()

# # Array to store queries
# queries_array = []
# lock = threading.Lock()

# def translate_to_english(text):
#     translated_text = translator.translate(text, dest='en').text
#     return translated_text

# def save_to_file():
#     global queries_array
#     global lock
    
#     with lock:
#         queries_to_save = queries_array[:]
#         queries_array.clear()

#     translated_queries = []
#     for query, lang in queries_to_save:
#         # Translate to English if not already in English
#         if lang != 'en':
#             query = translate_to_english(query)
#         translated_queries.append(query)

#     with open('user_queries.txt', 'a') as f:
#         for query in translated_queries:
#             f.write(query + '\n')

# def start_save_timer():
#     threading.Timer(10.0, save_to_file).start()

# @app.route('/save_to_file', methods=['POST'])
# @cross_origin()
# def add_to_file():
#     global queries_array
#     data = request.json
#     query = data.get('data', '')
#     lang = data.get('selected_language', 'en')

#     with lock:
#         queries_array.append((query, lang))

#     start_save_timer()
#     return jsonify({'message': 'Query added to save list!'})

# if __name__ == '__main__':
#     app.run(debug=True, port=5001)




# from flask import Flask, request, jsonify
# from flask_cors import CORS, cross_origin
# from googletrans import Translator

# app = Flask(__name__)
# CORS(app)

# def translate_to_english(text):
#     translator = Translator()
#     translated_text = translator.translate(text, dest='en').text
#     return translated_text

# @app.route('/save_to_file', methods=['POST'])
# @cross_origin()
# def save_to_file():
#     data = request.json
#     queries = data.get('data', [])
#     selected_language = data.get('selected_language', 'en')

#     translated_queries = []
#     for query in queries:
#         # Translate to English if not already in English
#         if selected_language != 'en':
#             query = translate_to_english(query)
#         translated_queries.append(query)

#     with open('user_queries.txt', 'a') as f:
#         for query in translated_queries:
#             f.write(query + '\n')

#     return jsonify({'message': 'Queries saved successfully!'})

# if __name__ == '__main__':
#     app.run(debug=True, port=5001)



# from flask import Flask, request, jsonify
# from flask_cors import CORS, cross_origin
# from googletrans import Translator

# app = Flask(__name__)
# CORS(app)

# def translate_to_english(text):
#     translator = Translator()
#     translated_text = translator.translate(text, dest='en').text
#     return translated_text

# @app.route('/save_to_file', methods=['POST'])
# @cross_origin()
# def save_to_file():
#     data = request.json
#     query = data.get('data', '')
    
#     # Translate to English if not already in English
#     if data.get('selected_language', 'en') != 'en':
#         query = translate_to_english(query)
    
#     with open('user_queries.txt', 'a') as f:
#         f.write(query + '\n')
    
#     return jsonify({'message': 'Query saved successfully!'})

# if __name__ == '__main__':
#     app.run(debug=True, port=5001)
