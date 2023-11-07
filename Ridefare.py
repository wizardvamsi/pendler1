from flask import Flask, jsonify, request
import requests
import creds
import maincase
app = Flask(__name__)


@app.route('/get_distance', methods=['GET'])
def get_distance():
    api_key = creds.api_key
    # Replace with your Google Map API key
    origin = request.args.get('origin')
    destination = request.args.get('destination')
    units = 'metric'
    if not origin or not destination:
        return jsonify({"error": "Both origin and destination are required."})

    url = f'https://maps.googleapis.com/maps/api/distancematrix/json?origins={origin}&destinations={destination}&units={units}&key={api_key}'

    try:
        response = requests.get(url)
        data = response.json()

        # Extract the relevant information from the JSON response
        destination_addresses = data['destination_addresses']
        origin_addresses = data['origin_addresses']
        distance_text = data['rows'][0]['elements'][0]['distance']['text']
        duration_text = data['rows'][0]['elements'][0]['duration']['text']

        status = data['status']

        result = maincase.get_fare1()

        return jsonify(result)

    except Exception as e:
        return jsonify({"error": str(e)})


if __name__ == '__main__':
    app.run(debug=True)
