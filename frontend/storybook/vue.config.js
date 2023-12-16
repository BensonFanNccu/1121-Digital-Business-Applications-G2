const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: true,
  chainWebpack: config => {
    config.module
      .rule('pug')
        .test(/\.pug$/)
          .oneOf('pug-in-js')
            .resourceQuery(/blockType=template/)
            .use('raw-loader')
              .loader('raw-loader')
              .end()
            .use('pug-plain-loader')
              .loader('pug-plain-loader')
              .end()
            .end()
          .oneOf('pug-in-vue')
            .use('vue-pug-loader')
              .loader('vue-pug-loader')
              .end()
            .end();

    
  }
  
})
