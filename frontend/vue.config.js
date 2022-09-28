const path = require("path");
function resolve(dir) {
  return path.join(__dirname, dir);
}

const port = 9595;

module.exports = {
  css: {
    loaderOptions: {
      sass: {
        additionalData: `@import "@/styles/variables.scss";`,
      },
    },
  },
  configureWebpack: {
    resolve: {
      alias: {
        "@": resolve("src"),
      },
    },
  },
  devServer: {
    port: port,
  },
};
