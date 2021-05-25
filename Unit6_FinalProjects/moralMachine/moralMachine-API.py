from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from moralMachine import moralBrake

app = Flask(__name__)
CORS(app)
app.config["DEBUG"] = True


@app.errorhandler(404)
@cross_origin()
def error404(e):
    return "404 Error: resource not found", 404


@app.route('/api/selfDriving/moralBrake')
@cross_origin()
def moralMachine():
    carOccupants = [int(i) for i in list(request.args.get("car"))]
    crosswalkOccupants = [int(i) for i in list(request.args.get("crosswalk"))]
    greenLight = request.args.get("green") == "1"
    return jsonify({"decision": moralBrake(carOccupants, crosswalkOccupants, greenLight)})


if __name__ == '__main__':
    app.run(port=8888)
