from flask import Flask, request, jsonify
from geopy.geocoders import Nominatim

app = Flask(__name__)
geolocator = Nominatim(user_agent="Geopy Library")

@app.route('/geocode', methods=['GET'])
def geocode():
    address = request.args.get('address')
    if not address:
        return jsonify({'error': 'Address parameter is required'}), 400

    location = geolocator.geocode(address)
    if location:
        return jsonify({
            'address': location.address,
            'latitude': location.latitude,
            'longitude': location.longitude
        })
    else:
        return jsonify({'error': 'Location not found'}), 404


if __name__ == '__main__':
    app.run(debug=True)
