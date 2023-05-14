module.exports = {
  packagerConfig: {
  },
  rebuildConfig: {},
  makers: [
    {
      // 全平台都可用
      name: '@electron-forge/maker-zip',
      certificateFile: './cert.pfx',
      certificatePassword: process.env.CERTIFICATE_PASSWORD
    },
    {
      name: '@electron-forge/maker-squirrel',
      certificateFile: './cert.pfx',
      certificatePassword: process.env.CERTIFICATE_PASSWORD
    }
  ]
};
