const path = require('path');

module.exports = ({ config, mode }) => {
  // handle scss resource in vue file
  const sassRule = {
    test: /\.scss$/,
    oneOf: [
      {
        resourceQuery: /\?vue/,
        use: ["vue-style-loader", "css-loader", "postcss-loader", "sass-loader"]
      }
    ]
  };

  // Handle js resource
  const jsRule = {
    test: /\.js$/,
    use: [{ loader: "babel-loader" }]
  };

  config.module.rules.push(jsRule, sassRule);
  return config;
};
