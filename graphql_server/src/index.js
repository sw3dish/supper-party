const { ApolloServer } = require("apollo-server");
const { MongoClient } = require("mongodb");

const typeDefs = require("./schema");
const resolvers = require("./resolvers");
const RecipeAPI = require("./datasources/recipe");

const client = new MongoClient("mongodb://localhost:27017/supper_party", {
  useUnifiedTopology: true,
  useNewUrlParser: true,
});
client
  .connect()
  .then(() => {
    const server = new ApolloServer({
      typeDefs,
      resolvers,
      dataSources: () => ({
        RecipeAPI: new RecipeAPI(client.db().collection("bon_appetit_recipes")),
      }),
    });

    server.listen().then(({ url }) => {
      console.log(`🍕 Server ready at ${url}`);
    });
  })
  .catch((err) => {
    console.error(err);
  });
