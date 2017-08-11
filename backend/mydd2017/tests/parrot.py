from flask import Flask, current_app, jsonify
from flask_assistant import Assistant, ask, tell, event, context_manager, request
from flask_assistant import ApiAi

app = Flask(__name__)
assist = Assistant(app,  '/')


@assist.action('fallback', is_fallback=True)
def say_response():
    """ Setting the fallback to act as a looper """
    speech = request['result']['resolvedQuery']
    return ask(speech)

@assist.action('help')
def help():
    speech = "I just parrot things back!"
    return ask(speech)

@assist.action('quit')
def quit():
    speech = "Leaving program"
    return tell(speech)

if __name__ == '__main__':
    app.run(debug=False, use_reloader=False)