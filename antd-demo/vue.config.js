// vue.config.js for less-loader@6.0.0
module.exports = {
    css: {
      sourceMap: true, 
      loaderOptions: {
        less: {
          //lessOptions: {
            modifyVars: {
              'primary-color': '#1DA57A',
              'link-color': '#1DA57A',
              'border-radius-base': '2px',
              // Layout
              'layout-body-background' : '#1da57a',
              'layout-header-background': '#1da57a',
// @layout-body-background: #f0f2f5;
// @layout-header-background: #001529;
// @layout-footer-background: @layout-body-background;
// @layout-header-height: 64px;
// @layout-header-padding: 0 50px;
// @layout-footer-padding: 24px 50px;
// @layout-sider-background: @layout-header-background;
// @layout-trigger-height: 48px;
// @layout-trigger-background: #002140;
// @layout-trigger-color: #fff;
// @layout-zero-trigger-width: 36px;
// @layout-zero-trigger-height: 42px;
// // Layout light theme
// @layout-sider-background-light: #fff;
// @layout-trigger-background-light: #fff;
// @layout-trigger-color-light: @text-color;
            },
            javascriptEnabled: true,
          //},
        },
      },
    },
  };

  