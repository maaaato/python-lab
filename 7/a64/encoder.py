import base64


def str_to_base64(x):
    """文字列をbase64表現に変換する

    b64encode()はbyte-like objectを引数にとるため
    文字列はencode()でbyte型にして渡す
    """
    return base64.b64encode(x.encode('utf-8'))


__all__ = ['str_to_base64']
