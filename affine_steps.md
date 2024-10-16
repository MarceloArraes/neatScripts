# How to use Clipboard API with Affine

Unfortunately, due to the restriction of browsers, many features like Clipboard only work under Secure Contexts (i.e. HTTPS or localhost). I would recommend you either setup your own CA, or proxy the server to the localhost.You can set the flag in Chrome to disable the Secure Contexts in the trusted sources. Input the chrome://flags/#unsafely-treat-insecure-origin-as-secure in URL to set.
