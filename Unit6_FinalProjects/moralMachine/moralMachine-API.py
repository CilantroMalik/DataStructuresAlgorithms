from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from moralMachine import weight

app = Flask(__name__)
CORS(app)
app.config["DEBUG"] = True


# main function that encapsulates the algorithm that chooses the action the car will take
def moralBrake(carOccupants: list, crosswalkOccupants: list, greenLight: bool):
    # -- create helper variables and store useful quantities --
    driveStraight = True  # keep track of the final decision once we make it; this value will be returned
    # calculate and store the number of humans and animals in each group
    numHumansCar, numHumansCrosswalk = len([0 for i in carOccupants if i <= 4]), len([0 for i in crosswalkOccupants if i <= 4])
    numAnimalsCar, numAnimalsCrosswalk = len([0 for i in carOccupants if i >= 5]), len([0 for i in crosswalkOccupants if i >= 5])
    # calculate the weights of each group of people
    weightsCar, weightsCrosswalk = sum([weight(i) for i in carOccupants]), sum([weight(i) for i in crosswalkOccupants])
    # -- algorithm start --
    # we begin to work through cases one by one
    # -> Case 1: pedestrians abiding by the law
    if greenLight:
        # Sub-case 1a: different numbers of humans and animals differ by at most 1 --> kill less people no matter what
        if numHumansCar != numHumansCrosswalk and abs(numAnimalsCar - numAnimalsCrosswalk) <= 1:
            driveStraight = numHumansCar > numHumansCrosswalk
        # Sub-case 1b: different numbers of humans and animals differ by 2 or more --> use weighting system
        # Sub-case 1c: same numbers of humans --> use weighting system
        if abs(numAnimalsCar - numAnimalsCrosswalk) >= 2 or numHumansCar == numHumansCrosswalk:
            driveStraight = weightsCar > weightsCrosswalk
    # -> Case 2: pedestrians flouting the law
    else:
        # If the weights for the groups are within 2 of each other, kill the law-breakers; if not, save whoever is weighted higher
        driveStraight = True if abs(weightsCar - weightsCrosswalk) <= 2 else (weightsCar > weightsCrosswalk)

    # finally, finish off the function
    return (
        "The vehicle will maintain its current course to drive through the intersection" if driveStraight
        else "The vehicle will change its course to drive into the barricade."
    )  # convert the boolean to the corresponding string output for what action the car will take


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
