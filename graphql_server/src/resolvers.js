module.exports = {
  Query: {
    recipes: async (_, __, { dataSources }) =>
      dataSources.RecipeAPI.getAllRecipes(),
  },
};
