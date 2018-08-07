from flask import Flask, request

app = Flask(__name__)


@app.route('/', methods=['POST'])
def get_url():
    entry = request.get_json()['message']
    if entry.startswith('!'):
        entry = entry[1:]
    return 'https://git.devinfra.ptec/infra-tools/semic/merge_requests/%s' % entry


if __name__ == '__main__':
    app.run(debug=True)
