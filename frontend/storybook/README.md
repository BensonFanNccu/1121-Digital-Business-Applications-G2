# storybook
> 關於元件的規劃與進度可以參考 [元件地圖](https://github.com/WAFFLE900/bricks/blob/master/Bricks/frontend/storybook/src/stories/overview/components_map.md)

> 點此查看 [Storybook](https://644cdb54238cc4fa28d2fa00-woehhqscui.chromatic.com/?path=/docs/general-%E9%80%9A%E7%94%A8-icons-%E5%9C%96%E6%A8%99-icons-wiki-%E5%9C%96%E6%A8%99%E5%A4%A7%E5%85%A8--docs)

## 初始化專案
```
npm install // 安裝相依套件
```
### 運行 Storybook
```
npm run storybook // the function of storybook is to run Storybook locally.
```
這裡會執行 storybook，並且在瀏覽器上開啟 localhost:6006

### 運行伺服器
```
npm run serve // the function of serve is to start a development server.
```
這裡會執行 App.vue，並且在瀏覽器上開啟 localhost:8080

### 檢查程式碼
```
npm run lint // the function of lint is to check the code style and format.
```

### 編譯專案
```
npm run build // the function of build is to build a production-ready app.
```

## 備註: 環境設定

### 使用環境簡介

環境：node.js v18.16.0

套件管理工具：npm v9.5.1

框架：Vue2

前端預處理器：Pug + Sass + JavaScript

### 安裝 Vue2 with Pug + Sass + JavaScript

1. 首先，確保你已經安裝了 Node.js 和 Vue CLI。如果你還沒有安裝 Vue CLI，可以在終端機中執行以下命令安裝：

```bash
npm install -g @vue/cli
```

2. 在終端機中進入你想要初始化專案的目錄，然後執行以下命令：

```bash
vue create my-project
```

其中**`my-project`**是你希望為這個專案命名的名稱。

3. 在選擇應用程式配置時，請依照以下選擇

```bash
? Please pick a preset: 
# Manually select features
? Check the features needed for your project: 
# 按下空格選取 TS, CSS Pre-processors
? Choose a version of Vue.js that you want to start the project with
# 2.x
? Use class-style component syntax?
# Yes
? Use Babel alongside TypeScript (required for modern mode, auto-detected polyfills, transpiling 
JSX)? 
# Yes
? Pick a CSS pre-processor (PostCSS, Autoprefixer and CSS Modules are supported by default): 
# Sass/SCSS (with dart-sass)
? Pick a linter / formatter config: 
# ESLint with error prevention only
? Pick additional lint features: 
# Lint on save
? Where do you prefer placing config for Babel, ESLint, etc.?
# In package.json
? Save this as a preset for future projects? 
# No
```

4. 在這個時候，專案已經成功初始化了，但是沒有安裝 Pug 的相關套件，因此我們需要手動安裝這些套件。在終端機中輸入以下命令：

```bash
cd my-project
npm install -D pug vue-pug-loader pug-plain-loader raw-loader
# -D 開發階段
# pug vue-pug-loader pug-plain-loader raw-loader 是四個依賴模組
```

5. 安裝完成後，打開 **`vue.config.js`** 文件（如果不存在，請創建一個），並添加以下代碼：

```jsx
module.exports = {
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
}
```

這段代碼告訴 Webpack 使用 **`pug-plain-loader`** 和 **`pug-plain-loader`** 套件來處理 **`.pug`** 文件，使用 `**vue-pug-loader`** 處理 **`.vue`** 文件裡的 `**<template lang="pug">` 。**


---

### 安裝 Storybook with Pug + Sass + JavaScript

1. 初始化 Storybook

```bash
npx storybook@latest init
```

2. 在 **`.storybook`** 目錄中創建一個名為 **`webpack.config.js`** 的新文件，其內容如下：

```jsx
const path = require('path');

module.exports = async ({ config }) => {
  // 添加對 Pug 和 Sass 的支持
  config.module.rules.push(
    {
      test: /\.sass$/,
      use:[
        require.resolve('vue-style-loader'),
        require.resolve('css-loader'),
        {
          loader: require.resolve('sass-loader'),
          options: {
            sassOptions: {
              indentedSyntax: true// 使用縮排語法
            }
          }
        }
      ],
    },
    {
      test: /\.pug$/,
      oneOf: [
        {
          exclude: /\.vue$/,
          use:[
              'raw-loader',
              'pug-plain-loader'
          ]
        },
        {
          use: 'vue-pug-loader'
        }
      ]
    },
    {
      test: /\.(png|jpe?g|gif)$/i,
      use: [
        {
          loader: "file-loader",
        },
      ],
    },
  );

  // 解析文件擴展名
  config.resolve.extensions.push('.pug', '.sass');

  // 返回修改後的配置
  return config;
};
```
