from flask import Flask, request

app = Flask(__name__)

form = '''
<form method="POST">
<button type="button" name="too big">Too Big</button>
<button type="button" name="too small">Too Small</button>
<button type="button" name="you win">You Win</button>
</form>
'''
@app.route('/')
def display_form():
    return form













if __name__ == '__main__':
    app.run()