from flask import Flask, jsonify
from pydantic import ValidationError
from api.routes.professores import professores_blueprint
from api.routes.alunos import alunos_blueprint
from api.routes.turmas import turmas_blueprint
from flasgger import Swagger
from api.spec.swagger import SWAGGER_CONFIG, SWAGGER_TEMPLATE

app = Flask(__name__)

Swagger(app, template=SWAGGER_TEMPLATE, config=SWAGGER_CONFIG)

app.register_blueprint(professores_blueprint)
app.register_blueprint(alunos_blueprint)
app.register_blueprint(turmas_blueprint)

@app.errorhandler(ValidationError)
def handle_validation_errors(e):
    errors = e.errors(include_url=False, include_input=False)
    try:
        error_message = {
            ".".join(map(str, error["loc"])): error["msg"] for error in errors
        }
 
        return (
            jsonify(
                msg="Dados inválidos!",
                details={**error_message},
                error="VALIDATION_ERROR",
            ),
            400,
        )
    except TypeError:
        return jsonify(errors), 400

app.run(host="0.0.0.0", port=8000, debug=False)