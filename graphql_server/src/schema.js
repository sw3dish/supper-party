const { gql } = require("apollo-server");

const typeDefs = gql`
  type Recipe {
    id: ID!
    title: String
    url: String
    description: String
  }

  type Query {
    recipes: [Recipe]
    recipe(id: ID!): Recipe
  }
`;

module.exports = typeDefs;
