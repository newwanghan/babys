# pip install pycryptodome
# pip install python-alipay-sdk

from alipay import AliPay

alipay_public_key_string = """-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAh9MMaRHtJ3c3HoPUQs/seQKHsGbdE7wLznz96E53oj78qyt56h131/XVn6LAW8UMpSjBKpWaeVqUy+C9sR9vGFzCr33h5BCf8cplYwdqyWAJG+pRDKlb8YtLo5wcR2SflRCvZo7uhN8B+2dTEoV2GEQtERaRt0uw5DLru7s1kcGSspAk/VDoRKuX5Z1VPnQR1yl55NMx/wyh7YakepuLrS4uiJTwW6iWw9fNWOVJ7d61Vwq5WWfkkPr29URGzZ4s+Mo8TPDaa0vzzPOKoOlGID+7xONBsG/S/VL2j0lRx9xtCE6zHWTlmiTlImov/UySdWTJ7547nfghbSHtdp5yHwIDAQAB
-----END PUBLIC KEY-----"""
app_private_key_string = """-----BEGIN RSA PRIVATE KEY-----
MIIEpAIBAAKCAQEAh9MMaRHtJ3c3HoPUQs/seQKHsGbdE7wLznz96E53oj78qyt56h131/XVn6LAW8UMpSjBKpWaeVqUy+C9sR9vGFzCr33h5BCf8cplYwdqyWAJG+pRDKlb8YtLo5wcR2SflRCvZo7uhN8B+2dTEoV2GEQtERaRt0uw5DLru7s1kcGSspAk/VDoRKuX5Z1VPnQR1yl55NMx/wyh7YakepuLrS4uiJTwW6iWw9fNWOVJ7d61Vwq5WWfkkPr29URGzZ4s+Mo8TPDaa0vzzPOKoOlGID+7xONBsG/S/VL2j0lRx9xtCE6zHWTlmiTlImov/UySdWTJ7547nfghbSHtdp5yHwIDAQABAoIBADK543yqMUP4BiHjYjbBqLNY+owrHo3sQQyRKdLE23FAzOSwjAufjc6eBXZlNioP4bUdD2d0EAkah0/NU4r/DmKu4hbgkKi4fMO0r0DY2Ez1DPHcBQERj0EaoNktyHHxZpgpbxiCcRo2n2rhH+le5sgRTjN/llQ6dIoFanzmYg9ZCheMiNlPagyoh8X0mFA80N/VkeBcJJXoXypEYtNd584j2oqqtW5pNHKFMCA8mRzi2KNiJKhdalNJY+iPixvNJLQ95B7DfyN11kJ7Itx/l4K8jE80cJqqSMM8Xo+d2YpsRzkRMrieS5yZW8elRIVTrdQmD8JXLRy4hVGCySEPAIECgYEA4sNCs6bYlsrFWOj7Pw7x2WknsaOJTtPy0UZwrMfu4udGkYzj2V3ow1PThQHVOdpAHYM7YfFpA6tT8Jf+WiJJ8QRc5OliH+HMVbv7r/4AiNw4h9atXywhZbI5a4bEvywUvROowv47JCtoXDeZVPd4ZO5jMP5kDPmmWIPBnaZuvBECgYEAmVYxnfVdIYfDI+8oZraBKbJCXEuvVPwxEK1oaqsYJZ0ovwMVdJxImkqOO6YLEfGbRaLqU2fOfKYFgEG1VvEcQEqVgEG3KkCmd0e31F1ZvZ4voJViBlashiugaA7KAoT1u4fIv50fljoDBqshDh7NqP1n474SZqmdnSEEqU3SOy8CgYEA0XdBFCZZB+HCrkB4ZWVurj/edM71tSU/tWT2DASbfGna2/RjPJTswBGc384zor8iXqCsp+qR8NvALAya3bOyzboT/ThAdebkE4YUFhvxbnrOlVwOxk1DhGc/dz4EW/tiJM4WJBknlF+shRKuxrfaNJGoesdisEGkETuUDAaDX6ECgYAvKBXsSThSBomZ9IQNSpVgeGT2M4SBc2m3gkz5eRLdBn8wd0dS7HlbkhA6Ae+nnhEtklPUQLl9FiXc8thNG6ufjhB6ODuXb/iB+HltgyQFL6/gB/D0mBVI0gPr3Jh9u9xCxxiS7UR4k/C4TUrGJ+0ByqT3ok3QatuBJlVjp/4+mwKBgQCE9GfiwpeQfFsz/yvo4pqWPaXaUDpaLktyvIYr5b9M9i4SO+H8cjbjSc8jooiPdrt1VJ6P2v5QjmqhHlNEUTkRIuC+nUSQ4MCDFyUMCSU02d034g2F70s6DfkCzTUGBsTYZZdNmKRI05gOGI0HPhw4z4Zfu6yxSvzgy8RcNJqSoA==
-----END RSA PRIVATE KEY-----"""


def get_pay(out_trade_no, total_amount, return_url):
    # 实例化支付应用
    alipay = AliPay(
        appid="2021000118641034",
        app_notify_url=None,
        app_private_key_string=app_private_key_string,
        alipay_public_key_string=alipay_public_key_string,
        sign_type="RSA2"
    )
    # 发起支付请求
    order_string = alipay.api_alipay_trade_page_pay(
        # 订单号，每次发送请求都不能一样
        out_trade_no=out_trade_no,
        # 支付金额
        total_amount=str(total_amount),
        # 交易信息
        subject="测试宝贝商城",
        return_url=return_url + '?t=' + out_trade_no,
        notify_url=return_url + '?t=' + out_trade_no
    )
    return 'https://openapi.alipaydev.com/gateway.do?' + order_string
