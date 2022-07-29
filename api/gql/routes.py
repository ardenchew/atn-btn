from ariadne import ObjectType
from gql.resolvers.user import user_resolver
from gql.resolvers.user import createUser_resolver


def generate_query_resolvers() -> ObjectType:
    query = ObjectType("Query")

    query.set_field("user", user_resolver)

    return query


def generate_mutation_resolvers() -> ObjectType:
    mutation = ObjectType("Mutation")

    mutation.set_field("createUser", createUser_resolver)

    return mutation
