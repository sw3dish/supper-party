const { MongoDataSource } = require("apollo-datasource-mongodb");

class RecipeAPI extends MongoDataSource {
  async getAllRecipes() {
    return await this.collection.find({}).toArray();
  }
}

module.exports = RecipeAPI;
