module.exports = {
  packagerConfig: {},
  rebuildConfig: {},
  makers: [
    {
      // 全平台都可用
      name: '@electron-forge/maker-zip',
      certificateFile: './cert.pfx',
      certificatePassword: process.env.CERTIFICATE_PASSWORD
    },
    {
      // Windows
      name: '@electron-forge/maker-squirrel',
      config: {
        authors: '蒋钦禹',
        certificateFile: './cert.pfx',
        certificatePassword: process.env.CERTIFICATE_PASSWORD
      }
    },
    {
      name: '@electron-forge/maker-wix',
      config: {
        language: 2052,
        manufacturer: '蒋钦禹',
        certificateFile: './cert.pfx',
        certificatePassword: process.env.CERTIFICATE_PASSWORD
      }
    }
  ]
};
