from flask import Flask
from ariadne import load_schema_from_path, make_executable_schema, graphql_sync, snake_case_fallback_resolvers
from ariadne.constants import PLAYGROUND_HTML
from flask import request, jsonify

import gql.routes as routes


def init_routes(app: Flask) -> None:
    query = routes.generate_query_resolvers()
    mutation = routes.generate_mutation_resolvers()

    type_defs = load_schema_from_path("gql/schema")
    schema = make_executable_schema(
        type_defs, query, mutation, snake_case_fallback_resolvers
    )

    @app.route("/health")
    def health():
        return "ok"

    @app.route("/graphql", methods=["GET"])
    def graphql_playground():
        return PLAYGROUND_HTML, 200

    @app.route("/graphql", methods=["POST"])
    def graphql_server():
        data = request.get_json()

        success, result = graphql_sync(
            schema,
            data,
            context_value=request,
            debug=app.debug
        )

        status_code = 200 if success else 400
        return jsonify(result), status_code