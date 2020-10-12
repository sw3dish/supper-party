const { MongoDataSource } = require("apollo-datasource-mongodb");

class RecipeAPI extends MongoDataSource {
  async getAllRecipes() {
    const results = await this.collection.find({}).toArray();
    return results;
  }
}

module.exports = RecipeAPI;
