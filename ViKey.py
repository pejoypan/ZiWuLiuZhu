# -- coding: utf-8 --
import platform

from  ctypes import *

if 'Windows' in platform.system():
    if "32bit" in platform.architecture():
        ViKeyDll=windll.LoadLibrary('ViKey.dll')
    else:
        ViKeyDll=windll.LoadLibrary('./ViKey64.dll')
else:
    if "32bit" in platform.architecture():
        ViKeyDll=cdll.LoadLibrary('ViKey.X86.so')
    else:
        ViKeyDll=cdll.LoadLibrary('ViKey.X64.so')

##查找加密狗
VikeyFind=ViKeyDll.VikeyFind
VikeyFind.argtypes=[c_void_p]
VikeyFind.restypes=(c_int)

##获取加密狗硬件ID
VikeyGetHID=ViKeyDll.VikeyGetHID
VikeyGetHID.argtypes=[c_short,c_void_p]
VikeyGetHID.restypes=(c_int)

##获取加密狗类型
VikeyGetType=ViKeyDll.VikeyGetType
VikeyGetType.argtypes=[c_short,c_void_p]
VikeyGetType.restypes=(c_int)

##获取ViKey加密狗的当前权限
VikeyGetLevel=ViKeyDll.VikeyGetLevel
VikeyGetLevel.argtypes=[c_short,c_void_p]
VikeyGetLevel.restypes=(c_int)

##设置ViKey加密狗的设备名称
VikeySetPtroductName=ViKeyDll.VikeySetPtroductName
VikeySetPtroductName.argtypes=[c_short,c_wchar_p]
VikeySetPtroductName.restypes=(c_int)

##获取ViKey加密狗的设备名称
VikeyGetPtroductName=ViKeyDll.VikeyGetPtroductName
VikeyGetPtroductName.argtypes=[c_short,c_wchar_p]
VikeyGetPtroductName.restypes=(c_int)

##获取ViKey加密狗的设备名称
VikeyGetPtroductNameA=ViKeyDll.VikeyGetPtroductNameA
VikeyGetPtroductNameA.argtypes=[c_short,c_char_p]
VikeyGetPtroductNameA.restypes=(c_int)

##用户登权限陆加密狗
VikeyUserLogin=ViKeyDll.VikeyUserLogin
VikeyUserLogin.argtypes=[c_short,c_void_p]
VikeyUserLogin.restypes=(c_int)

##管理员登权限陆加密狗
VikeyAdminLogin=ViKeyDll.VikeyAdminLogin
VikeyAdminLogin.argtypes=[c_short,c_void_p]
VikeyAdminLogin.restypes=(c_int)

##登出(关闭)加密狗
VikeyLogoff=ViKeyDll.VikeyLogoff
VikeyLogoff.argtypes=[c_short]
VikeyLogoff.restypes=(c_int)

##置加密狗的用户密码错误尝试次数
VikeySetUserPassWordAttempt=ViKeyDll.VikeySetUserPassWordAttempt
VikeySetUserPassWordAttempt.argtypes=[c_short,c_char]
VikeySetUserPassWordAttempt.restypes=(c_int)

##设置加密狗的管理员密码错误尝试次数
VikeySetAdminPassWordAttempt=ViKeyDll.VikeySetAdminPassWordAttempt
VikeySetAdminPassWordAttempt.argtypes=[c_short,c_char]
VikeySetAdminPassWordAttempt.restypes=(c_int)

##获取加密狗的用户密码错误尝试次数
VikeyGetUserPassWordAttempt=ViKeyDll.VikeyGetUserPassWordAttempt
VikeyGetUserPassWordAttempt.argtypes=[c_short,c_char_p,c_char_p]
VikeyGetUserPassWordAttempt.restypes=(c_int)

##获取加密狗的管理员密码错误尝试次数
VikeyGetAdminPassWordAttempt=ViKeyDll.VikeyGetAdminPassWordAttempt
VikeyGetAdminPassWordAttempt.argtypes=[c_short,c_char_p,c_char_p]
VikeyGetAdminPassWordAttempt.restypes=(c_int)

##修改ViKey加密狗的用户密码和管理员密码
VikeyResetPassword=ViKeyDll.VikeyResetPassword
VikeyResetPassword.argtypes=[c_short,c_void_p,c_void_p]
VikeyResetPassword.restypes=(c_int)

##设置加密狗的软件ID
VikeySetSoftIDString=ViKeyDll.VikeySetSoftIDString
VikeySetSoftIDString.argtypes=[c_short,c_char_p]
VikeySetSoftIDString.restypes=(c_int)

##获取加密狗的软件ID
VikeyGetSoftIDString=ViKeyDll.VikeyGetSoftIDString
VikeyGetSoftIDString.argtypes=[c_short,c_char_p]
VikeyGetSoftIDString.restypes=(c_int)

##读取加密狗的数据
VikeyReadData=ViKeyDll.VikeyReadData
VikeyReadData.argtypes=[c_short,c_short,c_short,c_char_p]
VikeyReadData.restypes=(c_int)

##写入数据到加密狗
VikeyWriteData=ViKeyDll.VikeyWriteData
VikeyWriteData.argtypes=[c_short,c_short,c_short,c_char_p]
VikeyWriteData.restypes=(c_int)

##获取4个随机数
ViKeyRandom=ViKeyDll.ViKeyRandom
ViKeyRandom.argtypes=[c_short,c_void_p,c_void_p,c_void_p,c_void_p]
ViKeyRandom.restypes=(c_int)

##将指定计数器中的数值减一
ViKeyDecraseModule=ViKeyDll.ViKeyDecraseModule
ViKeyDecraseModule.argtypes=[c_short,c_short]
ViKeyDecraseModule.restypes=(c_int)

##获取加密狗中计数器的值
ViKeyGetModule=ViKeyDll.ViKeyGetModule
ViKeyGetModule.argtypes=[c_short,c_short,c_void_p]
ViKeyGetModule.restypes=(c_int)

##设置递减计数器的初始值和模式
ViKeySetModule=ViKeyDll.ViKeySetModule
ViKeySetModule.argtypes=[c_short,c_short,c_short,c_short]
ViKeySetModule.restypes=(c_int)

##检查计数器的数值是否为零 模式是否允许可以递减
ViKeyCheckModule=ViKeyDll.ViKeyCheckModule
ViKeyCheckModule.argtypes=[c_short,c_short,c_void_p,c_void_p]
ViKeyCheckModule.restypes=(c_int)

##设置3DES算法用到的秘钥Key
Vikey3DesSetKey=ViKeyDll.Vikey3DesSetKey
Vikey3DesSetKey.argtypes=[c_short,c_char_p,c_short]
Vikey3DesSetKey.restypes=(c_int)

##3DES加密数据
Vikey3DesEncrypt=ViKeyDll.Vikey3DesEncrypt
Vikey3DesEncrypt.argtypes=[c_short,c_short,c_char_p,c_void_p]
Vikey3DesEncrypt.restypes=(c_int)

##3DES解密数据
Vikey3DesDecrypt=ViKeyDll.Vikey3DesDecrypt
Vikey3DesDecrypt.argtypes=[c_short,c_short,c_void_p,c_void_p]
Vikey3DesDecrypt.restypes=(c_int)

##设置DES算法用到的秘钥Key
VikeyDesSetKey=ViKeyDll.VikeyDesSetKey
VikeyDesSetKey.argtypes=[c_short,c_char_p]
VikeyDesSetKey.restypes=(c_int)

##DES加密数据
VikeyDesEncrypt=ViKeyDll.VikeyDesEncrypt
VikeyDesEncrypt.argtypes=[c_short,c_short,c_char_p,c_char_p,c_void_p]
VikeyDesEncrypt.restypes=(c_int)

##DES解密数据
VikeyDesDecrypt=ViKeyDll.VikeyDesDecrypt
VikeyDesDecrypt.argtypes=[c_short,c_short,c_char_p,c_char_p,c_void_p]
VikeyDesDecrypt.restypes=(c_int)

##设置自动打开网页的网址
VikeySetAutoRunUrl=ViKeyDll.VikeySetAutoRunUrl
VikeySetAutoRunUrl.argtypes=[c_short,c_char_p]
VikeySetAutoRunUrl.restypes=(c_int)

##通过此接口获取自动打开网页的网址
VikeyGetAutoRunUrl=ViKeyDll.VikeyGetAutoRunUrl
VikeyGetAutoRunUrl.argtypes=[c_short,c_char_p]
VikeyGetAutoRunUrl.restypes=(c_int)

##设置网络狗允许连接的最大客户端数
VikeySetMaxClientCount=ViKeyDll.VikeySetMaxClientCount
VikeySetMaxClientCount.argtypes=[c_short,c_short]
VikeySetMaxClientCount.restypes=(c_int)

##获取网络狗允许连接的最大客户端数
VikeyGetMaxClientCount=ViKeyDll.VikeyGetMaxClientCount
VikeyGetMaxClientCount.argtypes=[c_short,c_void_p]
VikeyGetMaxClientCount.restypes=(c_int)

##进行MD5哈希运算
VikeyMD5=ViKeyDll.VikeyMD5
VikeyMD5.argtypes=[c_short,c_short,c_char_p,c_char_p]
VikeyMD5.restypes=(c_int)

##设置MD5算法秘钥
VikeySetMD5Key=ViKeyDll.VikeySetMD5Key
VikeySetMD5Key.argtypes=[c_short,c_char_p]
VikeySetMD5Key.restypes=(c_int)

##进行HMAC_MD5哈希运算
VikeyHmacMD5=ViKeyDll.VikeyHmacMD5
VikeyHmacMD5.argtypes=[c_short,c_short,c_char_p,c_char_p]
VikeyHmacMD5.restypes=(c_int)

##进行SHA1哈希运算
VikeySHA1=ViKeyDll.VikeySHA1
VikeySHA1.argtypes=[c_short,c_short,c_char_p,c_char_p]
VikeySHA1.restypes=(c_int)

##设置SHA1算法秘钥
VikeySetSHA1Key=ViKeyDll.VikeySetSHA1Key
VikeySetSHA1Key.argtypes=[c_short,c_char_p]
VikeySetSHA1Key.restypes=(c_int)

##进行HMAC_SHA1哈希运算
VikeyHmacSHA1=ViKeyDll.VikeyHmacSHA1
VikeyHmacSHA1.argtypes=[c_short,c_short,c_char_p,c_char_p]
VikeyHmacSHA1.restypes=(c_int)

##执行加密狗国秘SM3算法
VikeySM3=ViKeyDll.VikeySM3
VikeySM3.argtypes=[c_short,c_short,c_char_p,c_char_p]
VikeySM3.restypes=(c_int)

##设置加密狗中SM4算法中的秘钥
VikeySM4SetKey=ViKeyDll.VikeySM4SetKey
VikeySM4SetKey.argtypes=[c_short,c_char_p]
VikeySM4SetKey.restypes=(c_int)

##执行加密狗中SM4算法中的加密操作
VikeySM4Encrypt=ViKeyDll.VikeySM4Encrypt
VikeySM4Encrypt.argtypes=[c_short,c_short,c_char_p,c_char_p,c_void_p]
VikeySM4Encrypt.restypes=(c_int)

##执行加密狗中SM4算法中的解密操作
VikeySM4Decrypt=ViKeyDll.VikeySM4Decrypt
VikeySM4Decrypt.argtypes=[c_short,c_short,c_char_p,c_char_p,c_void_p]
VikeySM4Decrypt.restypes=(c_int)

##执行非对称加密SM2算法的密钥对
VikeySM2CreateKey=ViKeyDll.VikeySM2CreateKey
VikeySM2CreateKey.argtypes=[c_short,c_void_p,c_void_p]
VikeySM2CreateKey.restypes=(c_int)

##SM2算法通过私钥计算公钥
VikeySM2CalcPubKey=ViKeyDll.VikeySM2CalcPubKey
VikeySM2CalcPubKey.argtypes=[c_short,c_char_p,c_void_p]
VikeySM2CalcPubKey.restypes=(c_int)

##SM2算法把私钥写入加密狗中
VikeySetSM2PrivateKey=ViKeyDll.VikeySetSM2PrivateKey
VikeySetSM2PrivateKey.argtypes=[c_short,c_char_p]
VikeySetSM2PrivateKey.restypes=(c_int)

##SM2算法把公钥写入加密狗中
VikeySetSM2PublicKey=ViKeyDll.VikeySetSM2PublicKey
VikeySetSM2PublicKey.argtypes=[c_short,c_char_p]
VikeySetSM2PublicKey.restypes=(c_int)

##SM2算法通过私钥签名数据
VikeySM2Sign=ViKeyDll.VikeySM2Sign
VikeySM2Sign.argtypes=[c_short,c_char_p,c_short,c_char_p,c_short,c_void_p,c_void_p]
VikeySM2Sign.restypes=(c_int)

##SM2算法通过公钥验证签名
VikeySM2Verify=ViKeyDll.VikeySM2Verify
VikeySM2Verify.argtypes=[c_short,c_char_p,c_short,c_char_p,c_short,c_void_p,c_void_p]
VikeySM2Verify.restypes=(c_int)

##SM2算法通过公钥进行数据加密
VikeySM2Encrypt=ViKeyDll.VikeySM2Encrypt
VikeySM2Encrypt.argtypes=[c_short,c_char_p,c_short,c_void_p,c_void_p]
VikeySM2Encrypt.restypes=(c_int)

##SM2算法通过私钥进行数据解密
VikeySM2Decrypt=ViKeyDll.VikeySM2Decrypt
VikeySM2Decrypt.argtypes=[c_short,c_char_p,c_short,c_void_p,c_void_p]
VikeySM2Decrypt.restypes=(c_int)

##取加密狗内部时钟的时间
VikeyGetTime=ViKeyDll.VikeyGetTime
VikeyGetTime.argtypes=[c_short,c_void_p]
VikeyGetTime.restypes=(c_int)

##获取时钟型加密狗中的到期时间
VikeyGetValidTime=ViKeyDll.VikeyGetValidTime
VikeyGetValidTime.argtypes=[c_short,c_void_p]
VikeyGetValidTime.restypes=(c_int)

##设置时钟型加密狗中的到期时间
VikeySetValidTime=ViKeyDll.VikeySetValidTime
VikeySetValidTime.argtypes=[c_short,c_char_p]
VikeySetValidTime.restypes=(c_int)

##检测时钟型加密狗的时钟功能是否到期
VikeyCheckValidTime=ViKeyDll.VikeyCheckValidTime
VikeyCheckValidTime.argtypes=[c_short,c_void_p]
VikeyCheckValidTime.restypes=(c_int)

######################################以上是ViKey接口库的函数声明，可以单独封装一个Python文件，进行引用